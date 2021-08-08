

#     Ab hum pichli wali game ko thoda change karenge.
#      Humne sirf yeh check kara the ki kya user ne jo number 
#      input kiya hai wo humare number ke barabar hai ya nahi.
#     Ab hum user ko yeh bhi batayenge ki jo usne number guess kiya hai,
#      woh humare number se chota hai ya bada hai.
#     Jaise, agar user ne 4 input kiya.
#      Hum check karenge ki kya 4 5 se chota hai? 
#     Haan 4 5 se chota hai.
#      Hum print karenge ki "aapka number chota hai! Ek aur baar try karo".
#     Phir hum user se ek baar aur number input lenge.
#      Socho iss baar user ne 7 daala.
#      Ab hum check karenge ki kya 7 5 se chota hai.
#       Iska jawab nahi hoga.
#        Ab hum print karenge ki "aapka number bada hai! Ek aur baar try karo".
#     Ab socho user ne 5 input kar diya.
#      Yeh number humare number ke barabar ho jayega. 
#      Ab hum print karenge ki " waah! Aapne number guess kar liya".
#     Hum aisa tab tak karte rahenge jab tak user 
#     humara number guess nahi kar leta.
#      Ya uski chances (jo ki 10 hain) khatam nahi ho jaati.


x=6
i=1
while i<=6:
    user=int(input("enter number"))
    if user==x:
        print("aapne sahi gess kiya")
        break
    elif user<x:
        print("aapne low number gess kiya") 
    else:
        print("aapne high number gess kiya")
    i=i+1

    





