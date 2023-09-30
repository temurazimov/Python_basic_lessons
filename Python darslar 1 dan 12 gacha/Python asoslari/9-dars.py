# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 19:23:48 2023

@author: T480
"""

# 9-dars: FOR yordamida kodni takrorlash
# Muallif: Azimov Temurbek

# mehmonlar = ['Ali', 'Vali', 'Hasan', "Husan", 'Olim']
# for mehmon in mehmonlar:
#     print('Salom', mehmon)
#     print("Xayr", mehmon)
    
# mehmonlar = ['Ali', 'Vali', 'Hasan', "Husan", 'Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 25-sentyabr kuni naxorgi oshga taklif qilamiz")
#     print("Hurmat bilan Azimovlar oilasi\n")
    
# mehmonlar = ['Ali', 'Vali', 'Hasan', "Husan", 'Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 25-sentyabr kuni naxorgi oshga taklif qilamiz")
# print("Hurmat bilan Azimovlar oilasi\n")    # tsikldan tashqariga tushib qolyapti

# sonlar = list(range(1, 11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yozamiz
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
#     # print(sonlar_kvadrati) # boshqacha ko'rinishda qiymat chiqadi
# print(sonlar)
# print(sonlar_kvadrati)    

# dostlar = [] # bo'sh ro'yxat
# print("5 ta eng yaqin do'stingiz kim?\n")
# for n in range(5):
#     dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
# print(dostlar)

# dostlar = [] # bo'sh ro'yxat
# print("5 ta eng yaqin do'stingiz kim?")
# for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
#     dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
# print(dostlar)

# AMALIYOT

# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, 
# va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# ismlar = ['Temur', 'Farrux', 'Humoyun', 'Hayotbek', 'Iroda']
# for ism in ismlar:
#     print(f"Assalom aleykum, Hurmatli {ism}, sizni tavallud ayyomingiz bilan tabriklaymiz!")

# # Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring 
# # (n o'rniga kod necha marta takrorlanganini yozing)

# print(f"Kod {len(ismlar)} marta takrorlandi")
    
# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. 
# Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.

# toq_sonlar = list(range(11,100,2))
# for n in toq_sonlar:
#     print(f"{n} ning kubi {n**3} ga teng")
# print(toq_sonlar)

# toq_sonlar = list(range(11,100,2))
# sonning_kubi = []
# for n in toq_sonlar:
#     sonning_kubi.append(n**3)

# print(toq_sonlar)
# print(sonning_kubi)

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling.
# Natijani konsolga chiqaring.
# kinolar = []
# print("5 ta eng sevimli kinoingiz qaysi?\n")
# for n in range(5):
#     kinolar.append(input(f"{n+1}-eng sevimli kinongiz? "))
# print(kinolar)    

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang,
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.

# odamlar = []
# suxbatdosh_soni = int(input("Bugun nechta odam bilan suhbatlashdingiz? >>>"))
# for k in range(suxbatdosh_soni):
#     odamlar.append(input(f"{k+1} - suxbatdosh: "))
# print(odamlar)    


# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, 
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.

odamlar_soni = int(input("Bugun nechta odam bilan suxbatlashdingiz? >>>"))
ismlar = []
for n in range(odamlar_soni):
    ismlar.append(input(f"{n+1}-suxbatdosh: "))
print(ismlar)