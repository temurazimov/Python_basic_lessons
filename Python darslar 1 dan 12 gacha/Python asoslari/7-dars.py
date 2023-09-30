# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 18:54:43 2023

@author: T480
"""

# 7-Dars.List (Ro'yxat)
# Muallif: Azimov Temurbek
# Web sahifa: https://python.sariq.dev

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati
# narhlar = [12000, 18000, 10900, 22000, 25000, 36000, -25, 63.2] # narhlar ro'yxati (sonlar)
# sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxati
# ismlar = [] # bo'sh ro'yxat

# hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']

# bozorlik = ["yog'", "un", "piyoz", "banan", "go'sht"]
# mahsulot = bozorlik.pop(3) # Ro'yxatdan bananni sug'urib oladi
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: " , bozorlik)

# # append() metodi

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar.append('tarvuz')
# print (mevalar)


# cars = [] # bo'sh ro'yxat yaratamiz
# cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
# cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
# cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
# cars.append('Tracker') # ro'yxatga Cobalt  mashinasini qo'shamiz
# print(cars)

# .insert() metodi - Ro'yxatning istalgan joyiga yangi element qo'shish uchun .insert() metodidan foydalanamiz. 

# cars = ['Lacetti', 'Nexia 3', 'Cobalt', 'Tracker']
# cars.insert(2, 'Matiz')
# print(cars)

#  Inedks yordamida olib tashlash uchun del operatoridan foydalanamiz:

# mevalar = ['olma', 'shaftoli', 'o\'rik', 'anor'] 
# del mevalar[1]
# print(mevalar)   

# Element qiymati bo'yichi o'chirish uchun esa .remove(qiymat) metodidan foydalanamiz. Buning uchun qavs ichida o'chirib tashlash kerak bo'lgan qiymatni yozamiz

# mevalar = ['olma', 'anjir', 'shaftoli', 'o\'rik', 'anor'] 
# mevalar.remove('shaftoli')
# print (mevalar)

# hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
# hayvonlar.remove("mushuk") # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
# print(hayvonlar)

# Elementni sug'urib olish .pop(indeks)

# bozorlik = ['yog\'', 'un', 'piyoz', 'banan', 'go\'sht']
# mahsulot = bozorlik.pop(3)
# mahsulot2 = bozorlik.pop() # Agar .pop() metodida indeks berilmasa, ro'yxatdan o'xirgi qiymat sug'urib olinadi.
# print('Men ' + mahsulot + ' sotib oldim')
# print('Olinmagan mahsulotlar: ' , bozorlik)

# AMALIYOT

# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# ismlar = ['Farrux', 'Bobur', 'Humoyun']
# # Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
# print (f"Salom {ismlar[0]}, bugun choyxona bormi?")
# print (f"{ismlar[1].upper()}, choyxonaga boramizmi?")
# print (f"{ismlar[2].title()} qale ishlar?")

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 

# sonlar = [1000, 2000, -1000, -2000, 1000.5, 2000.5, -1000.5, -2000.5]
# sonlar[0] = (sonlar[0]-500)/100 + sonlar[2]
# sonlar[1] = 0
# sonlar[3] = sonlar[0]+sonlar[-2]
# del sonlar[7]
# sonlar.remove(0)
# print(sonlar)

# t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 

# t_shaxslar = ['Imom Buxoriy', 'Amir Temur', 'Mirzo Ulug\'bek']
# z_shaxslar = ['Bill Gates', 'Elon Musk', 'Billie Eilish']

# # Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
# print ("Men tarixiy shaxslardan ", t_shaxslar.pop(0), 'bilan, zamonaviy shaxslardan esa ', \
#        z_shaxslar.pop(1), 'bilan suhbat qilishni istar edim')

# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 

# friends = []

# friends.append('Farrux')
# friends.append("Bobur")
# friends.append('Humoyun')
# friends.append('Hayotbek')

# # print(friends)

# # # Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 

# kelaolmaydiganlar = friends.remove('Bobur')
# kelaolmaydiganlar2 = friends.remove('Farrux')
# # print(friends)

# # # Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

# friends.append('Hasan')
# friends.append('Husan')
# # print(friends)

# friends.insert(0, 'Iroda')
# friends.insert(3, 'Mushtariy')
# friends.insert(6, 'Orziqul')
# # print (friends)

# # Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

# yangi_mehmonlar = []
# yangi_mehmonlar.append(friends.pop(0))
# yangi_mehmonlar.append(friends.pop(0))
# yangi_mehmonlar.append(friends.pop(0))
# print("\nKelmagan mehmonlar ,", friends)
# print("\nKelgan mehmonlar ", yangi_mehmonlar)
                       