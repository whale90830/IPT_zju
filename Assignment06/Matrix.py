class matrix:
    m = []  # proximity matrix
    PointsDic = {}  # cluster result
    def __init__(self,points):
        self.centerpoints = points
        for i in range(0,len(points)):
            self.PointsDic[i] = points[i]
            self.m.append([])   # append empty list to m thus initiate an empty proximity matrix
        for i in range(0,len(points)):
            for j in range(0,i):
                self.m[i].append(abs(points[i]-points[j]))

    def nextcluster(self):
        min = float('Inf')
        minx = -1
        miny = -1
        # find the min in the proximity matrix and note these two clusters
        for i in range(0,len(self.m)):
            for j in range(0,len(self.m[i])):
                if self.m[i][j]<min:
                    min = self.m[i][j]
                    minx = j
                    miny = i
        # update the cluster result
        self.PointsDic[minx] = (self.PointsDic[minx], self.PointsDic[miny])
        # update the centerpoints
        self.centerpoints[minx] = (self.centerpoints[minx]+self.centerpoints[miny])/2
        # update the proximity matrix
        del self.m[miny]
        del self.centerpoints[miny]
        for i in range(minx+1,len(self.m)):
            self.m[i][minx] = abs(self.centerpoints[minx]-self.centerpoints[i])
        for i in range(miny,len(self.m)):
            del self.m[i][miny]
            self.PointsDic[i] = self.PointsDic[i+1]