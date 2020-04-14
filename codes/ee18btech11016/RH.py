# License
'''
Code by Ganraj Borade
April 12,2020
Released under GNU GPL
'''

#This code generates Routh array and indicates the no of sign changes for the given polynomial
import numpy as np
import itertools

#enter the polynomial 
n=int(input("Degree of the polynomial:"))
c=np.zeros(100)
#enter coefficients from highest degree to lowest degree , one by one 
for i in range(0,n+1):
	if (n-i ==3):
		c[i]=input("Enter the "+str(n-i)+"rd coefficient:")
	else:
		c[i]=input("Enter the "+str(n-i)+"th coefficient:")

#creates routh array for different cases
if (n%2==0):
	d=np.zeros([n+1,n])
else:
	d=np.zeros([n+1,n])
	
for j in range (0,n-1):
	d[0,j]=c[2*j]
	d[1,j]=c[(2*j)+1]
	
	

for i in range(2,n+1):	
	u=[]
	for j in range (0,n-1):
		
		d[i,j]= (((d[i-1,0]*d[i-2,j+1])-(d[i-1,j+1]*d[i-2,0]))/(d[i-1,0]))
	
		u.append(d[i,j])
	
	l=np.count_nonzero(u)
	
	for k in range(0,n-1):
		if (l==0):
			d[i,k]=(d[i-1,k]*(n+1-i-(2*k)))
		else:
			continue
		
	if(d[i,0]==0):
		d[i,0]=0.000001     #value of epsilon
		
#prints routh array		
print(d)		
x=[]
for i in range (0,n+1):
	x.append(d[i,0])

k=(len(list(itertools.groupby(x, lambda x: x > 0)))-1)
if k==0:
	print("The polynomial has no poles on right half of s plane")
else:
	print("The no of poles on right half of s plane is:",k) 