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



# 3-MAVZU: Instance atributlari va metodlari

# Bu mavzuda asosiy tushuncha — har bir object o‘ziga tegishli ma’lumotga ega bo‘lishi.


# 1. Instance variable (Instance atribut)
# Bu self orqali yaratiladigan atributlar.

# class Person:
#     def __init__(self, name):
#         self.name = name

# self.name — instance variable.


# Agar 2 ta object yaratsak:

# p1 = Person("Ali")
# p2 = Person("Vali")

# p1.name → Ali
# p2.name → Vali

# Har biri alohida saqlanadi.


# 2. Instance method
# Bu oddiy metod bo‘lib, birinchi parametri doim self bo‘ladi.

# def info(self):
#     print(self.name)

# Nega self kerak?
# Chunki metod object ichidagi ma’lumotlarga murojaat qiladi.



# 3. Metod ichida atributlardan foydalanish

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount


# Bu yerda:

# self.balance o‘zgaradi
# Har bir account o‘z balansiga ega


# Muhim farqni tushun

# Instance atribut → har bir object uchun alohida
# Instance metod → object ichidagi atribut bilan ishlaydi


# --------------------------------------------------------------------

# Amaliy masala


# Shart:

# "BankAccount" nomli class yozing.

# Atributlar:

# owner
# balance

# Metodlar:

# deposit(amount)
# withdraw(amount) → balans yetarli bo‘lsa ayirsin, aks holda "Yetarli mablag‘ yo‘q" chiqarsin
# info() → quyidagicha chiqarishi kerak:

# Hisob egasi: Ali
# Balans: 1200

# Sinov:

# 2 ta account yarating.
# Birining balansini o‘zgartirganda ikkinchisiga ta’sir qilmasligi kerak.



# class BankAccount:
#     def __init__(self, owner:str):
#         self.owner = owner
#         self.balance = 0


#     def deposit(self,amount):
#         if amount < 0:
#             print("Amount cannot be negative")
#         else:
#             self.balance += amount
#         return f"Pul solindi: {self.balance}"

#     def withdraw(self,amount):
#         if amount < self.balance:
#             self.balance -= amount
#         else:
#             print("Not enought balance")
#         return f"Pul yechilish miqdori: {amount}"


#     def info(self):
#         result = f"Hisob egasi: {self.owner}  Balance: {self.balance}"
#         return result


# o1 = BankAccount("Abdurasul")
# o2 = BankAccount("Robiya")


# print(o1.deposit(777.7))
# print(o1.withdraw(77.7))
# print(o1.info())

# print()

# print(o2.deposit(777.7))
# print(o2.withdraw(778.7))
# print(o2.info())





# 4-MAVZU: Class atributlari va class metodlari

# Bu mavzuda 3 ta yangi tushuncha:

# Class variable
# @classmethod
# @staticmethod

# Va ularning instance bilan farqi.

# 1. Class variable (class atribut)
# Bu atribut hamma objectlar uchun umumiy bo‘ladi masalan:

# class Student:
#     school = "IT School"

# s1 = Student()
# s2 = Student()

# Ikkalasida ham:

# s1.school → IT School
# s2.school → IT School

# Bu atribut bitta joyda saqlanadi.

# Instance vs Class farqi

# Instance atribut:
# self.name

# → har objectda alohida

# Class atribut:
# Student.school

# → hammaga umumiy


# 2. Class method (@classmethod)

# Bu metod class bilan ishlaydi, object bilan emas.
# Birinchi parametri self emas, cls bo‘ladi.

# class Student:
#     school = "IT School"

#     @classmethod
#     def change_school(cls, new_name):
#         cls.school = new_name

# Student.change_school("New School")
# Endi barcha objectlarda school o‘zgaradi.


# 3. Static method (@staticmethod)

# Bu metod:
# class atribut ishlatmaydi
# instance atribut ishlatmaydi

# Oddiy yordamchi funksiya, lekin class ichida turadi.

# class MathUtils:

#     @staticmethod
#     def add(a, b):
#         return a + b


# Qachon qaysi biri ishlatiladi

# Instance method → object ma’lumotlari bilan ishlasa
# Class method → class darajasida o‘zgarish bo‘lsa
# Static method → mantiqiy yordamchi funksiya bo‘lsa



# --------------------------------------------------------------------

# Amaliy masala


# Shart:
# "Employee" nomli class yozing.

# Class atribut:
# company_name = "TechCorp"

# Instance atribut:
# name
# salary

# Metodlar:
# info() → name, salary, company chiqaradi
# @classmethod change_company(new_name)
# @staticmethod is_valid_salary(amount)
# → salary 0 dan katta bo‘lsa True qaytarsin



# class Employee:
#     company_name = "TechCorp"

#     def __init__(self, name:str, salary:int):
#         self.name = name 
#         self.salary = salary


#     def info(self):
#         result = f"Name: {self.name}  Salary: {self.salary} Company: {Employee.company_name}"
#         return result


#     @classmethod
#     def change_company(cls, new_name):
#         cls.company_name = new_name
        


#     @staticmethod
#     def is_valid_salary(amount):
#         result = False

#         if amount > 0:
#             result = True
        
#         return result
    

# o1 = Employee("Abdurasul",5000)
# o2 = Employee("Robiya",10)

# Employee.change_company("Python")

# print(o1.is_valid_salary(20))
# print(o1.info())

# print()

# print(o2.is_valid_salary(-30))
# print(o2.info())




# 5-MAVZU: Encapsulation (Inkapsulyatsiya)

# Bu OOPning eng muhim g‘oyalaridan biri.
# Oddiy ma’nosi:
# Object ichidagi ma’lumotni tashqaridan himoyalash


# 1. Public atribut

# Oddiy atribut — hamma joydan ochiq.

# class User:
#     def __init__(self, name):
#         self.name = name


# Tashqaridan:

# u = User("Ali")
# u.name = "Vali"


# Hech qanday cheklov yo‘q.


# 2. Protected atribut (_attribute)

# Bu signal:
# “Bu ichki atribut, tashqaridan tegma”

# class User:
#     def __init__(self, name):
#         self._name = name


# Tashqaridan kirish mumkin, lekin tavsiya etilmaydi.

# u._name

# Bu faqat OOP odobi (convention).

# 3. Private atribut (__attribute)

# Bu haqiqiy himoya.

# class User:
#     def __init__(self, name):
#         self.__name = name

# Tashqaridan:

# u.__name
# Xato beradi
# Chunki Python uni yashiradi:
# _User__name
# ga o‘zgartiradi.


# 4. Nega encapsulation kerak?

# Masalan bank balans.

# Agar public bo‘lsa:
# acc.balance = -999999

# Bu noto‘g‘ri.

# Shuning uchun:

# self.__balance

# qilib yashiramiz.
# Va nazorat bilan o‘zgartiramiz.


# 5. Getter va Setter

# Private atributga nazorat bilan kirish.

# class Bank:
#     def __init__(self, balance):
#         self.__balance = balance

#     def get_balance(self):
#         return self.__balance

#     def set_balance(self, amount):
#         if amount >= 0:
#             self.__balance = amount



# --------------------------------------------------------------------

# Amaliy masala


# Shart:
# "BankAccount" class yozing.

# Private atribut:

# __balance

# Metodlar:

# deposit(amount) → qo‘shsin
# withdraw(amount) → yetarli bo‘lsa ayirsin
# get_balance() → balansni qaytarsin



# class BankAccount:
#     def __init__(self):
#         self.__balance = 0


#     def deposit(self,amount: float):
#         if amount <= 0:
#             print("Amount cannot be negative")
#         else:
#             self.__balance = self.__balance + amount
            
#         return f"{self.__balance:.2f} $"


#     def withdraw(self,amount: float):
#         if amount <= 0:
#             print("Amount cannot be negative")
#         else:
#             if self.__balance >= amount:
#                 self.__balance = self.__balance - amount
#             else:
#                 print("Not enought balance")

#         return f"{amount:.2f} $"


#     def get_balance(self):
#         return f"{self.__balance:.2f} $"
    

# o1 = BankAccount()

# print(o1.deposit(23.8))
# print(o1.withdraw(14.2))
# print(o1.get_balance())


# o1.__balance




# 6-MAVZU: Magic (Dunder) metodlar

# Magic metodlar — bu Python ichki ishlatadigan maxsus metodlar.

# Ular har doim:
# __nom__
# ko‘rinishida bo‘ladi.

# Masalan:

# __init__
# __str__
# __len__
# __add__


# 1. __str__ — objectni chiroyli chiqarish

# Agar classda __str__ bo‘lmasa:

# print(obj)
# chiqadi:
# <__main__.Car object at 0x000...>
# Yomon ko‘rinadi.

# Agar __str__ yozsak:

# class Car:
#     def __init__(self, brand):
#         self.brand = brand

#     def __str__(self):
#         return f"Car: {self.brand}"


# Endi:

# print(car1)
# chiqadi:
# Car: BMW

# 2. __repr__ — developer uchun ko‘rinish

# Bu objectni aniq tasvirlash.

# def __repr__(self):
#     return f"Car('{self.brand}')"

# Console ichida object yozilsa ishlaydi.


# 3. __len__ — len(obj) ishlatish

# class Team:
#     def __init__(self, members):
#         self.members = members

#     def __len__(self):
#         return len(self.members)

# Endi:
# len(team)
# ishlaydi.


# 4. __add__ — objectlarni qo‘shish

# class Money:
#     def __init__(self, amount):
#         self.amount = amount

#     def __add__(self, other):
#         return Money(self.amount + other.amount)

# m1 + m2
# ishlaydi.


# 5. __eq__ — tenglik tekshirish

# def __eq__(self, other):
#     return self.amount == other.amount

# m1 == m2

# Eng muhim tushuncha

# Magic metodlar =
# Python operatorlarini o‘z classingga moslash

# Masalan:

# +  → __add__
# == → __eq__
# len → __len__
# print → __str__


# --------------------------------------------------------------------

# Amaliy masala


# Shart:


# class Book:
#     def __init__(self,title:str, pages:int):
#         self.title = title
#         self.pages = pages


#     def __str__(self):
#         return f"Book: {self.title} ({self.pages} pages)"


#     def __len__(self):
#         return self.pages


#     def __eq__(self, value):
#         if self.pages == value.pages:
#             return True
#         else:
#             return False


# b1 = Book("Python", 300)
# b2 = Book("Java", 300)

# print(b1)
# print(len(b1))
# print(b1 == b2)





# 7-MAVZU: Inheritance (Vorislik)

# Inheritance — bu bir class boshqa classdan xususiyat va metodlarni meros olishi.

# Real hayot:

# Animal

# Dog
# Cat

# Dog — Animaldan kelib chiqqan.


# 1. Oddiy vorislik

# class Animal:
#     def speak(self):
#         print("Animal sound")

# class Dog(Animal):
#     pass

# Dog — Animaldan meros oldi.

# Endi:

# d = Dog()
# d.speak()


# ishlaydi 


# 2. Voris class nima oladi?

# Child class parentdan:
# metodlar
# atributlar

# hammasini oladi.


# 3. O‘z atribut qo‘shish

# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, name, breed):
#         self.breed = breed


# Lekin bu yerda xato bor 
# Parent name yo‘qoladi.


# 4. super() — parentni chaqirish

# To‘g‘risi:

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed


# super() → parent classga murojaat.



# 5. Method override

# Child class parent metodni o‘zgartirishi mumkin.

# class Animal:
#     def speak(self):
#         print("Animal sound")

# class Dog(Animal):
#     def speak(self):
#         print("Bark")


# Endi:
# Dog().speak()
# → Bark


# 6. Ko‘p darajali vorislik
# class Animal:
#     pass

# class Mammal(Animal):
#     pass

# class Dog(Mammal):
#     pass

# Dog → Mammal → Animal


# Muhim tushuncha

# Inheritance =
#  kodni qayta ishlatish
#  umumiy xususiyatni parentga qo‘yish
#  maxsusini childga qo‘yish



# --------------------------------------------------------------------

# Amaliy masala


# Shart:
# "Vehicle" parent class yozing.

# Atribut:
# brand

# Metod:
# info() → "Brand: BMW"

# "Car" child class yozing.

# Qo‘shimcha atribut:
# model

# Override:
# info() → "Brand: BMW, Model: X5"

# Sinov
# c = Car("BMW", "X5")
# c.info()

# Natija:

# Brand: BMW, Model: X5



# class Vehicle:
#     def __init__(self,brand):
#         self.brand = brand
    
#     def info(self):
#         return f"Brand: {self.brand}"
    
# class Car(Vehicle):
#     def __init__(self,brand,model):
#         super().__init__(brand)
#         self.model = model

#     def info(self):
#         return f" Brand: {self.brand}, Model: {self.model}"
    

# o1 = Car("BMW", "M3")
# print(o1.info())