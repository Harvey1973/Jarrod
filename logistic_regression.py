import sklearn.linear_model
import random
import cluster
import pylab
import K_nearest

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
def Test1(x,y,k):
     clusters = cluster.Test(1, 4, False) ## get a cluster
     features, labels = [], []
     for c in clusters :
        for p in c.points:
            features.append(p.getFeatures())
            labels.append(p.label)
     features = pylab.array(features)
     labels = pylab.array(labels)
     model =sklearn.linear_model.LogisticRegression().fit(features, labels)
     for i in range(len(model.coef_)):
        print('For label', model.classes_[i], 'feature weights = ', model.coef_[i])
     print(x,y, 'prob =', model.predict_proba([[x, y]])[0])
     type(model.predict_proba([[x, y]])[0])
##     print('[500, 700] prob =', model.predict_proba([[500, 700]])[0])
##     print('[1200, 500] prob =', model.predict_proba([[1200, 500]])[0])
##     print('[1500, 600] prob =', model.predict_proba([[1500, 600]])[0])
     data = K_nearest.getGazedata(clusters)
     examples = K_nearest.buildGazeExamples(data)
    ##training, testSet = dividesample(examples)
     training = examples
     a = K_nearest.Example(None,x,y)
     testSet = []
     testSet.append(a)

##    truePos, falsePos, trueNeg, falseNeg = kNearestClassify(training, testSet, 'A', 9)
##    getStats(truePos, falsePos, trueNeg, falseNeg)
     result, prob = kNearestClassify(training, testSet,k)
    
     print(str(result)+' '+ str(float(prob)))
     pylab.show()
 



