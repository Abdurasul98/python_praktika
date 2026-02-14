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


