     
           
           
           
            #    PRIME NUMBER

user=int(input("enter the number"))
i=1
count=0
while i<=user:
    if user%i==0:
        count=count+1
    i=i+1
if count==2:
    print("it is a prime number")
else:
    print("it is not prime number")


# i=2
# while i<=100:
#     j=2
#     x=0
#     while j<i-1:
#         if i%j==0:
#             x=x+1
#         j=j+1
#     if i>=1 and x==0:
#         print(i,"primenumber")
#     else:
#         print(i,"not prime number")
#     i=i+1
    


        
