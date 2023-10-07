# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 22:34:32 2023

@author: T480
"""

# 16-dars. NESTING

# Lug'atlar ro'yxati:
    
# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':'2018',
#         'narh':'13000',
#         'km':'50000',
#         'korobka':'avtomat',
#         }    

# car1 = {
#         'model':'nexia 3',
#         'rang':'qora',
#         'yil':'2015',
#         'narh':'9000',
#         'km':'89000',
#         'korobka':'mexanika',
#         }  

# car2 = {
#         'model':'gentra',
#         'rang':'qizil',
#         'yil':'2019',
#         'narh':'15000',
#         'km':'20000',
#         'korobka':'mexanika',
#         }  

# # car = car0
# # print(f"{car['model'].title()}, "
# #       f"{car['rang']} rang, "
# #       f"{car['yil']}-yil, {car['narh']}$" )

# # car = car1
# # print(f"{car['model'].title()}, "
# #       f"{car['rang']} rang, "
# #       f"{car['yil']}-yil, {car['narh']}$" )

# # car = car2
# # print(f"{car['model'].title()}, "
# #       f"{car['rang']} rang, "
# #       f"{car['yil']}-yil, {car['narh']}$" ) # kod juda uzun bo'lib ketdi

# cars = [car0, car1, car2]

# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['rang']} rang, "
#           f"{car['yil']}-yil, {car['narh']}$" )


# print(cars[0]['model'].capitalize()) # cars degan ro'yxatda 0-lug'atni olib, modelga teng qiymatni chiqaramiz

# print(f"{cars[2]['rang'].title()} "
#       f"{cars[2]['model']}")

# malibus = []
# for n in range(10):
#     new_car = {
#         'model':'malibu',
#         'rang':None, # rangi noaniq
#         'yil':2023,
#         'narh':None,
#         'km':0,
#         'korobka':'avto'
#         }
#     malibus.append(new_car)
    
# # for malibu in malibus:
# #     print(malibu)    

# for malibu in malibus[0:3]: # boshidagi 3 tasi rangi qizil bo'ladi
#     malibu['rang'] = 'qizil'
 
# # for malibu in malibus:
# #   print(malibu)       

# for malibu in malibus[3:6]: # keyingi 3 tasi rangi qora bo'ladi
#     malibu["rang"] = "qora"
    
# # for malibu in malibus:
# #     print(malibu)       

# for malibu in malibus[6:]: # oxirgi 4 tasi rangi qirmizi, korobkasi mexanika bo'ladi
#     malibu['rang'] = 'qirmizi'
#     malibu['korobka'] = 'mexanika'
    
# # for malibu in malibus:
# #     print(malibu)  

# for malibu in malibus:
#     if malibu['korobka'] == 'avto':
#         malibu['narh'] = 40000
#     else:
#         malibu['narh'] = 35000
        
# for malibu in malibus:
#     print(malibu)        

# Lug'at ichida ro'yxatlar:
    
# dasturchilar = {
#     'ali':['python','c++'],
#     'vali':['html','css','js'],
#     'hasan':['php','sql'],
#     'husan':['python','php'],
#     'maryam':['c++','c#']
#     }

# # for ism, tillar in dasturchilar.items(): # natijani tagma tag chiqaradi
# #     print(f"\n{ism.title()} quyidagi tillarni biladi:")
# #     for til in tillar:
# #         print(til.upper())

# for ism, tillar in dasturchilar.items(): # natijani bir qatorda chiqarish
#     print(f"\n{ism.title()} quyidagi tillarni biladi: ", end = ' ')  
#     for til in tillar:
#           print(f"{til.upper()} " , end = ' ')

# Nesting - Lug'atni ichiga lug'at 

# hamkasblar = {
#      'ali':{'familiya':'valiyev',
#             'tyil':1995,
#             'malumot':'oliy',
#             'tillar':['python','c++']},       
          
#     'vali':{'familiya':'aliyev',
#             'tyil':2001,
#             'malumot':'o\'rta-maxsus',
#             'tillar':['html','css','js']},        
           
#     'hasan':{'familiya':'husanov',
#              'tyil':1999,
#              'malumot':'maxsus',
#              'tillar':['python','php']}        

#     }

# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, "
#           f"{info['tyil']}-yilda tug'ilgan.\n"
#           f"Ma'lumoti: {info['malumot']}."
#           "\nQuyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper(), end=" \n")
    

# Amaliyot-1
# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. 
# Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.

# shaxs0 = {
#           'ism-familiya':'Abu Abdulloh Muhammad ibn Ismoil',
#           'tyil':810,
#           'shahar':"Buxoro",
#           'vafotetgan':870
#          }


# shaxs1 = {
#           'ism-familiya':'Abdulla Qodiriy',
#           'tyil':1894,
#           'shahar':"Toshkent",
#           'vafotetgan':1938
#          }    
    
# shaxs2 = {
#           'ism-familiya':'Erkin Vohidov',
#           'tyil':1936,
#           'shahar':"Farg'ona",
#           'vafotetgan':2016
#          }  

# shaxs3 = {
#           'ism-familiya':'Alisher Navoiy',
#           'tyil':1441,
#           'shahar':"Xirot",
#           'vafotetgan':1501
#          }   

# # shaxs = shaxs0 # 1-usulda chiqarish

# # print(f"\n{shaxs['ism-familiya']}"
# #       f" {shaxs['tyil']}-yilda {shaxs['shahar']}da tavallud topgan."
# #       f"{shaxs['vafotetgan']-shaxs['tyil']} yil umr ko'rgan" )

# # shaxs = shaxs1

# # print(f"\n{shaxs['ism-familiya']}"
# #       f" {shaxs['tyil']}-yilda {shaxs['shahar']}da tavallud topgan."
# #       f"{shaxs['vafotetgan']-shaxs['tyil']} yil umr ko'rgan" )

# # shaxs = shaxs2

# # print(f"\n{shaxs['ism-familiya']}"
# #       f" {shaxs['tyil']}-yilda {shaxs['shahar']}da tavallud topgan."
# #       f"{shaxs['vafotetgan']-shaxs['tyil']} yil umr ko'rgan" )

# # shaxs = shaxs3

# # print(f"\n{shaxs['ism-familiya']}"
# #       f" {shaxs['tyil']}-yilda {shaxs['shahar']}da tavallud topgan."
# #       f"{shaxs['vafotetgan']-shaxs['tyil']} yil umr ko'rgan" )

# shaxslar = [shaxs0, shaxs1, shaxs2, shaxs3]

# for shaxs in shaxslar:
#     print(f"\n{shaxs['ism-familiya']}"
#           f" {shaxs['tyil']}-yilda {shaxs['shahar']}da tavallud topgan."
#           f"{shaxs['vafotetgan']-shaxs['tyil']} yil umr ko'rgan")
    
# for shaxs in shaxslar:
#     ism = shaxs['ism-familiya']
#     tyil = shaxs['tyil']
#     vyil = shaxs['vafotetgan']
#     tjoy = shaxs['shahar']
#     print(f"{ism} {tyil}-yilda {tjoy}da tavallud topgan. "
#           f"{vyil-tyil} yil umr ko'rgan.")    
    
# Amaliyot-2
# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. 
# For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.    

# shaxs0 = {
#           'ism-familiya':'Abu Abdulloh Muhammad ibn Ismoil',
#           'tyil':810,
#           'tjoy':"Buxoro",
#           'vyil':870,
#           'asarlar':['Al-jome\' as-sahih', "Al-adab al-mufrad", "Al-tarix al kabir", 'At-tarix as-sag\'ir']
#          }


# shaxs1 = {
#           'ism-familiya':'Abdulla Qodiriy',
#           'tyil':1894,
#           'tjoy':"Toshkent",
#           'vyil':1938,
#           'asarlar':['O\'tkan kunlar', 'Mehrobdan chayon', 'Obid ketmon']
#          }    
    
# shaxs2 = {
#           'ism-familiya':'Erkin Vohidov',
#           'tyil':1936,
#           'tjoy':"Farg'ona",
#           'vyil':2016,
#           'asarlar':['Tong nafasim', 'Qo\'shiqlarim sizga', 'O\'zbegim', 'Qiziquvchan Matmusa']
#          }  

# shaxs3 = {
#           'ism-familiya':'Alisher Navoiy',
#           'tyil':1441,
#           'tjoy':"Xirot",
#           'vyil':1501,
#           'asarlar':['Xamsa', 'Lison ut -Tayr', 'Mahbub Al-qulub', 'Munojat']
#          }   

# shaxslar = [shaxs0, shaxs1, shaxs2, shaxs3]

# for shaxs in shaxslar:
#     print(f"\n{shaxs['ism-familiya']}ning mashhur asarlari: ")
#     for asar in shaxs['asarlar']:
#         print(asar.capitalize())
        
# Amaliyot-3
# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. 
# Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.

# s_kinolar = {
#              'ali':['Terminator', 'Rambo', 'Titanic'],
#              'vali':['Tenet','Inception','Intersteller'],
#              'hasan':['Abdullajon','Bomba','shaytanat'],
#              'husan':['mahallada duv-duv gap','john wick']
#             }        

# for ism, kinolar in s_kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari: ")
#     for kino in kinolar:
#         print(kino.capitalize())
        
# Amaliyot-4
# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. 
# Har bir davlat haqida ma'lumotni konsolga chiqaring. 

# 1-variant
# davlatlar = {
#              "o'zbekiston":{'poytaxti':'toshkent',
#                             'hududi':'448978 kv.km',
#                             'aholisi':33000000,
#                             'pul birligi':'so\'m'},    
            
#                  "rossiya":{'poytaxti':'moskva',
#                             'hududi':'17098246 kv.km',
#                             'aholisi':144000000,
#                             'pul birligi':'rublm'},  

#                     "aqsh":{'poytaxti':'vashington',
#                             'hududi':'9631418 kv.km',
#                             'aholisi':327000000,
#                             'pul birligi':'dollar'}, 

#                "malayziya":{'poytaxti':'Kuala-Lumpur',
#                             'hududi':'329750 kv.km',
#                             'aholisi':25000000,
#                             'pul birligi':'rinngit'}                        
#             }       

# for davlat, info in davlatlar.items():
#     print(f"\n{davlat.capitalize()}ning ", end=" ")
#     for k,q in info.items():
#         print(k.title(),q)

# 2-variant

# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }

# for davlat, info in davlatlar.items():
#     if davlat.lower() == 'aqsh':
#         davlat = davlat.upper()
#     else:
#         davlat = davlat.capitalize()
#     print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")
    
    
# Amaliyot-5

# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering. 
# Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.

davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                    'maydon':448978,
                    'aholi':33_000_000,
                    'pul birligi':"so'm"
                    },
        "rossiya":{'poytaxt':"moskva",
                    'maydon':17_098_246,
                    'aholi':144_000_000,
                    'pul birligi':"rubl"
                    },
            "aqsh":{'poytaxt':"vashington",
                    'maydon':9_631_418,
                    'aholi':327_000_000,
                    'pul birligi':"dollar"},
      "malayziya":{'poytaxt':"kuala-lumpur",
                    'maydon':329750,
                    'aholi':25_000_000,
                    'pul birligi':"rinngit"}
          }

davlat = input("Davlat nomini kiriting: ").lower()

if davlat in davlatlar.keys():
    info = davlatlar[davlat]
    if davlat.lower() == 'aqsh':
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
    print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}" )
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")
    
# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }

# davlat = input('Davlat nomini kiriting: ').lower()
# if davlat in davlatlar:
#     info = davlatlar[davlat]
#     print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi: {info['maydon']} kv.km"
#           f"\nAholisi: {info['aholi']}"
#           f"\nPul birligi: {info['pul birligi']}")
# else:
#     print("Bizda bu davlat haqida ma'lumot mavjud emas")    