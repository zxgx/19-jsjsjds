import glob
import cv2
import numpy as np
import pandas as pd

"""
    load data and shuffle it
"""

def bin2class(row):
    if row[0] == False and row[1] == False: return 0
    elif row[0] == False and row[1] == True: return 1
    elif row[0] == True and row[1] == False: return 2
    elif row[0] == True and row[1] == True: return 3
    
def load_data(rsize=None):
    if rsize is not None:
        images = [cv2.resize(cv2.imread(file),(rsize,rsize),interpolation=cv2.INTER_AREA) for file in glob.glob(r'data\TrainingData\*.jpg')]
    else:
        images = [cv2.imread(file) for file in glob.glob(r'data\TrainingData\*.jpg')]
    
    x = np.array(images, dtype=np.float64)          # x.shape = N, height, width, channel

    tags = pd.read_excel(r'data\DataInfo.xlsx', true_values=["'High'", "'MIBC'"], false_values=["'Low'","'NMIBC'"])
    y = tags.iloc[:, 1:].values.astype(np.int)     # tags.shape = N, grading, staging
    # y = np.apply_along_axis(bin2class, 1, tags)     # y.shape = (N, ) prepare for one-hot encoding of 4 classes

    # shuffle data
    N = y.shape[0]
    shuffle_mask = np.random.shuffle(np.arange(N))
    x[:] = x[shuffle_mask]
    y[:] = y[shuffle_mask]
    
    return x, y