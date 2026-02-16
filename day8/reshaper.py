import numpy as np

arr = np.arange(24)

arr_reshaped = arr.reshape(4, 3, 2)

arr_transposed = arr_reshaped.transpose(0, 2, 1)

print("Final shape:", arr_transposed.shape)
print(arr_transposed)
