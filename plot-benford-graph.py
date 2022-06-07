from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

records = []
file = open('data.txt', 'r')
lines = file.readlines()
for line in lines: 
    records.append(int(line))

print(records)
count1,count2,count3,count4,count5,count6,count7,count8,count9 = 0,0,0,0,0,0,0,0,0
for num in records:
    if str(num)[:1]=='1':
        count1=count1+1
    if str(num)[:1]=='2':
        count2=count2+1
    if str(num)[:1]=='3':
        count3=count3+1
    if str(num)[:1]=='4':
        count4=count4+1
    if str(num)[:1]=='5':
        count5=count5+1
    if str(num)[:1]=='6':
        count6=count6+1
    if str(num)[:1]=='7':
        count7=count7+1
    if str(num)[:1]=='8':
        count8=count8+1
    if str(num)[:1]=='9':
        count9=count9+1
counted_list = [count1,count2,count3,count4,count5,count6,count7,count8,count9]
print(counted_list)
x_axis = [1,2,3,4,5,6,7,8,9]
y_axis = counted_list
fig, ax = plt.subplots()
ax.set_xticks(x_axis, labels=['1','2','3','4','5','6','7','8','9'])
ax.set_title('Count of Leading Digits')
ax.bar(x_axis, y_axis)
plt.show()