'''
- append ones in arr
- H = transposed M values
- m1T         ai
  m2T * Pi =  bi
  m3T         ci
'''

import numpy as np

data = np.loadtxt('data.txt')
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

# A modern approach
# A = np.array(map(lambda x: x.transpose(), np.dstack((col_1, col_2, col_3))))
A = np.zeros((982,3,4))
A[::,0] = col_1
A[::,1] = col_2
A[::,2] = col_3

# This is broken now
# AtA = A.transpose().dot(A)
# eig_val, eig_vect = np.linalg.eig(AtA)
# print eig_val, eig_vect
