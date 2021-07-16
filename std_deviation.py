
import math



# list of elements to calculate mean
import csv
with open('data1.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)


data = file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for i in data:
        total = total + int(i)
    mean = total / n
    return(mean)


squaredList = []
for i in data:
    num = int(i) - mean(data)
    num = num**2
    squaredList.append(num)
fs = 0
for i in squaredList:
    fs = fs+i
result = fs/(len(data) - 1)
std = math.sqrt(result)
print(std)