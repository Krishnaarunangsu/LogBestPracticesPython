import numpy as np


array_1 = np.zeros(3)
print(f'Zero Array:{array_1}')

list_1 = [0, 0, 0]
print(f'List:{list_1}')

array_2 = np.array(list_1)
print(f'List -> Array:{array_2}')

# 2 rows & 3 columns
array_3 = np.zeros((2, 3))
print(f'Zero Array:{array_3}')

# 3 sets of 2 rows & 3 columns
array_4 = np.zeros((3, 2, 3))
print(f'Zero Array:{array_4}')

array_5 = np.full((3, 4), 2)
print(f'Two array: {array_5}')


#  3×5 array of random floats between 0-1
array_6 = np.random.rand(3, 5)
print(f'Random Array:\n{array_6}')


# 3×4 array with all values 1
array_7 = np.ones((3, 4))
print(f'One array:{array_7}')

#  4×4 array of 0 with 1 on diagonal
array_8 = np.eye(4)
print(f'Array on diagonal:{array_8}')

array_9 = np.zeros((2, 2), dtype=np.int16)
print(f'Zero array 2*2:\n{array_9}')
print(f'Datatype of array9:{array_9.dtype}')

array_10 = np.zeros((2, 2), dtype=np.int64)
print(f'Zero array 2*2:\n{array_10}')
print(f'Datatype of array10:{array_10.dtype}')

array_11 = np.ones((1, 2, 3), dtype=np.int16)
print(f'One array 2*3:\n{array_11}')
