num=int(input("enter the number:"))#enter the number
temp=num
rev=0
while(num>0):#looping if the condition true means it will enter into next line
    dig=num%10
    rev=rev*10+dig
    num=num//10
    if(temp==rev):#if the condition is fail it will come hear
         print("the number is palindrom number:")
    else:
         print("the number is not palindrom number:")
