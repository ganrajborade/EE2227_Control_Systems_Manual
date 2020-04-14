#Code by B.Varuni
#April 12,2020
#Released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt 
#p = np.poly1d([1,2,3,1,4,2])  # enter the coefficients of characteristic polynomial
#p = np.poly1d([1,3,2,6])  # enter the coefficients of characteristic polynomial
p = np.poly1d([1,1,7,14,31,73,25,200])  # enter the coefficients of characteristic polynomial

c = p.c	  
#s = p.r                      #uncomment this line if u want to know the roots of characteritics equation

r = np.zeros((len(c),len(c)-1))
try:
	for i in range(len(r[1])):
		r[0][i] = c[2*i+1]       #filling first row of the routh matrix 
except IndexError:
	print("calculating...")

try:
	for i in range(len(r[1])):
		r[1][i] = c[2*i]        #filling second row of the routh matrix 
except IndexError:
	print("...")
#print(r)
for i in range(2,len(c)):
	if(i%2 ==  0):
		try:
			for j in range(int(i/2),len(c)):     # filling remaining rows of routh matrix
				r[i][j] = r[0][j-int(i/2)]
		except IndexError:
			print("...")
	else:
		try:
			for j in range(int(i/2),len(c)):
				r[i][j] = r[1][j-int(i/2)]
		except IndexError:
			print("...")
		
print("THE ROUTH MATRIX IS:")
print(r)
det_array = np.array([])
for i in range(2,len(c)):
	z = np.zeros((i,i))
	for j in range(0,i):
		z[j] = r[j][0:i]
	det_array = np.append(det_array,[np.linalg.det(z)])        #calculating the determinent of each of square matrix of the routh matrix
print("CALCULATED DETERMINENT ARRAY IS: ")
print(det_array)

if(min(det_array)>0):
	print("DETERMINENT ARRAY HAS ALL POSITIVE VALUES")
	print("THEREFORE THE SYSTEM IS STABLE")
else:
	print("DETERMINENT ARRAY HAS NEGATIVE VALUES")
	print("THEREFORE THE SYSTEM IS UNSTABLE")

	
	
	
	
	
	
