num=int(input("enter the number"))#input
temp=num
sum=0
while(num>0):#Rotating the loop
    r=num%10
    sum=sum+(r*r*r)
    num=num//10
if (temp==sum):#After rotating the loop it will come to if condition
        print("armstrong number:")#if the number is true it will print this statement
else:
         print("not amstrong number:")#if the number is false it will print this statement