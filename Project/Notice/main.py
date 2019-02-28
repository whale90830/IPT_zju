from classpoint import point
import functions
import json
import load

K = input("Please input how many centroid you'd like to have:   ")
rawpoints = load.GetList("dividedNotice.json")
Clauses = []
points = []
for rawpoint in rawpoints:
    points.append(point(rawpoint))

for i in range(0,int(K)):
    Clauses.append([])

if int(K)>len(points):
    exit("Too Many centroids!")

Centroids = functions.GenerateCentroids(points,int(K),Clauses)
functions.adjust(points,Centroids,Clauses)
print("------")
for Clause in Clauses:
    if(len(Clause)):
        print(functions.avg(Clause).words)
    for point in Clause:
        point.show()
    print("------")


