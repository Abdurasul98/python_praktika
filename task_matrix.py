# a = [
#     [1,2],
#     [3,4]
# ]
# temp1 = len(a)

# b = [
#     [5,6],
#     [7,8]
# ]
# temp2 = len(b)

# c = [[0,0],[0,0]]


# for i in range(temp1):
#     for j in range(temp2):
#         c[i][j] = a[i][j] + b[i][j]


# print(c)




# A = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# B = list()

# for i in A:
#     list_temp = list()
#     for j in i:
#         temp = j * 2
#         list_temp.append(temp)
#     B.append(list_temp)
    
# print(B)



# A = [
#     [2, 4, 6],
#     [1, 3, 5],
#     [7, 8, 9]
# ]

# B = list()


# for i in A:
#     temp_list = list()
#     index = len(i)
#     for j in range(index):
#         if i[j] % 2 == 1:
#             temp_list.append(1)
#         else:
#             temp_list.append(0)
#     B.append(temp_list)

# print(B)


# A = [
#     [2, 4, 6],
#     [1, 3, 5],
#     [7, 8, 9]
# ]

# result = 0

# for i in range(len(A)):
#     result = result + A[i][i]

# print(result)


# matrix = [
#     [1,2],
#     [3,4]
# ]

# for i in matrix:
#     for j in i:
#         result = j * 3
#         print(result,end=" ")
#     print()




# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# len_r = len(matrix)


# for i in range(len_r):
#     for j in range(len_r):
#         if i + j == len_r -1:
#             print(matrix[i][j], end= " ")




matrix = [
    [3, 1, 2],
    [7, 4, 1],
    [2, 8, 3]
]


class MatrixJavob:
    def result(self,value):
        if isinstance(value,list):
            max_value = None

            for i in value:
                temp_sum = 0
                for j in i:
                    temp_sum += j
                    
                if max_value is None:
                    max_value = temp_sum
                else:
                    if max_value < temp_sum:
                        max_value = temp_sum
            return f"Eng katta qiymat:{max_value} shu matrix ichidan:{i}"

        else:
            return f"Faqat list typeda MATRIX keladi"
        
o1 = MatrixJavob()
result = o1.result(matrix)
print(result)