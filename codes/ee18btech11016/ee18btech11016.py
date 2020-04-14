# License
'''
Code by Ganraj Borade
April 12,2020
Released under GNU GPL
'''

#Bode phase plot using scipy in python
from scipy import signal
import matplotlib.pyplot as plt
from pylab import *
#Defining the transfer function 
#Since the transfer function is 1/(s(1+2s)(s+1)) = 1/(2s^3 + 3s^2 + s)
s1 = signal.lti([1],[2, 3,1,0])

#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
w,mag,phase = signal.bode(s1)


subplot(2,1,1)
#plt.xlabel('Frequency(rad/s)')
plt.ylabel('Mag(deg)')
plt.title('Magnitude plot')
plt.plot(0.7,-3.5,'o')
plt.text(0.7,-3.5, '({}, {})'.format(0.7,-3.5))
plt.axvline(x = 0.7,ymax = 0.59,color='k',linestyle='dashed')
plt.semilogx(w, mag,'b')        # Bode Magnitude plot
plt.grid() 

subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')

plt.axhline(y = -180,xmin=0,xmax= 0.605,color = 'r',linestyle='dashed')
plt.axvline(x = 0.7,ymin=0.479,color='k',linestyle='dashed')
plt.plot(0.7,-180,'o')
plt.text(0.7,-180, '({}, {})'.format(0.7,-180))
plt.title('Phase plot')
plt.semilogx(w,phase)          # Bode phase plot
plt.grid() 




plt.show()
