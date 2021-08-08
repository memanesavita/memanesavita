n=int(input("enter the number"))
i=1
sum=0
while i<n:
    if n%i==0:
        sum=sum+i
    i=i+1
if n==sum:
    print("it is a perfect number")
else:
    print("it is a not perfect nuber")
    

