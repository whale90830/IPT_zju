from point import point
import functions

N = input("Please input how many points you have:   ")
K = input("Please input how many centroid you'd like to have:   ")
points = []
Clauses = []

for i in range(0,int(K)):
    Clauses.append([])
for i in range(0,int(N)):
    value = input("Please input the point:  ")
    points.append(point(float(value)))

Centroids = functions.GenerateCentroids(points,int(K),Clauses)
functions.adjust(points,Centroids,Clauses)
print("------")
for Clause in Clauses:
    for point in Clause:
        print(point.value)
    print("------")


