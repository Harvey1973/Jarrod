import sklearn.linear_model
import random
import cluster
import pylab
import K_nearest
import matplotlib.pyplot as plt
import numpy as np

def Test():
    features, labels = [], []
    for  i in range(25000) :
        features.append([random.gauss(0,0.5), random.gauss(0, 0.5), random.random()])
        labels.append('A')
        features.append([random.gauss(0,0.5), random.gauss(2, 0.), random.random()])
        labels.append('B')
        features.append([random.gauss(2,0.5), random.gauss(0, 0.5), random.random()])
        labels.append('C')
        features.append([random.gauss(2,0.5), random.gauss(2, 0.5), random.random()])
        labels.append('D')

    model = sklearn.linear_model.LogisticRegression().fit(features, labels)

    print('model.classes_ =', model.classes_)
    for i in range(len(model.coef_)):
        print('For label', model.classes_[i], 'feature weights = ', model.coef_[i])
    print('[0, 0] prob =', model.predict_proba([[0, 0, 1]])[0])
    print('[0, 2] prob =', model.predict_proba([[0, 2, 2]])[0])
    print('[2, 0] prob =', model.predict_proba([[2, 0, 1]])[0])
    print('[2, 2] prob =', model.predict_proba([[2, 2, 1]])[0])
def readCoor(fileName):
    samples = []
    i = 0
    with open(fileName,'r') as f :
        try :
            for line in f :
                contents = line.split(',')
                x = contents[0]
                y = contents[1]
                
                ##only read the first 2 columns of data ,ignore time stamp for now 
                samples.append([float(x),float(y)])
                i = i + 1
                
        except ValueError :
            pass
    return samples 
def distance(p1,p2):
        #distance function is used to calculate the euclidean distance between two points
        result = 0.0 
        for i in range(2):
            result = result + (p1[i]-p2[i])**2   #euclidean distance formular 
        return result ** 0.5
def Test1():
     selection =['a','b','c','d']
     clusters = cluster.Test(4, 4, False) ## get a cluster
     features, labels = [], []
     count = 0
     liklihood = [0.0, 0.0, 0.0, 0.0]
     centroids = []
     for c in clusters :
        centroids.append(c.getCentroid().getFeatures.tolist())
        for p in c.points:
            features.append(p.getFeatures())
            labels.append(p.label)
     features = pylab.array(features)
     labels = pylab.array(labels)
     model =sklearn.linear_model.LogisticRegression().fit(features, labels)
     ##for i in range(len(model.coef_)):
     ##   print('For label', model.classes_[i], 'feature weights = ', model.coef_[i])
     
     #read a data file 
     test = readCoor('testdata.txt')  ## a list of list of coordinates
     for point in test :
         for c in centroids :
             if distance(point,centroids[c]) < 350 :
                 count += 1
     if count > 60:
         probVec = model.predict_proba(test).tolist()  #@ a list of list of probabilities for each point
         for i in range(len(probVec)) :
               maxindex = probVec[i].index(max(probVec[i]))
               liklihood[maxindex] += 1
               if max(liklihood) > 120 :
         # output mostlikely selection 
            
                  print (selection[liklihood.index(max(liklihood))])
                  liklihood = [0.0, 0.0, 0.0, 0.0]
##     print(type(probVec[0].index(max(probVec[0]))))



    # print(x,y, 'prob =', model.predict_proba([[x, y]])[0])
##     data = K_nearest.getGazedata(clusters)
##     examples = K_nearest.buildGazeExamples(data)
##    ##training, testSet = dividesample(examples)
##     training = examples
##     a = K_nearest.Example(None,x,y)
##     testSet = []
##     testSet.append(a)
##     result, prob = K_nearest.kNearestClassify(training, testSet,65)
##    
##     print(str(result)+' '+ str(float(prob)))
     pylab.show()
 



