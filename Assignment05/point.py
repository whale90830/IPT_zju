class point:
    def __init__(self,value):
        self.value = value
        self.inclause = -1

    def __lt__(self,other):         #overload '<' operator
        if isinstance(other,point):     #check the comparing object is a point
            return self.value < other.value
        else:
            return NotImplemented

    def __nearest(self,dists):
        min = float('Inf')
        for dist in dists:
            if dist < min:
                min = dist
        return dists.index(min)

    def group(self,centroids):
        dists = []
        for centroid in centroids:
            dists.append(abs(self.value-centroid))
        self.inclause = self.__nearest(dists)
