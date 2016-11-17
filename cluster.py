import random , string, copy, pylab

class Point(object):
    def __init__(self, name, originalAttrs, normalizedAttrs = None )
        """normalizedAttrs and originalAttrs are both lists"""
        self.name = name 
        self.unNormalized = originalAttrs
        if normalizedAttrs = None :
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
              retun oldcentroid.distance(self.centroid)
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
         centroid = self.pointType('mean', totoalVals/float(len(self.points)),totoalVals/float(len(self.points)))
         return centroid 

 ## clusterSet is used to hierachical clustering         
 class ClusterSet(object) :
     """set of cluster"""
     def __init__(self,pointType):
         self.members = []
     def add(self, c):
         if c in self.members :
             raise ValueError
         self.members.append(c)
     def getClusters(self):
         return self.members[:]
     def mergeClusters(self, c1, c2):
         points = [] 
         for p in c1.members() :
             points.append(p)
         for p in c2.members() :
             points.append(p)
         newC = Cluster(points , type(p))
         self.members.remove(c1)
         self.members.remove(c2)
         return c1, c2
      def findClosest 




