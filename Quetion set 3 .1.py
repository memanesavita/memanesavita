
# Aisa code likho jisse 20 se 100 mein wahi 
# numbers print ho jo 2 se divisible hai yaani 
# numbers ka 2 se bhaag karne par remainder (shesh) 0 bachta hai.



i=20
while i<=100:
    if i%2==0:
        print(i)
    i=i+1
user=int(input("enter the no."))
i=0
a=user
while user>0:
    i=(i*10)+user%10
    user=user//10
if a==i:
    print("palodrom")
else:
    print("not")



