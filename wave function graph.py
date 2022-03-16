import matplotlib.pyplot as plt
import numpy as np
t=np.arange(0,12,0.1)
g=np.arange(0, 20, 0.2)
amp=np.sin(t)
smp=np.cos(g)

a=input('Enter graph you want sin@/cos@:')
if a=='sin@':
    plt.plot(t,amp)
    plt.grid(True)
    plt.xlabel('time')
    plt.ylabel('amp')
    plt.show()
    
elif a=='cos@':
    plt.plot(g,smp)
    plt.grid(True)
    plt.xlabel('time')
    plt.ylabel('amp')
    plt.show()
    
    
else:
    print('INVALID INPUT')
