# ss list ko dekhein:
 
marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]



i=0
sum=0
while i<1:
    j=0
    sum1=0
    while j<5:
        sum1=sum1+marks[0][j]
        j=j+1
        print(sum1)
    # i=i+1
    avrg=sum1/5
    print(avrg)
    k=0
    sum2=0
    while k<5:
        sum2=sum2+marks[1][k]
        k=k+1
        print(sum2)
    avrg=sum2/5
    print(avrg)
    # i=i+1
    l=0
    sum3=0
    while l<5:
        sum3=sum3+marks[2][l]
        l=l+1
        print(sum3)
    avrg=sum3/5
    print(avrg)
    i=i+1
    total_sum=sum+(sum1+sum2+sum3)
    print(total_sum)
    total_avrg=total_sum/15
    print(total_avrg)

# kisi student ke peechle teen saal ke marks hai.
# Aap ko jitne bhi saal hai, har saal ke average marks print karne hai.
# Jaise, uppar wali list ka output yeh hona chahiye: