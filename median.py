import csv
with open("HeightWeight.csv",newline="") as f:
    r = csv.reader(f)
    listr = list(r)

listr.pop(0)
k = []
for i in range(len(listr)):
    h = listr [i][1]
    k.append(float(h))

k.sort()
lengthofk = len(k)
if(lengthofk % 2 == 0):
    median = (k [lengthofk/2]+k [lengthofk/2-1])/2
else :
    median = k [lengthofk/2]
print(median)






# 1,3,7,11,