#Code by  Abhishek Shetkar
#April 2, 2020
#Released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

x = np.linspace(0,6,1000)
y = 1-(np.exp(-x))-(x*np.exp(-x))
plt.plot(4.52218,0.94,'o')
plt.text(3.4,0.95,'(4.52,0.94)')
plt.xlabel("$t$")
plt.ylabel("$c(t)$")
plt.grid()
plt.plot(x,y)

#if using termux
plt.savefig('./figs/ee18btech11002.pdf')
plt.savefig('./figs/ee18btech11002.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11002.pdf"))
#else
#plt.show()
