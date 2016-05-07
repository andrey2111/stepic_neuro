import numpy as np
import random
mat = np.array(random.sample(range(1000), 12)) # одномерный массив из 12 случайных чисел от 1 до 1000
mat = mat.reshape((2, 2, 3)) # превратим w в трёхмерную матрицу
mat = mat.reshape((12, 1))
print(mat)
