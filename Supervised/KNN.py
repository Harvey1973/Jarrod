import random
import cluster
import pylab
class Example(object): 
    """this class is used to creat instances of a single point in the gaze data which will be used for traing"""
    def __init__(self,selection,x_coor,y_coor) :
        self.featureVec = (x_coor,y_coor)
        self.label = selection 
    def featureDist(self, other):
        """returns the euclidean distance of 2 example"""
        dist = 0.0 
        for i in range(len(self.featureVec)):
            dist += abs(self.featureVec[i]-other.featureVec[i])
        return dist**0.5
    def getX(self):
        return self.featureVec[0]
    def getY(self):
        return self.featureVec[1]
    def getLabel(self):
        return self.label 
    def getFeature(self):
        return self.featureVec
    def __str__(self):
        return  str(self.getX()) +','+str(self.getY()) + ',' + str(self.label)
def getGazedata(fileName):
    data ={}  ##defined as dictionary 
    data['selection'], data['x_coor'], data['y_coor'] = [], [], []
    f = open(fileName,'r')
    for line in f :
           contents = line.split(',')
           data['selection'].append(contents[3])
           data['x_coor'].append(contents[0])
           data['y_coor'].append(contens[1])
    return data
def buildGazeExample(fileName):
    data = getData(fileName)
    examples = []
    for i in range(len(data['x_coor'])):
        a = Example(data['selection'][i], data['x_coor'][i], data['y_coor'][i])
        examples.append(a)
    return examples