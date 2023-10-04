# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 20:40:17 2023

@author: T480
"""

# 15-dars. Lug'at elementlari bilan ishlash

# # items() metodi
# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamsiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }
# print(talaba_0.items())

# # for kalit, qiymat in talaba_0.items():
# #     print(f"Kalit: {kalit}")
# #     print(f"Qiymat:{qiymat}\n")

# for key, value in talaba_0.items():
#     print(f"Kalit: {key}")
#     print(f"Qiymat:{value}\n")

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")

# .keys()

# mahsulotlar = {
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }

# # print(mahsulotlar.keys())

# # print('Do\'kondagi mahsulotlar:')
# # for mahsulot in mahsulotlar.keys():
# #     print(mahsulot.title())

# # print('Do\'kondagi mahsulotlar:')
# # for mahsulot in mahsulotlar:
# #     print(mahsulot.title())

# # bozorlik = ['anor', 'uzum', 'non', 'baliq']
# # for mahsulot in mahsulotlar:
# #     if mahsulot in bozorlik:
# #         print(f"{mahsulot.title()} narhi {mahsulotlar[mahsulot]} so'm")
# #     # else:
# #     #     print("Bu mahsulot do'konda yo'q")
    
# # for buyum in bozorlik:
# #     if buyum not in mahsulotlar:
# #         print(f"Iltimos, do'koningizga {buyum} ham olib keling")
        
# # print(mahsulotlar.keys())     

# # Lug'at elementlarini tartib bilan chiqarish

# print('Do\'kondagi mahsulotlar:')
# for mahsulot in sorted(mahsulotlar.keys()):
#     print(mahsulot.title()) 

# Values () 
# print(telefonlar)
# print(telefonlar.items()) 
# print(telefonlar.keys()) 
# print(telefonlar.values())   

# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel.capitalize())

# set()

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':"huawei p30",
#     'tohir':'iphone x',
#     'umar':"iphone x"
#     }

# # print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# # for tel in telefonlar.values():
# #     print(tel.capitalize()) # elementlar takrorlanmoqda
    
# print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi:')
# for tel in sorted(set(telefonlar.values())):
#     print(tel.capitalize())    

# # set() - takrorlanmaydigan ma'lumot turlari
# toys = {"ball","car","lamp","ball","bear","car"}
# print(type(toys))
# print(toys)

# AMALIYOT-1

# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. 
# Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.

# dictionary = {
#     'integer':'butun sonlar',
#     'float':'o\'nli sonlar',
#     'string':'matn',
#     'boolean':'mantiqiy amallar',
#     'if':'agar',
#     'else':'aks holda',
#     'elif':'aks holda, agar',
#     'list':'ro\'yxatlar',  
#     'tuple':'o\'zgarmas ro\'yxat'
#     }

# for k,q in sorted(dictionary.items()):
#     # print(f"Kalit: {k}")
#     # print(f"Qiymat: {q}\n")
#     print(f"{k.title()} - {q}")

# AMALIYOT-2

# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, 
# keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.

# davlatlar = {
#     'o\'zbekiston':"toshkent",
#     "tojikiston":"dushanbe", 
#     "rossiya":"moskva",
#     "amerika":'vashington'
#     }

# for davlat in sorted(davlatlar.keys()):
#     print(F"Davlatlar: {davlat.title()}")

# print("")

# for poytaxt in sorted(davlatlar.values()):
#     print(f"Poytaxtlar: {poytaxt.title()}")    
    
# AMALIYOT-3
# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. 
# Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.  

# davlatlar = {
#     'o\'zbekiston':"toshkent",
#     "tojikiston":"dushanbe", 
#     "rossiya":"moskva",
#     "amerika":'vashington'
#     }  

# # foydalanuvchi = input("Istalgan davlatni kiriting: >>> ").lower()
# # if foydalanuvchi in davlatlar.keys():
# #     print(f'{foydalanuvchi.title()} ning poytaxti {davlatlar[foydalanuvchi].capitalize()}')
# # else:
# #     print("Bizda bunday ma'lumot yo'q")

# country = input("Qaysi davlatni poytaxtini bilishni istaysiz?: ").lower()
# # capital = davlatlar.get(country, "Bizda bunday ma'lumot yo'q")
# # print(capital)
# capital = davlatlar.get(country)

# if capital == None:
#     print("Bunday davlat mavjud emas")
# else:
#     print(f"{country.upper()}ning poytaxti {capital.title()} shahri")

# AMALIYOT-4

# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). 
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring,
# agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

menu = {
        "osh":15000,
        'somsa':4000,
        'tandir':100000,
        'jiz':120000,
        "sho'rva":25000,
        'kabob':60000,
        'qizilcha':80000
        }

buyurtma = []

for n in range(3):
    buyurtma.append(input(f"{n+1}-buyurtmangiz nima? >>> ").lower())
    
# print(buyurtma)

for taom in menu:
    if taom in buyurtma:
        print(f"{taom.title()} ning narxi {menu[taom]} so'm")

for element in buyurtma:
    if not element in menu:
        print("Bizda bunday taom yo'q")        