import urllib
from urllib import request
import numpy as np

#fname = 'https://stepic.org/media/attachments/lesson/16462/boston_houses.csv'
fname = input()  # read file name from stdin
f = urllib.request.urlopen(fname)  # open file from URL
data = np.loadtxt(f, delimiter=',', skiprows=1)  # load data to work with

Y = np.array([data.T[0]]).T
X = np.array(data.T[1:]).T
X = np.hstack((np.ones_like(Y), X))
beta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y)

print(' '.join(map(str, beta.flatten())))
