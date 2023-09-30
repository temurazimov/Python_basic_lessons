# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 16:50:03 2023

@author: T480
"""

# 8-dars. Ro'yxatlar bilan ishlash
# Muallif: Azimov Temurbek

# TARTIBLASH
# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)

# cars = ['Bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)

# sonlar = [10, -20, 1000, 500]
# sonlar.sort()
# print(sonlar)

# TESKARI TARTIB
# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort(reverse=True)
# print(cars)
# print(sorted(cars, reverse=True))
# print(sorted(cars)) # Asl ro'yxatni o'zini chiqarib beradi

# # Ro'yxatni uzunligi
# fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
# print('Elementlar soni: ', len(fruits))

# # RANGE()
# sonlar = list(range(0,20))
# print(sonlar)

# RANGE va QADAM

# juft_sonlar = list(range(0,100,2))
# toq_sonlar = list(range(1,100,2))
# print ("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar:", toq_sonlar)

# MAX(), MIN() va SUM()

# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh: ", arzon, "\nEng qimmati: ", qimmat, "\nJami: ", jami)

# Ro'yxatni kesish 
# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[1:4] # 1-indeksdan boshlab 3 ta element ajratadi
# print(my_cars)
# print(cars[2:5]) # 2-3-4-elementlarni ajratib oladi
# print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi
# print(cars[4:]) # 4-elementdan boshlab ro'yxat oxirigicha kesadi

# Ro'yxatdan nusxa olish
# cars = ['bmw', 'mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars [:]
# my_cars.remove('bmw')
# cars.append('Tico')
# print(cars)
# print(my_cars)

# TUPLES
# tomonlar = (20, 30 ,55.2)
# print(tomonlar)


# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
# toys[0] = 'teddy' # 'tuple' object does not support item assignment
# toys.append("teddy")  # 'tuple' object has no attribute 'append'
# toys.remove('bear') # 'tuple' object has no attribute 'remove'
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])

# TUPLES -> LIST

# toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard') # o'zgarmas ro'yxat - tuple
# toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga o'tkazish

# toys.append('dragon')
# toys.insert(2, 'wiki')
# toys.remove('dino')
# toys[1] = 'mcqueen'
# toys = tuple(toys) # ro'yxatni qaytadan o'zgarmas ro'yxatga aylantiramiz
# print(toys)

# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print("sorted() qaytargan ro'yxat:", sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoldi:", mehmonlar)
# print(sorted(mehmonlar, reverse=True))

# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))

# fruits = ['pear','banana','apple','watermelon','lemon']
# fruits.reverse()
# print(fruits)
# print('Elementlar soni: ', len(fruits))

# sonlar = list(range(1,101))
# print(sonlar)

# juft_sonlar = list(range(0,101,2))
# toq_sonlar = list(range(1,101,2))
# print("1 dan 100 gacha juft sonlar:", juft_sonlar)
# print("1 dan 100 gacha toq sonlar:",toq_sonlar)

# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)

# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[1:3]
# print(cars[:4])
# print(cars[3:])
# print(my_cars)

# sonlar = [1, 2, 3, 4, 5] # sonlar degan ro'yxat yaratamiz
# sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

# sonlar = [1, 2, 3, 4, 5]
# #sonlar2 = sonlar[0:5] bu usul ham pastdagi bilan bir xil natija chiqadi
# sonlar2 = sonlar[:]
# sonlar2.append(6)
# sonlar2.append(7)
# print(sonlar)
# print(sonlar2)

# tomonlar = (20, 30, 55.2)
# print(tomonlar)

# toys = ('bus','car','bear','dino','snake','lizard')
# print(toys(0)) bunda natija chiqmaydi, chunki tuple ichidagi elementlarga huddi ro'yxat elementlariga murojaat qilingani kabi murojat qilinaveradi
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])

# toys = ('bus','car','bear','dino','snake','lizard')
# toys[3] = 'dragon'
# print(toys) #Shu kabi ro'yxatdan biror elementni o'chirish yoki yangi element qo'shish ham mumkin emas

# Agar Tuple ga o'zgartirish talab qilinsa, yagona yo'li o'zgarmas ro'yxatni list() funktsiyasi yordamida List (oddiy ro'yxat) ko'rinishiga keltirib olish, o'zgarishlarni bajarsih va qaytarib tuple() funktsiyasi yordamida o'zgarmas ro'yxatga o'tkazish mumkin:
    
# toys = ('bus','car','bear','dino','snake','lizard')  # o'zgarmas ro'yxat
# toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (list) aylantiramiz
# # ro'yxatga o'zgartirishlar kiritamiz
# toys.append("dragon")
# toys.remove('dino')
# toys.insert(5, "book")
# toys[4] = 'macbook'
# toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
# print(toys)

# AMALIYOT

# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring

# davlatlar = ['O\'zbekiston', 'Tojikiston', 'Turkmaniston', 'Qozoqiston', 'Afgoniston']
# print(davlatlar)

# # Ro'yxatning uzunligini konsolga chiqaring
# print('Elementlar soni:',len(davlatlar))

# # sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# print(sorted(davlatlar))

# # sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# print(sorted(davlatlar, reverse=True))

# # Asl ro'yxatni qaytadan konsolga chiqaring
# print(davlatlar)

# # reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# davlatlar.reverse()
# print(davlatlar)

# # sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.

# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing

# juft_sonlar = list(range(120, 1201, 2))
# print(juft_sonlar)

# # Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# print("120 dan 1200 gacha juft sonlar yig'indisi:" ,sum(juft_sonlar))

# # Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# eng_kattasi = max(juft_sonlar)
# eng_kichiki = min(juft_sonlar)
# ayirma = eng_kattasi - eng_kichiki
# print(ayirma)

# # Ro'yxatdagi elementlar sonini hisoblang
# print(len(juft_sonlar))

# # Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
# boshidan = juft_sonlar[0:20]
# ortasidan = juft_sonlar[270:290]
# oxiridan = juft_sonlar[521:541]
# print(boshidan)
# print(juft_sonlar[:20])
# print(ortasidan)
# print(juft_sonlar[270:290])
# print(oxiridan)
# print(juft_sonlar[-20:])

# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = []
taomlar.append('osh')
taomlar.append('manti')
taomlar.append('sho\'rva')
taomlar.append('dimlama')
taomlar.append('shashlik')

# print(taomlar)

# nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]
# print(nonushta)

# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing

nonushta.remove('shashlik')
del nonushta[1]
nonushta.append('tovuqli pirog')
nonushta.append('quymoq')
# print(nonushta)

# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(taomlar)
print(nonushta)

# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.

nonushta = tuple(nonushta)
nonushta[0] = 'qaymoq va non' # tuplega qiymat o'zgartirib bo'lmaydi
print(nonushta)