#publishing under GNU GPL
#7-04-20 C Shruti
import numpy as np
A = np.matrix([[0, 1, 0],
               [0, 0, 1],
               [-1, -2, -3]])

eigenvalues = np.linalg.eigvals(A)
print('The eigenvalues are:')
print (eigenvalues)
print("Roots of the the polynomial:")
print(np.roots([1, 3, 2,1]))
