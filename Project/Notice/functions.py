import random
import operator
from classpoint import point

def avg(points):
    countdic = {}
    centerpoint = []
    if len(points):
        for apoint in points:
            for word in apoint.words:
                if word in countdic:
                    countdic[word] += 1
                else:
                    countdic[word] = 1
        sortedWord = sorted(countdic.items(), key=operator.itemgetter(1), reverse=True)
        for word in sortedWord:
            centerpoint.append(word[0])
        if len(centerpoint) > 6:
            return point(centerpoint[0:6])
        else:
            return point(centerpoint)

def FreshClauses(points, Clauses):      #Clauses is a 2-dimension, k-length list, storing point[]
    for Clause in Clauses:
        Clause.clear()
    for point in points:
        Clauses[point.inclause].append(point)

def SSE(Clauses,centroids):
    sse = 0
    for Clause in Clauses:
        for point in Clause:
            sse += pow(point.distance(centroids[point.inclause]),2)
    return sse

def TryNextLoop(points,centroids,Clauses):
    for Clause in Clauses:
        centroids[Clauses.index(Clause)] = avg(Clause)
    for point in points:
        point.group(centroids)
    FreshClauses(points, Clauses)
    return SSE(Clauses,centroids)


def adjust(points, centroids, Clauses):      #centroids is a list of centroid, with a size of k
    sse = SSE(Clauses,centroids)
    while 1:
        temp_points = points        #back up
        temp_centroids = centroids
        temp_Clauses = Clauses
        new_sse = TryNextLoop(temp_points,temp_centroids,temp_Clauses)
        if new_sse < sse:
            points = temp_points    #fresh
            centroids = temp_centroids
            Clauses = temp_Clauses
            sse = new_sse
        else:
            break

def GenerateCentroids(points,K,Clauses):
    GenerateSet = []
    while len(set(GenerateSet)) < K:
        GenerateSet.append(random.randint(0,len(points)))
    Centroids = []
    for i in GenerateSet:
        Centroids.append(points[i])
    for point in points:
        point.group(Centroids)
    FreshClauses(points, Clauses)
    return Centroids


