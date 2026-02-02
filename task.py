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

#     return f" neg kattasi {max_number} , eng kichigi {min_number}"

# result = kichik_katta(my_list)
# print(result)



# my_list = [4 ,7, 2, 9, 10, 3]

# def toq_juft(n:list) -> str:
#     toq_number = 0
#     juft_number = 0

#     for i in n:
#         if i % 2 == 0:
#             juft_number += 1
#         else:
#             toq_number +=1

#     return f" Natija juft {[juft_number]} ta va toq {[toq_number]} ta"

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
# x = 3

# def nechi_marta(n:list,x:int) -> int:
#     count = 0

#     for i in n:
#         if x == i:
#             count +=1
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




my_list = [3,7,2,9,5]
print(my_list)

def kattasi_oxiriga(n:list) -> list:
    max_number= n[0]
    result_index = 0

    for index,value in enumerate(n):
        if value > max_number:
            max_number = value
            result_index = index
    result = n.pop(result_index)
    n.append(result)
    return n
        

result = kattasi_oxiriga(my_list)

print(result)
