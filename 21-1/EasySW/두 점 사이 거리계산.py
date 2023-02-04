import numpy as np

class Distance():

    def __init__(self,dim):
        self.dim = dim
        self.x = np.zeros(self.dim)
        self.y = np.zeros(self.dim)

        for i in range(self.dim):
            self.x[i] = float(input())
        for i in range(self.dim):
            self.y[i] = float(input())

    def Euclidean(self,ceil):
        tmp = (self.x-self.y) ** 2
        dist = 0
        for i in range(self.dim):
            dist += tmp[i]
        dist = np.sqrt(dist)
        if ceil==True:
            return int(np.ceil(dist))
        if ceil==False:
            return dist

ceil=True
Distance = Distance(2)
print(Distance.Euclidean(ceil))