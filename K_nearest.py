import random
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

def buildGazeExample(fileName):
    data = getData(fileName)
    examples = []
    for i in range(len(data['x_coor'])):
        a = Example(data['selection'][i], data['x_coor'][i], data['y_coor'][i])
        examples.append(a)
    return examples
def dividesample(examples):
    test_index = random.sample(range(len(examples)),len(examples)/5)
    trainingSet = []
    testSet = []
    for i in range (len(examples)):
        if i in test_index :
            testSet.append(examples[i])
        else :
            trainingSet.append(examples[i])
    return trainingSet , testSet



