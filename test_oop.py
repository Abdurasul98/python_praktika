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

            