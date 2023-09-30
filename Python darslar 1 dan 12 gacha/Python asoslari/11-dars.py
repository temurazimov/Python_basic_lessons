# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:50:31 2023

@author: T480
"""

# 11-dars. IF-ELIF-ELSE
# Muallif: Azimov Temurbek

# son = 50
# if son<0:
#     print("manfiy son")
# else:
#     print("musbat son")

# yosh =  int(input("Yoshingiz nechida? >>> "))
# if yosh<=4:
#     print("Sizga kirish bepul")
# elif yosh<=12:
#     print("Sizga kirish 5000 so'm")
# elif yosh<=18:
#     print("Sizga kirish 8000 so'm")
# else:
#     print("Sizga kirish 10000 so'm")


# 2-usulda yozish, or yoki and foydalanilganda pastdagi usul hamma holni tekshirmaydi
# yosh =  int(input("Yoshingiz nechida? >>> "))
# if yosh<=4:
#     narh = 0
# elif yosh<=12:
#     narh = 5000
# elif yosh<=18:
#     narh = 8000
# else:
#     narh = 10000
# print(f"Sizga kirish {narh} so'm")

# or yoki and operatorlari
# kun = input("Bugun nima kun? >>> ")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print("Dam olish kuni")
# else:
#     print("Bugun ish kuni")

# kun =  input("Bugun nima kun? >>> ")
# harorat = float(input("Havo harorati qanday? >>> "))

# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Cho'milgani ketdik")
# elif kun.lower()=='yakshanba' and harorat<30:
#     print("Uyda dam olamiz!")

# kun =  input("Bugun nima kun? >>> ")
# harorat = float(input("Havo harorati qanday? >>> "))

# if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=30:
#     print("Cho'milgani ketdik")
# elif (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat<30:
#     print("Uyda dam olamiz!")    

# narh = 15000 # mijoz 15000 so'mga taom oldi
# choy = True # mijoz choy ham oldi
# salat = False # mijoz salat olmadi

# if choy and salat: # agar mijoz choy ham salat ham olgan bo'lsa
#    narh = narh + 10000 # narhga 10000 so'm qo'shamiz
# elif choy or salat: # agar mijoz choy yoki salat olgan bo'lsa
#    narh = narh + 5000 # narhga 5000 so'm qo'shamiz

# print(f"Jami {narh} so'm") # yakuniy narhni chiqaramiz

# narh = 15000 # mijoz 15000 so'mga ovqat oldi
# choy = True
# salat = False
# non = True 
# kompot = True
# assorti = False

# if choy: # agar choy olsa
#     print("Mijoz choy oldi")
#     narh = narh + 3000    
# if salat: # agar salat olsa
#     print("Mijoz salat oldi")
#     narh = narh + 5000
# if non: # agar non olsa
#     print("Mijoz non oldi")
#     narh = narh + 2000
# if kompot: # agar kompot olsa
#     print("Mijoz kompot oldi")
#     narh = narh + 5000  
# if assorti: # agar assorti olsa
#     print("Mijoz assorti oldi")
#     narh = narh + 15000
# print(f"Jami {narh} so'm ")       

# # True/False o'rniga 1/0 qo'yib ketsa ham bo'ladi

# narh = 15000 # mijoz 15000 so'mga ovqat oldi
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assorti = 1

# if choy: # agar choy olsa
#     print("Mijoz choy oldi")
#     narh = narh + 3000    
# if salat: # agar salat olsa
#     print("Mijoz salat oldi")
#     narh = narh + 5000
# if non: # agar non olsa
#     print("Mijoz non oldi")
#     narh = narh + 2000
# if kompot: # agar kompot olsa
#     print("Mijoz kompot oldi")
#     narh = narh + 5000  
# if assorti: # agar assorti olsa
#     print("Mijoz assorti oldi")
#     narh = narh + 15000
# print(f"Jami {narh} so'm ")   

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# "manti" in menu # menuda manti bormi 

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input("Nma ovqat yeysiz? >>> ")
# if ovqat.lower() in menu:
#     print("Buyurtmangiz qabul qilindi")
# else:
#     print("Afsuski bizda bunday ovqat yo'q")

# Not in menu

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input("Nma ovqat yeysiz? >>> ")
# if ovqat.lower() not in menu:
#     print("Afsuski bizda bunday ovqat yo'q")
# else:
#     print("Buyurtmangiz qabul qilindi")

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")
        
# buyurtmalar = []

# if buyurtmalar:
#     print(f"ro'yxatda {len(buyurtmalar)} ta taom bor")
# else:
#     print("ro'yxat bo'sh")

# menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# # buyurtmalar = []
# buyurtmalar = ['osh', 'somsa', 'manti', 'shashlik']
# if buyurtmalar: # ro'yxatda biror element bo'lsa, bu ifoda true qaytaradi
#    for taom in buyurtmalar:
#        if taom in menu:
#            print(f"Menuda {taom} bor")
#        else:
#            print(f"Kechirasiz, menuda {taom} yo'q")
# else: # agar ro'yxat bo'sh bo'lsa
#     print("Savatchangiz bo'sh!")

# Amaliyot-1
# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", 
# agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

# son = float(input("Juft son kiriting: >>> "))
# print("Rahmat!") if son%2==0 else print("Bu son juft emas")

# Amaliyot-2
# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

# yosh = int(input("Yoshingiz nechida? >>> "))
# if yosh<=4 or yosh>=60:
#     price = 0
# elif yosh<18:
#     price = 10000
# elif yosh>=18:
#     price = 20000
# print(f"Sizga kirish {price} so'm")    

# Amaliyot-3
# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va 
# ularning teng yoki katta/kichikligi haqida xabarni chiqaring

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))

# if x>y:
#     print(f"{x}>{y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}={y}")
    
# Amaliyot-4
# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
# Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang.
# Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa 
# "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

# mahsulot = ['non', 'olma','uzum','o\'rik','mandarin','kartoshka','piyoz','kola','go\'sht','pomidor']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
# for zakazlar in savat:
#               if zakazlar in mahsulot:
#                   print(f"Do'konimizda {zakazlar} bor") 
#               else:
#                   print(f"Do'konimizda {zakazlar} yo'q")

# Amaliyot-5
# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang.
# Foydalanuvchi so'ragan va do'konda bor mahsulotlarni bor_mahsulotlar degan ro'yxatga, do'konda 
# yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, 
# "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa 
# "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.

# mahsulotlar = ['non', 'olma','uzum','o\'rik','mandarin','kartoshka','piyoz','kola','go\'sht','pomidor']
# savat = []
# for k in range(5):
#     savat.append(input(f"{k+1}-mahsulotni kiriting:"))
# print(f"Savatdagi mahsulotlar: {savat}")
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# # print(f"Do'konda bor mahsulotlar: {bor_mahsulotlar}")
# # print(f"Do'konda mavjud bo'lmagan mahsulotlar: {mavjud_emas}")
# if mavjud_emas == []:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# else:
#     print(f"Quyidagi mahsulotlar do'konimizda yo'q: {mavjud_emas}")
    
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
  
  
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']     
# for mahsulot in mahsulotlar:
#     print(mahsulot)

# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print(mehmon)

# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 29-sentyabr naxorgi oshga taklif etamiz")
#     print("Hurmat bilan Azimovlar oilasi")

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kubi {son**3}")
# print(sonlar)

# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
    
# print(sonlar)
# print(sonlar_kvadrati)

# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
# Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar
# degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, 
# "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

# foydalanuvchilar = ['anvar', 'temur', 'hayot', 'humoy', 'justin']
# # for x in foydalanuvchilar:
# #     print(x)
# foydalanuvchi = input('Yangi login tanlang: ')

# if foydalanuvchi.lower() in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
# else:
#     print("Xush kelibsiz")
    
# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 
# 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 

# son = int(input("Istalgan butun sonni kiriting: >>> "))

# for k in range(2,11):
#     if son%k==0:
#         print(f"{son} soni {k} ga qoldiqsiz bo'linadi")