# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 13:21:19 2023

@author: T480
"""

# 12-dars
# Title: Xatolar bilan ishlash

# SintaxError
# print "Hello world!"
# print("Hello world! 
# print("Assalom alaykum")  

# IndentationError
 # print("Hello world!")    # print biroz oldinga surilgani xisobiga xatolik bermoqda

# print("O'ngacha sanaymiz")
# for n in range(10):
# #print(n+1) # masofa tashlanmagan
#    print(n) # bir xilda surish kk shuni uchun xato bo'ladi
#     print(n+1)

# RuntimeError
# TypeError

# son =  input("Istalgan sonni kiriting: ") # integerga o'tkazilmagani uchun xato chiqaradi
# son = int(son) # buni qushib to'g'irlaymiz
# print(f"{son} ning kvadrati {son**2} ga teng")

# NameError
# prit("Hello world!")

# mevalar =  ['olma','uzum','nok','anor','anjir']
# for meva in mvalar:
#     print(meva)

# ValueError
# son = int(input("Istalgan son kiriting: ")) # yoki floatga o'zgartirsak o'nli son ham kiritsak bo'ladi
# if son>=0:
#     print("Musbat son")
# else:
#     print("Manfiy son") # float - o'nli son kiritsak valueerror beradi

# IndexError
# mevalar = ['olma', 'anor', 'uzum']
# print(mevalar[3])

# ZeroDivisionError
# x, y = 50, 50
# z = 250/(x-y)

# Mantiqiy xatolar

# son =  float(input("Istalgan son kiriting: "))
# ildiz =  son**1/2 # 1/2 qavs ichida yoziladi, aks holda avval sonning 1-darajasi hisoblanadi, kn 2 ga bo'ladi
# print(f"{son} ning ildiz {ildiz} ga teng")

# son =  float(input("Istalgan son kiriting: "))
# ildiz =  son**(1/2) # 1/2 qavs ichida yoziladi, aks holda avval sonning 1-darajasi hisoblanadi, kn 2 ga bo'ladi
# print(f"{son} ning ildiz {ildiz} ga teng")

# mevalar =  ['olma','uzum','nok','anor','anjir']
# for meva in mevalar:
#     print(meva)
#     print("Dastur tugadi")

# Amaliyot-1
# son = float(input("Juft son kiriting: "))
# if son %2 == 1 :
#     print("Bu son juft emas.")
# else:
#     print("Rahmat!")

# Amaliyot-2
# yosh = int(input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")

# Amaliyot-3

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")

# Amaliyot-4

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []

# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")    

# Amaliyot-5

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: '))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for mahsulot in mavjud_emas:
#   print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# Amaliyot-6

users = ['alisher1983','aziza','yasina' 'umar']

login = input("Yangi login tanlang:" )

if login in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")    