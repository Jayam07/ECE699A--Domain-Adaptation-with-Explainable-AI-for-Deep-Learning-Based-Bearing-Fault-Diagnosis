# model_utils.py
import tensorflow as tf
from tensorflow.keras import layers, models, losses, optimizers
import tensorflow.keras.backend as K

# -------------------------------
# CNN 1D Model
# -------------------------------
def build_cnn1d(input_shape, num_classes):
    inputs = layers.Input(shape=input_shape)

    x = layers.Conv1D(32, kernel_size=7, padding='same', activation='relu')(inputs)
    x = layers.BatchNormalization()(x)
    x = layers.MaxPooling1D(pool_size=2)(x)

    x = layers.Conv1D(64, kernel_size=5, padding='same', activation='relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.MaxPooling1D(pool_size=2)(x)

    x = layers.Conv1D(128, kernel_size=3, padding='same', activation='relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.GlobalAveragePooling1D()(x)

    x = layers.Dense(64, activation='relu')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(num_classes, activation='softmax')(x)

    model = models.Model(inputs=inputs, outputs=outputs)
    return model

# -------------------------------
# CNN 2D Model
# -------------------------------
def build_cnn2d(input_shape, num_classes):
    inputs = layers.Input(shape=input_shape)

    x = layers.Conv2D(16, (3,3), padding='same', activation='relu')(inputs)
    x = layers.MaxPooling2D((2,2), padding='same')(x)

    x = layers.Conv2D(32, (3,3), padding='same', activation='relu')(x)
    x = layers.MaxPooling2D((2,2), padding='same')(x)

    x = layers.Conv2D(64, (3,3), padding='same', activation='relu')(x)
    x = layers.MaxPooling2D((2,2), padding='same')(x)

    x = layers.Conv2D(128, (3,3), padding='same', activation='relu')(x)
    x = layers.MaxPooling2D((2,2), padding='same')(x)

    x = layers.Flatten()(x)
    x = layers.Dense(100, activation='relu')(x)
    x = layers.Dense(50, activation='relu')(x)
    outputs = layers.Dense(num_classes, activation='softmax')(x)

    model = models.Model(inputs=inputs, outputs=outputs)
    return model


# -------------------------------
# MMD Loss
# -------------------------------
def mmd_loss(source_features, target_features, kernel_mul=2.0, kernel_num=5, fix_sigma=None):
    """Compute Maximum Mean Discrepancy (MMD) loss between source and target features."""
    batch_size = int(source_features.shape[0])
    x = source_features
    y = target_features

    def gaussian_kernel_matrix(x, y):
        x_size = tf.shape(x)[0]
        y_size = tf.shape(y)[0]
        dim = tf.shape(x)[1]
        xx = tf.reshape(tf.reduce_sum(tf.square(x), axis=1), [x_size, 1])
        yy = tf.reshape(tf.reduce_sum(tf.square(y), axis=1), [1, y_size])
        xy = tf.matmul(x, tf.transpose(y))
        dist = xx + yy - 2.0 * xy
        if fix_sigma:
            bandwidth = fix_sigma
        else:
            bandwidth = tf.reduce_sum(dist) / tf.cast(x_size * y_size, tf.float32)
        bandwidth_list = [bandwidth * (kernel_mul ** i) for i in range(kernel_num)]
        kernel_val = [tf.exp(-dist / b) for b in bandwidth_list]
        return tf.add_n(kernel_val)
    
    k_xx = gaussian_kernel_matrix(x, x)
    k_yy = gaussian_kernel_matrix(y, y)
    k_xy = gaussian_kernel_matrix(x, y)
    loss = tf.reduce_mean(k_xx) + tf.reduce_mean(k_yy) - 2*tf.reduce_mean(k_xy)
    return loss

# -------------------------------
# CORAL Loss
# -------------------------------
def coral_loss(source, target):
    """Compute CORAL loss between source and target features."""
    d = tf.cast(tf.shape(source)[1], tf.float32)
    # Covariance
    xm = source - tf.reduce_mean(source, axis=0, keepdims=True)
    xc = tf.matmul(tf.transpose(xm), xm) / (tf.cast(tf.shape(source)[0]-1, tf.float32))
    xmt = target - tf.reduce_mean(target, axis=0, keepdims=True)
    xt = tf.matmul(tf.transpose(xmt), xmt) / (tf.cast(tf.shape(target)[0]-1, tf.float32))
    loss = tf.reduce_sum(tf.square(xc - xt)) / (4.0 * d * d)
    return loss

# -------------------------------
# Custom Training Step (for DA)
# -------------------------------
class DAModel(tf.keras.Model):
    def __init__(self, base_model, mmd_weight=0.0, coral_weight=0.0):
        super(DAModel, self).__init__()
        self.base_model = base_model
        self.mmd_weight = mmd_weight
        self.coral_weight = coral_weight
        self.loss_fn = losses.SparseCategoricalCrossentropy()
        self.acc_metric = tf.keras.metrics.SparseCategoricalAccuracy()

    def compile(self, optimizer):
        super(DAModel, self).compile()
        self.optimizer = optimizer

    def train_step(self, data):
        (x_s, y_s), (x_t, _) = data
        with tf.GradientTape() as tape:
            s_feats = self.base_model.layers[:-1][0](x_s) if False else self.base_model(x_s, training=True)
            t_feats = self.base_model.layers[:-1][0](x_t) if False else self.base_model(x_t, training=True)
            y_pred = self.base_model(x_s, training=True)
            ce_loss = self.loss_fn(y_s, y_pred)
            mmd = mmd_loss(s_feats, t_feats) if self.mmd_weight>0 else 0.0
            coral = coral_loss(s_feats, t_feats) if self.coral_weight>0 else 0.0
            total_loss = ce_loss + self.mmd_weight*mmd + self.coral_weight*coral
        grads = tape.gradient(total_loss, self.base_model.trainable_variables)
        self.optimizer.apply_gradients(zip(grads, self.base_model.trainable_variables))
        self.acc_metric.update_state(y_s, y_pred)
        return {"loss": total_loss, "acc": self.acc_metric.result()}

    def test_step(self, data):
        x, y = data
        y_pred = self.base_model(x, training=False)
        loss = self.loss_fn(y, y_pred)
        self.acc_metric.update_state(y, y_pred)
        return {"loss": loss, "acc": self.acc_metric.result()}
