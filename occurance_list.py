list=[1,2,3,4,5,6,1,1,1,1]#declearing a list
occurance={item:list.count(item) for item in list} #This lines for counting the number of times number will occuring
print(occurance.get(1)) #This line print the occurance of numbers