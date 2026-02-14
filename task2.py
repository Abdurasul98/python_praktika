# 1-MAVZU: OOP ga kirish


# 1. OOP nima?

# OOP (Object Oriented Programming) — bu dasturlash usuli bo‘lib, dastur obyektlar orqali quriladi.

# Real hayotdan misol:

# Mashina — bu obyekt
# Uning rangi, tezligi — bu atribut
# Harakatlanish, signal berish — bu metod

# Demak:

# Atribut → ma’lumot (xususiyat)
# Metod → harakat (funksiya)

# OOP da ham shunday ishlaymiz:

# Class — shablon (model)
# Object — shu shablondan yaratilgan nusxa



# 2. Procedural vs OOP farqi
# Procedural (oddiy usul)

# Funksiyalar alohida ishlaydi, ma’lumotlar alohida turadi.

# -------------------------
# name = "Ali"
# age = 20

# def info(name, age):
#     print(name, age)
# -------------------------
# Ma’lumot va funksiya ajralgan.


# Agar OOP usul bo'lsa
# -------------------------
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(self.name, self.age)
# -------------------------

# Bu yerda:

# Ma’lumot ham
# Harakat ham

# bitta joyda — class ichida.



# 3. Class va Object tushunchasi

# Class — bu chizma (blueprint)
# Masalan: Car degan class yozsak, u hali mashina emas.

# Object — classdan yaratilgan real nusxa
# car1 = Car()

# car1 — object.

# Bitta classdan xohlagancha object yaratish mumkin.



# --------------------------------------------------------------------
# Amaliy masala

# Shart:
# "Student" nomli class yarating.
# Unda quyidagilar bo‘lsin:

# name
# age
# grade

# Va 1 ta metod:
# info() → student haqida quyidagi formatda chiqarishi kerak:

# Ism: Ali
# Yosh: 20
# Bahosi: 5

# Natija:
# Object yarating va metodni chaqirganda yuqoridagi ko‘rinishda chiqsin.
# --------------------------------------------------------------------


# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name 
#         self.age = age 
#         self.grade = grade


#     def info(self):
#         result = f"""
# Ism: {self.name}
# Yosh: {self.age}
# Bahosi: {self.grade}
#             """

#         return result


# def classni_ishlatish():
    
#     while True:
#         user = input("Choice yes/no: ")

#         if user == 'yes':
#             name = input("Enter your name: ")
#             age = int(input("Enter your age: "))
#             grade = int(input("Enter your grade: "))

#             o1 = Student(name,age,grade)

#             result = o1.info()

#             print(result)

#         else:
#             break

# classni_ishlatish()




# 2-MAVZU: Class va Object yaratish

# Bu mavzuda 3 ta muhim narsa bor:

# class sintaksisi
# __init__ metodi
# self tushunchasi


# 1. class sintaksisi

# Class yozish shakli:

# class ClassNomi:
#     pass

# Class nomi odatda katta harf bilan boshlanadi (Student, Car, Book).



# 2. __init__ metodi

# Bu maxsus metod. Uni constructor deyiladi yoki dander (dunder) method deyiladi.

# Object yaratilgan paytda avtomatik ishlaydi.

# class Person:
#     def __init__(self, name):
#         self.name = name

# p1 = Person("Ali")


# Bu yerda:

# Object yaratilganda __init__ ishlaydi
# "Ali" qiymati self.name ga saqlanadi


# 3. self nima?

# self — bu hozirgi objectning o‘zi.
# Oddiy qilib aytganda:

# self.name

# yani:

# "shu objectning name atributi"
# Agar 2 ta object yaratsak:

# p1 = Person("Ali")
# p2 = Person("Vali")

# Har birida self boshqacha bo‘ladi.

# --------------------------------------------------------------------

# Amaliy masala


# Shart:

# "Car" nomli class yarating.

# Atributlar:

# brand
# model
# year
# speed (boshlanishida 0 bo‘lsin)

# Metodlar:

# info() → mashina haqida chiqaradi
# accelerate(amount) → speed ga amount qo‘shadi
# brake(amount) → speed dan amount ayiradi (lekin speed 0 dan past tushmasin)


# Natija namunasi:

# Brand: BMW
# Model: X5
# Year: 2022
# Speed: 30


# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand 
#         self.model = model
#         self.year = year
#         self.speed = 0


#     def accelerate(self, amount:int):

#         if amount >= 0:
#             self.speed += amount
#         else:
#             print("Invalid number. True: speed > 0")
    

#     def brake(self, amount:int):
        
#         if amount >= 0:
#             if self.speed - amount < 0:
#                 self.speed = 0
#             else:
#                 self.speed = self.speed - amount
#         else:
#             print("Invalid number. True: speed > 0")
            

#     def info(self):
#         print(f"""
# Brand: {self.brand}
# Model: {self.model}
# Year: {self.year}
# Speed: {self.speed}
#         """)
    

# car1 = Car("BMW", "X5", 2022)

# car1.accelerate(50)
# car1.brake(2000)
# car1.info()

