import random
import cluster
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

def findKnearest(example, exampleSet, k):
    """example is a single point , and exampleSet is a set of points, this function will find k nearest neighbours a example has in the exampleSet"""
    kNearest, distance =[], [] 
    ## build a list that contains the first k exmaples and their distances with one given point ----this is a starting point 
    for i in range(k):
        kNearest.append(exampleSet[i])
        distance.append(example.featureDist(exampleSet[i]))
    maxDist = max(distance)   ##get maximum distance
    ##now consider the poins left  --- this is a iterative process that continuesly update the nearest points 
    for e in exampleSet[k:]:
        dist = example.feartureDist(e)
        if dist < maxDist :    
            ## in this case we need to update the kNearest since we have found a point that is closer 
            maxIndex = distance.index(maxDist)
            kNearest[maxIndex] = e 
            distances[maxIndex] = dis 
            maxDist = max(distances)  ##update the maximum distance 
    return kNearest, distances

def kNearestClassify(training, testSet, label, k):
    """assume training and testSet are both list of object examples , k is an integer , this method use findKnearest methond defined above to predict the category a given example will fall into,for testing purposes 
    , 20% of training data will be used for testing  """
    truePos, falsePos, trueNeg, falseNeg = 0, 0, 0, 0
    for e in testSet :
        ## tranverse each point in the testSet and classifiy it 
        nearest, distances = findKnearest(e, training, k)
        ## conduct vote 
        numMatch = 0
        for i in range(len(nearest)):
            ##this loop with count the occurences of each category in the nearest neighbours 
            if nearest[i].getLabel() == label :
                ## if an example in nearest has the given label then numMatch plus 1 
                numMatch += 1
        if numMatch > k//2 :
              #guess label
              if e.getLabel() == label :
                  truePos += 1
              else :
                  falsePos += 1
        else :
            if e.getLabel() != label :
                trueNeg += 1
            else :
                falseNeg += 1
    return truePos, falsePos, trueNeg, falseNeg 


##The follwing methods will be used to evaluate the performance of the classifier 
def accuracy(truePos, falsePos, trueNeg, falseNeg) :
    numerator = truePos + trueNeg 
    denominator = truePos + trueNeg + falseNeg +falsePos
    return numerator/denominator
def sensitivity(truePos, falseNeg):
    try :
        return truePos/(truePos + falseNeg)
    except ZeroDivisionError :
        return float('nan')
def specificity(trueNeg, falsePos):
    try :
        return trueNeg/(trueNeg+falsePos)
    except ZeroDivisionError:
        return float('nan')
def posPredVal(truePos, falsePos):
    try :
        return truePos/(truePos + falsePos)
    except ZeroDivisionError :
        return float('nan')
def negPredVal(trueNeg, falseNeg):
    try :
        return trueNeg/(trueNeg+falseNeg)
    except ZeroDivisionError :
        return float('nan')
def getStats(truePos, falsePos, trueNeg, falseNeg, verbose = True):
    accur = accuracy(truePos, falsePos, trueNeg, falseNeg)
    sens = sensitivity(truePos, falseNeg)
    spec = specificity(trueNeg, falsePos)
    ppv = posPredVal(truePos, falsePos)
    if verbose :
        print('Accuracy = ', round(accur, 3))
        print('Sensitivity = ', round(sens,3))
        print('specificity = ',round(spec,3))
        print('Positive Predicative value = ', round(ppv,3))
    return (accur, sens, spec, ppv)
##the following method will read the gaze point data 

clusters = Test(1, 4, False) ## get a cluster
def getGazedata(clusters):
    data ={}  ##defined as dictionary 
    data['selection'], data['x_coor'], data['y_coor'] = [], [], []
    for c in clusters :
        for p in c.points:
               data['selection'].append(p.label)
               data['x_coor'].append(p.getFeatures()[0])
               data['y_coor'].append(p.getFeatures()[1])
    return data
def buildGazeExamples(data):
    examples = []
    for i in range(len(data['selection'])):
        a = Example(data['selection'][i], data['x_coor'][i], data['y_coor'][i])
        examples.append(a)
    return examples













