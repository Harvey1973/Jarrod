import numpy as np 
class perceptron(object):
    """perceptron classifier.

    Parameters :
    eta : float 
          learning rate (between 0 and 1)
    n_inter : int
           iterations over the training set 
    
    Attributes :
    w_ : 1d array 
         weights after updateing 
    errors_ : list 
        number of misclassifiers every run 
    """
    def __init__(self, eta = 0.01, n_iter = 10):
        self.eta = eta 
        self.n_iter = n_iter 
    def fit(self, X, y):
        """fit training data 

        Parameters

        X: {array like}, shape = [n_samples, n_features] n_samples is the number of samples
        and n_features is the feature vector. Each row of X is a sample .
        y is target variables (true labels) , array like, shape = [n_samples]
        """
        ## plus 1 here because we arbitrarily added a W0 and a feature value of 1 to simplify the threshold function

        self.w_ = np.zeros(1 + X.shape[1])  
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X,y):
            ##zip function returns tuples like ([xi(1),xi(2)],y)  , the first element is a list of all the eatures or sample i 
            ## the second element is the true lables 
            ## THIS loop will go through all samples of x , and update the weights (eachweight corresponding to a feature)
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi 
                self.w_[0] += update 
                errors += int(update!=0.0)
            self.errors_.append(errors)
        return self 

    def net_input(self,X):
            """Calculate net input"""
            return np.dot(X, self.w_[1:]) + self.w_[0]
    def predict (self, X) :
            """return class labels after unit step function"""
            return np.where(self.net_input(X)>= 0.0, 1, -1)



