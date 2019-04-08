import numpy as np

def load_train_data():
	data_type = np.float64
	H, W = 48, 48
	num_train, num_val, num_test = 20000, 4000, 4709

	train = np.genfromtxt(r'data\ml2019spring-hw3\train.csv', delimiter=',', dtype='str', skip_header=1)
	X = []
	y = []

	for i in range(train.shape[0]):
		X.append(np.array(train[i,1].split(' ')).reshape(1, 48, 48))
		y.append(train[i,0])

	X_train = np.array(X[num_val:num_val+num_train], dtype=data_type)
	y_train = np.array(y[num_val:num_val+num_train], dtype=int)
	X_val = np.array(X[:num_val], dtype=data_type)
	y_val = np.array(y[:num_val], dtype=int)
	X_test = np.array(X[-num_test:], dtype=data_type)
	y_test = np.array(y[-num_test:], dtype=int)

	return (X_train, y_train, X_val, y_val, X_test, y_test)
	
def load_test_data():
	data_type = np.float64
	H, W = 48, 48
	
	tmp = np.genfromtxt(r'data\ml2019spring-hw3\test.csv', delimiter=',', dtype='str', skip_header=1)
	X = []
	for i in range(tmp.shape[0]):
		X.append(np.array(tmp[i,1].split(' '), dtype=data_type).reshape(1, 48, 48))
	test_set = np.array(X)
	
	return test_set

