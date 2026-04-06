# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 22:48:30 2025

@author: hg-tester
"""

import os
import scipy.io




def ImportData_PD_Condition1():
  folder_path = '/content/drive/MyDrive/Condition1'
  # X99_normal = scipy.io.loadmat('content/drive/MyDrive/BearingData_CaseWestern/99.mat')['X099_DE_time']
  file_path1 = os.path.join(folder_path, 'PD_C1_K001_1.mat')
  K001_1_normal = scipy.io.loadmat(file_path1)['PD_C1_K001_1']

  # X111_InnerRace_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/111.mat')['X111_DE_time']
  file_path2 = os.path.join(folder_path, 'PD_C1_KI01_1.mat')
  KI01_1_Inner  = scipy.io.loadmat(file_path2)['PD_C1_KI01_1']

  # X137_Outer_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/137.mat')['X137_DE_time']
  file_path3 = os.path.join(folder_path, 'PD_C1_KA01_1.mat')
  KA01_1_Outer = scipy.io.loadmat(file_path3)['PD_C1_KA01_1']

  return [K001_1_normal,KI01_1_Inner,KA01_1_Outer]

def ImportData_CWRU_LHP2_48K():
  folder_path = '/content/drive/MyDrive/BearingData_CaseWestern_48K1750'
  # X99_normal = scipy.io.loadmat('content/drive/MyDrive/BearingData_CaseWestern/99.mat')['X099_DE_time']
  file_path1 = os.path.join(folder_path, '99.mat')
  X99_normal = scipy.io.loadmat(file_path1)['X099_DE_time']

  # X111_InnerRace_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/111.mat')['X111_DE_time']
  file_path2 = os.path.join(folder_path, '111.mat')
  X111_InnerRace_007  = scipy.io.loadmat(file_path2)['X111_DE_time']

  # X124_Ball_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/124.mat')['X124_DE_time']
  file_path3 = os.path.join(folder_path, '124.mat')
  X124_Ball_007 = scipy.io.loadmat(file_path3)['X124_DE_time']

  # X137_Outer_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/137.mat')['X137_DE_time']
  file_path4 = os.path.join(folder_path, '137.mat')
  X137_Outer_007 = scipy.io.loadmat(file_path4)['X137_DE_time']

  # X176_InnerRace_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/176.mat')['X176_DE_time']
  file_path5 = os.path.join(folder_path, '176.mat')
  X176_InnerRace_014 = scipy.io.loadmat(file_path5)['X176_DE_time']

  # X191_Ball_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/191.mat')['X191_DE_time']
  file_path6 = os.path.join(folder_path, '191.mat')
  X191_Ball_014 = scipy.io.loadmat(file_path6)['X191_DE_time']

  # X203_Outer_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/203.mat')['X203_DE_time']
  file_path7 = os.path.join(folder_path, '203.mat')
  X203_Outer_014  = scipy.io.loadmat(file_path7)['X203_DE_time']

  #  X215_InnerRace_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/215.mat')['X215_DE_time']
  file_path8 = os.path.join(folder_path, '215.mat')
  X215_InnerRace_021  = scipy.io.loadmat(file_path8)['X215_DE_time']

  # X228_Ball_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/228.mat')['X228_DE_time']
  file_path9 = os.path.join(folder_path, '228.mat')
  X228_Ball_021  = scipy.io.loadmat(file_path9)['X228_DE_time']

  # X240_Outer_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/240.mat')['X240_DE_time']
  file_path10 = os.path.join(folder_path, '240.mat')
  X240_Outer_021  = scipy.io.loadmat(file_path10)['X240_DE_time']

  return [X99_normal,X111_InnerRace_007,X124_Ball_007,X137_Outer_007,X176_InnerRace_014,X191_Ball_014,X203_Outer_014,X215_InnerRace_021,X228_Ball_021,X240_Outer_021]

def ImportData_CWRU_LHP1_48K():
  folder_path = '/content/drive/MyDrive/BearingData_CaseWestern_48K1772'
  # X99_normal = scipy.io.loadmat('content/drive/MyDrive/BearingData_CaseWestern/99.mat')['X099_DE_time']
  file_path1 = os.path.join(folder_path, '98.mat')
  X98_normal = scipy.io.loadmat(file_path1)['X098_DE_time']

  # X111_InnerRace_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/111.mat')['X111_DE_time']
  file_path2 = os.path.join(folder_path, '110.mat')
  X110_InnerRace_007  = scipy.io.loadmat(file_path2)['X110_DE_time']

  # X124_Ball_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/124.mat')['X124_DE_time']
  file_path3 = os.path.join(folder_path, '123.mat')
  X123_Ball_007 = scipy.io.loadmat(file_path3)['X123_DE_time']

  # X137_Outer_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/137.mat')['X137_DE_time']
  file_path4 = os.path.join(folder_path, '136.mat')
  X136_Outer_007 = scipy.io.loadmat(file_path4)['X136_DE_time']

  # X176_InnerRace_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/176.mat')['X176_DE_time']
  file_path5 = os.path.join(folder_path, '175.mat')
  X175_InnerRace_014 = scipy.io.loadmat(file_path5)['X175_DE_time']

  # X191_Ball_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/191.mat')['X191_DE_time']
  file_path6 = os.path.join(folder_path, '190.mat')
  X190_Ball_014 = scipy.io.loadmat(file_path6)['X190_DE_time']

  # X203_Outer_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/203.mat')['X203_DE_time']
  file_path7 = os.path.join(folder_path, '202.mat')
  X202_Outer_014  = scipy.io.loadmat(file_path7)['X202_DE_time']

  #  X215_InnerRace_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/215.mat')['X215_DE_time']
  file_path8 = os.path.join(folder_path, '214.mat')
  X214_InnerRace_021  = scipy.io.loadmat(file_path8)['X214_DE_time']

  # X228_Ball_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/228.mat')['X228_DE_time']
  file_path9 = os.path.join(folder_path, '227.mat')
  X227_Ball_021  = scipy.io.loadmat(file_path9)['X227_DE_time']

  # X240_Outer_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/240.mat')['X240_DE_time']
  file_path10 = os.path.join(folder_path, '239.mat')
  X239_Outer_021  = scipy.io.loadmat(file_path10)['X239_DE_time']

  return [X98_normal,X110_InnerRace_007,X123_Ball_007,X136_Outer_007,X175_InnerRace_014,X190_Ball_014,X202_Outer_014,X214_InnerRace_021,X227_Ball_021,X239_Outer_021]

def ImportData_CWRU_LHP3_48K():
  folder_path = '/content/drive/MyDrive/BearingData_CaseWestern_48K1730'
  # X99_normal = scipy.io.loadmat('content/drive/MyDrive/BearingData_CaseWestern/99.mat')['X099_DE_time']
  file_path1 = os.path.join(folder_path, '100.mat')
  X100_normal = scipy.io.loadmat(file_path1)['X100_DE_time']

  # X111_InnerRace_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/111.mat')['X111_DE_time']
  file_path2 = os.path.join(folder_path, '112.mat')
  X112_InnerRace_007  = scipy.io.loadmat(file_path2)['X112_DE_time']

  # X124_Ball_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/124.mat')['X124_DE_time']
  file_path3 = os.path.join(folder_path, '125.mat')
  X125_Ball_007 = scipy.io.loadmat(file_path3)['X125_DE_time']

  # X137_Outer_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/137.mat')['X137_DE_time']
  file_path4 = os.path.join(folder_path, '138.mat')
  X138_Outer_007 = scipy.io.loadmat(file_path4)['X138_DE_time']

  # X176_InnerRace_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/176.mat')['X176_DE_time']
  file_path5 = os.path.join(folder_path, '177.mat')
  X177_InnerRace_014 = scipy.io.loadmat(file_path5)['X177_DE_time']

  # X191_Ball_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/191.mat')['X191_DE_time']
  file_path6 = os.path.join(folder_path, '192.mat')
  X192_Ball_014 = scipy.io.loadmat(file_path6)['X192_DE_time']

  # X203_Outer_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/203.mat')['X203_DE_time']
  file_path7 = os.path.join(folder_path, '204.mat')
  X204_Outer_014  = scipy.io.loadmat(file_path7)['X204_DE_time']

  #  X215_InnerRace_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/215.mat')['X215_DE_time']
  file_path8 = os.path.join(folder_path, '217.mat')
  X217_InnerRace_021  = scipy.io.loadmat(file_path8)['X217_DE_time']

  # X228_Ball_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/228.mat')['X228_DE_time']
  file_path9 = os.path.join(folder_path, '229.mat')
  X229_Ball_021  = scipy.io.loadmat(file_path9)['X229_DE_time']

  # X240_Outer_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/240.mat')['X240_DE_time']
  file_path10 = os.path.join(folder_path, '241.mat')
  X241_Outer_021  = scipy.io.loadmat(file_path10)['X241_DE_time']

  return [X100_normal,X112_InnerRace_007,X125_Ball_007,X138_Outer_007,X177_InnerRace_014,X192_Ball_014,X204_Outer_014,X217_InnerRace_021,X229_Ball_021,X241_Outer_021]

# def ImportData_CWRU_LHP0_48K():
#   folder_path = '../../Classification_of_bearing_faults_using_ML-main/BearingData_CaseWestern/CWRU_LHP0_48K1797'
#   # X99_normal = scipy.io.loadmat('content/drive/MyDrive/BearingData_CaseWestern/99.mat')['X099_DE_time']
#   file_path1 = os.path.join(folder_path, '97.mat')
#   X97_normal = scipy.io.loadmat(file_path1)['X097_DE_time']

#   # X111_InnerRace_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/111.mat')['X111_DE_time']
#   file_path2 = os.path.join(folder_path, '109.mat')
#   X109_InnerRace_007  = scipy.io.loadmat(file_path2)['X109_DE_time']

#   # X124_Ball_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/124.mat')['X124_DE_time']
#   file_path3 = os.path.join(folder_path, '122.mat')
#   X122_Ball_007 = scipy.io.loadmat(file_path3)['X122_DE_time']

#   # X137_Outer_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/137.mat')['X137_DE_time']
#   file_path4 = os.path.join(folder_path, '135.mat')
#   X135_Outer_007 = scipy.io.loadmat(file_path4)['X135_DE_time']

#   # X176_InnerRace_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/176.mat')['X176_DE_time']
#   file_path5 = os.path.join(folder_path, '173.mat')
#   X173_InnerRace_014 = scipy.io.loadmat(file_path5)['X173_DE_time']

#   # X191_Ball_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/191.mat')['X191_DE_time']
#   file_path6 = os.path.join(folder_path, '189.mat')
#   X189_Ball_014 = scipy.io.loadmat(file_path6)['X189_DE_time']

#   # X203_Outer_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/203.mat')['X203_DE_time']
#   file_path7 = os.path.join(folder_path, '201.mat')
#   X201_Outer_014  = scipy.io.loadmat(file_path7)['X201_DE_time']

#   #  X215_InnerRace_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/215.mat')['X215_DE_time']
#   file_path8 = os.path.join(folder_path, '213.mat')
#   X213_InnerRace_021  = scipy.io.loadmat(file_path8)['X213_DE_time']

#   # X228_Ball_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/228.mat')['X228_DE_time']
#   file_path9 = os.path.join(folder_path, '226.mat')
#   X226_Ball_021  = scipy.io.loadmat(file_path9)['X226_DE_time']

#   # X240_Outer_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/240.mat')['X240_DE_time']
#   file_path10 = os.path.join(folder_path, '238.mat')
#   X238_Outer_021  = scipy.io.loadmat(file_path10)['X238_DE_time']

#   return [X97_normal,X109_InnerRace_007,X122_Ball_007,X135_Outer_007,X173_InnerRace_014,X189_Ball_014,X201_Outer_014,X213_InnerRace_021,X226_Ball_021,X238_Outer_021]

def ImportData_CWRU_LHP2_12K():
  folder_path = '/content/drive/MyDrive/BearingData_CaseWestern_12K1750'
  # X99_normal = scipy.io.loadmat('content/drive/MyDrive/BearingData_CaseWestern/99.mat')['X099_DE_time']
  file_path1 = os.path.join(folder_path, '99.mat')
  X99_normal = scipy.io.loadmat(file_path1)['X099_DE_time']

  # X111_InnerRace_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/111.mat')['X111_DE_time']
  file_path2 = os.path.join(folder_path, '107.mat')
  X107_InnerRace_007  = scipy.io.loadmat(file_path2)['X107_DE_time']

  # X124_Ball_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/124.mat')['X124_DE_time']
  file_path3 = os.path.join(folder_path, '120.mat')
  X120_Ball_007 = scipy.io.loadmat(file_path3)['X120_DE_time']

  # X137_Outer_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/137.mat')['X137_DE_time']
  file_path4 = os.path.join(folder_path, '132.mat')
  X132_Outer_007 = scipy.io.loadmat(file_path4)['X132_DE_time']

  # X176_InnerRace_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/176.mat')['X176_DE_time']
  file_path5 = os.path.join(folder_path, '171.mat')
  X171_InnerRace_014 = scipy.io.loadmat(file_path5)['X171_DE_time']

  # X191_Ball_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/191.mat')['X191_DE_time']
  file_path6 = os.path.join(folder_path, '187.mat')
  X187_Ball_014 = scipy.io.loadmat(file_path6)['X187_DE_time']

  # X203_Outer_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/203.mat')['X203_DE_time']
  file_path7 = os.path.join(folder_path, '199.mat')
  X199_Outer_014  = scipy.io.loadmat(file_path7)['X199_DE_time']

  #  X215_InnerRace_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/215.mat')['X215_DE_time']
  file_path8 = os.path.join(folder_path, '211.mat')
  X211_InnerRace_021  = scipy.io.loadmat(file_path8)['X211_DE_time']

  # X228_Ball_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/228.mat')['X228_DE_time']
  file_path9 = os.path.join(folder_path, '224.mat')
  X224_Ball_021  = scipy.io.loadmat(file_path9)['X224_DE_time']

  # X240_Outer_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/240.mat')['X240_DE_time']
  file_path10 = os.path.join(folder_path, '236.mat')
  X236_Outer_021  = scipy.io.loadmat(file_path10)['X236_DE_time']

  return [X99_normal,X107_InnerRace_007,X120_Ball_007,X132_Outer_007,X171_InnerRace_014,X187_Ball_014,X199_Outer_014,X211_InnerRace_021,X224_Ball_021,X236_Outer_021]

def ImportData_CWRU_LHP0_12K():
  folder_path = '/content/drive/MyDrive/BearingData_CaseWestern_12K1797'
  # X99_normal = scipy.io.loadmat('content/drive/MyDrive/BearingData_CaseWestern/99.mat')['X099_DE_time']
  file_path1 = os.path.join(folder_path, '97.mat')
  X97_normal = scipy.io.loadmat(file_path1)['X097_DE_time']

  # X111_InnerRace_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/111.mat')['X111_DE_time']
  file_path2 = os.path.join(folder_path, '105.mat')
  X105_InnerRace_007  = scipy.io.loadmat(file_path2)['X105_DE_time']

  # X124_Ball_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/124.mat')['X124_DE_time']
  file_path3 = os.path.join(folder_path, '118.mat')
  X118_Ball_007 = scipy.io.loadmat(file_path3)['X118_DE_time']

  # X137_Outer_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/137.mat')['X137_DE_time']
  file_path4 = os.path.join(folder_path, '130.mat')
  X130_Outer_007 = scipy.io.loadmat(file_path4)['X130_DE_time']

  # X176_InnerRace_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/176.mat')['X176_DE_time']
  file_path5 = os.path.join(folder_path, '169.mat')
  X169_InnerRace_014 = scipy.io.loadmat(file_path5)['X169_DE_time']

  # X191_Ball_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/191.mat')['X191_DE_time']
  file_path6 = os.path.join(folder_path, '185.mat')
  X185_Ball_014 = scipy.io.loadmat(file_path6)['X185_DE_time']

  # X203_Outer_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/203.mat')['X203_DE_time']
  file_path7 = os.path.join(folder_path, '197.mat')
  X197_Outer_014  = scipy.io.loadmat(file_path7)['X197_DE_time']

  #  X215_InnerRace_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/215.mat')['X215_DE_time']
  file_path8 = os.path.join(folder_path, '209.mat')
  X209_InnerRace_021  = scipy.io.loadmat(file_path8)['X209_DE_time']

  # X228_Ball_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/228.mat')['X228_DE_time']
  file_path9 = os.path.join(folder_path, '222.mat')
  X222_Ball_021  = scipy.io.loadmat(file_path9)['X222_DE_time']

  # X240_Outer_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/240.mat')['X240_DE_time']
  file_path10 = os.path.join(folder_path, '234.mat')
  X234_Outer_021  = scipy.io.loadmat(file_path10)['X234_DE_time']

  return [X97_normal,X105_InnerRace_007,X118_Ball_007,X130_Outer_007,X169_InnerRace_014,X185_Ball_014,X197_Outer_014,X209_InnerRace_021,X222_Ball_021,X234_Outer_021]

def ImportData_CWRU_LHP1_12K():
  folder_path = '/content/drive/MyDrive/BearingData_CaseWestern_12K1772'
  # X99_normal = scipy.io.loadmat('content/drive/MyDrive/BearingData_CaseWestern/99.mat')['X099_DE_time']
  file_path1 = os.path.join(folder_path, '98.mat')
  X98_normal = scipy.io.loadmat(file_path1)['X098_DE_time']

  # X111_InnerRace_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/111.mat')['X111_DE_time']
  file_path2 = os.path.join(folder_path, '106.mat')
  X106_InnerRace_007  = scipy.io.loadmat(file_path2)['X106_DE_time']

  # X124_Ball_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/124.mat')['X124_DE_time']
  file_path3 = os.path.join(folder_path, '119.mat')
  X119_Ball_007 = scipy.io.loadmat(file_path3)['X119_DE_time']

  # X137_Outer_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/137.mat')['X137_DE_time']
  file_path4 = os.path.join(folder_path, '131.mat')
  X131_Outer_007 = scipy.io.loadmat(file_path4)['X131_DE_time']

  # X176_InnerRace_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/176.mat')['X176_DE_time']
  file_path5 = os.path.join(folder_path, '170.mat')
  X170_InnerRace_014 = scipy.io.loadmat(file_path5)['X170_DE_time']

  # X191_Ball_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/191.mat')['X191_DE_time']
  file_path6 = os.path.join(folder_path, '186.mat')
  X186_Ball_014 = scipy.io.loadmat(file_path6)['X186_DE_time']

  # X203_Outer_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/203.mat')['X203_DE_time']
  file_path7 = os.path.join(folder_path, '198.mat')
  X198_Outer_014  = scipy.io.loadmat(file_path7)['X198_DE_time']

  #  X215_InnerRace_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/215.mat')['X215_DE_time']
  file_path8 = os.path.join(folder_path, '210.mat')
  X210_InnerRace_021  = scipy.io.loadmat(file_path8)['X210_DE_time']

  # X228_Ball_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/228.mat')['X228_DE_time']
  file_path9 = os.path.join(folder_path, '223.mat')
  X223_Ball_021  = scipy.io.loadmat(file_path9)['X223_DE_time']

  # X240_Outer_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/240.mat')['X240_DE_time']
  file_path10 = os.path.join(folder_path, '235.mat')
  X235_Outer_021  = scipy.io.loadmat(file_path10)['X235_DE_time']

  return [X98_normal,X106_InnerRace_007,X119_Ball_007,X131_Outer_007,X170_InnerRace_014,X186_Ball_014,X198_Outer_014,X210_InnerRace_021,X223_Ball_021,X235_Outer_021]

def ImportData_CWRU_LHP3_12K():
  folder_path = '/content/drive/MyDrive/BearingData_CaseWestern_12K1730'
  # X99_normal = scipy.io.loadmat('content/drive/MyDrive/BearingData_CaseWestern/99.mat')['X099_DE_time']
  file_path1 = os.path.join(folder_path, '100.mat')
  X100_normal = scipy.io.loadmat(file_path1)['X100_DE_time']

  # X111_InnerRace_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/111.mat')['X111_DE_time']
  file_path2 = os.path.join(folder_path, '108.mat')
  X108_InnerRace_007  = scipy.io.loadmat(file_path2)['X108_DE_time']

  # X124_Ball_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/124.mat')['X124_DE_time']
  file_path3 = os.path.join(folder_path, '121.mat')
  X121_Ball_007 = scipy.io.loadmat(file_path3)['X121_DE_time']

  # X137_Outer_007 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/137.mat')['X137_DE_time']
  file_path4 = os.path.join(folder_path, '133.mat')
  X133_Outer_007 = scipy.io.loadmat(file_path4)['X133_DE_time']

  # X176_InnerRace_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/176.mat')['X176_DE_time']
  file_path5 = os.path.join(folder_path, '172.mat')
  X172_InnerRace_014 = scipy.io.loadmat(file_path5)['X172_DE_time']

  # X191_Ball_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/191.mat')['X191_DE_time']
  file_path6 = os.path.join(folder_path, '188.mat')
  X188_Ball_014 = scipy.io.loadmat(file_path6)['X188_DE_time']

  # X203_Outer_014 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/203.mat')['X203_DE_time']
  file_path7 = os.path.join(folder_path, '200.mat')
  X200_Outer_014  = scipy.io.loadmat(file_path7)['X200_DE_time']

  #  X215_InnerRace_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/215.mat')['X215_DE_time']
  file_path8 = os.path.join(folder_path, '212.mat')
  X212_InnerRace_021  = scipy.io.loadmat(file_path8)['X212_DE_time']

  # X228_Ball_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/228.mat')['X228_DE_time']
  file_path9 = os.path.join(folder_path, '225.mat')
  X225_Ball_021  = scipy.io.loadmat(file_path9)['X225_DE_time']

  # X240_Outer_021 = scipy.io.loadmat('/content/drive/MyDrive/BearingData_CaseWestern/240.mat')['X240_DE_time']
  file_path10 = os.path.join(folder_path, '237.mat')
  X237_Outer_021  = scipy.io.loadmat(file_path10)['X237_DE_time']

  return [X100_normal,X108_InnerRace_007,X121_Ball_007,X133_Outer_007,X172_InnerRace_014,X188_Ball_014,X200_Outer_014,X212_InnerRace_021,X225_Ball_021,X237_Outer_021]