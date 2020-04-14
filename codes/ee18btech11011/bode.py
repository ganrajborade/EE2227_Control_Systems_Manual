import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib import style
import control
from control import tf
# a=alpha and b=beta
#if using termux
import subprocess
import shlex
#end if

a=[0.01, 0.1, 1.1, 1, 5]
b=[0.01, 1.1, 0.1, 2, 2.1]
for i in range(0,5):
    system= signal.lti([1,2*b[i]+2],[ 1, 2*b[i], a[i]])
    w, mag, phase =signal.bode(system)
    plt.figure()
    plt.semilogx(w, mag)    
    plt.xlabel ("Frequency")
    plt.ylabel ("Magnitude")
plt.legend()

#if using termux
plt.savefig('./figs/ee18btech11011.pdf')
plt.savefig('./figs/ee18btech11011.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11011.pdf"))
#else
#plt.plot()

