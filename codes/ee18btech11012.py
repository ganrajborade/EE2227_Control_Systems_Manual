import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,5,1000)
H1=np.array([])
H2 = np.array([])
H3 =[]
for i in t:
    h2=(25*i*np.exp(-5*i))
    h3 = (30/np.sqrt(35))*np.sin((np.sqrt(35)*i)/2)*np.exp(-5*i/2)
    h1 =(35/(2*np.sqrt(46)))*(np.exp((-9+np.sqrt(46))*i)-np.exp((-9-np.sqrt(46))*i))
    H1 =np.append(H1,[h1])
    H2 = np.append(H2,[h2])
    H3 = np.append(H3,[h3])
plt.plot(t,(H1),label="overdamped")
plt.plot(t,H2,label="critically damped")
plt.plot(t,H3,label="underdamped")
plt.xlabel("t")
plt.ylabel("Transfer funtion in time domain")
plt.title("DIfferent types of systems")
plt.legend()
plt.show()
