# son = int(input("Enter number: "))

# if son > 0:
#     print('Yes')

# else:
#     print('No')




# son = int(input('Enter number: '))

# if son == 0:
#     print('Nol ni bolib bolmaydi')

# elif son % 2 == 0:
#     print('Bu juft son:',son)

# else:
#     print('Bu toq son:',son)




# son = int(input("Enter number: "))

# if son == 0:
#     print('ZERO')

# elif son > 0:
#     print('POSITIVE')

# else:
#     print('NEGATIVE')




# n = int(input("Enter number: "))
# result = 0

# for i in range(1,n+1):
#     result = result + i

# print(result)



# n = int(input("Enter number: "))

# for i in range(1,n+1):
#     if i % 2 == 0:
#         print(i,end=" ")




# start = int(input("Enter start: "))+1

# while start > 1:
#     start = start - 1
#     print(start)




# n = input("Enter number: ")
# index = 0
# count = 0
# while index < len(n):
#     if int(n) % 10:
#         count += int(n[index])
#     index +=1
# print(count)


# n = int(input("Enter number: "))

# count = 0

# while n != 0:

#     count +=1
#     n = n // 10
# print(count)




# n = int(input("Enter number: "))

# for i in range(1,n):
#     if i % 3 == 0:
#         print(i,end=" ")




# n = int(input("Enter number: "))
# count = 0
# for i in range(1,n+1):
#     if i % 2 == 1:
#         count = count + 1

# print(count)


# n = int(input("Enter number: "))
# max_juft = 0

# for i in range(1,n+1):
#     if i % 2 == 0:
#         if i > max_juft:
#             max_juft = i 
        
# print(max_juft)



# words = input("Enter words: ")

# for i in words:
#     print(i)


# words = input("Enter words: ")

# for i in words:
#     if i.isdigit():
#         print(i,end="")




# words = input("Enter words: ")
# count = 0
# unli = 'aeiou'

# for i in words:
#     if i.islower() and i in unli:
#         count += 1
# print(count)




# my_list = [ 3, 7, 1 ]


# for i in my_list:
#     print(i)


# my_list = [4, 9, 2, 6]
# max_number = my_list[0]
# min_number = my_list[0]

# for i in my_list:
#     if i > max_number:
#         max_number = i
#     if i < min_number:
#         min_number = i

# print('bu eng katta son',max_number)
# print('bu eng kichik son',min_number)




# my_list =[-2, 5, -1, 4]
# result = 0

# for i in my_list:
#     if i > 0:
#         result  = result + i

# print(result)





# my_list = [1, 4, 6, 7, 9, 10]
# result = []
# count = 0


# for i in my_list:
#     if i % 2 == 0:
#         result.append(i)
#         count = count + 1

# print('Natija:',count,'ta juft sonlar bor va ular ->',result)



# my_list = [8, 3, 11, 2, 6]
# result = my_list[0]
# for i in my_list:
#     if i < result:
#         result = i
# print(result)


# my_list = [5, -3, 7, -2, 4]
# result = 0
# for i in my_list:
#     if i < 0 :
#         result = result + i
# print(result)




# n = int(input("Enter number: "))

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()




# n = int(input("Enter number: "))

# juft = []
# toq = []

# for i in range(1,n+1):
#     if i % 2 == 0:
#         juft.append(i)
#     else:
#         toq.append(i)
    

# print(f"Natija juftlar: {juft} -> {len(juft)} ta va toqlar: {toq} -> {len(toq)} ta")



# start = int(input("Enter start number: "))
# end = int(input("Enter end number: "))


# for i in range(start,end+1):
#     if i % 3 == 0 or i % 5 == 0:
#         print(i)




# n = int(input("Enter number: "))


# def juft_sonlar (n: int) -> int:
#     count = 0
#     for i in range(1,n+1):
#         if i % 2 == 0:
#             count += 1
#     return count
        

# result  = juft_sonlar(n)
# print(result)



# n = int(input("Enter number: "))

# def raqamlarning_yegindisi(n):
#     result = 0
#     while n != 0:
#         result += n % 10
#         n = n //10
#     return result

# print(raqamlarning_yegindisi(n))



# my_list = [3, 11, 6, 1]

# def orasidagi_farqi(a:list) -> int:
#     max_number = a[0]
#     min_number = a[0]

#     for i in a:
#         if i > max_number:
#             max_number = i
#         if i < min_number:
#             min_number = i
        
#     result = max_number - min_number

#     return result


# result = orasidagi_farqi(my_list)
# print(result)




# my_list = [2, 7, 5, 9, 1, 6]

# def orasidagi_farqi(a:list) -> int:
#     count = 0

#     for i in a:
#         if i > 5:
#             count +=1

#     return count


# result = orasidagi_farqi(my_list)
# print(result)



# my_list = [1, 4, 3, 8, 5]

# def orasidagi_farqi(a:list) -> int:
#     result = 0
#     for i in a:
#         if i % 2 == 1:
#             result += i

#     return result

# result = orasidagi_farqi(my_list)
# print(result)




# my_list = [1, 1, 2, 2, 2, 3]

# def orasidagi_farqi(a:list) -> int:
#     count = 0
#     for i in range(len(a)-1):
#         if a[i] == a[i+1]:
#             count += 1

#     return count

    

# result = orasidagi_farqi(my_list)
# print(result)





# n = int(input("Enter number: "))


# def toq_juft(n:int):
#     juft_result = 0
#     toq_result = 0

#     while n != 0:
#         result = n % 10

#         if result % 2 == 1:
#             toq_result += result
#         if result % 2 == 0:
#             juft_result += result

#         n = n // 10
    
#     return f"Natija juft raqamlar yegindisi {juft_result} va toq raqamlar {toq_result}"


# result = toq_juft(n)
# print(result)




# n = int(input("Enter number: "))


# def soni_yegindisi(n: int) :
#     raqamlar_soni = 0
#     raqamlar_yegindisi = 0

#     while n != 0:
#         raqamlar_yegindisi = raqamlar_yegindisi + (n % 10)
#         raqamlar_soni += 1
#         n = n // 10
#     return f"Natija raqamlar soni {raqamlar_soni} ta va raqamlar yegindisi {raqamlar_yegindisi}"
# result = soni_yegindisi(n)
# print(result)



# n = int(input("Enter number: "))


# def eng_kattasi(n: int) -> int:

#     while n != 0:
#         result = 0
#         max_number = n %10
        
#         if  result < max_number:
#             result = max_number
#         n = n //10

#     return max_number
    

# result = eng_kattasi(n)
# print(result)
# ----------------------------------------------
# n = int(input("Enter number: "))


# def eng_kattasi(n: int) -> int:
#     result = 0
#     while n != 0:
        
#         max_number = n %10
        
#         if  max_number > result:
#             result = max_number
#         n = n //10

#     return result
    

# result = eng_kattasi(n)
# print(result)
# ----------------------------------------------

# n = int(input("Enter number: "))

# def teskari_son(n: int) -> int:
#     temp = str(n)
#     temp = temp[::-1]
#     return int(temp)

# def teskari_son(n: int) -> int:
#     result = 0
#     while n != 0:
#         temp = n % 10
#         result = result * 10 + temp
#         n = n // 10
        
        
#     return result
# result = teskari_son(n)
# print(result)



# n = int(input("Enter number: "))

# def palendrom_son(n: int) -> int:
#     result = 0
#     while n != 0 :
#         temp = n % 10
#         result = result * 10 + temp
#         n = n // 10
#     return result

# result = palendrom_son(n)
# if result == n:
#     print('YES ->',result)
# else:
#     print('NO ->',result)




# n = int(input("Enter number: "))

# def kvadrat_jadval(n: int):
#     for i in range(n):
#         for j in range(n):
#             print('*',end="")
#         print()


# kvadrat_jadval(n)




# n = int(input("Enter number: "))

# def kvadrat_jadval(n: int):
#     for i in range(n):
#         for j in range(i+1):
#             print('*',end="")
#         print()


# kvadrat_jadval(n)




# n = int(input("Enter number: "))

# def kvadrat_jadval(n: int):
#     for _ in range(n):
#         for j in range(1,n+1):
#             print(j,end=" ")
#         print()


# kvadrat_jadval(n)





# n = int(input("Enter number: "))

# def kvadrat_jadval(n: int):
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             print(i*j,end=" ")
#         print()


# kvadrat_jadval(n)




# n = int(input("Enter number: "))

# def kvadrat_jadval(n: int):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(i,end="")
#         print()


# kvadrat_jadval(n)



# my_list = [5,2,9,1,7]

# def kichik_katta(n:list ):
#     max_number = n[0]
#     min_number = n[0]
#     for i in n:
#         if i > max_number:
#             max_number = i

#         if i < min_number:
#             min_number = i

#     return f" eng kattasi {max_number} , eng kichigi {min_number}"

# result = kichik_katta(my_list)
# print(result)



# my_list = [4 ,7, 2, 9, 10, 3]

# def toq_juft(n:list) -> str:
#     toq_number = 0
#     toq_result = []
#     juft_number = 0
#     juft_result = []

#     for i in n:
#         if i % 2 == 0:
#             juft_number += 1
#             juft_result.append(i)
#         else:
#             toq_number +=1
#             toq_result.append(i)

#     return f" Natija {juft_result} -> juft {[juft_number]} ta va {toq_result} -> toq {[toq_number]} ta"

# result = toq_juft(my_list)

# print(result)



# my_list = [ 2, 4, 6,8]

# def yegindisi_ortachasi(n:list) -> str:
#     sum = 0
#     avg = 0

#     for i in n:
#         sum +=i
#     avg = sum // len(n)
#     return f"Natija yegindisi: {sum} va ortacha qiymati: {avg}"

# result = yegindisi_ortachasi(my_list)
# print(result)



# my_list = [1,3,5,3,7,3,9,3]
# x = 4

# def nechi_marta(n:list,x:int) -> int:
#     count = 0

#     for i in n:
#         if x == i:
#             count +=1
#         else:
#             pass
#     return count

# result = nechi_marta(my_list,x)
# print(result)




# my_list = [1,2,3,4,5]

# def teskari(n:list) -> list:
#     temp = []
#     for i in n[::-1]:
#         temp.append(i)
#     return temp

# def teskari(n:list) -> list:
#     result = []
#     for i in range(len(n)-1,-1,-1):
#         result.append(n[i])
#     return result

# result = teskari(my_list)
# print(result)





# my_list = [4,6,1,9,3]
# x= 9

# def tekshirish(n:list,x:int) -> str:
#     count = 0
#     for i in n:
#         if i == x:
#             count +=1

#     if count:
#         return "Yes"
#     else:
#         return "No"


# result = tekshirish(my_list,x)
# print(result)



# my_list = [5,7,3,7,9]
# x = 7

# def birinchi_uchragan_index(n:list,x:int) ->int:
#     result = -1 

#     for index,value in enumerate(n):
#         if value == x:
#             result = index
#             break
    
#     return result


# result = birinchi_uchragan_index(my_list,x)
# print(result)




# my_list = [8,4,6,2,9]

# def eng_kichik_elemnt(n:list) -> int:
#     min_number = n[0]
#     result = 0

#     for index,value in enumerate(n):
#         if value < min_number:
#             min_number = value
#             result = index
    
#     return result

# result = eng_kichik_elemnt(my_list)
# print(result)




# my_list = [5,2,9,1,6]

# def sortlash(n:list) -> list:
    
#     for i in range(len(n)):
#         for j in range(len(n)-i-1):
#             if n[j] > n[j+1]:
#                 n[j], n[j+1] = n[j+1] ,n[j]
#     return n


# result = sortlash(my_list)
# print(result)




# my_list = [3,7,2,9,5]
# print(my_list)

# def kattasi_oxiriga(n:list) -> list:
#     max_number= n[0]
#     result_index = 0

#     for index,value in enumerate(n):
#         if value > max_number:
#             max_number = value
#             result_index = index
#     result = n.pop(result_index)
#     n.append(result)
#     return n
        

# result = kattasi_oxiriga(my_list)

# print(result)




# my_list = [3,5,1,4,2]
# print(my_list)

# def eng_kattasi_ogiriga(n:list) -> list:
#     max_number = n[0]
#     value_index = 0
    
#     for index,value in enumerate(n):
#         if value > max_number:
#             max_number = value
#             value_index = index

#     result = n.pop(value_index)
#     n.append(result)
#     return n

# result = eng_kattasi_ogiriga(my_list)
# print(result)




# s = "a3b2c1"

# def faqat_raqamlar_teskarisi(n:str) -> str:
#     temp = []
#     result = ""
#     for i in n:
#         if i.isdigit():
#             temp.append(int(i))
    
#     for i in range(len(temp)):
#         for j in range(len(temp)-i-1):
#             if temp[j] > temp[j+1]:
#                 temp[j],temp[j+1] = temp[j+1],temp[j]
    
    
#     for i in temp:
#         result +=str(i)
    

#     return result[::-1]

# result = faqat_raqamlar_teskarisi(s)
# print(result)





# my_list = [1, 2, 3, 4, 5, 6]
# print(my_list)


# def juft_yangi_list(n:list) -> list:
#     result =[]
#     for i in n:
#         if i % 2 ==0:
#             result.append(i)

#     return result
# result = juft_yangi_list(my_list)
# print(result)




# my_tuple = (4,1,3,2)

# def kichik_raqam_kik(n:tuple) -> str:
#     test = n
#     my_list = list(n)

#     min_number = my_list[0]
#     index_value = 0

#     for index,value in enumerate(my_list):
#         if value < min_number:
#             min_number = value
#             index_value = index
#     my_list.remove(index_value)
#     n = tuple(my_list)

#     return f"Eng kichik raqam: {[min_number]} va shu {test} dan olib tashlandi natija:{n}"

# result = kichik_raqam_kik(my_tuple)
# print(result)




# my_tuple = (1, 2, 3, 4, 5)
# print("Eski xolati",my_tuple)


# def tuplega_qaytarish(n:tuple) -> list:
#     result = []
#     temp = list(n)

#     for value in temp:
#         if value % 2 == 1:
#             result.append(value)
    
#     return result


# result = tuplega_qaytarish(my_tuple)
# print("hozirgi xolati",result)




# my_tuple = (2, -1, 3, -4)

# def manfiyni_nolga(n:tuple) -> tuple:
#     temp = list(n)
#     value_index = 0

#     for index,value in enumerate(temp):
#         if value < 0:
#             value_index = index
#             temp.remove(value)
#             temp.insert(value_index,0)
           
#     temp = tuple(temp)
#     return temp

# result = manfiyni_nolga(my_tuple)
# print(result)




# my_list = [1, 2, 2, 3, 1, 4]

# def unikal_list(n:list):
#     temp = set(n)
#     temp = list(temp)

#     # for i in range(len(temp)):
#     #     for j in range(len(temp)-i-1):
#     #         if temp[j] > temp[j+1]:
#     #             temp[j], temp[j+1] = temp[j+1],temp[j]

#     result = sorted(temp)

#     return result

# result = unikal_list(my_list)
# print(result) 




# my_list1 = [1, 2, 3, 4]
# my_list2 = [3, 4, 5, 6]


# def bor_qiymat_bita_list(n:list,m:list) -> list:
#     temp1 = set(n)
#     temp2 = set(m)
#     result = list(temp1.intersection(temp2))
#     return result

# result = bor_qiymat_bita_list(my_list1,my_list2)
# print(result)




# my_list1 = [1, 2, 3, 4]
# my_list2 = [2, 4]


# def bor_qiymat_bita_list(n:list,m:list) -> list:
#     temp1 = set(n)
#     temp2 = set(m)
#     result = list(temp1.symmetric_difference(temp2))
#     return result

# result = bor_qiymat_bita_list(my_list1,my_list2)
# print(result)




# my_list = [1, 2, 2, 3, 1, 2]

# def dct_count(n:list) -> dict:
#     count = 0
#     dct = {}
#     for i in n:
#         count = n.count(i)
#         dct[i] = count
#     return dct

# result1 = dct_count(my_list)
# print(result1)

# def max_element(n:dict) -> int:
#     max_value = 0
#     result = 0
#     for key,value in n.items():
#         if value > max_value:
#             max_value = value
#             result = key
#     return result

# result2 = max_element(result1)
# print(result2)



# my_dict = {1: 2, 2: 1, 3: 4}

# def yangi_dict(n:dict) -> dict:
#     max_value = 1
#     result = {}

#     for key,value in n.items():
#         if value > max_value:
#             result[key] = value
#     return result

# result = yangi_dict(my_dict)
# print(result)



# class NumberTools:
#     def __init__(self,n:list):
#         self.n = n

#     def count_positive(self):
#         count = 0

#         for i in self.n:
#             if i > 0:
#                 count += 1
        
#         return count
    
# my_numbers = [-1, 2, 3, -4, 5]

# o1 = NumberTools(my_numbers)
# result = o1.count_positive()
# print(result)
                


# class ArrayUtils:
#     def __init__(self,n:list):
#         self.n = n

#     def max_element(self):
#         max_value = self.n[0]

#         for i in self.n:
#             if i > max_value:
#                 max_value = i
#         return max_value

#     def min_element(self):
#         min_value = self.n[0]

#         for i in self.n:
#             if i < min_value:
#                 min_value = i
#         return min_value

#     def unique_elements(self):
#         unique_value = []

#         for i in self.n:
#             if i not in unique_value:
#                 unique_value.append(i)

#         return unique_value
    
# my_list = [1, 2, 2, 3]

# o1 = ArrayUtils(my_list)

# result1 = o1.max_element()
# result2 = o1.min_element()
# result3 = o1.unique_elements()


# print("Max =",result1)
# print("Min =",result2)
# print("Unique =",result3)



# my_list = [5, 4, 3, 5, 2, 4, 3]

# def unikal_sortlash(n:list) -> tuple:
#     temp = set(n)
#     sorting = list(temp)
#     # value_sorted = sorted(sorting)


#     for i in range(len(sorting)):
#         for j in range(len(sorting)-i-1):
#             if sorting[j] > sorting[j+1]: 
#                 sorting[j] , sorting[j+1] = sorting[j+1] , sorting[j]


#     # result = tuple(value_sorted)
#     result = tuple(sorting)
#     return result

# result = unikal_sortlash(my_list)
# print(result)


# students = {
#     "Ali": {"math", "physics", "english"},
#     "Vali": {"math", "english"},
#     "Hasan": {"math", "english", "biology"}
# }



# def umumiy_fan(n:dict) -> dict:
#     result = None
#     for values in n.values():
#         if result is None :
#             result = values.copy()
#         else:
#             result = values.intersection(result)
#     return result

# result = umumiy_fan(students)
# print(result)



# students = {
#     "Ali": {"math", "physics"},
#     "Vali": {"math", "english"},
#     "Hasan": {"math", "biology"}
# }


# def bita_fan_mashxur(n:dict) -> dict:
#     result = None

#     for i in n.values():
#         if result is None:
#             result = i.copy()
#         else:
#             result = result.intersection(i)

#     return result

# result = bita_fan_mashxur(students)
# print(result)



# student_courses = {
#     "Ali": ["Math", "Physics", "Chemistry"],
#     "Vali": ["Biology", "Chemistry", "Math"],
#     "Guli": ["Physics", "Biology", "Math"]
# }


# def umumiy_fan(n:dict) ->set:
#     result = None

#     for i in n.values():
#         temp = set(i)
#         if result is None:
#             result = temp.copy()
#         else:
#             result = result.intersection(temp)
#     return result

# result = umumiy_fan(student_courses)
# print(result)




# students_books = {
#     "Samira": ["Harry Potter", "Lord of the Rings", "Python Basics"],
#     "Anvar": ["Python Basics", "Data Science 101", "Lord of the Rings"],
#     "Nodir": ["Lord of the Rings", "Python Basics", "Deep Learning"]
# }


# def oqimagan_kitoblar(n:dict) -> set:

#     all_books = {"Harry Potter", "Lord of the Rings", "Python Basics", "Data Science 101", "Deep Learning", "Machine Learning"}


#     result = set()
#     for i in n.values():
#         result.update(i)

#     return all_books - result

# result = oqimagan_kitoblar(students_books)
# print(result)



# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]

# temp1 = set(a)
# temp2 = set(b)
# result = temp1.intersection(temp2)
# print(result)



# a = [10, 20, 30, 40]
# b = [30, 40, 50]


# temp1 = set(a)
# temp2 = set(b)
# result = temp1.difference(temp2)
# print(result)




# s = {5, 10, 15, 20}
# n = 10

# if n in s:
#     print('Bor')
# else:
#     print('Yoq')
    


# words = ["apple", "banana", "apple", "cherry", "banana", "date"]


# def set_qaytarish(n:list) -> set:
    
#     result = set()

#     for i in n:
#         if n.count(i) == 1:
#             result.add(i)
        
#     return result

# result = set_qaytarish(words)
# print(result)



# my_dict = {
#     "Ali": ["Math", "Physics", "Python"],
#     "Vali": ["Python", "Biology"],
#     "Hasan": ["Math", "Chemistry"],
#     "Husan": ["Chemistry"]
# }



# def unikal_fan(n:dict) -> set:
#     result = set()
#     temp = list()

#     for values in n.values():
#         for value in values:
#             temp.append(value)

#     for i in temp:
#         if temp.count(i) == 1:
#             result.add(i)
#     return result
        

# result = unikal_fan(my_dict)
# print(result)




# my_dict = {
#     "Ali": ["Math", "Physics", "Python"],
#     "Vali": ["Python", "Biology"],
#     "Hasan": ["Math", "Chemistry"],
#     "Husan": ["Chemistry"]
# }


# def kop_fan(n:dict) -> set:
#     result = set()
#     count = dict()

#     for i in n.values():
#         for j in i:
#             count[j] = count.get(j,0) + 1
    
#     for key,value in count.items():
#         if value == 1:
#             result.add(key)

#     return result


# result = kop_fan(my_dict)
# print(result)



# my_strings = 'aabbbc'

# def count_dict(n:str) -> dict:
#     count = dict()
#     result = dict()

#     for i in n:
#         count[i] = count.get(i,0) +1

#     for key,value in count.items():
#         result[key] = value
#     return result

# result = count_dict(my_strings)
# print(result)



# my_list = [1, 3, 2, 3, 3, 4, 3, 2]


# def kop_takrorlangan(n:list) -> int:
#     result = 0

#     for i in n:
#         temp = n.count(i) 
        
#         if temp > result:
#             result = temp

            
#     return result

# result = kop_takrorlangan(my_list)
# print(result)



# my_list = [4, 5, 4, 6, 7, 5]

# def unikal_raqam(n:list) -> list:
#     count = {}
#     result = list()
    
#     for value in n:
#         count[value] = count.get(value,0) +1

#     for key,values in count.items():
#         if values == 1:
#             result.append(key)
        
#     return result
# result = unikal_raqam(my_list)
# print(result)





#                                             FINESH TASK


# String --------------------------------------------------------

# task - Easy

# temp = 'hello world'

# def katta_harf(n:str)-> str:

#     result = str()
#     for i in n:
#         result = result + i.upper()
#     return result

# result = katta_harf(temp)
# print(result)


# task - Medium

# temp = 'apple,banana,orange'

# # temp = 'apple,banana,orange'.capitalize().split(',')
# # print(temp)

# def list_katta_harf(n:str)->str:
#     result = []
#     temp = n.split(',')
#     for i in temp:
#         if not i[0].isupper():
#             result.append(i.capitalize())

#     return result
# result = list_katta_harf(temp)
# print(result)



# task - Hard

# temp = "The quick brown fox jumps over the lazy dog"

# def oxirgi_harfi(n:str)-> str:
#     value = n.split(' ')
#     result = []

#     for i in value:
#         result.append(i[-1])

#     return result

# result = oxirgi_harfi(temp)
# print(result)


# List --------------------------------------------------------

# task - Easy

# temp = [1, 2, 3, 4, 5]

# def raqamlar_kopaytmasi(n:list)-> list:
#     result = []

#     for i in n:
#         result.append(i*2)

#     return result
# result = raqamlar_kopaytmasi(temp)
# print(result)




# task - Medium

# temp = [1, 2, 2, 3, 4, 4, 4, 5]

# def takrorsiz_list(n:list)-> list:
#     result = []
#     for value in n:
#         if n.count(value) >= 1 and value not in result:
#             result.append(value)
            
#     return result

# result = takrorsiz_list(temp)
# print(result)


# task - Hard


# my_list = [1, 2, [3, 4, [5, 6]], 7]
# result = []

# def bita_listga(n):
  
#     for i in n:
#         if isinstance(i,int):
#             result.append(i)
#         else:
#             bita_listga(i)

# bita_listga(my_list)
# print(result)



# Tuple --------------------------------------------------------


# task - Easy


# my_tuple = (1, 2, 3, 4)

# def tuple_max(n:tuple)-> int:
#     max_number = n[0]

#     for i in n:
#         if i > max_number:
#             max_number = i

#     return max_number


# result = tuple_max(my_tuple)
# print(result)



# task - Medium


# my_tuple = (1, 2, 3, 4)
# x = 5

# def add_tuple(n:tuple,number:int)-> tuple:
#     my_list = list(n)
#     lenght = len(my_list)
#     max_index = 0

#     for index in range(lenght):
#         if index > max_index:
#             max_index = index+1

#     print(max_index)
#     if max_index == lenght:
#         my_list.insert(max_index,number)
    
#     result  = tuple(my_list)

#     return result


# result = add_tuple(my_tuple,x)
# print(result)



# task - Hard


# my_tuple = (1, 2, 3, 2, 1, 4)


# def unique_elements(n:tuple)-> tuple:
#     count = dict()
    
#     for value in n:
#         if value in count:
#             count[value] += 1

#         else:
#             count[value] = 1

#     unique = list()
#     duplicate = list()
    
#     for key,values in count.items():
#         if values == 1:
#             unique.append(key)
#         else:
#             duplicate.extend([key] * values)
   
#     return tuple(unique), tuple(duplicate)
# result = unique_elements(my_tuple)
# print(result)




# Set --------------------------------------------------------


# task - Easy


# a = {1, 2, 3, 3, 2, 4}

# print(a)


# task - Medium


# a = {1, 2, 3}
# b = {3, 4, 5}


# def yagona_set(a:set,b:set)-> set:
#     for i in a:
#         b.add(i)
    
#     return b
# result = yagona_set(a,b)
# print(result)


# # def yagona_set(a:set,b:set)-> set:
# #     result = a.union(b)
    
# #     return result
# # result = yagona_set(a,b)
# # print(result)

# task - Hard


# my_set = {1, 2, 3, 4, 5}

# def toq_sonlar(n:set):
#     my_list = list(n)
#     temp = list()

#     for index,value in enumerate(my_list):
#         if value % 2 == 0:
#             my_list.remove(value)
#         else:
#             number = my_list.pop(index)
#             temp.append(number)
#     temp =set(temp)
#     my_list = set(my_list)
#     return f"Ushbu setdagi qiymatlardan: {n} biz shularni: {my_list} olib tashladik, shu natijani sizga qaytardik: {temp}"

# result = toq_sonlar(my_set)
# print(result)





# Dictionary --------------------------------------------------------

# task - Easy


# my_dict = {"a": 1, "b": 2, "c": 3}


# def qiymatlarni_kopaytmasi(n:dict)-> dict:

#     for key,values in n.items():
#         n[key] = values * 10

#     return n
# result = qiymatlarni_kopaytmasi(my_dict)
# print(result)



# task - Medium


# my_dict = {"Ali": 20, "Vali": 25, "Hasan": 30}
# x = 25

# def eng_katta_qiymat(n:dict,m:int)-> dict:
    
#     result = dict()

#     for key,values in n.items():
#         if values > m:
#             result[key] = values
#     return result

# result = eng_katta_qiymat(my_dict,x)
# print(result)



# task - Hard



# my_dict = {"Ali": [80, 90], "Vali": [70, 60], "Hasan": [100, 90]}


# def ortacha_ball(n:dict)-> dict:
#     result = dict()
    

#     for key,values in n.items():
#         sum = 0
#         for i in values:
#             sum += i
#         result[key] = sum / len(values)
#     return result

# result = ortacha_ball(my_dict)
# print(result)





# my_list = [5, 4, 3, 5, 2, 4, 3]

# def unikal_element(n:list) -> tuple:
#     temp = list()

#     for i in n:
#         if i not in temp: temp.append(i)
            
            
#     for j in range(len(temp)):
#         for k in range(len(temp)-j-1):
#             if temp[k] > temp[k+1]:
#                 temp[k], temp[k+1] = temp[k+1], temp[k] 

#     result = tuple(temp)

#     return result



# result = unikal_element(my_list)
# print(result)




# my_dict = {
#     "Ali": {"math", "physics", "english"},
#     "Vali": {"math", "english"},
#     "Hasan": {"math", "english", "biology"}
# }


# def barcha_umumiy_fan(n:dict)-> set:
#     my_set = set()
#     count = dict()

#     for value in n.values():
#         for i in value:
#             count[i] = count.get(i,0) +1

#     print(count)

#     for key,values in count.items():
#         if values == len(n):
#             my_set.add(key)
    
#     return my_set

# result = barcha_umumiy_fan(my_dict)
# print(result)



# my_tuple = (1, 2, 3, 4, 5, 6)


# def juft_son_list(n:tuple) -> list:
#     result = list()

#     for i in n:
#         if i % 2 == 0 : result.append(i)
            
#     return result

# result = juft_son_list(my_tuple)
# print(result)




# my_dict = {
#     "olma": 80,
#     "banan": 120,
#     "anor": 150,
#     "nok": 90
# }

# x = 100


# def katta_maxsulot_list(n:dict,m:int) -> list:
#     result =list()

#     for key,value in n.items():
#         if value > m: result.append(key)
            
#     return result

# result = katta_maxsulot_list(my_dict,x)
# print(result)




# data = [1, "hello", 2, "world", 3]


# def list_elements_type_to_dict(n:list)-> dict:
#     # oldindan yozib ketish
#     # result = {"numbers": [], "strings": []}

#     result = dict()
#     numbers = []
#     words = []


#     for i in n:
#         if isinstance(i,int):
#             numbers.append(i)
#         else:
#             words.append(i)


#     result['numbers'] = numbers
#     result['strings'] = words
#     return result

# result =list_elements_type_to_dict(data)
# print(result)



# my_tuple = (1, 2, 3, 2, 4, 1, 5)


# def element_takrorlangan(n:tuple) -> set:
#     count = dict()
#     result = set()

#     for i in n:
#         count[i] = count.get(i,0) +1

#     for key,values in count.items():

#         if values != 1:
#             result.add(key)
    
#     return result

# result = element_takrorlangan(my_tuple)
# print(result)




# my_dict = {
#     "Ali": 5,
#     "Vali": 8,
#     "Hasan": 3
# }


# def katta_qiymat(n:dict) -> str:
#     max_number = 0 
#     result = None

#     for key,values in n.items():
#         if values > max_number:
#             max_number = values
#             result = key
#     return result
# result = katta_qiymat(my_dict)
# print(result)



# my_list = ["python", "list", "tuple"]


# def key_value_uzunligi(n:list) -> dict:
#     result = dict()

#     for i in n:
#         result[i] = len(i)

#     return result


# # def key_value_uzunligi(n:list) -> dict:
# #     result = dict()

# #     for i in n:
# #         count = 0
# #         for _ in i:
# #             count += 1
# #         result[i] = count

# #     return result

# # result = key_value_uzunligi(my_list)
# # print(result)




#                                OOP


# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author


#     def read(self):
#         print(f"Siz kitobni o‘qiysiz: {self.title} by {self.author}")


# o1 = Book("Python Basics",'Ali')
# o2 = Book("Data Science",'Vali')

# o1.read()
# o2.read()





# class Book:
#     def __init__(self,title:str, author:str, pages:int):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def read(self):
#         print(f"Siz kitobni o'qiysiz: {self.title} by {self.author}. Kitobda {self.pages} sahifa bor.")

# o1 = Book("Python Basic","Ali",200)
# o2 = Book("Data Science","Vali",350)
# o3 = Book("AI Guide","Hasan",500)


# o1.read()
# o2.read()
# o3.read()



# class Book:
#     def __init__(self,title:str , author:str, pages:int):
#         self.title = title
#         self.author = author
#         self.pages = pages

    
#     def read(self):
#         print(f"Siz kitobni o'qiysiz: {self.title} by {self.author}. Kitobda {self.pages} sahifa bor.")


#     def is_long(self):
#         if self.pages > 300 :
#             print("Bu uzun kitob")
#         else:
#             print("Bu qisqa kitob")



# o1 = Book("Python Basic","Ali",200)
# o2 = Book("Data Science","Vali",350)
# o3 = Book("AI Guide","Hasan",500)


# o1.is_long()
# o2.is_long()
# o3.is_long()


# class Book:
#     def __init__(self,title:str, author:str, pages:int):
#         self.title = title
#         self.author = author
#         self.pages = pages

    
#     def read(self):
#         print(f"Siz kitobni o'qiysiz: {self.title} by {self.author}. Kitobda {self.pages} sahifa bor.")


#     def is_long(self):
#         if self.pages > 300 :
#             print("Bu uzun kitob")
#         else:
#             print("Bu qisqa kitob")


#     def reading_time(self):
#         oqilish_vaqti = 2

#         result = self.pages * oqilish_vaqti

#         soat = result // 60
#         minut = result % 60

#         print(f"{self.title} kitobni o‘qish uchun {soat} soat {minut} daqiqa kerak.")



# o1 = Book("Python Basic","Ali",200)
# o2 = Book("Data Science","Vali",350)
# o3 = Book("AI Guide","Hasan",500)


# o1.reading_time()
# o2.reading_time()
# o3.reading_time()




# class Book:
#     def __init__(self,title,author,pages):
#         self.title = title
#         self.author = author
#         self.pages = pages


#     def read(self):
#         print(f"Siz kitobni o'qiysiz: {self.title} by {self.author}. Kitobda {self.pages} sahifa bor.")


#     def is_long(self):
#         if self.pages > 300 :
#             print("Bu uzun kitob")
#         else:
#             print("Bu qisqa kitob")


#     def reading_time(self):
#         oqilish_vaqti = 2

#         result = self.pages * oqilish_vaqti

#         soat = result // 60
#         minut = result % 60

#         print(f"{self.title} kitobni o‘qish uchun {soat} soat {minut} daqiqa kerak.")



#     def compare_pages(self,other_book):
#         if self.pages > other_book.pages:
#             print(f"{self.title} ko‘proq sahifaga ega")

#         elif self.pages < other_book.pages:
#             print(f"{other_book.title} ko‘proq sahifaga ega")
        
#         else:
#             print("Ikkala kitob teng")


# o1 = Book("Python Basic","Ali",200)
# o2 = Book("Data Science","Vali",350)
# o3 = Book("AI Guide","Hasan",500)


# o1.compare_pages(o2)
# o2.compare_pages(o3)




# class Book:
#     def __init__(self, title:str, author:str, pages:int):
#         self.title = title
#         self.author = author
#         self.pages = pages

    
#     def read(self):
#         print(f"Siz kitobni o'qiysiz: {self.title} by {self.author}. Kitobda {self.pages} sahifa bor.")


#     def is_long(self):
#         if self.pages > 300 :
#             print("Bu uzun kitob")
#         else:
#             print("Bu qisqa kitob")


#     def reading_time(self):
#         oqilish_vaqti = 2

#         result = self.pages * oqilish_vaqti

#         soat = result // 60
#         minut = result % 60

#         print(f"{self.title} kitobni o‘qish uchun {soat} soat {minut} daqiqa kerak.")



#     def compare_pages(self,other_book):
#         if self.pages > other_book.pages:
#             print(f"{self.title} ko‘proq sahifaga ega")

#         elif self.pages < other_book.pages:
#             print(f"{other_book.title} ko‘proq sahifaga ega")
        
#         else:
#             print("Ikkala kitob teng")


    
#     def better_book(self, other_book):
#         result_self = self.pages 
#         if self.pages > 400:
#             result_self = self.pages + 50

#         result_other_book = other_book.pages
#         if other_book.pages > 400:
#             result_other_book = other_book.pages + 50


#         if result_self > result_other_book:
#             print(f"{self.title} yaxshiroq kitob")
#         elif result_other_book > result_self:
#             print(f"{other_book.title} yaxshiroq kitob")
#         else:
#             print("Ikkala kitob teng baholandi")



# o1 = Book("Python Basic","Ali",200)
# o2 = Book("Data Science","Vali",350)
# o3 = Book("AI Guide","Hasan",500)



# o1.better_book(o2)
# o2.better_book(o3)




# class Book:
#     def __init__(self, title:str, author:str, pages:int):
#         self.title = title
#         self.author = author
#         self.pages = pages

    
#     def read(self):
#         print(f"Siz kitobni o'qiysiz: {self.title} by {self.author}. Kitobda {self.pages} sahifa bor.")


#     def is_long(self):
#         if self.pages > 300 :
#             print("Bu uzun kitob")
#         else:
#             print("Bu qisqa kitob")


#     def reading_time(self):
#         oqilish_vaqti = 2

#         result = self.pages * oqilish_vaqti

#         soat = result // 60
#         minut = result % 60

#         print(f"{self.title} kitobni o‘qish uchun {soat} soat {minut} daqiqa kerak.")



#     def compare_pages(self,other_book):
#         if self.pages > other_book.pages:
#             print(f"{self.title} ko‘proq sahifaga ega")

#         elif self.pages < other_book.pages:
#             print(f"{other_book.title} ko‘proq sahifaga ega")
        
#         else:
#             print("Ikkala kitob teng")


    
#     def better_book(self, other_book):
#         result_self = self.pages 
#         if self.pages > 400:
#             result_self = self.pages + 50

#         result_other_book = other_book.pages
#         if other_book.pages > 400:
#             result_other_book = other_book.pages + 50


#         if result_self > result_other_book:
#             print(f"{self.title} yaxshiroq kitob")
#         elif result_other_book > result_self:
#             print(f"{other_book.title} yaxshiroq kitob")
#         else:
#             print("Ikkala kitob teng baholandi")




# o1 = Book("Python Basic","Ali",200)
# o2 = Book("Data Science","Vali",350)
# o3 = Book("AI Guide","Hasan",500)



# o1.better_book(o2)
# o2.better_book(o3)





# my_list = [1,2,3]


# def natija(n:list)-> list:
#     result = list()

#     my_str = ""

#     for i in n:
#         my_str += str(i)
    
#     temp = str(int(my_str) +1)
    
#     for i in temp:
#         result.append(int(i))
    
#     return result

# print(natija(my_list))





# my_list = ["flower","flow","flight"]


# class Solution:
#     def longestCommonPrefix(self, strs):
#         prefix = str()

#         for i in range(len(strs[0])):
#             ch = strs[0][i]

#             for word in strs:
#                 if i >= len(word) or word[i] != ch:
#                     return prefix

#             prefix += ch

#         return prefix


# -------------------------------------------------------------------------------------
# Masala 1 — “Smart Phone Profil”

# Sizdan SmartPhone klassini yaratishingiz so‘raladi:

# Klass atributlari:
# total_phones — barcha yaratilgan SmartPhone obyektlar sonini saqlaydi (class variable).

# Instance atributlari (shaxsiy ma’lumotlar):
# _brand (private) — telefon brendi
# _model (private) — telefon modeli
# price — telefon narxi

# Encapsulation:
# brand va model uchun getter va setter yaratish (Property dekoratori orqali).
# Setter’da tekshirish: price 0 dan kichik bo‘lmasligi kerak.

# Instance metodi:
# phone_info() — telefon haqidagi barcha ma’lumotni o‘qish uchun.

# Class metodi:
# total_phones_created() — barcha yaratilgan telefonlar sonini qaytaradi.

# Magic metod (str):
# Telefonni print qilganda “Brand: {brand}, Model: {model}, Price: {price}” ko‘rinishi chiqsin.

# Test qilish:
# 2-3 telefon obyektini yarating.
# Narxni o‘zgartiring, getter orqali brend va modelni o‘qib ko‘ring.
# total_phones_created() chaqirib, umumiy sonini ko‘ring.
# Telefon obyektini print qiling (str ishlashini tekshirish).
# -------------------------------------------------------------------------------------


# class SmartPhone:
#     total_phones = 0

#     def __init__(self,brand,model,price):
#         self._brand = brand
#         self._model = model
#         self._price = price

#         SmartPhone.total_phones += 1

#     @property
#     def brand_model(self):
#         return f"Brand: {self._brand} Model: {self._model}"
    
#     @brand_model.setter
#     def brand_model(self,value):
#         if isinstance(value,tuple) and len(value) == 2:
#             self._brand , self._model = value
#         else:
#             print('Setter uchun tupleda yoziladi faqat 2 ta qiymat')


#     @property
#     def price(self):
#         return self._price
    
#     @price.setter
#     def price(self,value):
#         if value < 0:
#             print("Price 0 dan katta bo'lish kerak")
#         else:
#             self._price = value

#     def phone_info(self):
#         result = f"""
# Brand: {self._brand}
# Model: {self._model}
# Price: {self.price}
# """
#         return result
    
#     @classmethod
#     def total_phones_created(cls):
#         return cls.total_phones
    

#     def __str__(self):
#         return self.phone_info()



# o1 = SmartPhone("BMW","GTR",2026)
# o2 = SmartPhone("BMW","M3",2025)
# o3 = SmartPhone("BMW","M5",2024)


# print(SmartPhone.total_phones_created())

# print(o1)
# print(o2)
# print(o3)

# o1.brand_model = ("bwm","M4")
# print(o1)

# o2.price = -500
# print(o2)


# -------------------------------------------------------------------------------------
# Masala 2 — “Smart Devices Family”

# Sizdan quyidagi vazifani bajarish so‘raladi:

# Base klass yaratish: Device
# Instance atributlar: _brand (private), _model (private), _price
# Getter va setter orqali brand, model va price uchun encapsulation qilinsin.
# Instance metodi: device_info() — barcha ma’lumotni qaytaradi.

# Subclass yaratish: SmartPhone va SmartWatch
# SmartPhone — telefonlar uchun, qo‘shimcha atribut: camera_megapixels
# SmartWatch — soatlar uchun, qo‘shimcha atribut: heart_rate_monitor (True/False)
# Har bir subclass device_info() metodini override qilib, qo‘shimcha atributni ham chiqaradi.

# Polymorphism

# Bir nechta Device obyektlari (telefon va soat) ro‘yxatga joylashtiriladi.
# Bir loop orqali barcha obyektlar uchun device_info() chaqiriladi (method override ishlashini ko‘rsatadi).

# Class atribut
# Device klassida total_devices — barcha qurilmalar sonini hisoblaydi (class variable).
# -------------------------------------------------------------------------------------


# class Device:
#     total_devices = 0

#     def __init__(self,brand:str,model:str,price: float|int):
#         self.__brand = brand
#         self.__model = model
#         self.__price = price

#         Device.total_devices += 1


#     @property
#     def brand(self):
#         return self.__brand
    
#     @brand.setter
#     def brand(self,value:str):
#         if isinstance(value,str) and value != '':
#             self.__brand = value
#         else:
#             print("Faqat matn va bosh bolish taqiqlanadi")
    

#     @property
#     def model(self):
#         return self.__model
    
#     @model.setter
#     def model(self,value:str):
#         if isinstance(value,str) and  value != '':
#             self.__model = value
#         else:
#             print("Faqat matn va bosh bolish taqiqlanadi")


#     @property
#     def price(self):
#         return self.__price
    
#     @price.setter
#     def price(self,value):
#         if isinstance(value,(float,int)) and value > 0:
#             self.__price = value
#         else:
#             print("Qiymat musbat bolish kerak va noldan katta bolish kerak")


#     def device_info(self):
#         result = f"""
# Brand: {self.brand}
# Model: {self.model}
# Price: {self.price}
# """
#         return result
    


# class SmartPhone(Device):
#     def __init__(self,brand,model,price,camera_megapixels):
#         super().__init__(brand,model,price)
#         self.camera_megapixels = camera_megapixels

#     def device_info(self):
#         result = f"""
# {super().device_info()}
# Camera megapixels: {self.camera_megapixels}
# """
#         return result
    


# class SmartWatch(Device):
#     def __init__(self,brand,model,price,heart_rate_monitor):
#         super().__init__(brand,model,price)
#         self.heart_rate_monitor = heart_rate_monitor
    
#     def device_info(self):
#         result = f"""
# Brand: {self.brand}
# Model: {self.model}
# Price: {self.price}
# Heart rate monitor: {self.heart_rate_monitor}
# """
#         return result
    
# o1 = SmartPhone("Samsung", "Galaxy S24", 1100, 50)
# o2 = SmartPhone("Samsung", "Galaxy S21", 800, 30)
# o3 = SmartWatch("Samsung","Galaxy WORLD WACHT-2",300,True)
# o4 = SmartWatch("Samsung","Galaxy WORLD WACHT-1",200,False)

# my_list = [o1,o2,o3,o4]


# for i in my_list:
#     print(i.device_info())

# print("Device total:",Device.total_devices)







# 1 global
# 2 local
# 3 nonlocal
# 4 closure






# x = 10

# def outer():
#     x = 20
    
#     def inner():
#         x = 30
#         print("inner:", x)
    
#     inner()
#     print("outer:", x)

# outer()
# print("global:", x)






# x = 10 

# def outer():
#     x = 20

#     def inner():
#         x = 30
#         print(x)

#     inner()

# outer()





# x = 5

# def outer():
#     x = 10

#     def inner():
#         nonlocal x
#         x = 20
#         print(x)
    
#     inner()
#     print(x)

# outer()
# print(x)



# def my_decorator(func):
#     def wrapper(*args, **kwargs):
        
#         func(*args, **kwargs)
        
#     return wrapper


# @my_decorator
# def test():
#     x = 1

#     return x





# import time

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()

#         func(*args, **kwargs)

#         end = time.time()
#         result = end - start
#         print(f"{result:.10f}")

#     return wrapper


# @my_decorator
# def salom():
#     print("selloo")

# salom()



# counter = 0

# def my_decotarot(func):
#     def wrapper(*args, **kwargs):
#         global counter
#         counter += 1
#         result = func(*args, **kwargs)
#         return f"Funksiya {counter} marta chaqirildi. Funksiya natijasi: {result}"
#     return wrapper



# @my_decotarot
# def salom():
#     return "Salom"


# print(salom())
# print(salom())
# print(salom())
# print(salom())
# print(salom())




# def kvadrat(func):
#     def wrapper(*args, **kwargs):
#         results = func(*args, **kwargs)
#         for i in results:
#             result = i ** 2
#         return result
#     return wrapper



# a = 4

# @kvadrat
# def son(x):
#     return x

# result = son(a)
# print(result)




# def validate_name(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         if len(args) != 2:
#             raise ValueError("Faqat 2 ta qiymat")
        
#         a = args[0]
#         b = args[1]

#         if not isinstance(b,str):
#             raise ValueError("Faqat matndan iborat qiymat bolsin")
        
#         if b[0].islower():
#             b = b.capitalize()
            
#         return func(a,b)


            
#     return wrapper

# a1 = 1
# b1 = "abdurasul"
# print(f"A: {a1} \nB: {b1}")
# print()



# @validate_name
# def test(a:int,b:str):
#     temp = 27

#     if a <= temp:
#         a = 27
#     return f"A: {a} \nB: {b}"


# result = test(a1,b1)
# print(result)






# 1 Mutable va Imutable   (O'zgaruvchan va O'zgarmas)
# 2 Copy va Deepcopy 
# 3 Garbage collection



# python 

# a = 1
# print(type(a))

# a = "Salom"
# print(type(a))


# c

# int a = 1
# print(type(a))

# char[100] a = "Salom"
# print(type(a))






# a = [1,2,3]
# print(id(a))

# mutable:

# list 
# set 
# dict


# a = (1,2,3)

# imutable:


# str
# float
# int
# bool
# tuple




# a = 1
# print(id(a))
# b = a
# print(id(b))


# a = [123]
# print(id(a))

# b = a.copy()
# print(id(b))



# a = [123,1234,[123]]
# print(id(a[-1]))

# b = a.copy()
# print(id(b[-1]))


# import copy

# a = [123,1234,[123]]
# print(id(a[-1]))

# b = copy.deepcopy(a)
# print(id(b[-1]))





# single Thread

# import time


# def read_file(name:str):
#     print(f"Fayl o'qilyapti: {name}")
#     time.sleep(2)
#     print(f"Tugadi: {name}")

# o1 = "file-1"
# o2 = "file-2"
# o3 = "file-3"

# read_file(o1)
# read_file(o2)
# read_file(o3)







# import time
# import threading


# def read_file(name:str):
#     print(f"Fayl o'qilyapti: {name}")
#     time.sleep(2)
#     print(f"Tugadi: {name}")



# f1 = "file-1"
# f2 = "file-2"
# f3 = "file-3"


# o1 = threading.Thread(target = read_file, args=(f1,))
# o2 = threading.Thread(target = read_file, args=(f2,))
# o3 = threading.Thread(target = read_file, args=(f3,))

# o1.start()
# o3.start()
# o2.start()

# o1.join()
# o2.join()
# o3.join()


# from multiprocessing import Process

# def task():
#     print("Process ishlayapti")


# if __name__ == '__main__':
#     p1 = Process(target=task)
#     p2 = Process(target=task)

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()







# import asyncio

# async def asinxron1(n:int):
#     count = 0
#     print(f"Asinxron-1 boshlandi u 10 gacha aylanadi")
#     for i in range(0,n+1):
#         count +=i
#     await asyncio.sleep(5)
#     print('Natija-1:',count)

# async def asinxron2(n:int):
#     count = 0
#     print()
#     print(f"Asinxron-2 boshlandi u 100 gacha aylanadi")
#     for i in range(0,n+1):
#         count += i
#     await asyncio.sleep(10)
#     print('Natija-2:',count)

# number1 = 50
# number2 = 100

# async def start_asinxron():
#     await asyncio.gather(asinxron1(number1),asinxron2(number2))


# asyncio.run(start_asinxron())




# import asyncio

# async def task1():
#     print("Task 1 boshlandi")
#     await asyncio.sleep(3)
#     print("Task 1 tugadi")

# async def task2():
#     print("Task 2 boshlandi")
#     await asyncio.sleep(5)
#     print("Task 2 tugadi")


# async def main():
#     await asyncio.gather(task1(),task2())

# asyncio.run(main())






# import time

# def sinxron1():
#     print("Sinxron-1 boshlandi")
#     time.sleep(5)
#     print("Sinxron-1 tugadi")

# def sinxron2():
#     print("Sinxron-2 boshlandi")
#     time.sleep(5)
#     print("Sinxron-2 tugadi")

# def main():
#     sinxron1()
#     sinxron2()

# main()


# import asyncio


# async def asinxron1():
#     print("Asinxron-1 boshlandi")
#     await asyncio.sleep(4)
#     print("Asinxron-1 tugadi")

# async def asinxron2():
#     print("Asinxron-2 boshlandi")
#     await asyncio.sleep(15)
#     print("Asinxron-2 tugadi")




# async def main():
#     await asyncio.gather(asinxron1(),asinxron2())

# asyncio.run(main())