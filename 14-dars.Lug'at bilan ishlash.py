# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 22:33:27 2023

@author: T480
"""

# LUG'AT BILAN ISHLASH
# Muallif: Azimov Temurbek

# car_0 = {'model':'ferrari','rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])

# en_uz = {'apple':'olma', 'apricot':'shaftoli', 'banana':"banan"}
# print(en_uz['apple'])
# print(en_uz['apricot'])
# print(en_uz['banana'])

# mevalar = {'olma':10000, 'tarvuz':8000, "qovun":10000}
# print(f"Olma narhi {mevalar['olma']}")

# Lug'atda istalgan ma'lumot turlarini saqlash mumkin
# talaba_0 = {'ism':'murod olimov', 'yosh':20, 't_yil':2000}
# print(f"{talaba_0['ism'].title()},\
#       {talaba_0['t_yil']} - da tug'ilgan,\
#        {talaba_0['yosh']} yoshda")
       
# # Yangi kalit so'z va qiymat qo'shish
# talaba_0['kurs'] = 4 
# talaba_0['fakultet'] = 'informatika' 
# talaba_0['ism'] = 'abdulloh' # biron qiymatni o'zgartirsak agar
# print(talaba_0)     

# Bo'sh lug'at 
# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(talaba_1)
# # print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# # Qiymatni yangilash
# talaba_1['kurs'] = 4
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# Kalit so'z qiymatini o'chirib tashlash
# talaba_0 = {'ism':'murod olimov', 'yosh':20, 't_yil':2000}
# print(talaba_0)
# del talaba_0['yosh']
# print(talaba_0)


# Lug'atlarni bir necha qatorda yozish mumkin

# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'anvar':'pixel 3xl'
#     }

# # get() metodi
# # phone = telefonlar['ali']
# # print(f"Alining telefoni {phone}")

# # phone =  telefonlar['hasan']
# # print(f"Hasanning telefoni {phone}")
# # phone = telefonlar.get('ali',"Bunday ism mavjud emas")
# # phone = telefonlar.get('hasan',"Bunday ism mavjud emas")
# phone = telefonlar.get('hasan')
# print(phone)

# AMALIYOT
# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting 
# (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring: 
# Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
# ukam = {'ismi':'Farrux', 't_yili':1998, 'shahar':'Buxoro'}
# print(f"Ukamning ismi {ukam['ismi'].title()}, {ukam['t_yili']}-yilda, {ukam['shahar']} viloyatida tug'ilgan ")

# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. 
# Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh

# s_taomlar = {
#     'farrux':'osh',
#     'temur':'shirguruch',
#     'iroda':'shashlik',
#     'humoyun':'nonkabob',
#     'hayotbek':'kasha'
#     }
# farrux = s_taomlar['farrux']
# humoyun = s_taomlar['humoyun'] 
# hayotbek = s_taomlar['hayotbek']

# print(f"Farruxning sevimli taomi {farrux}")
# print(f"Humoyunning sevimli taomi {humoyun}")
# print(f"Hayotbekning sevimli taomi {hayotbek}")

# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z 
# (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha 
# tarjimasini yozing.

dictionary = {
    'integer':'butun sonlar',
    'float':'o\'nli sonlar',
    'string':'matn',
    'boolean':'mantiqiy amallar',
    'if':'agar',
    'else':'aks holda',
    'elif':'aks holda, agar',
    'list':'ro\'yxatlar',  
    'tuple':'o\'zgarmas ro\'yxat'
    }

# tarjima_1 = dictionary['integer']
# tarjima_2 = dictionary['float']
# tarjima_3 = dictionary['string']
# tarjima_4 = dictionary['boolean']
# tarjima_5 = dictionary['if']
# tarjima_6 = dictionary['else']
# tarjima_7 = dictionary['elif']
# tarjima_8 = dictionary['list']

# print(f"integer so'zi tarjimasi {tarjima_1}")

# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
# Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

word = input("So'z kiriting: >>> ").lower()

# print(dictionary.get(word, "Bunday so'z mavjud emas"))

# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
tarjima = dictionary.get(word)
if tarjima==0:
    print("Bunday so'z mavjud emas")
else:
    print(f"{word} so'zi {tarjima} deb tarjima qilinadi")
