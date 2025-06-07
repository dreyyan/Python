# Import
import numpy as np

# Note:
# - uniform data type
# - contiguous memory block
# - fixed size
# - homogenuous shape
# - n-dimensional
# - strided views (no data copy)
# - broadcasting (can perform operations between different shapes)

# Definition
a = np.array([1, 2, 3], dtype='int16')
b = np.array([[1.0, 2.0, 3.0, 4.0], [3.0, 4.0, 5.0, 6.0]])
c = np.array([[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]])
d = np.array([1, 2, 3], dtype='int16')
e = np.array([4, 5, 6], dtype='int16')
print(b)

# Operations
# 1. # of dimensions
print(f"# of dimensions: {a.ndim}")
# 2. Array dimensions
print(f"     dimensions: {b.shape}")
# 3. # of elements
print(f"  # of elements: {b.size}")
# 4. Data type of elements
print(f"      data type: {b.dtype}")
# 5. Size(bytes) of an element
print(f"element size(b): {a.itemsize}")
# 6. Total memory consumed(bytes)
print(f"  total size(b): {a.nbytes}")
# 7. Get specific element
print(f"  element[1, 2]: {b[1, 2]}")
# 8. Get specific row
print(f"         row[0]: {b[0, :]}")
# 9. Get specific column
print(f"         col[1]: {b[:, 1]}")
# 10. Get specific range
print(f"  col[2-6 by 2]: {c[0, 1:6:2]}")
# 11. Sum
print(f"            sum: {np.sum(c)}")
# 12. Max
print(f"            max: {np.max(c)}")
# 13. Min
print(f"            min: {np.min(c)}")
# 14. Reshape
print(f"        reshape:\n{c.reshape(4, 4)}")
# 15. Broadcasting
print(f"            add: {d + e}")
# 16. Convert data type
a.astype('int8')
# 17. Boolean indexing/filtering
print(f"         n > 10: {c[c > 10]}")
# 18. Math functions
print(f"            sin:\n{np.sin(c)}")
print(f"            cos:\n{np.cos(c)}")
print(f"            tan:\n{np.tan(c)}")
# 19. Array initialization shortcuts
np.full((2, 2), 7)                              # 2x2 array filled with 7
np.eye(3)                                       # 3x3 identity matrix
np.random.rand(2, 2)                            # Random floats in [0, 1)
np.random.randint(0, 10, size=(3, 3))           # Random ints
# 20. Axis operations
print(f"        col sum: {np.sum(c, axis=0)}")  # Sum across columns
print(f"        row sum: {np.sum(c, axis=1)}")  # Sum across rows
# 21. Copy
x = np.array([1, 2, 3])
y = x.copy()
y[0] = 100
print(x, y)                                     # x unchanged, y modified
