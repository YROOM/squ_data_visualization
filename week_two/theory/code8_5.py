import matplotlib.pyplot as plt
import numpy as np

fig,axes =plt.subplots()
t = np.arange(0.0,2.0,0.01)
s = np.sin(2*np.pi*t)
axes.plot(t,s,color='k',linestyle='-',label='line1')
axes.set_xticks(np.arange(0.0,2.5,0.5))
axes.set_yticks([-1,0,1])
axes.minorticks_on()
#
# axes.spines['right'].set_color('none')
# axes.spines['top'].set_color('none')
# axes.spines['bottom'].set_position(('data',0))
# axes.spines['left'].set_position(('data',0))
#
# axes.legend()

#
# plt.show()
