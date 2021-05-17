#  marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ] 
# Yeh kisi student ke peechle teen saal ke marks hai. 
# Aap ko teeno saalo, ke sab subjects ke marks ka total calculate karna hai.
# Jaise uppar di hui nested list ka sum - 1142 aayega. 
# Edge Cases: Check your program for following nested lists as well
# (bina code change kiye chalna chahiye, nahi toh aapne sahi se code nahi
# likha):
# arks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ] 
# k=marks[0]+marks[1]+marks[2]
# j=k
# i=0
# sum=0
# while i<len(j):
#     sum=sum+k[i]m
#     i=i+1
# print(sum)    




# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ] 
# a=marks[0]+marks[1]+marks[2]
# s=a
# i=0
# sum=0
# while i<len(s):
#     sum=sum+a[i]
#     i=i+1
# print(sum)

# Jaise uppar di hui nested list ka sum - 965 aayega.
    
    

marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
] 

y=marks[0]+marks[1]+marks[2]+marks[3]
x=y
i=0
sum=0
while i<len(y):
    sum=sum+x[i]
    i=i+1
print(sum)



# Jaise uppar di hui nested list ka sum - 1324 aayega.