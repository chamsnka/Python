def sort(num):#defining the sorting
    for i in range(len(num)-1,0,-1):#Here we declear the start and stop and step bit
      for j in range(i):#looping
          if(num[j]>num[j+1]):#It will check the if condition if the condition is true it will enter in to sorting logic
             temp=num[j]#sorting
             num[j]=num[j+1]
             num[j+1]=temp
num=[4,6,8,9,0,1,2]#after sorting it will print in order
sort(num)
print(num)#printing the number

