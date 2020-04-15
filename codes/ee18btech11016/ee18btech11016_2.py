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
#Since the transfer function is 1/(s(1+2s)(s+1)^2) = 1/(2s^4 + 5s^3 + 4s^2 + s)
s1 = signal.lti([1],[2, 5,4,1,0])

#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
w,mag,phase = signal.bode(s1)


subplot(2,1,1)
#plt.xlabel('Frequency(rad/s)')
plt.ylabel('Mag(deg)')
plt.title('Magnitude plot')
plt.semilogx(w, mag,'b')        # Bode Magnitude plot
plt.grid() 

subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.title('Phase plot')
plt.semilogx(w,phase,'g')          # Bode phase plot
plt.grid() 




plt.show()
