


           # PATTERN CODE TRANGLE

num=int(input("enter the number"))
colum=1
while colum<=num:
    row=1
    while row<=colum:
        print(row,end=" ")
        row=row+1
    k=colum
    while k>0:
        print(k,end=" ")
        k=k-1
    print()
    colum=colum+1

