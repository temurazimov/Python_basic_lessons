# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 22:34:32 2023

@author: T480
"""

# 16-dars. NESTING

# Lug'atlar ro'yxati:
    
car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':'2018',
        'narh':'13000',
        'km':'50000',
        'korobka':'avtomat',
        }    

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':'2015',
        'narh':'9000',
        'km':'89000',
        'korobka':'mexanika',
        }  

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':'2019',
        'narh':'15000',
        'km':'20000',
        'korobka':'mexanika',
        }  

# car = car0
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narh']}$" )

# car = car1
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narh']}$" )

# car = car2
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang, "
#       f"{car['yil']}-yil, {car['narh']}$" ) # kod juda uzun bo'lib ketdi

cars = [car0, car1, car2]

for car in cars:
    print(f"{car['model'].title()}, "
          f"{car['rang']} rang, "
          f"{car['yil']}-yil, {car['narh']}$" )


print(cars[0]['model'].capitalize()) # cars degan ro'yxatda 0-lug'atni olib, modelga teng qiymatni chiqaramiz

print(f"{cars[2]['rang'].title()} "
      f"{cars[2]['model']}")