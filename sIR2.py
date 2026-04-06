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




##3 2nd NOL.PY

# -*- coding: utf-8 -*-
"""
# -----------------------------------------------------------------------------
Created on Tue Aug 13 23:41:44 2024

@author: YLiu
# -----------------------------------------------------------------------------
"""

"""
# -----------------------------------------------------------------------------
# Setup Initial Python Code for Reproducibility
# -----------------------------------------------------------------------------
"""

import tensorflow as tf
import numpy as np
import random
import os

# Set a fixed seed value for reproducibility
SEED = 1
random.seed(SEED)            # Python random module
np.random.seed(SEED)         # NumPy
tf.random.set_seed(SEED)     # TensorFlow

# Enforce deterministic behavior for GPU operations
os.environ['TF_DETERMINISTIC_OPS'] = '1'  # Ensure deterministic execution
os.environ['TF_CUDNN_DETERMINISTIC'] = '1'  # Deterministic cuDNN algorithms

# Control GPU memory allocation (prevents TensorFlow from using all GPU memory)
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)  # Enable memory growth

# Restrict parallelism (ensures consistent execution order)
tf.config.threading.set_inter_op_parallelism_threads(1)
tf.config.threading.set_intra_op_parallelism_threads(1)


# import os
import scipy.io 
# import numpy as np
from sklearn.model_selection import train_test_split #, KFold
from sklearn.metrics import confusion_matrix
# import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import seaborn as sns 
# import pandas as pd

from scipy import signal
from skimage.transform import resize
from sklearn.model_selection import StratifiedKFold
from scipy.signal import resample_poly

from CWRU_data import ImportData_CWRU_LHP0_12K

"""
# -----------------------------------------------------------------------------
# Read CWRU Bearing Data (Load - 2HP)
# -----------------------------------------------------------------------------
"""
"""
def ImportData():
  folder_path = '../../Classification_of_bearing_faults_using_ML-main/BearingData_CaseWestern/CWRU_LHP2_48K' 
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
"""

"""
# -----------------------------------------------------------------------------
# Data Processing and Feature Extraction
# -----------------------------------------------------------------------------
"""
# def Sampling(Data, interval_length, samples_per_block):
#     No_of_blocks = (round(len(Data)/interval_length) - round(samples_per_block/interval_length) - 1)
#     SplitData = np.zeros([No_of_blocks, samples_per_block])
#     for i in range(No_of_blocks):
#         SplitData[i,:] = Data[i*interval_length:(i*interval_length)+samples_per_block].T
#     return SplitData

def Sampling(Data, interval_length, samples_per_block, ignore_points=0):
    # Adjust data length to ignore the first and last 'ignore_points'
    adjusted_length = len(Data) - 2 * ignore_points
    # Adjust the number of blocks
    No_of_blocks = (round(adjusted_length / interval_length) - round(samples_per_block / interval_length) - 1)
    SplitData = np.zeros([No_of_blocks, samples_per_block])
    
    for i in range(No_of_blocks):
        # Skip the first 'ignore_points' and start sampling from that position
        start_idx = ignore_points + i * interval_length
        SplitData[i, :] = Data[start_idx:(start_idx + samples_per_block)].T
    
    return SplitData


def DataPreparation(Data, interval_length, samples_per_block):
  for count,i in enumerate(Data):
    SplitData = Sampling(i, interval_length, samples_per_block)
    y = np.zeros([len(SplitData),10])
    y[:,count] = 1
    y1 = np.zeros([len(SplitData),1])
    y1[:,0] = count
    # Stack up and label the data   
    if count==0:
      X = SplitData
      LabelPositional = y
      Label = y1
    else:
      X = np.append(X, SplitData, axis=0)
      LabelPositional = np.append(LabelPositional,y,axis=0)
      Label = np.append(Label,y1,axis=0)
  return X, LabelPositional, Label


def min_max_norm(ary):
    ary = (ary - ary.min()) / np.abs(ary.max() - ary.min())
    return ary


def generate_spectrogram_image(data_y_vector, image_shape):
    """
    Calculate the spectrogram of an array data_y_vector and resize it in 
    the image_shape resolution
    """
    fs = 48000
    # data_y_vector_len = np.shape(data_y_vector)[0]

    f, t, sxx = signal.spectrogram(
        data_y_vector,
        fs)

    sxx = min_max_norm(sxx)
    sxx = resize(sxx, image_shape, mode='constant', anti_aliasing=True)

    return sxx

def resample_48K_to_12K(signal_48K):
    """
    Resample a 1D signal from 48 kHz to 12 kHz using polyphase resampling.
    Assumes signal_48k is a 1D numpy array.
    """
    # downsample by factor 4 -> up=1, down=4
    sig_12K = resample_poly(signal_48K, up=1, down=4)
    return sig_12K

Data = ImportData_CWRU_LHP0_12K()
data_12K = resample_48K_to_12K(Data[0])
Data[0] = data_12K

interval_length = 400 #320 #290 #200  
samples_per_block = 400 #1650-25*2


# Y_CNN is of shape (n, 10) representing 10 classes as 10 columns. In each sample, for the class to which it belongs, 
# the corresponding column value is marked 1 and the rest as 0, facilitating Softmax implementation in CNN 
# Y is of shape (m, 1) where column values are between 0 and 9 representing the classes directly. - 1-hot encoding
X, Y_CNN, Y = DataPreparation(Data, interval_length, samples_per_block) 


print('Shape of Input Data =', X.shape)
print('Shape of Label Y_CNN =', Y_CNN.shape)
print('Shape of Label Y =', Y.shape)

# XX = {'X':X}
# scipy.io.savemat('Data.mat', XX)

"""
# -----------------------------------------------------------------------------
# Multiclass Classification CNN Model Training
# -----------------------------------------------------------------------------
"""

# k-fold cross validation 
kSplits = 5
# kfold = KFold(n_splits=kSplits, random_state=42, shuffle=True)
kfold = StratifiedKFold(n_splits=kSplits, random_state=42, shuffle=True)

## 2-Dimensional Convolutional Neural Network Classification

# Reshape the data - 2 dimensional feed 
Input_2D = X.reshape([-1,20,20,1])

# Input_2D = X_image.reshape([-1,96,96,1])
print(Input_2D.shape)

# Test-Train Split 
X_2D_train, X_2D_test, y_2D_train, y_2D_test, y_label_train, y_label_test = train_test_split(Input_2D, Y_CNN, Y, train_size=0.8, test_size=0.2, random_state=42, stratify=Y)
# X_2D_train, X_2D_test, y_2D_train, y_2D_test = train_test_split(Input_2D, Y_CNN, train_size=0.8, test_size=0.2, random_state=42, shuffle=True)

# Define the CNN Classification model
"""
class CNN_2D():
  def __init__(self):
    self.model = self.CreateModel()

  def CreateModel(self):
    model = models.Sequential([
        # layers.Conv2D(filters=16, kernel_size=(3,3), strides=(2,2), padding ='same',activation='relu'),
        layers.Conv2D(filters=16, kernel_size=(3,3), padding='same',activation='relu', input_shape=(20,20,1)),
        layers.MaxPool2D(pool_size=(2,2), padding='same'),
        layers.Conv2D(filters=32, kernel_size=(3,3), padding ='same',activation='relu'),
        layers.MaxPool2D(pool_size=(2,2), padding='same'),
        layers.Conv2D(filters=64, kernel_size=(3,3),padding ='same', activation='relu'),
        layers.MaxPool2D(pool_size=(2,2), padding='same'),
        layers.Conv2D(filters=128, kernel_size=(3,3),padding ='same', activation='relu'),
        layers.MaxPool2D(pool_size=(2,2), padding='same'),
        layers.Flatten(),
        layers.InputLayer(),
        layers.Dense(100,activation='relu'),
        layers.Dense(50,activation='relu'),
        # layers.Dense(64,activation='relu'),
        layers.Dense(10),
        layers.Softmax()
        ])
    model.compile(optimizer='adam',
              loss=tf.keras.losses.CategoricalCrossentropy(),
              metrics=['accuracy'])
    return model
"""

class CNN_2D():
  def __init__(self):
    self.model = self.CreateModel()

  def CreateModel(self):
    model = models.Sequential([
        # layers.Conv2D(filters=16, kernel_size=(3,3), strides=(2,2), padding ='same',activation='relu'),
        layers.Conv2D(filters=16, kernel_size=(3,3), padding='same',activation='relu', input_shape=(20,20,1)),
        layers.BatchNormalization(),
        # layers.Activation('relu'),
        layers.MaxPooling2D((2,2)),                
        # layers.MaxPool2D(pool_size=(2,2), padding='same'),
        layers.Conv2D(filters=32, kernel_size=(3,3), padding ='same',activation='relu'),
        layers.BatchNormalization(),
        # layers.Activation('relu'),
        layers.MaxPooling2D((2,2)),
        # layers.MaxPool2D(pool_size=(2,2), padding='same'),
        layers.Conv2D(filters=64, kernel_size=(3,3),padding ='same', activation='relu'),
        layers.BatchNormalization(),
        # layers.Activation('relu'),
        layers.MaxPooling2D((2,2)),                
        # layers.MaxPool2D(pool_size=(2,2), padding='same'),
        layers.Conv2D(filters=128, kernel_size=(3,3),padding ='same', activation='relu'),
        layers.BatchNormalization(),
        # layers.Activation('relu'),
        # layers.MaxPooling2D((2,2)),        
        # layers.MaxPool2D(pool_size=(2,2), padding='same'),
        # layers.Flatten(),
        layers.GlobalAveragePooling2D(),
        layers.Dense(100,activation='relu'),
        layers.Dense(50,activation='relu'),
        # layers.Dense(64,activation='relu'),
        layers.Dropout(0.4),
        # layers.Dense(10),
        # layers.Softmax()
        layers.Dense(10,activation='softmax')
        ])
    model.compile(optimizer='adam',
              loss=tf.keras.losses.CategoricalCrossentropy(),
              metrics=['accuracy'])
    return model


# File path name to save best models
# foldername = "CNN2D_TS_LHP1_12K_NOL_exp1n/"
foldername = "/content/drive/MyDrive/CNN2D_TS_CWRU_12K_NOL_LHP0/"
os.makedirs(foldername, exist_ok=True)

from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import load_model

accuracy_train = []
accuracy_val = []
accuracy_test = []
pred_all_val = np.zeros([len(X_2D_train),10])
y_2D_val = np.zeros([len(X_2D_train),10])
kfold_test_len = []

fl1 = 0
k = 1

early_stop = EarlyStopping(monitor='val_accuracy', patience=50, restore_best_weights=True)

# Train the model 
# for train, test in kfold.split(X_2D_train,y_2D_train):
for fold, (train, test) in enumerate(kfold.split(X_2D_train, y_label_train)):    

  # Define where to save the best model
  checkpoint_filepath = foldername + "best_model_" + str(k) + ".h5"
    
  # Create a ModelCheckpoint callback
  checkpoint = ModelCheckpoint(
      filepath=checkpoint_filepath,
      monitor='val_accuracy',  # Monitor validation accuracy
      save_best_only=True,  # Save only the best model
      mode='max',  # Maximize accuracy
      verbose=1
  )        

  Classification_2D = CNN_2D()
  # history = Classification_2D.model.fit(X_2D_train[train], y_2D_train[train], verbose=1, epochs=50) #epochs=12
  history = Classification_2D.model.fit(
        X_2D_train[train], y_2D_train[train],
        validation_data=(X_2D_train[test], y_2D_train[test]),  # Validation set for monitoring
        epochs=200,
        verbose=1,
        callbacks=[checkpoint, early_stop]  # Save the best model
  )
  
  print("Best model saved at:", checkpoint_filepath)
  CNN_2D_best_model = load_model(checkpoint_filepath)
  print("Best model loaded successfully!")
  
  fl2 = fl1 + len(test)
  pred_all_val[fl1:fl2,:] = CNN_2D_best_model.predict(X_2D_train[test])
  y_2D_val[fl1:fl2,:] = y_2D_train[test]
  kfold_test_len.append(fl2-fl1)
  fl1 = fl2  

  # Evaluate the accuracy of the model on the training set 
  train_loss, train_accuracy = CNN_2D_best_model.evaluate(X_2D_train[train], y_2D_train[train]) 
  accuracy_train.append(train_accuracy)
  
  # Evaluate the accuracy of the model on the validation set 
  val_loss, val_accuracy = CNN_2D_best_model.evaluate(X_2D_train[test], y_2D_train[test]) 
  accuracy_val.append(val_accuracy)
  
  # Evaluate the accuracy of the model on the validation set 
  test_loss, test_accuracy = CNN_2D_best_model.evaluate(X_2D_test, y_2D_test) 
  accuracy_test.append(test_accuracy)  
  
  # Evaluate the accuracy of the model on the training set 
  # kf_loss, kf_accuracy = Classification_2D.model.evaluate(X_2D_train[test], y_2D_train[test]) 
  # accuracy_2D.append(kf_accuracy)
  
  k = k + 1

"""
# -----------------------------------------------------------------------------
# Multiclass Classification CNN Model Evaluation
# -----------------------------------------------------------------------------
"""

# Classification_2D.model.summary()

CNN_2D_train_accuracy = np.average(accuracy_train)*100
print('CNN 2D train accuracy =', CNN_2D_train_accuracy)
# print(accuracy_train)

CNN_2D_val_accuracy = np.average(accuracy_val)*100
print('CNN 2D validation accuracy =', CNN_2D_val_accuracy)
# print(accuracy_val)

CNN_2D_test_accuracy = np.average(accuracy_test)*100
print('CNN 2D test accuracy =', CNN_2D_test_accuracy)
# print(accuracy_test)

# Evaluate the accuracy of the model on the test set
# CNN_2D_test_loss, CNN_2D_test_accuracy = Classification_2D.model.evaluate(X_2D_test, y_2D_test)
# CNN_2D_test_accuracy*=100
# print('CNN 2D test accuracy =', CNN_2D_test_accuracy)


def ConfusionMatrix(Model, X, y):
  y_pred = np.argmax(Model.predict(X), axis=1)
  ConfusionMat = confusion_matrix(np.argmax(y, axis=1), y_pred)
  return ConfusionMat

# Plot results - CNN 2D
plt.figure(5)
plt.title('Confusion Matrix - CNN 2D Train') 
sns.heatmap(
    ConfusionMatrix(CNN_2D_best_model, X_2D_train, y_2D_train),
    annot=True, fmt='d', annot_kws={"fontsize":8}, cmap="YlGnBu"
)
plt.tight_layout()
plt.savefig(foldername + "confusion_matrix_train.png", dpi=300)
plt.show()

plt.figure(6)
plt.title('Confusion Matrix - CNN 2D Test') 
sns.heatmap(
    ConfusionMatrix(CNN_2D_best_model, X_2D_test, y_2D_test),
    annot=True, fmt='d', annot_kws={"fontsize":8}, cmap="YlGnBu"
)
plt.tight_layout()
plt.savefig(foldername + "confusion_matrix_test.png", dpi=300)
plt.show()


plt.figure(7)
plt.title('Train - Accuracy - CNN 2D')
plt.bar(np.arange(1,kSplits+1), [i*100 for i in accuracy_val])
plt.ylabel('accuracy')
plt.xlabel('folds')
plt.ylim([70,100])
plt.tight_layout()
plt.savefig(foldername + "fold_validation_accuracy.png", dpi=300)
plt.show()

plt.figure(8)
plt.title('Train vs Test Accuracy - CNN 2D')
plt.bar([1,2], [CNN_2D_train_accuracy, CNN_2D_test_accuracy])
plt.ylabel('accuracy')
plt.xlabel('folds')
plt.xticks([1,2], ['Train', 'Test'])
plt.ylim([70,100])
plt.tight_layout()
plt.savefig(foldername + "train_vs_test_accuracy.png", dpi=300)
plt.show()

# ==========================================
# ROBUST 2D Grad-CAM for CNN_2D_best_model
# ==========================================

import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# ------------------------------------------
# 0) Output folder
# ------------------------------------------
gradcam_dir = os.path.join(foldername, "gradcam_results")
os.makedirs(gradcam_dir, exist_ok=True)

# ------------------------------------------
# 1) Prepare labels and predictions
# ------------------------------------------
y_true = y_2D_test
if len(y_2D_test.shape) > 1 and y_2D_test.shape[-1] > 1:
    y_true = np.argmax(y_2D_test, axis=1)

pred_probs = CNN_2D_best_model.predict(X_2D_test, verbose=0)
y_pred = np.argmax(pred_probs, axis=1)

correct_idx = np.where(y_pred == y_true)[0]
wrong_idx   = np.where(y_pred != y_true)[0]

print("Correct:", len(correct_idx), " Misclassified:", len(wrong_idx))

if len(correct_idx) == 0:
    print("No correct samples found.")
if len(wrong_idx) == 0:
    print("No misclassified samples found.")

# ------------------------------------------
# 2) Find last Conv2D layer
# ------------------------------------------
def get_last_conv2d_layer_name(model):
    for layer in reversed(model.layers):
        if isinstance(layer, tf.keras.layers.Conv2D):
            return layer.name
    raise ValueError("No Conv2D layer found in model.")

LAST_CONV_LAYER = get_last_conv2d_layer_name(CNN_2D_best_model)
print("Using last conv layer:", LAST_CONV_LAYER)

# ------------------------------------------
# 3) Build robust Grad-CAM models
# ------------------------------------------
last_conv_layer = CNN_2D_best_model.get_layer(LAST_CONV_LAYER)

# input -> last conv output
conv_model = tf.keras.Model(
    inputs=CNN_2D_best_model.inputs,
    outputs=last_conv_layer.output
)

# last conv output -> final prediction
classifier_input = tf.keras.Input(shape=last_conv_layer.output.shape[1:])

x = classifier_input
start_collecting = False
for layer in CNN_2D_best_model.layers:
    if layer.name == LAST_CONV_LAYER:
        start_collecting = True
        continue
    if start_collecting:
        x = layer(x)

classifier_model = tf.keras.Model(classifier_input, x)

# ------------------------------------------
# 4) Compute 2D Grad-CAM
# ------------------------------------------
def compute_gradcam_2d(img_batch, class_idx=None):
    """
    img_batch: shape (1, H, W, C)
    returns heatmap: shape (H, W) in [0,1]
    """
    img_batch = tf.cast(img_batch, tf.float32)

    with tf.GradientTape() as tape:
        conv_out = conv_model(img_batch, training=False)
        tape.watch(conv_out)

        preds = classifier_model(conv_out, training=False)

        if class_idx is None:
            class_idx = int(tf.argmax(preds[0]))
        else:
            class_idx = int(class_idx)

        loss = preds[:, class_idx]

    grads = tape.gradient(loss, conv_out)

    if grads is None:
        raise ValueError("Gradients are None. Grad-CAM could not be computed.")

    # conv_out: (1,h,w,c), grads: (1,h,w,c)
    conv_out = conv_out[0]
    grads = grads[0]

    # Global average pooling over spatial dims
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1))   # (c,)

    # Weighted combination of channels
    heatmap = tf.reduce_sum(conv_out * pooled_grads, axis=-1)   # (h,w)

    heatmap = tf.maximum(heatmap, 0)
    heatmap = heatmap / (tf.reduce_max(heatmap) + 1e-9)
    heatmap = heatmap.numpy()

    # Resize to input image size
    H, W = img_batch.shape[1], img_batch.shape[2]
    if heatmap.shape != (H, W):
        heatmap = tf.image.resize(heatmap[..., None], (H, W)).numpy().squeeze()

    return heatmap, class_idx

# ------------------------------------------
# 5) Plot function
# ------------------------------------------
def plot_gradcam_triplet(img, heatmap, true_label, pred_label, title, save_path):
    img2 = img[:, :, 0] if img.ndim == 3 else img

    plt.figure(figsize=(12, 4))

    ax1 = plt.subplot(1, 3, 1)
    im1 = ax1.imshow(img2, cmap="gray")
    ax1.set_title(f"{title}\nTrue={true_label}, Pred={pred_label}")
    plt.colorbar(im1, ax=ax1, fraction=0.046, pad=0.04)

    ax2 = plt.subplot(1, 3, 2)
    im2 = ax2.imshow(heatmap, cmap="jet", vmin=0, vmax=1)
    ax2.set_title("Grad-CAM heatmap")
    plt.colorbar(im2, ax=ax2, fraction=0.046, pad=0.04)

    ax3 = plt.subplot(1, 3, 3)
    ax3.imshow(img2, cmap="gray")
    im3 = ax3.imshow(heatmap, cmap="jet", alpha=0.45, vmin=0, vmax=1)
    ax3.set_title("Overlay")
    plt.colorbar(im3, ax=ax3, fraction=0.046, pad=0.04)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()
    print("Saved:", save_path)

# ------------------------------------------
# 6) Generate multiple correct + wrong samples
# ------------------------------------------
N_SHOW = 10

correct_samples = correct_idx[:N_SHOW]
wrong_samples   = wrong_idx[:N_SHOW]

print("\n--- Generating Grad-CAM for CORRECT samples ---")
for idx in correct_samples:
    img_batch = X_2D_test[idx:idx+1]
    true_label = int(y_true[idx])
    pred_label = int(y_pred[idx])

    heatmap, _ = compute_gradcam_2d(img_batch, class_idx=pred_label)

    save_path = os.path.join(
        gradcam_dir,
        f"gradcam_correct_idx{idx}_true{true_label}_pred{pred_label}.png"
    )
    plot_gradcam_triplet(
        img_batch[0], heatmap, true_label, pred_label,
        "Correct sample (Grad-CAM)", save_path
    )

print("\n--- Generating Grad-CAM for MISCLASSIFIED samples ---")
for idx in wrong_samples:
    img_batch = X_2D_test[idx:idx+1]
    true_label = int(y_true[idx])
    pred_label = int(y_pred[idx])

    heatmap, _ = compute_gradcam_2d(img_batch, class_idx=pred_label)

    save_path = os.path.join(
        gradcam_dir,
        f"gradcam_wrong_idx{idx}_true{true_label}_pred{pred_label}.png"
    )
    plot_gradcam_triplet(
        img_batch[0], heatmap, true_label, pred_label,
        "Misclassified sample (Grad-CAM)", save_path
    )

print("\nRobust 2D Grad-CAM completed.")


# ==========================================
# SHAP FOR 2D CNN
# ==========================================

import os
import numpy as np
import shap
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import shutil

# ------------------------------------------
# 0) Output folder
# ------------------------------------------
shap_dir = os.path.join(foldername, "shap_results")

if os.path.exists(shap_dir):
    shutil.rmtree(shap_dir)

os.makedirs(shap_dir, exist_ok=True)

# ------------------------------------------
# 1) Predictions + labels
# ------------------------------------------
y_true = y_2D_test
if len(y_2D_test.shape) > 1 and y_2D_test.shape[-1] > 1:
    y_true = np.argmax(y_2D_test, axis=1)

pred_probs = CNN_2D_best_model.predict(X_2D_test, verbose=0)
y_pred = np.argmax(pred_probs, axis=1)

correct_idx = np.where(y_pred == y_true)[0]
wrong_idx = np.where(y_pred != y_true)[0]

print("Correct samples:", len(correct_idx))
print("Misclassified samples:", len(wrong_idx))

# ------------------------------------------
# 2) Confusion matrix
# ------------------------------------------
cm = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap="YlGnBu")
plt.title("Confusion Matrix - 2D CNN (SHAP Analysis Set)")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.tight_layout()
plt.savefig(os.path.join(shap_dir, "confusion_matrix_shap_2dcnn.png"), dpi=300)
plt.show()

# ------------------------------------------
# 3) Background data for SHAP
# ------------------------------------------
np.random.seed(1)
bg_size = min(50, len(X_2D_train))
bg_idx = np.random.choice(len(X_2D_train), size=bg_size, replace=False)
background = X_2D_train[bg_idx]

print("Background shape:", background.shape)

# ------------------------------------------
# 4) SHAP explainer
# ------------------------------------------
explainer = shap.GradientExplainer(CNN_2D_best_model, background)

# ------------------------------------------
# 5) Helper: get SHAP values for one sample
# ------------------------------------------
def get_single_sample_shap_2d(sample, pred_label):
    """
    sample shape: (1, 20, 20, 1)
    pred_label: int
    returns shap values shape: (20, 20)
    """
    shap_values = explainer.shap_values(sample)

    if isinstance(shap_values, list):
        sv = shap_values[pred_label][0, :, :, 0]
    else:
        sv = np.array(shap_values)

        if sv.ndim == 5 and sv.shape[0] == 1:
            sv = sv[0, :, :, 0, pred_label]
        elif sv.ndim == 5 and sv.shape[1] == 1:
            sv = sv[pred_label, 0, :, :, 0]
        elif sv.ndim == 4:
            sv = sv[0, :, :, 0]
        else:
            sv = sv.reshape(sample.shape[1], sample.shape[2])

    return sv

# ------------------------------------------
# 6) Convert 2D sample + SHAP back to 1D
# ------------------------------------------
def flatten_2d_to_1d(img_2d):
    if img_2d.ndim == 3:
        img_2d = img_2d[:, :, 0]
    return img_2d.reshape(-1)

# ------------------------------------------
# 7) Plot SHAP in 1D signal style
# ------------------------------------------
def save_shap_signal_plot_from_2d(img_2d, shap_2d, true_label, pred_label, save_path, title):
    """
    img_2d: shape (20,20) or (20,20,1)
    shap_2d: shape (20,20)
    """
    signal_1d = flatten_2d_to_1d(img_2d)
    shap_1d = flatten_2d_to_1d(shap_2d)

    x = np.arange(len(signal_1d))

    fig, axes = plt.subplots(3, 1, figsize=(12, 8), sharex=True)

    # Original signal
    axes[0].plot(x, signal_1d, linewidth=1)
    axes[0].set_title(f"{title}\nTrue={true_label}, Pred={pred_label}")
    axes[0].set_ylabel("Amplitude")
    axes[0].grid(True, alpha=0.3)

    # SHAP values band
    max_abs = np.max(np.abs(shap_1d)) + 1e-9
    im = axes[1].imshow(
        shap_1d.reshape(1, -1),
        aspect='auto',
        cmap='coolwarm',
        vmin=-max_abs,
        vmax=max_abs,
        extent=[0, len(signal_1d), 0, 1]
    )
    axes[1].set_title("SHAP Importance")
    axes[1].set_yticks([])
    plt.colorbar(im, ax=axes[1], fraction=0.02, pad=0.02)

    # Overlay
    ymin, ymax = signal_1d.min(), signal_1d.max()
    axes[2].plot(x, signal_1d, color='black', linewidth=1, alpha=0.85)
    axes[2].imshow(
        shap_1d.reshape(1, -1),
        aspect='auto',
        cmap='coolwarm',
        alpha=0.35,
        vmin=-max_abs,
        vmax=max_abs,
        extent=[0, len(signal_1d), ymin, ymax]
    )
    axes[2].set_title("Signal + SHAP Overlay")
    axes[2].set_xlabel("Time Index")
    axes[2].set_ylabel("Amplitude")
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()
    print("Saved:", save_path)

# ------------------------------------------
# 8) Generate MULTIPLE SHAP examples per class
# ------------------------------------------
N_PER_CLASS_SHAP = 3
print("Generating multiple SHAP examples per class...")

classes = np.unique(y_true)

for cls in classes:
    cls = int(cls)

    cls_correct_idx = np.where((y_true == cls) & (y_pred == cls))[0][:N_PER_CLASS_SHAP]
    cls_wrong_idx = np.where((y_true == cls) & (y_pred != cls))[0][:N_PER_CLASS_SHAP]

    correct_cls_dir = os.path.join(shap_dir, f"class_{cls}", "correct")
    wrong_cls_dir = os.path.join(shap_dir, f"class_{cls}", "misclassified")
    os.makedirs(correct_cls_dir, exist_ok=True)
    os.makedirs(wrong_cls_dir, exist_ok=True)

    # Correct examples
    for j, idx_c in enumerate(cls_correct_idx):
        idx_c = int(idx_c)
        sample_c = X_2D_test[idx_c:idx_c+1]
        img_c = sample_c[0]
        true_c = int(y_true[idx_c])
        pred_c = int(y_pred[idx_c])

        shap_c = get_single_sample_shap_2d(sample_c, pred_c)

        save_c = os.path.join(
            correct_cls_dir,
            f"shap_correct_idx{idx_c}_true{true_c}_pred{pred_c}_{j+1}.png"
        )

        save_shap_signal_plot_from_2d(
            img_c,
            shap_c,
            true_c,
            pred_c,
            save_c,
            f"Correct Sample (SHAP) | Class {cls}"
        )

    # Misclassified examples
    for j, idx_w in enumerate(cls_wrong_idx):
        idx_w = int(idx_w)
        sample_w = X_2D_test[idx_w:idx_w+1]
        img_w = sample_w[0]
        true_w = int(y_true[idx_w])
        pred_w = int(y_pred[idx_w])

        shap_w = get_single_sample_shap_2d(sample_w, pred_w)

        save_w = os.path.join(
            wrong_cls_dir,
            f"shap_wrong_idx{idx_w}_true{true_w}_pred{pred_w}_{j+1}.png"
        )

        save_shap_signal_plot_from_2d(
            img_w,
            shap_w,
            true_w,
            pred_w,
            save_w,
            f"Misclassified Sample (SHAP) | True Class {cls}"
        )

print("Multiple SHAP sample generation completed.")

# ------------------------------------------
# 9) SHAP summary on a few test samples
# ------------------------------------------
summary_n = min(20, len(X_2D_test))
summary_samples = X_2D_test[:summary_n]
summary_preds = y_pred[:summary_n]

summary_shap = explainer.shap_values(summary_samples)

summary_maps = []
for i in range(summary_n):
    pred_cls = summary_preds[i]

    if isinstance(summary_shap, list):
        sv_i = summary_shap[pred_cls][i, :, :, 0]
    else:
        sv = np.array(summary_shap)
        if sv.ndim == 5 and sv.shape[0] == summary_n:
            sv_i = sv[i, :, :, 0, pred_cls]
        elif sv.ndim == 5 and sv.shape[0] != summary_n:
            sv_i = sv[pred_cls, i, :, :, 0]
        elif sv.ndim == 4:
            sv_i = sv[i, :, :, 0]
        else:
            sv_i = sv[i].reshape(summary_samples.shape[1], summary_samples.shape[2])

    summary_maps.append(sv_i)

summary_maps = np.array(summary_maps)
summary_input = summary_samples[:, :, :, 0]

summary_matrix = summary_maps.reshape(summary_n, -1)
summary_input_flat = summary_input.reshape(summary_n, -1)

shap.summary_plot(summary_matrix, summary_input_flat, show=False)
plt.savefig(os.path.join(shap_dir, "shap_summary_plot_2dcnn.png"), dpi=300, bbox_inches='tight')
plt.show()

print("\n2D CNN SHAP analysis completed.")


# ==========================================
# STATISTICAL ANALYSIS OF 2D CNN FEATURE VECTORS
# ==========================================

import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import shutil

from tensorflow.keras.models import Model
from scipy.stats import skew, kurtosis, entropy

# ------------------------------------------
# 0) Output folder
# ------------------------------------------
stats_dir = os.path.join(foldername, "feature_statistics_2d")

if os.path.exists(stats_dir):
    shutil.rmtree(stats_dir)

os.makedirs(stats_dir, exist_ok=True)

# ------------------------------------------
# 1) Identify Conv2D layers
# ------------------------------------------
conv_layer_names = []
for layer in CNN_2D_best_model.layers:
    if isinstance(layer, tf.keras.layers.Conv2D):
        conv_layer_names.append(layer.name)

print("Conv2D layers found:", conv_layer_names)

if len(conv_layer_names) < 2:
    raise ValueError("Need at least 2 Conv2D layers for this analysis.")

LAYER1_NAME = conv_layer_names[0]
LAYER2_NAME = conv_layer_names[1]

print("Using Layer 1:", LAYER1_NAME)
print("Using Layer 2:", LAYER2_NAME)

# ------------------------------------------
# 2) Build feature extractor models
# ------------------------------------------
model_conv1 = Model(
    inputs=CNN_2D_best_model.inputs,
    outputs=CNN_2D_best_model.get_layer(LAYER1_NAME).output
)

model_conv2 = Model(
    inputs=CNN_2D_best_model.inputs,
    outputs=CNN_2D_best_model.get_layer(LAYER2_NAME).output
)
# ------------------------------------------
# 3) Prepare labels/predictions
# ------------------------------------------
y_true = y_2D_test
if len(y_2D_test.shape) > 1 and y_2D_test.shape[-1] > 1:
    y_true = np.argmax(y_2D_test, axis=1)

pred_probs = CNN_2D_best_model.predict(X_2D_test, verbose=0)
y_pred = np.argmax(pred_probs, axis=1)

correct_idx = np.where(y_pred == y_true)[0]
wrong_idx = np.where(y_pred != y_true)[0]

print("Correct samples:", len(correct_idx))
print("Misclassified samples:", len(wrong_idx))

# ------------------------------------------
# 4) Helper functions
# ------------------------------------------
def compute_feature_statistics_2d(feature_maps):
    """
    feature_maps shape: (1, H, W, C)
    returns:
        stats_array shape: (C, 6)
    """
    fmap = feature_maps[0]
    stats = []

    for i in range(fmap.shape[-1]):
        vec = fmap[:, :, i].flatten()

        mean_val = np.mean(vec)
        var_val = np.var(vec)
        skew_val = skew(vec)
        kurt_val = kurtosis(vec)
        energy_val = np.sum(vec ** 2)

        hist, _ = np.histogram(vec, bins=20, density=True)
        ent_val = entropy(hist + 1e-8)

        stats.append([mean_val, var_val, skew_val, kurt_val, energy_val, ent_val])

    return np.array(stats)

def save_feature_map_grid_2d(feature_maps, layer_name, save_path, max_maps=16):
    fmap = feature_maps[0]
    n_maps = min(fmap.shape[-1], max_maps)

    rows = int(np.ceil(n_maps / 4))
    plt.figure(figsize=(12, 3 * rows))

    for i in range(n_maps):
        plt.subplot(rows, 4, i + 1)
        plt.imshow(fmap[:, :, i], cmap="viridis")
        plt.title(f"Map {i}")
        plt.axis("off")

    plt.suptitle(f"Feature Maps - {layer_name}")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()

def save_all_activation_histogram_2d(feature_maps, layer_name, save_path):
    fmap = feature_maps[0].flatten()

    plt.figure(figsize=(7, 5))
    plt.hist(fmap, bins=50)
    plt.title(f"All Activation Histogram - {layer_name}")
    plt.xlabel("Activation Value")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()

def save_filter_histogram_grid_2d(feature_maps, layer_name, save_path, max_maps=16):
    fmap = feature_maps[0]
    n_maps = min(fmap.shape[-1], max_maps)

    rows = int(np.ceil(n_maps / 4))
    plt.figure(figsize=(12, 3 * rows))

    for i in range(n_maps):
        plt.subplot(rows, 4, i + 1)
        plt.hist(fmap[:, :, i].flatten(), bins=30)
        plt.title(f"F{i}")

    plt.suptitle(f"Filter Histograms - {layer_name}")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()

def save_statistics_heatmap_2d(stats_array, layer_name, save_path):
    stat_names = ["Mean", "Variance", "Skewness", "Kurtosis", "Energy", "Entropy"]

    plt.figure(figsize=(10, 6))
    sns.heatmap(stats_array, cmap="viridis", xticklabels=stat_names)
    plt.title(f"Feature Statistics Heatmap - {layer_name}")
    plt.xlabel("Statistic")
    plt.ylabel("Feature Map")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()

def save_energy_bar_2d(stats_array, layer_name, save_path):
    energy_vals = stats_array[:, 4]

    plt.figure(figsize=(8, 5))
    plt.bar(np.arange(len(energy_vals)), energy_vals)
    plt.title(f"Feature Map Energy - {layer_name}")
    plt.xlabel("Feature Map")
    plt.ylabel("Energy")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()

def save_correct_vs_wrong_hist_2d(correct_feat, wrong_feat, layer_name, save_path):
    plt.figure(figsize=(8, 5))
    plt.hist(correct_feat.flatten(), bins=40, alpha=0.6, label="Correct")
    plt.hist(wrong_feat.flatten(), bins=40, alpha=0.6, label="Misclassified")
    plt.title(f"Correct vs Misclassified Histogram - {layer_name}")
    plt.xlabel("Activation Value")
    plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()

def save_correct_vs_wrong_boxplot_2d(correct_stats, wrong_stats, layer_name, save_path):
    df = pd.DataFrame({
        "Energy": np.concatenate([correct_stats[:, 4], wrong_stats[:, 4]]),
        "Type": ["Correct"] * len(correct_stats[:, 4]) + ["Misclassified"] * len(wrong_stats[:, 4])
    })

    plt.figure(figsize=(7, 5))
    sns.boxplot(data=df, x="Type", y="Energy")
    plt.title(f"Correct vs Misclassified Energy - {layer_name}")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()

def save_layer_comparison_bar_2d(stats1, stats2, layer1_name, layer2_name, save_path):
    mean_energy_1 = np.mean(stats1[:, 4])
    mean_energy_2 = np.mean(stats2[:, 4])

    plt.figure(figsize=(6, 5))
    plt.bar([layer1_name, layer2_name], [mean_energy_1, mean_energy_2])
    plt.title("Mean Feature Energy Across Layers")
    plt.ylabel("Mean Energy")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()

# ------------------------------------------
# 5) Extract one correct and one misclassified sample
# ------------------------------------------
if len(correct_idx) == 0:
    raise ValueError("No correct sample found for statistical analysis.")
if len(wrong_idx) == 0:
    print("No misclassified sample found. Correct-vs-misclassified plots will be skipped.")

correct_sample = X_2D_test[correct_idx[0]:correct_idx[0] + 1]
feat1_correct = model_conv1.predict(correct_sample, verbose=0)
feat2_correct = model_conv2.predict(correct_sample, verbose=0)

stats1_correct = compute_feature_statistics_2d(feat1_correct)
stats2_correct = compute_feature_statistics_2d(feat2_correct)

if len(wrong_idx) > 0:
    wrong_sample = X_2D_test[wrong_idx[0]:wrong_idx[0] + 1]
    feat1_wrong = model_conv1.predict(wrong_sample, verbose=0)
    feat2_wrong = model_conv2.predict(wrong_sample, verbose=0)

    stats1_wrong = compute_feature_statistics_2d(feat1_wrong)
    stats2_wrong = compute_feature_statistics_2d(feat2_wrong)

# ------------------------------------------
# 6) Save plots for Layer 1
# ------------------------------------------
layer1_dir = os.path.join(stats_dir, LAYER1_NAME)
os.makedirs(layer1_dir, exist_ok=True)

save_feature_map_grid_2d(
    feat1_correct,
    LAYER1_NAME,
    os.path.join(layer1_dir, "feature_map_grid.png")
)

save_all_activation_histogram_2d(
    feat1_correct,
    LAYER1_NAME,
    os.path.join(layer1_dir, "all_activation_histogram.png")
)

save_filter_histogram_grid_2d(
    feat1_correct,
    LAYER1_NAME,
    os.path.join(layer1_dir, "filter_histogram_grid.png")
)

save_statistics_heatmap_2d(
    stats1_correct,
    LAYER1_NAME,
    os.path.join(layer1_dir, "statistics_heatmap.png")
)

save_energy_bar_2d(
    stats1_correct,
    LAYER1_NAME,
    os.path.join(layer1_dir, "energy_bar.png")
)

if len(wrong_idx) > 0:
    save_correct_vs_wrong_hist_2d(
        feat1_correct,
        feat1_wrong,
        LAYER1_NAME,
        os.path.join(layer1_dir, "correct_vs_wrong_histogram.png")
    )

    save_correct_vs_wrong_boxplot_2d(
        stats1_correct,
        stats1_wrong,
        LAYER1_NAME,
        os.path.join(layer1_dir, "correct_vs_wrong_boxplot.png")
    )

# ------------------------------------------
# 7) Save plots for Layer 2
# ------------------------------------------
layer2_dir = os.path.join(stats_dir, LAYER2_NAME)
os.makedirs(layer2_dir, exist_ok=True)

save_feature_map_grid_2d(
    feat2_correct,
    LAYER2_NAME,
    os.path.join(layer2_dir, "feature_map_grid.png")
)

save_all_activation_histogram_2d(
    feat2_correct,
    LAYER2_NAME,
    os.path.join(layer2_dir, "all_activation_histogram.png")
)

save_filter_histogram_grid_2d(
    feat2_correct,
    LAYER2_NAME,
    os.path.join(layer2_dir, "filter_histogram_grid.png")
)

save_statistics_heatmap_2d(
    stats2_correct,
    LAYER2_NAME,
    os.path.join(layer2_dir, "statistics_heatmap.png")
)

save_energy_bar_2d(
    stats2_correct,
    LAYER2_NAME,
    os.path.join(layer2_dir, "energy_bar.png")
)

if len(wrong_idx) > 0:
    save_correct_vs_wrong_hist_2d(
        feat2_correct,
        feat2_wrong,
        LAYER2_NAME,
        os.path.join(layer2_dir, "correct_vs_wrong_histogram.png")
    )

    save_correct_vs_wrong_boxplot_2d(
        stats2_correct,
        stats2_wrong,
        LAYER2_NAME,
        os.path.join(layer2_dir, "correct_vs_wrong_boxplot.png")
    )

# ------------------------------------------
# 8) Layer comparison plot
# ------------------------------------------
save_layer_comparison_bar_2d(
    stats1_correct,
    stats2_correct,
    LAYER1_NAME,
    LAYER2_NAME,
    os.path.join(stats_dir, "layer_energy_comparison.png")
)

print("\nStatistical analysis of 2D CNN feature vectors completed.")
print("Results saved in:", stats_dir)


## NOL_Test.py

# -*- coding: utf-8 -*-
"""
# -----------------------------------------------------------------------------
Created on Tue Aug 13 23:41:44 2024

@author: YLiu
# -----------------------------------------------------------------------------
"""

"""
# -----------------------------------------------------------------------------
# Setup Initial Python Code for Reproducibility
# -----------------------------------------------------------------------------
"""

import tensorflow as tf
import numpy as np
import random
import os

# Set a fixed seed value for reproducibility
SEED = 1
random.seed(SEED)            # Python random module
np.random.seed(SEED)         # NumPy
tf.random.set_seed(SEED)     # TensorFlow

# Enforce deterministic behavior for GPU operations
os.environ['TF_DETERMINISTIC_OPS'] = '1'  # Ensure deterministic execution
os.environ['TF_CUDNN_DETERMINISTIC'] = '1'  # Deterministic cuDNN algorithms

# Control GPU memory allocation (prevents TensorFlow from using all GPU memory)
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)  # Enable memory growth

# Restrict parallelism (ensures consistent execution order)
tf.config.threading.set_inter_op_parallelism_threads(1)
tf.config.threading.set_intra_op_parallelism_threads(1)


# import os
import scipy.io 
# import numpy as np
from sklearn.model_selection import train_test_split #, KFold
from sklearn.metrics import confusion_matrix
# import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import seaborn as sns 
# import pandas as pd

from scipy import signal
from skimage.transform import resize
from sklearn.model_selection import StratifiedKFold
from scipy.signal import resample_poly

from CWRU_data import ImportData_CWRU_LHP2_12K

"""
# -----------------------------------------------------------------------------
# Read CWRU Bearing Data (Load - 2HP)
# -----------------------------------------------------------------------------
"""
"""
def ImportData():
  folder_path = '../../Classification_of_bearing_faults_using_ML-main/BearingData_CaseWestern/CWRU_LHP2_48K' 
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
"""

"""
# -----------------------------------------------------------------------------
# Data Processing and Feature Extraction
# -----------------------------------------------------------------------------
"""
# def Sampling(Data, interval_length, samples_per_block):
#     No_of_blocks = (round(len(Data)/interval_length) - round(samples_per_block/interval_length) - 1)
#     SplitData = np.zeros([No_of_blocks, samples_per_block])
#     for i in range(No_of_blocks):
#         SplitData[i,:] = Data[i*interval_length:(i*interval_length)+samples_per_block].T
#     return SplitData

def Sampling(Data, interval_length, samples_per_block, ignore_points=0):
    # Adjust data length to ignore the first and last 'ignore_points'
    adjusted_length = len(Data) - 2 * ignore_points
    # Adjust the number of blocks
    No_of_blocks = (round(adjusted_length / interval_length) - round(samples_per_block / interval_length) - 1)
    SplitData = np.zeros([No_of_blocks, samples_per_block])
    
    for i in range(No_of_blocks):
        # Skip the first 'ignore_points' and start sampling from that position
        start_idx = ignore_points + i * interval_length
        SplitData[i, :] = Data[start_idx:(start_idx + samples_per_block)].T
    
    return SplitData


def DataPreparation(Data, interval_length, samples_per_block):
  for count,i in enumerate(Data):
    SplitData = Sampling(i, interval_length, samples_per_block)
    y = np.zeros([len(SplitData),10])
    y[:,count] = 1
    y1 = np.zeros([len(SplitData),1])
    y1[:,0] = count
    # Stack up and label the data   
    if count==0:
      X = SplitData
      LabelPositional = y
      Label = y1
    else:
      X = np.append(X, SplitData, axis=0)
      LabelPositional = np.append(LabelPositional,y,axis=0)
      Label = np.append(Label,y1,axis=0)
  return X, LabelPositional, Label


def min_max_norm(ary):
    ary = (ary - ary.min()) / np.abs(ary.max() - ary.min())
    return ary


def generate_spectrogram_image(data_y_vector, image_shape):
    """
    Calculate the spectrogram of an array data_y_vector and resize it in 
    the image_shape resolution
    """
    fs = 48000
    # data_y_vector_len = np.shape(data_y_vector)[0]

    f, t, sxx = signal.spectrogram(
        data_y_vector,
        fs)

    sxx = min_max_norm(sxx)
    sxx = resize(sxx, image_shape, mode='constant', anti_aliasing=True)

    return sxx

def resample_48K_to_12K(signal_48K):
    """
    Resample a 1D signal from 48 kHz to 12 kHz using polyphase resampling.
    Assumes signal_48k is a 1D numpy array.
    """
    # downsample by factor 4 -> up=1, down=4
    sig_12K = resample_poly(signal_48K, up=1, down=4)
    return sig_12K

Data = ImportData_CWRU_LHP2_12K()
data_12K = resample_48K_to_12K(Data[0])
Data[0] = data_12K

interval_length = 400 #320 #290 #200  
samples_per_block = 400 #1650-25*2


# Y_CNN is of shape (n, 10) representing 10 classes as 10 columns. In each sample, for the class to which it belongs, 
# the corresponding column value is marked 1 and the rest as 0, facilitating Softmax implementation in CNN 
# Y is of shape (m, 1) where column values are between 0 and 9 representing the classes directly. - 1-hot encoding
X, Y_CNN, Y = DataPreparation(Data, interval_length, samples_per_block) 


print('Shape of Input Data =', X.shape)
print('Shape of Label Y_CNN =', Y_CNN.shape)
print('Shape of Label Y =', Y.shape)

# XX = {'X':X}
# scipy.io.savemat('Data.mat', XX)

"""
# -----------------------------------------------------------------------------
# Multiclass Classification CNN Model Training
# -----------------------------------------------------------------------------
"""

# k-fold cross validation 
kSplits = 5
# kfold = KFold(n_splits=kSplits, random_state=42, shuffle=True)
kfold = StratifiedKFold(n_splits=kSplits, random_state=42, shuffle=True)

## 2-Dimensional Convolutional Neural Network Classification

# Reshape the data - 2 dimensional feed 
Input_2D = X.reshape([-1,20,20,1])

# Input_2D = X_image.reshape([-1,96,96,1])
print(Input_2D.shape)

# Test-Train Split 
X_2D_train, X_2D_test, y_2D_train, y_2D_test, y_label_train, y_label_test = train_test_split(Input_2D, Y_CNN, Y, train_size=0.8, test_size=0.2, random_state=42, stratify=Y)
# X_2D_train, X_2D_test, y_2D_train, y_2D_test = train_test_split(Input_2D, Y_CNN, train_size=0.8, test_size=0.2, random_state=42, shuffle=True)

# Define the CNN Classification model
"""
class CNN_2D():
  def __init__(self):
    self.model = self.CreateModel()

  def CreateModel(self):
    model = models.Sequential([
        # layers.Conv2D(filters=16, kernel_size=(3,3), strides=(2,2), padding ='same',activation='relu'),
        layers.Conv2D(filters=16, kernel_size=(3,3), padding='same',activation='relu', input_shape=(20,20,1)),
        layers.MaxPool2D(pool_size=(2,2), padding='same'),
        layers.Conv2D(filters=32, kernel_size=(3,3), padding ='same',activation='relu'),
        layers.MaxPool2D(pool_size=(2,2), padding='same'),
        layers.Conv2D(filters=64, kernel_size=(3,3),padding ='same', activation='relu'),
        layers.MaxPool2D(pool_size=(2,2), padding='same'),
        layers.Conv2D(filters=128, kernel_size=(3,3),padding ='same', activation='relu'),
        layers.MaxPool2D(pool_size=(2,2), padding='same'),
        layers.Flatten(),
        layers.InputLayer(),
        layers.Dense(100,activation='relu'),
        layers.Dense(50,activation='relu'),
        # layers.Dense(64,activation='relu'),
        layers.Dense(10),
        layers.Softmax()
        ])
    model.compile(optimizer='adam',
              loss=tf.keras.losses.CategoricalCrossentropy(),
              metrics=['accuracy'])
    return model
"""

class CNN_2D():
  def __init__(self):
    self.model = self.CreateModel()

  def CreateModel(self):
    model = models.Sequential([
        # layers.Conv2D(filters=16, kernel_size=(3,3), strides=(2,2), padding ='same',activation='relu'),
        layers.Conv2D(filters=16, kernel_size=(3,3), padding='same',activation='relu', input_shape=(20,20,1)),
        layers.BatchNormalization(),
        # layers.Activation('relu'),
        layers.MaxPooling2D((2,2)),                
        # layers.MaxPool2D(pool_size=(2,2), padding='same'),
        layers.Conv2D(filters=32, kernel_size=(3,3), padding ='same',activation='relu'),
        layers.BatchNormalization(),
        # layers.Activation('relu'),
        layers.MaxPooling2D((2,2)),
        # layers.MaxPool2D(pool_size=(2,2), padding='same'),
        layers.Conv2D(filters=64, kernel_size=(3,3),padding ='same', activation='relu'),
        layers.BatchNormalization(),
        # layers.Activation('relu'),
        layers.MaxPooling2D((2,2)),                
        # layers.MaxPool2D(pool_size=(2,2), padding='same'),
        layers.Conv2D(filters=128, kernel_size=(3,3),padding ='same', activation='relu'),
        layers.BatchNormalization(),
        # layers.Activation('relu'),
        # layers.MaxPooling2D((2,2)),        
        # layers.MaxPool2D(pool_size=(2,2), padding='same'),
        # layers.Flatten(),
        layers.GlobalAveragePooling2D(),
        layers.Dense(100,activation='relu'),
        layers.Dense(50,activation='relu'),
        # layers.Dense(64,activation='relu'),
        layers.Dropout(0.4),
        # layers.Dense(10),
        # layers.Softmax()
        layers.Dense(10,activation='softmax')
        ])
    model.compile(optimizer='adam',
              loss=tf.keras.losses.CategoricalCrossentropy(),
              metrics=['accuracy'])
    return model


# File path name to save best models
# foldername = "CNN2D_TS_LHP1_12K_NOL_exp1n/"
foldername = "/content/drive/MyDrive/CNN2D_TS_CWRU_12K_NOL_LHP0/"
os.makedirs(foldername, exist_ok=True)

from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import load_model

accuracy_train = []
accuracy_val = []
accuracy_test = []
pred_all_val = np.zeros([len(X_2D_train),10])
y_2D_val = np.zeros([len(X_2D_train),10])
kfold_test_len = []

fl1 = 0
k = 1

early_stop = EarlyStopping(monitor='val_accuracy', patience=50, restore_best_weights=True)

# Train the model 
# for train, test in kfold.split(X_2D_train,y_2D_train):
for fold, (train, test) in enumerate(kfold.split(X_2D_train, y_label_train)):    

  # Define where to save the best model
  checkpoint_filepath = foldername + "best_model_" + str(k) + ".h5"
  """    
  # Create a ModelCheckpoint callback
  checkpoint = ModelCheckpoint(
      filepath=checkpoint_filepath,
      monitor='val_accuracy',  # Monitor validation accuracy
      save_best_only=True,  # Save only the best model
      mode='max',  # Maximize accuracy
      verbose=1
  )        

  Classification_2D = CNN_2D()
  # history = Classification_2D.model.fit(X_2D_train[train], y_2D_train[train], verbose=1, epochs=50) #epochs=12
  history = Classification_2D.model.fit(
        X_2D_train[train], y_2D_train[train],
        validation_data=(X_2D_train[test], y_2D_train[test]),  # Validation set for monitoring
        epochs=200,
        verbose=1,
        callbacks=[checkpoint, early_stop]  # Save the best model
  )
  """  
  print("Best model saved at:", checkpoint_filepath)
  CNN_2D_best_model = load_model(checkpoint_filepath)
  print("Best model loaded successfully!")
  
  fl2 = fl1 + len(test)
  pred_all_val[fl1:fl2,:] = CNN_2D_best_model.predict(X_2D_train[test])
  y_2D_val[fl1:fl2,:] = y_2D_train[test]
  kfold_test_len.append(fl2-fl1)
  fl1 = fl2  

  # Evaluate the accuracy of the model on the training set 
  # train_loss, train_accuracy = CNN_2D_best_model.evaluate(X_2D_train[train], y_2D_train[train])
  train_loss, train_accuracy = CNN_2D_best_model.evaluate(X_2D_train, y_2D_train)
  accuracy_train.append(train_accuracy)
  
  # Evaluate the accuracy of the model on the validation set 
  # val_loss, val_accuracy = CNN_2D_best_model.evaluate(X_2D_train[test], y_2D_train[test])
  val_loss, val_accuracy = CNN_2D_best_model.evaluate(X_2D_test, y_2D_test)
  accuracy_val.append(val_accuracy)
  
  # Evaluate the accuracy of the model on the validation set 
  # test_loss, test_accuracy = CNN_2D_best_model.evaluate(X_2D_test, y_2D_test)
  test_loss, test_accuracy = CNN_2D_best_model.evaluate(Input_2D, Y_CNN)
  accuracy_test.append(test_accuracy)  
  
  # Evaluate the accuracy of the model on the training set 
  # kf_loss, kf_accuracy = Classification_2D.model.evaluate(X_2D_train[test], y_2D_train[test]) 
  # accuracy_2D.append(kf_accuracy)
  
  k = k + 1

"""
# -----------------------------------------------------------------------------
# Multiclass Classification CNN Model Evaluation
# -----------------------------------------------------------------------------
"""

# Classification_2D.model.summary()

CNN_2D_train_accuracy = np.average(accuracy_train)*100
print('CNN 2D train accuracy =', CNN_2D_train_accuracy)
# print(accuracy_train)

CNN_2D_val_accuracy = np.average(accuracy_val)*100
print('CNN 2D validation accuracy =', CNN_2D_val_accuracy)
# print(accuracy_val)

CNN_2D_test_accuracy = np.average(accuracy_test)*100
print('CNN 2D test accuracy =', CNN_2D_test_accuracy)
# print(accuracy_test)

# Evaluate the accuracy of the model on the test set
# CNN_2D_test_loss, CNN_2D_test_accuracy = Classification_2D.model.evaluate(X_2D_test, y_2D_test)
# CNN_2D_test_accuracy*=100
# print('CNN 2D test accuracy =', CNN_2D_test_accuracy)


def ConfusionMatrix(Model, X, y):
  y_pred = np.argmax(Model.predict(X), axis=1)
  ConfusionMat = confusion_matrix(np.argmax(y, axis=1), y_pred)
  return ConfusionMat

# Plot results - CNN 2D

plt.figure(5)
plt.title('Confusion Matrix - CNN 2D Train') 
sns.heatmap(
    ConfusionMatrix(CNN_2D_best_model, X_2D_train, y_2D_train),
    annot=True, fmt='d', annot_kws={"fontsize":8}, cmap="YlGnBu"
)
plt.tight_layout()
plt.savefig(foldername + "confusion_matrix_train.png", dpi=300)
plt.show()

plt.figure(6)
plt.title('Confusion Matrix - CNN 2D Test') 
sns.heatmap(
    ConfusionMatrix(CNN_2D_best_model, X_2D_test, y_2D_test),
    annot=True, fmt='d', annot_kws={"fontsize":8}, cmap="YlGnBu"
)
plt.tight_layout()
plt.savefig(foldername + "confusion_matrix_test.png", dpi=300)
plt.show()


plt.figure(7)
plt.title('Train - Accuracy - CNN 2D')
plt.bar(np.arange(1,kSplits+1), [i*100 for i in accuracy_val])
plt.ylabel('accuracy')
plt.xlabel('folds')
plt.ylim([70,100])
plt.tight_layout()
plt.savefig(foldername + "fold_validation_accuracy.png", dpi=300)
plt.show()

plt.figure(8)
plt.title('Train vs Test Accuracy - CNN 2D')
plt.bar([1,2], [CNN_2D_train_accuracy, CNN_2D_test_accuracy])
plt.ylabel('accuracy')
plt.xlabel('folds')
plt.xticks([1,2], ['Train', 'Test'])
plt.ylim([70,100])
plt.tight_layout()
plt.savefig(foldername + "train_vs_test_accuracy.png", dpi=300)
plt.show()

# ==========================================
# ROBUST 2D Grad-CAM for CNN_2D_best_model
# ==========================================

import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# ------------------------------------------
# 0) Output folder
# ------------------------------------------
gradcam_dir = os.path.join(foldername, "gradcam_results")
os.makedirs(gradcam_dir, exist_ok=True)

# ------------------------------------------
# 1) Prepare labels and predictions
# ------------------------------------------
y_true = y_2D_test
if len(y_2D_test.shape) > 1 and y_2D_test.shape[-1] > 1:
    y_true = np.argmax(y_2D_test, axis=1)

pred_probs = CNN_2D_best_model.predict(X_2D_test, verbose=0)
y_pred = np.argmax(pred_probs, axis=1)

correct_idx = np.where(y_pred == y_true)[0]
wrong_idx   = np.where(y_pred != y_true)[0]

print("Correct:", len(correct_idx), " Misclassified:", len(wrong_idx))

if len(correct_idx) == 0:
    print("No correct samples found.")
if len(wrong_idx) == 0:
    print("No misclassified samples found.")

# ------------------------------------------
# 2) Find last Conv2D layer
# ------------------------------------------
def get_last_conv2d_layer_name(model):
    for layer in reversed(model.layers):
        if isinstance(layer, tf.keras.layers.Conv2D):
            return layer.name
    raise ValueError("No Conv2D layer found in model.")

LAST_CONV_LAYER = get_last_conv2d_layer_name(CNN_2D_best_model)
print("Using last conv layer:", LAST_CONV_LAYER)

# ------------------------------------------
# 3) Build robust Grad-CAM models
# ------------------------------------------
last_conv_layer = CNN_2D_best_model.get_layer(LAST_CONV_LAYER)

# input -> last conv output
conv_model = tf.keras.Model(
    inputs=CNN_2D_best_model.inputs,
    outputs=last_conv_layer.output
)

# last conv output -> final prediction
classifier_input = tf.keras.Input(shape=last_conv_layer.output.shape[1:])

x = classifier_input
start_collecting = False
for layer in CNN_2D_best_model.layers:
    if layer.name == LAST_CONV_LAYER:
        start_collecting = True
        continue
    if start_collecting:
        x = layer(x)

classifier_model = tf.keras.Model(classifier_input, x)

# ------------------------------------------
# 4) Compute 2D Grad-CAM
# ------------------------------------------
def compute_gradcam_2d(img_batch, class_idx=None):
    """
    img_batch: shape (1, H, W, C)
    returns heatmap: shape (H, W) in [0,1]
    """
    img_batch = tf.cast(img_batch, tf.float32)

    with tf.GradientTape() as tape:
        conv_out = conv_model(img_batch, training=False)
        tape.watch(conv_out)

        preds = classifier_model(conv_out, training=False)

        if class_idx is None:
            class_idx = int(tf.argmax(preds[0]))
        else:
            class_idx = int(class_idx)

        loss = preds[:, class_idx]

    grads = tape.gradient(loss, conv_out)

    if grads is None:
        raise ValueError("Gradients are None. Grad-CAM could not be computed.")

    # conv_out: (1,h,w,c), grads: (1,h,w,c)
    conv_out = conv_out[0]
    grads = grads[0]

    # Global average pooling over spatial dims
    pooled_grads = tf.reduce_mean(grads, axis=(0, 1))   # (c,)

    # Weighted combination of channels
    heatmap = tf.reduce_sum(conv_out * pooled_grads, axis=-1)   # (h,w)

    heatmap = tf.maximum(heatmap, 0)
    heatmap = heatmap / (tf.reduce_max(heatmap) + 1e-9)
    heatmap = heatmap.numpy()

    # Resize to input image size
    H, W = img_batch.shape[1], img_batch.shape[2]
    if heatmap.shape != (H, W):
        heatmap = tf.image.resize(heatmap[..., None], (H, W)).numpy().squeeze()

    return heatmap, class_idx

# ------------------------------------------
# 5) Plot function
# ------------------------------------------
def plot_gradcam_triplet(img, heatmap, true_label, pred_label, title, save_path):
    img2 = img[:, :, 0] if img.ndim == 3 else img

    plt.figure(figsize=(12, 4))

    ax1 = plt.subplot(1, 3, 1)
    im1 = ax1.imshow(img2, cmap="gray")
    ax1.set_title(f"{title}\nTrue={true_label}, Pred={pred_label}")
    plt.colorbar(im1, ax=ax1, fraction=0.046, pad=0.04)

    ax2 = plt.subplot(1, 3, 2)
    im2 = ax2.imshow(heatmap, cmap="jet", vmin=0, vmax=1)
    ax2.set_title("Grad-CAM heatmap")
    plt.colorbar(im2, ax=ax2, fraction=0.046, pad=0.04)

    ax3 = plt.subplot(1, 3, 3)
    ax3.imshow(img2, cmap="gray")
    im3 = ax3.imshow(heatmap, cmap="jet", alpha=0.45, vmin=0, vmax=1)
    ax3.set_title("Overlay")
    plt.colorbar(im3, ax=ax3, fraction=0.046, pad=0.04)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()
    print("Saved:", save_path)

# ------------------------------------------
# 6) Generate multiple correct + wrong samples
# ------------------------------------------
N_SHOW = 10

correct_samples = correct_idx[:N_SHOW]
wrong_samples   = wrong_idx[:N_SHOW]

print("\n--- Generating Grad-CAM for CORRECT samples ---")
for idx in correct_samples:
    img_batch = X_2D_test[idx:idx+1]
    true_label = int(y_true[idx])
    pred_label = int(y_pred[idx])

    heatmap, _ = compute_gradcam_2d(img_batch, class_idx=pred_label)

    save_path = os.path.join(
        gradcam_dir,
        f"gradcam_correct_idx{idx}_true{true_label}_pred{pred_label}.png"
    )
    plot_gradcam_triplet(
        img_batch[0], heatmap, true_label, pred_label,
        "Correct sample (Grad-CAM)", save_path
    )

print("\n--- Generating Grad-CAM for MISCLASSIFIED samples ---")
for idx in wrong_samples:
    img_batch = X_2D_test[idx:idx+1]
    true_label = int(y_true[idx])
    pred_label = int(y_pred[idx])

    heatmap, _ = compute_gradcam_2d(img_batch, class_idx=pred_label)

    save_path = os.path.join(
        gradcam_dir,
        f"gradcam_wrong_idx{idx}_true{true_label}_pred{pred_label}.png"
    )
    plot_gradcam_triplet(
        img_batch[0], heatmap, true_label, pred_label,
        "Misclassified sample (Grad-CAM)", save_path
    )

print("\nRobust 2D Grad-CAM completed.")


# ==========================================
# SHAP FOR 2D CNN
# ==========================================

import os
import numpy as np
import shap
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
import shutil

# ------------------------------------------
# 0) Output folder
# ------------------------------------------
shap_dir = os.path.join(foldername, "shap_results")

if os.path.exists(shap_dir):
    shutil.rmtree(shap_dir)

os.makedirs(shap_dir, exist_ok=True)

# ------------------------------------------
# 1) Predictions + labels
# ------------------------------------------
y_true = y_2D_test
if len(y_2D_test.shape) > 1 and y_2D_test.shape[-1] > 1:
    y_true = np.argmax(y_2D_test, axis=1)

pred_probs = CNN_2D_best_model.predict(X_2D_test, verbose=0)
y_pred = np.argmax(pred_probs, axis=1)

correct_idx = np.where(y_pred == y_true)[0]
wrong_idx = np.where(y_pred != y_true)[0]

print("Correct samples:", len(correct_idx))
print("Misclassified samples:", len(wrong_idx))

# ------------------------------------------
# 2) Confusion matrix
# ------------------------------------------
cm = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap="YlGnBu")
plt.title("Confusion Matrix - 2D CNN (SHAP Analysis Set)")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.tight_layout()
plt.savefig(os.path.join(shap_dir, "confusion_matrix_shap_2dcnn.png"), dpi=300)
plt.show()

# ------------------------------------------
# 3) Background data for SHAP
# ------------------------------------------
np.random.seed(1)
bg_size = min(50, len(X_2D_train))
bg_idx = np.random.choice(len(X_2D_train), size=bg_size, replace=False)
background = X_2D_train[bg_idx]

print("Background shape:", background.shape)

# ------------------------------------------
# 4) SHAP explainer
# ------------------------------------------
explainer = shap.GradientExplainer(CNN_2D_best_model, background)

# ------------------------------------------
# 5) Helper: get SHAP values for one sample
# ------------------------------------------
def get_single_sample_shap_2d(sample, pred_label):
    """
    sample shape: (1, 20, 20, 1)
    pred_label: int
    returns shap values shape: (20, 20)
    """
    shap_values = explainer.shap_values(sample)

    if isinstance(shap_values, list):
        sv = shap_values[pred_label][0, :, :, 0]
    else:
        sv = np.array(shap_values)

        if sv.ndim == 5 and sv.shape[0] == 1:
            sv = sv[0, :, :, 0, pred_label]
        elif sv.ndim == 5 and sv.shape[1] == 1:
            sv = sv[pred_label, 0, :, :, 0]
        elif sv.ndim == 4:
            sv = sv[0, :, :, 0]
        else:
            sv = sv.reshape(sample.shape[1], sample.shape[2])

    return sv

# ------------------------------------------
# 6) Convert 2D sample + SHAP back to 1D
# ------------------------------------------
def flatten_2d_to_1d(img_2d):
    if img_2d.ndim == 3:
        img_2d = img_2d[:, :, 0]
    return img_2d.reshape(-1)

# ------------------------------------------
# 7) Plot SHAP in 1D signal style
# ------------------------------------------
def save_shap_signal_plot_from_2d(img_2d, shap_2d, true_label, pred_label, save_path, title):
    """
    img_2d: shape (20,20) or (20,20,1)
    shap_2d: shape (20,20)
    """
    signal_1d = flatten_2d_to_1d(img_2d)
    shap_1d = flatten_2d_to_1d(shap_2d)

    x = np.arange(len(signal_1d))

    fig, axes = plt.subplots(3, 1, figsize=(12, 8), sharex=True)

    # Original signal
    axes[0].plot(x, signal_1d, linewidth=1)
    axes[0].set_title(f"{title}\nTrue={true_label}, Pred={pred_label}")
    axes[0].set_ylabel("Amplitude")
    axes[0].grid(True, alpha=0.3)

    # SHAP values band
    max_abs = np.max(np.abs(shap_1d)) + 1e-9
    im = axes[1].imshow(
        shap_1d.reshape(1, -1),
        aspect='auto',
        cmap='coolwarm',
        vmin=-max_abs,
        vmax=max_abs,
        extent=[0, len(signal_1d), 0, 1]
    )
    axes[1].set_title("SHAP Importance")
    axes[1].set_yticks([])
    plt.colorbar(im, ax=axes[1], fraction=0.02, pad=0.02)

    # Overlay
    ymin, ymax = signal_1d.min(), signal_1d.max()
    axes[2].plot(x, signal_1d, color='black', linewidth=1, alpha=0.85)
    axes[2].imshow(
        shap_1d.reshape(1, -1),
        aspect='auto',
        cmap='coolwarm',
        alpha=0.35,
        vmin=-max_abs,
        vmax=max_abs,
        extent=[0, len(signal_1d), ymin, ymax]
    )
    axes[2].set_title("Signal + SHAP Overlay")
    axes[2].set_xlabel("Time Index")
    axes[2].set_ylabel("Amplitude")
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.show()
    print("Saved:", save_path)

# ------------------------------------------
# 8) Generate MULTIPLE SHAP examples per class
# ------------------------------------------
N_PER_CLASS_SHAP = 3
print("Generating multiple SHAP examples per class...")

classes = np.unique(y_true)

for cls in classes:
    cls = int(cls)

    cls_correct_idx = np.where((y_true == cls) & (y_pred == cls))[0][:N_PER_CLASS_SHAP]
    cls_wrong_idx = np.where((y_true == cls) & (y_pred != cls))[0][:N_PER_CLASS_SHAP]

    correct_cls_dir = os.path.join(shap_dir, f"class_{cls}", "correct")
    wrong_cls_dir = os.path.join(shap_dir, f"class_{cls}", "misclassified")
    os.makedirs(correct_cls_dir, exist_ok=True)
    os.makedirs(wrong_cls_dir, exist_ok=True)

    # Correct examples
    for j, idx_c in enumerate(cls_correct_idx):
        idx_c = int(idx_c)
        sample_c = X_2D_test[idx_c:idx_c+1]
        img_c = sample_c[0]
        true_c = int(y_true[idx_c])
        pred_c = int(y_pred[idx_c])

        shap_c = get_single_sample_shap_2d(sample_c, pred_c)

        save_c = os.path.join(
            correct_cls_dir,
            f"shap_correct_idx{idx_c}_true{true_c}_pred{pred_c}_{j+1}.png"
        )

        save_shap_signal_plot_from_2d(
            img_c,
            shap_c,
            true_c,
            pred_c,
            save_c,
            f"Correct Sample (SHAP) | Class {cls}"
        )

    # Misclassified examples
    for j, idx_w in enumerate(cls_wrong_idx):
        idx_w = int(idx_w)
        sample_w = X_2D_test[idx_w:idx_w+1]
        img_w = sample_w[0]
        true_w = int(y_true[idx_w])
        pred_w = int(y_pred[idx_w])

        shap_w = get_single_sample_shap_2d(sample_w, pred_w)

        save_w = os.path.join(
            wrong_cls_dir,
            f"shap_wrong_idx{idx_w}_true{true_w}_pred{pred_w}_{j+1}.png"
        )

        save_shap_signal_plot_from_2d(
            img_w,
            shap_w,
            true_w,
            pred_w,
            save_w,
            f"Misclassified Sample (SHAP) | True Class {cls}"
        )

print("Multiple SHAP sample generation completed.")

# ------------------------------------------
# 9) SHAP summary on a few test samples
# ------------------------------------------
summary_n = min(20, len(X_2D_test))
summary_samples = X_2D_test[:summary_n]
summary_preds = y_pred[:summary_n]

summary_shap = explainer.shap_values(summary_samples)

summary_maps = []
for i in range(summary_n):
    pred_cls = summary_preds[i]

    if isinstance(summary_shap, list):
        sv_i = summary_shap[pred_cls][i, :, :, 0]
    else:
        sv = np.array(summary_shap)
        if sv.ndim == 5 and sv.shape[0] == summary_n:
            sv_i = sv[i, :, :, 0, pred_cls]
        elif sv.ndim == 5 and sv.shape[0] != summary_n:
            sv_i = sv[pred_cls, i, :, :, 0]
        elif sv.ndim == 4:
            sv_i = sv[i, :, :, 0]
        else:
            sv_i = sv[i].reshape(summary_samples.shape[1], summary_samples.shape[2])

    summary_maps.append(sv_i)

summary_maps = np.array(summary_maps)
summary_input = summary_samples[:, :, :, 0]

summary_matrix = summary_maps.reshape(summary_n, -1)
summary_input_flat = summary_input.reshape(summary_n, -1)

shap.summary_plot(summary_matrix, summary_input_flat, show=False)
plt.savefig(os.path.join(shap_dir, "shap_summary_plot_2dcnn.png"), dpi=300, bbox_inches='tight')
plt.show()

print("\n2D CNN SHAP analysis completed.")