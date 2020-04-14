#Code by  Abhishek Shetkar
#April 2, 2020
#Released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt

t = 0
c = 0
y = 0

# defining a function whose solution of f=0 will give us the value of t for 94% of output
def s(a):									
	v = 0.06 - np.exp(-a) - a*np.exp(-a)
	return v

#loop starts at t = 0, checks wether function is +ve, if not, then increases t by 0.001
while c == 0:				
	y = s(t) 						
	if y < 0:
		c = 0
		t = t+0.001

	else:
		c = 1				


#approx. the curve as a straight line, we find the crossing point by weighted mean of the two succesive values
t1 = ((t-0.001)*(-s(t-0.001)) + t*s(t))/(-s(t-0.001) + s(t)) 

print(t1)

