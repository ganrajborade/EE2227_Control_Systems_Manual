#Bode phase plot using scipy in python
from scipy import signal
import matplotlib.pyplot as plt

#Defining the transfer function 
#plug [2],[1,3,2] if your transfer function is (2/s^2+3s+2)
s1 = signal.lti([2],[1, 3,2])

#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
w,mag,phase = signal.bode(s1)

#plt.figure()            #uncomment these two lines if you want bode magnitude plot
#plt.semilogx(w,mag)    # Bode magnitude plot

plt.figure()
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.title('Phase plot')
plt.semilogx(w,phase)          # Bode phase plot
plt.grid() 
plt.show()
