import numpy as np
import matplotlib.pyplot as plt

scrambled_matrix = np.load('encoded_array.npy')


side_length = int(np.sqrt(scrambled_matrix.size))
square_matrix = scrambled_matrix.reshape((side_length, side_length))


transposed_matrix = square_matrix.T


decoded_matrix = np.fliplr(transposed_matrix)

plt.imshow(decoded_matrix, cmap='gray')
plt.title("The Final Decoded Image!")
plt.show()