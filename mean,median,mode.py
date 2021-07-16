import csv
with open("HeightWeight.csv",newline="") as f:
    r = csv.reader(f)
    listr = list(r)

listr.pop(0)
k = []
for i in range(len(listr)):
    h = listr [i][1]
    k.append(float(h))

lengthofk = len(k)
total = 0
for j in k:
    total = total+j
mean = total/lengthofk
print(mean)