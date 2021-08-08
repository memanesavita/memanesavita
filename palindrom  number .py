
num=int(input("enter the no."))
i=0
a=num
while num>0:
    i=(i*10)+num%10
    num=num//10
if a==i:
    print("palindrom")
else:
    print("not")



























