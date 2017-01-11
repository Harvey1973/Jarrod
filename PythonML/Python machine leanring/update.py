from multiclassSVM import *
import numpy as np
from collections import Counter
from sklearn.preprocessing import StandardScaler
def update(canvas , pos):
#assume x,y are the coordiates supplied by the eye tracker 
    pos = np.array([x,y])
#standardize it before make predictions 
    stdsc = StandardScaler()
    pos = stdsc.fit_transform(pos)
    prediction = SVC.predict([pos])

    window = np.append(prediction)
    
    #depend on how many points we want to look in order to make prediction
    if len(window == 20):
        b = Counter(a)
        prediction = b.mostcommon(1)    ##output the most common class labels 








