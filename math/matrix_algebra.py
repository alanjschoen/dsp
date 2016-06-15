# Matrix Algebra
import numpy as np

A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1],[1,2,3]])

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([[1,8,0,5]])

print '1.1'
print A.shape

print '1.2'
print B.shape

print '1.3'
print C.shape

print '1.4'
print D.shape

print '1.5'
print u.shape

print '1.6'
print w.shape


# print '3.1'
# print A + C
# Error

print '3.2'
print A - C.T
# [[-4 -7 -3]
#  [ 3  6  4]]

print '3.3'
print (C.T + 3*D)
# [[14  3  3]
#  [ 2  7  9]]

print '3.4'
print np.dot(B, A)
# [[-1 -5 -1]
#  [ 2  7  4]]

print '3.5'
# print np.dot(B, A.T)
# Error

print '3.6'
# print np.dot(B, C)
# Error

print '3.7'
print np.dot(C, B)
# [[ 5 -6]
#  [ 9 -8]
#  [ 6 -6]]

print '3.8'
print np.linalg.matrix_power(B,4)
# [[ 1 -4]
#  [ 0  1]]

print '3.9'
print np.dot(A, A.T)
# [[14 28]
#  [28 69]]

print '3.10'
print np.dot(D.T, D)
# [[10 -4  0]
#  [-4  8  8]
#  [ 0  8 10]]
