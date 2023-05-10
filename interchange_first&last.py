
list=[]#Declearing a list
num = int(input("enter the no index"))#input
for i in range(num):# This loop will rotating number of times
    list1 = int(input())
    list.append(list1)
print("Before the list is :", list)
temp=list.pop(0)#removing the first element
temp1=list.pop(-1)#removing the last element
print(list)#printing the list
list.insert(0,temp1)#this is for inserting a number
list.append(temp)#last element
print(list)#printing the list