import math
import csv
with open("data5.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)
data= file_data[0]

def mean(data):
    n = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/n
    print(total)
    print(mean)

    return mean

squared_list = []
for number in data:
    a = int(number)-mean(data)
    a = a**2
    print(a)
    squared_list.append(a)
    
sum1 = 0
for i in squared_list:
    sum1 = sum1+i
    print(sum1)
result = sum1/(len(data)-1)
stdr_dvatn = math.sqrt(result)
print(stdr_dvatn)
