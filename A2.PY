list1=[10,30,45,23,45,12]
print(list1)
sum=0
for i in list1:
    sum=sum+i
print("sum of list1 is",sum)
a=sum/len(list1)
print("average of list1 is",a)
s=sorted(list1)
print("sorted list is",s)
print("largest number is",s[-1])
print("smallest number is",s[0])
list1.append(100)
print("list after appending 100",list1)



