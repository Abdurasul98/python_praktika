# class Student:
#     def __init__(self, name:str, age:int, grade:int):
#         self.name = name
#         self.age = age
#         self.grade = grade

    
#     def info(self):
#         print(f"""
#     Name: {self.name}
#     Age: {self.age}
#     Grade: {self.grade}
# """)


#     def is_passed(self):
#         if self.grade >= 60:
#             return "Passed"
#         else:
#             return "Failed"


# o1 = Student("Abdurasul",27,100)
# o2 = Student("Robiya",25,100)
# o3 = Student("Malina",23,59)


# print(o1.is_passed())
# o1.info()

# print(o2.is_passed())
# o2.info()

# print(o3.is_passed())
# o3.info()




# class BankAccount:
#     def __init__(self, owner:str, balance:float):
#         if owner == "":
#             print("Owner name cannot be empty")
#             self.owner = None
#         else:
#             self.owner = owner
        
#         if balance < 0:
#             print("Balance cannot be negative")
#             self.balance = 0
#         else:
#             self.balance = balance


#     def deposit(self, amount):
#         if amount <= 0:
#             return "Invalid deposit amount"

#         self.balance = self.balance + amount
#         return ''


#     def withdraw(self, amount):
#         if amount <= 0:
#             return "Invalid withdraw amount"
        
#         if amount > self.balance:
#             return "Not enough balance"
        
#         self.balance = self.balance - amount
#         return ''

#     def info(self):
#         return f"""
# Owner: {self.owner}
# Balance: {self.balance} $
# """
    

# def class_ishlatish():
#     while True:
#         choice = input("Enter choice yes/no: ").lower()

#         if choice == "yes":
#             value_name = input("Enter name for bank account: ")
#             value_amount_deposit = float(input("Enter amount for deposit: "))
#             value_amount_withdraw = float(input("Enter amount for withdraw: "))

#             o1 = BankAccount(value_name,0)

#             print(o1.deposit(value_amount_deposit))
#             print(o1.withdraw(value_amount_withdraw))
#             print(o1.info())
#         else:
#             break

# class_ishlatish()




# class User:
#     def __init__(self, username: str, password: str, age: int):
        
#         if not username:
#             print("Username cannot be empty")
#         else:
#             self.username = username
        
#         if len(password) < 4:
#             print("Password too short")
#             self.password = None
#         else:
#             self.password = password
            
#         if age < 0:
#             print("Age cannot be negative")
#             self.age = 0
#         else:
#             self.age = age
    


#     def check_password(self,other_pw):
#         if other_pw == self.password:
#             print("Correct")
#         else:
#             print("Incorrect")
                
            
    
#     def is_adult(self):
#         if self.age >= 18:
#             print("Adult")
#         else:
#             print("Minor")

    
#     def info(self):
#         result = f""" 
#         User: {self.username}
#         Age: {self.age}
#             """
#         return result

# o1 = User("Abdurasul",'12qw',27)
# o2 = User("Robiya",'qw12',17)

# o1.check_password('12qw')
# o1.is_adult()
# print(o1.info())

# o2.check_password('12qw')
# o2.is_adult()
# print(o2.info())

            

# class Course:
#     school_name = "Online School"


#     def __init__(self, title: str, duration: int, price: float):
#         if title == '':
#             print("Bo'sh bo'lishi mumkin emas")
#             self.title = None
#         else:
#             self.title = title
        
#         if duration > 0:
#             self.duration = duration
#         else:
#             print("O dan katta bo'lish kerak")
#             self.duration = 0
        
#         if price < 0:
#             print("Manfik kiritish mumkin emas")
#             self.price = 0
#         else:
#             self.price = price

    

#     def info(self):
#         return f"""
# Course: {self.school_name}
# Title: {self.title}
# Duration: {self.duration}
# Price: {self.price:.2f}
# """     
        

#     def apply_discount(self,percent):
#         if 0 <= percent <= 100:
#             self.price = self.price * (1 - percent / 100)
#             return ''
#         else:
#             print("0-100 oraliqda bo'lishi kerak")

#     @classmethod
#     def change_school_name(cls, new_name):
#         cls.school_name = new_name

    
#     @staticmethod
#     def is_valid_duration(hours):
#         result = False
#         if hours >= 10:
#             result = True
        
#         return result
    

# o1 = Course("Python",12,1000.0)
# o2 = Course("C",2,300.0)

# Course.change_school_name("Najot Ta'lim")

# o1.apply_discount(44)
# print(o1.is_valid_duration(12))
# print(o1.info())

# print()

# o2.apply_discount(95)
# print(o2.is_valid_duration(7))
# print(o2.info())




# class Student:
#     school_name = "Online School"
#     student_count = 0

#     def __init__(self, name: str, age: int, grade: int):
#         if not name:
#             print("Name cannot be empty")
#             self.name = None
#         else:
#             self.name = name 


#         if age < 0:
#             print("Age must be positive")
#             self.age = 0
#         else:
#             self.age = age


#         if 0 <= grade <= 100:
#             self.grade = grade
#         else:
#             print("Grade must be 0-100")
#             self.grade = 0
        
#         Student.student_count +=1


#     def info(self):
#         return f"""
# School name: {self.school_name}
# Name: {self.name}
# Age: {self.age}
# Grade: {self.grade}
# """
    
#     def is_passed(self):
#         result = True 
#         if self.grade < 0:
#             result = False
#             print("Grade cannot be negative")

#         if result:
#             if self.grade >= 60:
#                 print("Passed")
#             else:
#                 print("Failed")
            
        
#     def update_grade(self, new_grade: int):
#         result = True 
#         if self.grade < 0:
#             result = False
#             print("Grade cannot be negative")

#         if result:
#             if 0 <= new_grade <= 100:
#                 self.grade = new_grade
#             else:
#                 print("Grade must be 0-100")



#     @classmethod
#     def total_students(cls):
#         return cls.student_count
    


#     @classmethod
#     def change_school_name(cls,new_name: str):
#         cls.school_name = new_name



#     @staticmethod
#     def is_valid_age(age: int):
#         result = False

#         if 7 <= age <= 100:
#             result = True

#         return result
    


# o1 = Student("Abdurasul",27,100)
# o2 = Student("Robiya",25,59)
# o3 = Student("Malina",7,-100)

# Student.change_school_name("Najot Ta'lim")

# o1.update_grade(99)
# print(Student.total_students())
# print(o1.is_valid_age(6))
# print(o1.info())
# print(o2.info())
# print(o3.info())




# class Student:
#     school_name = "Python Academy"

#     def __init__(self, name: str, age: int, list_grade: list):
#         self.name = name
#         self.age = age
#         self.__list_grade = list_grade


#     def add_grade(self,grade: int):
#         if isinstance(grade,int) and 0 <= grade <=5:
#             self.__list_grade.append(grade)
#         else:
#             print("Grade cannot be negative")

#     def average(self):
#         length_list = 0
#         sum_value = 0

#         for value in self.__list_grade:
#             length_list +=1
#             sum_value += value
        
#         result = sum_value // length_list
#         return result


#     def info(self):
#         result = f""" 
# Name: {self.name}
# Age: {self.age}
# Grade: {self.get_grade()}
# School: {self.school_name}
# """
#         return result


#     def get_grade(self):
#         return self.__list_grade

#     @classmethod
#     def change_school_name(cls,new_name):
#         cls.school_name = new_name


# s1 = Student("Ali",20 , [4,5,3])
# s1.add_grade(5)

# print(s1.average())
# print(s1.info())

# Student.change_school_name("Najot Ta'lim")
# print(s1.info())



# class BankAccount:
#     bank_name = "Python Bank"

#     def __init__(self, owner_name: str, account_number: str, balance):
#         if isinstance(owner_name,str) and len(owner_name) > 0:
#             self.owner_name = owner_name
#         else:
#             self.owner_name = None


#         if isinstance(account_number,str) and len(account_number) == 8 and account_number.isdigit():
#             self.__account_number = account_number
#         else:
#             self.__account_number = None

        
#         if isinstance(balance,(int,float)) and balance >= 0:
#             self.__balance = balance
#         else:
#             self.__balance = 0.0


#     def deposit(self,amount):
#         if isinstance(amount, (int,float)) and amount > 0:
#             self.__balance += amount
#         else:
#             print("Another data type or amount cannot be negative")


#     def withdraw(self,amount):
#         if isinstance(amount, (int,float)) and amount > 0:
#             if amount <= self.__balance:
#                 self.__balance -= amount
#             else:
#                 print("Insufficient funds")
#         else:
#             print("Another data type or amount cannot be negative")

    
#     def get_balance(self):
#         return self.__balance
    

#     def info(self):
#         result = f"""
# Owner: {self.owner_name}
# Account: {self.__account_number}
# Balance: {self.get_balance()}
# Bank: {self.bank_name}
# """
#         return result
    
#     @classmethod
#     def change_bank_name(cls,new_name):
#         if isinstance(new_name, str) and len(new_name) > 0:
#             cls.bank_name = new_name
#         else:
#             print("Another data type or bank name must be non-empty string")


# acc = BankAccount("Ali", "12345678", 1000)

# acc.deposit(500)
# acc.withdraw(200)

# print(acc.get_balance())
# print(acc.info())

# BankAccount.change_bank_name("IT Bank")
# print(acc.info())




# class Book:
#     def __init__(self,title, author,pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

    
#     def __str__(self):
#         return f"Book: {self.title} by {self.author} ({self.pages} pages)"
    

#     def __repr__(self):
#         return f"Book('{self.title}', {self.author}, {self.pages})"
    
    

# o1 = Book("Atomic Habits","James Clear",320)

# print(o1)
# print(repr(o1))




# class PlayList:
#     def __init__(self,songs: list):
#         self.songs = songs


#     def __len__(self,other_list: list):
#         count = 0

#         for _ in other_list:
#             count += 1

#         return count 

# print(len(["python",'c','bruno mars']))



# class Vector2D:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y

    
#     def __add__(self,other):
#         return Vector2D(self.x + other.x,self.y + other.y)
    
    
#     def __str__(self):
#         return f"{self.x} {self.y}"
    
# o1 = Vector2D(5,9)
# o2 = Vector2D(3,1)

# o3 = o1+o2
# print(o3)