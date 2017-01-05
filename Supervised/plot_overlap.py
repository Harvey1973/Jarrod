import matplotlib as p
import pylab
def plot(fileName):
    f = open (fileName,'r')
    for line in f :
        marker =''
        contents = line.split(',')
        x = float(contents[0])
        y = float(contents[1])
        label = int(contents[3])
        marker = ['ro','bo','ko','go']
        pylab.plot(x,y,marker[label-1])
plot('combined_calibration_log2x2.txt')
pylab.show()
