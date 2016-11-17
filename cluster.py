import random , string, copy, pylab

class Point(object):
    def __init__(self, name, originalAttrs, normalizedAttrs = None ):
        """normalizedAttrs and originalAttrs are both lists"""
        self.name = name 
        self.unNormalized = originalAttrs
        if normalizedAttrs == None :
            self.attrs = originalAttrs 
        else :
            self.attrs = normalizedAttrs
    def dimensionality (self):
        return (len(self.attrs))
    def getAttrs(self):
        return self.attrs
    def getOriginalAttrs(self):
        return self.unNormalized 
    def distance(self, other):
        #distance function is used to calculate the euclidean distance between two points
        result = 0.0 
        for i in range(self.dimensionality()):
            result = result + (self.attrs[i]-other.attrs[i])**2   #euclidean distance formular 
        return result ** 0.5
    def getName(self):
        return self.name
    def toStr(self):
        return self.name +str(self.attrs)
    def __str__(self):
        return self.name


class Cluster(object) :
      """points are list of object of type Point defined above , they are the points in a cluster """
      def __init__(self, points, pointType):
          self.points = points 
          self.pointType = pointType
          self.centroid = self.computeCentroid()
      def singleLinkageDist(self, other) :
          minDist = self.points[0].distance(other.points[0])
          for p1 in self.points :
              for p2 in other.points :
                  if p1.distance(p2)<minDist :
                      minDist = p1.distance(p2)
          return minDist 
      def maxLinkageDist (self, other) :
          maxDist = self.points[0].distance(other.points[0])
          for p1 in self.points:
              for p2 in other.points :
                  if p1.distance(p2)>maxDist :
                      maxDist = p1.distance(p2)
          return maxDist
      def averageLinkageDist(self, other):
          totdist = 0.0 
          for p1 in self.points :
              for p2 in other.points :
                  totdist += p1.distance(p2)
          average = totdist/(len(self.points)*len(other.points))
          return average
      def update (self, points) :
          """update the oldcentroid and returns the change between one iteration """
          oldcentroid = self.centroid 
          self.points = points 
          #make sure there are actual points in a cluster 
          if(len(points)>0):
              self.centroid = self.computeCentroid()
              return oldcentroid.distance(self.centroid)
          else :
              return 0.0 
      def members(self) :
          for p in self.points :
              yield p
      def isIn(self, name):
          """trying to find is a point is in a cluster """
          for p in self.points :
              if p.getName() == name :
                  return True 
          return False 
      def toStr(self):
         result = ''
         for p in self.points :
             result = result + p.toStr() + ','
         return result[:-2]
      def __str__(self):
         name = []
         for p in self.points :
             name.append(p.getName())
         name.sort()
         result = ''
         for p in name :
             result = result + p + ', '
         return result[:-2]
      def getCentroid(self):
         return self.centroid
      def computeCentroid(self):
         dim = self.points[0].dimensionality()
         totoalVals = pylab.array([0.0]*dim)
         for p in self.points :
             totoalVals += p.getAttrs()
         centroid = self.pointType('centroid', totoalVals/float(len(self.points)))
         return centroid 

 ## clusterSet is used to hierachical clustering         
class ClusterSet(object) :
     """set of cluster"""
     def __init__(self,pointType):
         self.members = []
     def add(self, c):
         """add one cluster in the list"""
         if c in self.members :
             raise ValueError
         self.members.append(c)
     def getClusters(self):
         return self.members[:]
     def mergeClusters(self, c1, c2):
         """this will merge two clusters , by appending its members in a list and instantiate using Cluster class"""
         points = [] 
         for p in c1.members() :
             points.append(p)
         for p in c2.members() :
             points.append(p)
         newC = Cluster(points , type(p))
         self.members.remove(c1)
         self.members.remove(c2)
         return newC 
     def findClosest(self, metric):
         """find the closest  pair of clusters and return a tuple of thoses 2 clusters"""
         minDistance = metric (self.members[0],self.members[1])
         toMerge = (self.members[0],self.members[1])
         for c1 in self.members :
             for c2 in self.members :
                 if c1 == c2 :
                     continue 
                 if metric (c1,c2) < minDistance :
                     minDistance = metric (c1, c2)
                     toMerge = (c1, c2)
         return toMerge
     def MergeOne(self, metric, toPrint = False ):
         """merge 2 cluster using findClosest"""
         if len(self.members ) == 1 :
             return None 
         if len(self.members)  == 2 :
             return mergeClusters(self.members[0],self.members[1])
         ##otherwise find the closest pair 
         toMerge = findClosest(metric) 
         if toPrint :
             print ('merged')
             print (' '+ str(toMerge[0]))
             print ('with')
             print (' '+str(toMerge[1]))
         self.mergeCluster(toMerge[0],toMerge[1])
         ##return the merged 2 clusters 
     def mergeN(self, metric, numClusters = 1, history = [], toPrint = False): 
          assert numClusters >=1 
          while len(self.members)> numClusters :
              merged = self.MergeOne(metric, toPrint)
              history.append(merged)
          return history 
     def numClusters(self):
          return len(self.members) + 1
     def __str__(self) :
          result = ''
          for c in self.members :
              result = result + str(c) + '\n'
          return result 


## k means 
def kmeans(points, k, cutoff, pointType, maxIter = 100, toPrint = False) :
    #first step : randomly choose k points 
    initialCentroids = random.sample(points, k)
    clusters = []
    #assign each of those points to its own cluster 
    for p in initialCentroids :
        clusters.append(Cluster(p, pointType))
    numIter = 0
    biggestChange = cutoff 
    while biggestChange >=cutoff and numIter < make :
        #creat a list containing k empty lists 
        newClusters = []
        for i in range (k):
            newClusters.append([])
        for p in points :
            #find the centroid closest to p ,which is a point 
            smallestDistance = p.distance(clusters[0].getCentroid())
            index = 0 
            for i in range(k) :
                distance = p.distance(centroid[i].getCentroid())
                if distance < smallestDistance :
                    smallestDistance = distance
                    index = i 
            ## add p to the list of points for appropriate cluster 
            newClusters[index].append(p)
        ## now update the cluster and calculate change
        biggestChange = 0.0
        for i in range(len(clusters)):
            change = cluster[i].update(newClusters[i])
            biggestChange = max(biggestChange,change)
        numIter +=1
    maxDist = 0.0
    for c in clusters :
        for p in c.members():
            if p.distance(c.getCentroid()) > maxDist :
                maxDist = p.distance(c.getCentroid())
    print ('Number of iterations =' + numIter +'Max diameter ' + maxDist)     
    return clusters , maxDist      
         





