# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 20:43:53 2023

@author: T480
"""

# 5-dars STRING va UNICODE
# Sana: 20.09.2023 yil
# Muallif: Azimov Temurbek

#ism = "Temur"
#shahar = "Муборак"
#viloyat = "Qashqadaryo"
#matn = "Men yangi 📱 oldim"
#smayl = "😂"
#print (matn)

# STRING USTIDA AMALLAR
# ism = "Temur"
# print ("mening ismim", ism)
# print ("mening ismim " + ism)

# ism = "Ahad"
# familiya = "Qayum"
# print(ism + familiya)
# print (ism + ' ' + familiya)

# f-string
# ism = "Ahad"
# familiya = "Qayum"
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif)

# ism = "James"
# familiya = "Bond"
# print(f"Salom, mening ismim {ism}. {ism} {familiya}!")

# MAHSUS BELGILAR

# print ('Hello world!')
# print ('Hello \tworld!')
# print ('Hello \nworld!')

# STRING METODLAR

# ism = 'james'
# familiya = 'bond'
# ism_sharif = f"{ism} {familiya}"
# ism_sharif = ism_sharif.upper()
# print (ism_sharif.upper())
# print (ism_sharif.lower())
# print (ism_sharif.title())
# print (ism_sharif.capitalize())

# meva = "    olma    "
# print (meva)
# print ("Men " + meva.lstrip() + " yaxshi ko'raman!")
# print ("Men " + meva.rstrip() + " yaxshi ko'raman!")
# print ("Men " + meva.strip() + " yaxshi ko'raman!")
# print ("Men " + meva + " yaxshi ko'raman!")

# INPUT

# ism = input("Ismingiz nima?")
# print("Assalomu alaykum, " + ism)

# ism = input("Ismingiz nima?\n>>>")
# print("Assalomu alaykum, " + ism.title())

# ism = input("Ismingiz nima?\n")
# print("Assalomu alaykum, " + ism.title())

# print("Azimov TEMUR".capitalize())

# AMALIYOT

# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor" 
# viloyat="Samarqand"
# print(kocha + " ko'chasi " + mahalla + " mahallasi",tuman," tumani",viloyat,"viloyati")

print("Iltimos quyidagi ma'lumotlarni kiriting")
kocha = input("Ko'changiz qaysi? ")
mahalla = input("Mahallangizchi? ")
tuman = input("Qaysi tumandan edingiz? ")
viloyat = input("Oxirgi savolim, qaysi viloyatdansiz? ")
print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n"+\
     tuman + " tumani,\n" + viloyat,"viloyati.")

# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
manzil = f"{kocha} kochasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati."  #.upper()
print (manzil)

# manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
print (manzil.title())
print (manzil.upper())
print (manzil.lower())
print (manzil.capitalize())