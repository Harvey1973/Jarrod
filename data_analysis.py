import matplotlib.pyplot as plt
import numpy as np
from filters import MovingAverage
from exp_filters import ExponentialAverage

dataset = [1.1,5.5,7.3,2.3,6.6,7.8,8.3,2.3,6.3,4.3,8.3,7.3,1.3,2.0,1.2,5.5]            

def moving_exp(values,window) :
       weights = np.exp(np.linspace(-1,0,window))
       weights /= weights.sum()
       return np.convolve(values,weights)[window-1:len(values)]
def moving (values,window) :
    weights = np.repeat (1.0,window)/window
    smas = np.convolve (values,weights,'valid')
    return smas

with open ('OriginalData.txt','r') as f_1:
    data = f_1.read()
data = data.split('\n')
  
eye_x = [row.split(',')[0] for row in data]
eye_y = [row.split(',')[1] for row in data]
x_coor = map(float,eye_x)
y_coor = map(float,eye_y)
sma_x = moving(x_coor,10)
sma_y = moving(y_coor,10)
exp_x = moving_exp(x_coor,10)
exp_y = moving_exp(y_coor,10)



fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title("Original gaze point")    
ax1.set_xlabel('x coordinates')
ax1.set_ylabel('y coordinates')
leg = ax1.legend()



ax1.plot(x_coor,y_coor, c='r',label = 'original data')
ax1.plot(sma_x,sma_y, c='b')
ax1.plot(exp_x,exp_y, c='g')

plt.show()








