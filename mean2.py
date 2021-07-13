import csv

with open('data.csv', newline="") as f:
  reader = csv.reader(f)
  height_weight_data = list(reader)

height_weight_data.pop(0)

print(height_weight_data[0])
sum_of_heights=0
for a in height_weight_data:
    sum_of_heights=sum_of_heights+float(a[1])
print(sum_of_heights)

count=0
for a in height_weight_data:
    count=count+1
print(count)

average=sum_of_heights/count
print(average)