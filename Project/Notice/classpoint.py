class point(object):
    def __init__(self,words):
        self.words = words
        self.inclause = -1

    def distance(self, other):
        return len([i for i in self.words if i not in other.words])

    def __nearest(self,dists):
        min = float('Inf')
        for dist in dists:
            if dist < min:
                min = dist
        return dists.index(min)

    def group(self, centroids):
        dists = []
        for centroid in centroids:
            dists.append(self.distance(centroid))
        self.inclause = self.__nearest(dists)

    def show(self):
        noticeString = ""
        for word in self.words:
            noticeString += word
        print(noticeString)
