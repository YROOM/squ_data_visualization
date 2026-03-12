import numpy as np
import matplotlib.pyplot as plt

#fig = plt.figure()
fig,axes = plt.subplots()
t = np.arange(0.0,2.0,0.01)
s = np.sin(2*np.pi*t)
axes.plot(t,s,color='k',linestyle='-',label='line1')

s2 = np.sin(2*np.pi*(t+0.5))
axes.plot(t,s2,color='c',linestyle='--',label='line2')
plt.show()