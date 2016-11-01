import numpy as np

def calibrateCamera(data):
	arr = np.repeat(data[:,0:3], 2, axis=0)
	arr = np.hstack((arr, np.ones((arr.shape[0], 1))))

	xs = data[:,3]
	ys = data[:,4]
	col_1 = arr.copy()
	col_2 = arr.copy()
	col_3 = arr.copy()

	col_1[1::2] = 0
	col_2[::2] = 0
	col_3[::2] *= np.atleast_2d(-xs).transpose() 
	col_3[1::2] *= np.atleast_2d(-ys).transpose() 

	A = np.column_stack((col_1, col_2, col_3))

	AtA = A.transpose().dot(A)
	eig_val, eig_vect = np.linalg.eig(AtA)

	return eig_val

def visualiseCameraCalibration3D(data, P):
	return

def evaluateCameraCalibration3D(data, P):
	return

data = np.loadtxt('data.txt')
P = calibrateCamera(data)
print P