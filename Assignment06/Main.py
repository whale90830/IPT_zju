import Matrix

str = input("Please input points, split by blank\n")
str = str.strip()   # eat the white before or after the valid input
strpoints = str.split(" ")  # divide the input and store it in a string list
points = []
for point in strpoints:
    try:
        points.append(float(point)) # transfer the string point to float
    except:
        print("Input error")

iMatrix = Matrix.matrix(points)
# call the cluster function until there is only one cluster
while(len(iMatrix.m) > 1):
    iMatrix.nextcluster()
# show the cluster result
print(iMatrix.PointsDic[0])