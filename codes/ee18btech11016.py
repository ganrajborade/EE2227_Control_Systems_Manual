import numpy as np 
import matplotlib.pyplot as plt 
from pylab import *

t1 = np.linspace(0,3,100)
t2 = np.linspace(0,20,1000)

x1 = np.sin(t1) #input to the system for range of time t1.
x2 = np.sin(t2) #input to the system for range of time t2.
y_o = np.cos(t2) - np.exp(-t2) #steady state output of the system
y_o1 = np.cos(t1) - np.exp(-t1) #for plotting wrt t1 .thats it.

y1 = np.cos(t2)
y2 = -np.exp(-t2)
subplot(2,1,1)
plt.plot(t1,x1,'g',label = 'Input x(t) = sin(t)')
plt.plot(t1,y_o1,'b',label = 'Resultant output y(t)')
plt.grid()
plt.legend()
plt.xlabel('t')
plt.ylabel('The input & output of the system in t-domain')

subplot(2,1,2)
plt.plot(t2,x2,'g',label = 'Input x(t) = sin(t)') #plotting input for more time i.e with respect to t2.
plt.plot(t2,y_o,'b',label = 'Resultant output y(t)')
plt.plot(t2,y1,'k',linestyle='dashed',label= 'steady state output :cos(t)')
plt.plot(t2,y2,'r',linestyle='dashed',label = '-e$^{-t}$')
plt.grid()
plt.legend()
plt.xlabel('t')
plt.ylabel('The output of the system in t-domain')
plt.show()
