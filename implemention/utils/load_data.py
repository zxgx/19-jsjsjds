import glob
import cv2
import numpy as np
import pandas as pd

def bin2class(row):
	if row[0] == False and row[1] == False:
		return 0
	elif row[0] == False and row[1] == True:
		return 1
	elif row[0] == True and row[1] == False:
		return 2
	elif row[0] == True and row[1] == True:
		return 3

def load():

	#images = [cv2.imread(file) for file in glob.glob(r'data\TrainingData\*.jpg')]
	images = [cv2.resize(cv2.imread(file),(256,256),interpolation=cv2.INTER_AREA) for file in glob.glob(r'data\TrainingData\*.jpg')]
	x = np.array(images, dtype=np.float64) / 255	# x.shape = N, height, width, channel

	tags = pd.read_excel(r'data\DataInfo.xlsx', true_values=["'High'", "'MIBC'"], false_values=["'Low'","'NMIBC'"])
	tags = tags.iloc[:, 1:].to_numpy(dtype=int) 	# tags.shape = N, grading, staging
	y = np.apply_along_axis(bin2class, 1, tags) 	# y.shape = (N, ) one-hot encoding
	
	# shuffle data
	N = grading.shape[0]
	shuffle_mask = np.random.shuffle(np.arange(N))
	x[:] = x[shuffle_mask]
	y[:] = y[shuffle_mask]

	return x, y
