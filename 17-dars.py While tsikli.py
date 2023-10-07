# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 16:49:56 2023

@author: T480
"""

# While tsikli

# input()

# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh) # yosh ni butun songa o'tkazamiz
# height = input("Bo'yingiz necha metr? ")
# height = float(height) # bo'yni o'nlik songa o'tkazamiz

# while()

# son = 1 # son ga 1 qiymatini beramiz
# while son<=5: # toki son 5 dan kichik yoki teng ekan...
#     print(son, end=' ') # son ni konsolga chiqaramiz,
#     son = son+1 # songa 1 qo'shamiz.
#     # son += 1 # songa 1 qo'shamiz.
# print('\nDastur tugadi')    

# son = 1 # son ga 1 qiymatini beramiz
# while son<=5: # toki son 5 dan kichik yoki teng ekan...
#     son += 1
#     print(son, end=' ') # son ni konsolga chiqaramiz,
# print('\nDastur tugadi')    

# son = 1 # son ga 1 qiymatini beramiz
# while son<=5: # toki son 5 dan kichik yoki teng ekan...
    
#     son = son+1 # songa 1 qo'shamiz.
#     # son += 1 # songa 1 qo'shamiz.
# print(son)    

# while and input

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting"
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): >>>"
# qiymat = ""
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print("Dastur tugadi")     

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting"
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): >>>"
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi")        

# break while

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting"
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): >>>"

# while True: # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi")    

# break operarotri
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     else:
#         print(f"{son} ning kvadrati {son**2}")
        
# continue operatori

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue # natijani chiqarmay tsikl boshiga qaytadi va keyingi qiymatni olib tsiklni davom etadi
#     else:
#         print(f"{son} ning kvadrati {son**2}")


# continue while
# son = 0 # juft sonlarni chiqaradi
# while son<10:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)
        
        
# son = 0 # toq sonlarni chiqaradi
# while son<10:
#     son += 1
#     if son%2==0:
#         continue
#     else:
#         print(son)        

# infinity loop - abadiy tsikl

# son = 0 
# while son<10:
#     if son%2!=0:
#         continue
#     else:
#         print(son)  

# son = 0 
# while son<10:
#     if son%2!=0:
#         continue
#     else:
#         print(son) 
#     son += 1   

son = 1
while son>0: # doim bajariladigan shart
    son += 1
    if son%2!=0: # doim bajariladigan shart
        continue
    else:
        print(son) # natija abadiy tsikl
