from point import point
import random

def FreshClauses(points, Clauses):      #Clauses is a 2-dimension, k-length list, storing point[]
    for Clause in Clauses:
        Clause.clear()
    for point in points:
        Clauses[point.inclause].append(point)

def avg(points):            # calculate the averange of a set of points
    sum = 0
    if len(points):
        for point in points:
            sum = sum + point.value
        return sum/len(points)
    else:
        print("Some centroids are too far from points")
        exit()

def SSE(Clauses,centroids):
    sse = 0
    for Clause in Clauses:
        for point in Clause:
            sse += pow(point.value-centroids[point.inclause],2)
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
    #---------      radom       ----------
    # max = float("-Inf")
    # min = float("Inf")
    # for point in points:
    #     if(point.value>max):
    #         max = point.value
    #     if(point.value<min):
    #         min = point.value
    # Centroids = []
    # for i in range(0,K):
    #     Centroids.append(random.uniform(min,max))
    # for point in points:
    #     point.group(Centroids)
    # FreshClauses(points, Clauses)
    # return Centroids

    #--------      sort     ----------
    points.sort()
    avg_len = len(points)/K
    Centroids = []
    for i in range(0,K):
        if i < K-1:
            Centroids.append(avg(points[int(i*avg_len):int((i+1)*avg_len)]))
        elif i == K-1:
            Centroids.append(avg(points[int(i * avg_len):]))
    for point in points:
        point.group(Centroids)
    FreshClauses(points, Clauses)
    return Centroids


