# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 21:26:40 2023

@author: T480
"""

# 10-dars. IF-ELSE
# Muallif: Azimov Temurbek

# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:
#     print(avto.title())

# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar: # ... avtolar ichidagi har  bir avto uchun...
#     if avto == 'bmw': # agar avto bmw ga teng bo'lsa
#         print(avto.upper())
#     else: # aks holda...
#         print(avto.title())

# ism = 'Ali'

# ism.lower() == 'ali'

# ism = input("Ismingiz nima? \n>>>")
# if ism.lower() != 'ali':
#     print(f"Uzr, {ism.title()} biz Alini kutyapmiz")
# else:
#     print("Salom, Ali!")

# javob = float(input("12x6 nechiga teng?\n>>>"))
# if javob != 72:
#     print("Javob xato")

# yosh = int(input('Yoshingiz nechida? >>> '))
# if yosh >= 18:
#     print('Xush kelibsiz!')
# else:
#     print('Kirish mumkin emas')

# Login = input('Yangi login tanlang: ')
# if len(Login) <= 5:
#     print("Login 5 harfdan kam bo'lmasligi kerak")  

# yil = int(input("Tug'ilgan yilingizni kiriting: "))
# if 2023-yil<18: # foydalanuvchining yoshini xisoblaymiz
#    print(f"Yoshingiz {2023-yil} da ekan.")
#    print("Kirish mumkin emas!")
# else:
#     print("Xush kelibsiz")

# yosh = int(input("Yoshingiz nechida? >>> "))
# if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")

# x, y = 40, 25 # x = 25, y = 50
# print("x>y") if x>y else print("x<y")

# avtolar = ['audi','bmw','volvo','kia','hyundai']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())

# ism = 'Ali'
# ism.lower() == 'ali'

# ism = input("Ismingiz nima? >>> ")
# if ism.lower() != 'ali':
#     print(f"Uzr {ism.title()}, biz Alini kutyapmiz ")
# else:
#     print("Salom, Ali!")

# javob = float(input("12x6 nechiga teng >>> "))
# if javob != 72:
#     print('Javob xato!')

# yosh = int(input('Yoshingiz nechida? >>> ')) 
# if yosh>=18:
#     print('Xush kelibsiz!')
# else:
#     print("Kirish taqiqlanadi!")

# yosh = int(input("Yoshingiz nechida? >>> "))
# if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")

# AMALIYOT
# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, 
# ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] 
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())
        
# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] 
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())

# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa,
# "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. 
# Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.

# login = input("Login kiriting: ")
# if login.lower() == 'admin':
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {login.title()}!")

# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, 
# "Sonlar teng" ekan degan yozuvni konsolga chiqaring.

# print("2 ta son kiriting")
# b1_son = float(input("Birinchi son: >>> "))
# i2_son = float(input("Ikkinchi son: >>> "))
# if b1_son == i2_son:
#     print("Sonlar teng")

# #Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting:"))
# if x==y: print(f"Sonlar teng: {x}={y}")

# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son",
# agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 

# x = float(input("Istalgan sonni kiriting: >>> "))
# if x<0:
#     print("Manfiy son")
# if x>0:
#     print("Musbat son")
# if x == 0:
#     print("0 manfiy son ham, musbat son ham emas")

# son = float(input("Istalgan son kiriting: "))
# print("Son manfiy") if son<0 else print("Son musbat")

# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. 
# Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 

# son = float(input("Son kiriting: >>> "))
# if son>=0:
#     print(f"{son} ning ildizi: {son**(1/2)}")
# else:
#     print("Musbat son kiriting")

#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
# son = float(input('Istalgan son kiriting: '))
# print(son**(1/2)) if son>0 else print('Musbat son kiriting')
