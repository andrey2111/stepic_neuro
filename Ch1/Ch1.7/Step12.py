import numpy as np

X = np.reshape([1, 60, 1, 50, 1, 75], (3, 2))
Y = np.reshape([10, 7, 12], (3, 1))
beta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y)
print(X)
print(Y)
print(beta)
