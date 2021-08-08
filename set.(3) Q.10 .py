# Ek algorithm banao jo fibonacci series ke pehle 100 number print kare.
# Fibonacci series aisi hoti hai:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 Iss series 
# ka pehla_number 0 hai aur dusra_number 1 hai.
#  Aur uske baad har number peechle do numbers ka sum hota hai. 
#  - Jaise, 
# teesra number = pehla_number + dusra_number1 = 0 + 1
#   chautha_number = dusra_number

num=int(input("enter the number :"))
x=0
y=1
z=0
while z<=num:
    print(z)
    x=y
    y=z
    z=x+y

    
    













