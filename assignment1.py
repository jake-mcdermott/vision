import numpy as np
import matplotlib.pyplot as plt

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
	col_3[::2] *= (-xs).reshape(data.shape[0], 1)
	col_3[1::2] *= (-ys).reshape(data.shape[0], 1)

	A = np.hstack((col_1, col_2, col_3))

	AtA = A.transpose().dot(A)
	eig_val, eig_vect = np.linalg.eig(AtA)

	eig_vect = eig_vect.transpose()
	return eig_vect[-1].reshape(3,4)


def getReprojectionPoints(data, P):
	reprojection_points = []
	for datapoint in data:
		point = np.array([datapoint[0], datapoint[1], datapoint[2], 1])
		reprojection = P.dot(point)
		reproject_x = reprojection[0]/reprojection[2]
		reproject_y = reprojection[1]/reprojection[2]
		reprojection_points.append((reproject_x, reproject_y))

	return np.array(reprojection_points)


def visualiseCameraCalibration3D(data, P):
	reproj_points = getReprojectionPoints(data, P)
	plt.plot(data[:,3], data[:,4],'r.')
	plt.plot(reproj_points[:,0], reproj_points[:,1],'g.')
	plt.show()


def getMean(data, P):
	data_points = data[:,0:3]
	reproj_points = getReprojectionPoints(data, P)
	for iii in xrange(data.shape[0]):
		error += np.linalg.norm(data_points[iii] - reproj_points[iii])
	return error / data.shape[0]


def getVariance():
	return


def getMinimum():
	return


def getMaximum():
	return


def evaluateCameraCalibration3D(data, P):
	return

data = np.loadtxt('data.txt')
P = calibrateCamera(data)
visualiseCameraCalibration3D(data, P)

