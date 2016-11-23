import sklearn.linear_model
import random

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
print('[0, 0] prob =', model.predict_proba([0, 0, 1])[0])
print('[0, 2] prob =', model.predict_proba([0, 2, 2])[0])
print('[2, 0] prob =', model.predict_proba([2, 0, 1])[0])
print('[2, 2] prob =', model.predict_proba([2, 2, 1])[0])
