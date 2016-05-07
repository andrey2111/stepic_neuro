import numpy as np


def sigmoid(x):
    """сигмоидальная функция, работает и с числами, и с векторами (поэлементно)"""
    return 1 / (1 + np.exp(-x))


def sigmoid_prime(x):
    """производная сигмоидальной функции, работает и с числами, и с векторами (поэлементно)"""
    return sigmoid(x) * (1 - sigmoid(x))

answer = 1
#w2 = 2*np.ones((2, 3))
w2 = np.array([[0.7, 0.2, 0.7], [0.8, 0.3, 0.6]])
#w3 = np.ones((1, 2))
w3 = np.array([0.2, 0.4])
#a1 = sigmoid(np.array([0, 1, 2]))
a1 = np.array([0, 1, 1])
sum2 = w2.dot(a1)
a2 = np.array([max(sum2[0], 0), sigmoid(sum2[1])])
sum3 = w3.dot(a2)
a3 = sigmoid(sum3)

error3 = (sigmoid(sum3)-1)*sigmoid_prime(sum3)
print(error3)
error2 = w3.T.dot(error3)*np.array([int(sum2[0] > 0), sigmoid_prime(sum2[1])])
print(error2)
ans = a1[2]*error2
print(ans)
