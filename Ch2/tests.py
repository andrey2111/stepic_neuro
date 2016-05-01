import numpy as np
input_matrix = np.full((20, 2), 2)
b = 0
w = np.full((2, 1), 3)
result = input_matrix.dot(w) + b > 0
print(result)
