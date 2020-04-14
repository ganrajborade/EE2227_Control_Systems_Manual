#Code by B.Varuni
#April 5,2020
#Released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt 
p = np.poly1d([1,2,3,1,8,5])  # enter the coefficients of characteristic polynomial
c = p.c	 
#s = p.r                      #uncomment this line if u want to know the roots of characteritics equation
r = np.zeros((len(c),len(c)-1))                   #initiating the routh array
try:
	for i in range(len(r[1])):
		r[0][i] = c[2*i]       #filling the first row
except IndexError:
	print("calculating...")

try:
	for i in range(len(r[1])):
		r[1][i] = c[2*i+1]    #filling the second row
except IndexError:
	print("...")
for j in range(2,len(r)):	
	try:
		for i in range(len(r[i])):        #filling the remaining rows
			r[j][i] = (r[j-2+1][0]*r[j-2+0][i+1]-r[j-2+0][0]*r[j-2+1][i+1])/r[j-2+1][0]
	except IndexError:
		print("...")	
count = 0
for i in range(1,len(r)):
		if(r[i][0]<0):
			count = count + 2            #counting the number of sign changes
print("routh array = ")
print(r)
print("NUMBER OF SIGN CHANGES IN ROUTH ARRAY = ",count)	
if(count > 0):
	print("SYSTEM IS UNSTABLE")
elif(count == 0):
	print("SYSTEM IS STABLE")
