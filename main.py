# for i in range(1, 5):
#     print(f'{i}')
#     # if i == 3:
#     #     break
#     for j in range(1, 7):
#         print(f'\t{j}')
#         if j == 5:
#             break


# i = 1
# j = 1
#
# while

# my_list = ['dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma', 'shanba', 'yakshanba']
#
# for hafta in range(1, 5):
#     print(f'hafta: {hafta}')
#     for i in my_list:
#         print(f'\t {i}')
#

# i = 1
# while i < 5:
#     print(f'{i}')
#     j = 0
#     while j < len(my_list):
#         print(f'\t{my_list[j]}')
#         j += 1
#     i += 1


# row = int(input("Row: "))
# col = int(input("Col: "))
# for i in range(1, row):
#     for j in range(1, col):
#         if j == 1 or i == 1 or j == col-1 or i == row-1:
#             print('0', end=' ')
#         else:
#          print('*', end=' ')
#
#     print()



# row = int(input("Row: "))
# col = int(input("Col: "))
#
# ortaRow = row // 2 + 1
# ortacol = col // 2 + 1
#
# for i in range(1, row):
#     for j in range(1, col):
#         if j == 1 or j == col-1:
#             print(i, end=' ')
#         else:
#          print('*', end=' ')
#
#     print()


# row = int(input("Row: "))
# col = int(input("Col: "))
#
# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1
#
# for i in range(1, row+1):
#     for j in range(1, col+1):
#         if i == ortaRow or j == ortaCol:
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')
#
#     print()


# FAMILIYA

# U harifi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))
#
# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1
#
# for i in range(1, row+1):
#     for j in range(1, col+1):
#         if  ( (i != row and j == 1) or
#             (i == row and j < col and j != 1) or
#             (i < row and j == col)
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')
#
#     print()


# R harifi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row+1):
#     for j in range(1, col+1):
#         if (
#             j == 1 or  
#             (i == 1 and j < col - 1) or  
#             (i == ortaRow and j < col - 1) or  
#             (j == col - 1 and i < ortaRow and i != 1) or  
#             (i - ortaRow == j - 2 and i > ortaRow) 
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')

#     print()


# A harifi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row+1):
#     for j in range(1, col+1):
#         if (
#              (j == 1 or j == col) and i != 1 or
#             i == 1 and (j > 1 and j < col) or
#             (i == ortaRow)
            
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')

#     print()



# K harifi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if (
#             (j == 1) or 
#             (i + j == ortaRow + 2) or
#             (i - j == ortaRow - 2)
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')

#     print()


# O harfi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if (
#             (i == 1 and j > 1 and j < col)  or
#             (i == row and j > 1 and j < col)  or 
#             (j == 1 and i > 1 and i < row)  or
#             (j == col and i > 1 and i < row)  
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')

#     print()

# V harfi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if (
#             (i == 1 and (j == 1 or j == col))  or
#             (j == ortaCol and i == row) or
#             (i == ortaRow and (j == 2 or j == col-1)) 
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')

#     print()



# ISM

# U harfi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))
#
# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1
#
# for i in range(1, row+1):
#     for j in range(1, col+1):
#         if  ( (i != row and j == 1) or
#             (i == row and j < col and j != 1) or
#             (i < row and j == col)
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')
#
#     print()

# L harfi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row+1):
#     for j in range(1, col+1):
#         if (
#            (j == 1 or i == row)
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')

#     print()



# U harfi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row+1):
#     for j in range(1, col+1):
#         if ((j == 1 or j == col) or
#             (i == row)
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')

#     print()



# G harfi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row+1):
#     for j in range(1, col+1):
#         if (
#            (i == 1 and j < col and j != 1) or
#            (j == 1 and i < ortaRow and i != 1) or
#            (i == ortaRow and j < col and j != 1) or 
#            (i == row and j < col and j != 1) or 
#            (j == col and i != 1)
            
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')

#     print()

# i != 1 or
#             i == 1 and (j > 1 and j < col+1) and
#             i != ortaRow or
#             i == ortaRow and (j > 1 and j < col+1) and
#             i != row or i == row and (j > 1 and j < col+1)

# B harifi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row+1):
#     for j in range(1, col+1):
#         if (
#            (j == 1 ) or 
#            (i == 1 and j < col) or 
#            (i == ortaRow and j < col) or
#            (i == row and j < col) or
#            (j == col and (i != 1 and i != ortaRow and i < row))
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')

#     print()



# E harfi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row+1):
#     for j in range(1, col+1):
#         if (
#            (j == 1) or 
#            (i == row and j < col) or
#            (i == 1 and j < col) or
#            (i == ortaRow and j < col)
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')

#     print()



# K harifi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if (
#             (j == 1) or 
#             (i + j == ortaRow + 2) or
#             (i - j == ortaRow - 2)
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')

#     print()


# OTCHESTVA

# U harfi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))
#
# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1
#
# for i in range(1, row+1):
#     for j in range(1, col+1):
#         if  ( (i != row and j == 1) or
#             (i == row and j < col and j != 1) or
#             (i < row and j == col)
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')
#
#     print()


# T harfi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row+1):
#     for j in range(1, col+1):
#         if (
#            (i == 1 or j == ortaCol)
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')

#     print()


# K harifi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if (
#             (j == 1) or 
#             (i + j == ortaRow + 2) or
#             (i - j == ortaRow - 2)
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')

#     print()



# I harfi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if (
#             (j == ortaCol) or
#             (i == 1 and j != 1) or
#             (i == row and j != 1) 
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')

#     print()




# R harifi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row+1):
#     for j in range(1, col+1):
#         if (
#             j == 1 or  
#             (i == 1 and j < col - 1) or  
#             (i == ortaRow and j < col - 1) or  
#             (j == col - 1 and i < ortaRow and i != 1) or  
#             (i - ortaRow == j - 2 and i > ortaRow) 
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')

#     print()



# O harfi
row = int(input('Enter the row: '))
col = int(input('Enter the col: '))

ortaRow = row // 2 + 1
ortaCol = col // 2 + 1

for i in range(1, row + 1):
    for j in range(1, col + 1):
        if (
            (i == 1 and j > 1 and j < col)  or
            (i == row and j > 1 and j < col)  or
            (j == 1 and i > 1 and i < row)  or
            (j == col and i > 1 and i < row)
        ):
            print('*', end=' ')
        else:
         print(' ', end=' ')

    print()


# V harfi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if (
#             (i == 1 and (j == 1 or j == col))  or
#             (j == ortaCol and i == row) or
#             (i == ortaRow and (j == 2 or j == col-1)) 
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')

#     print()



# I harfi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if (
#             (j == ortaCol) or
#             (i == 1 and j != 1) or
#             (i == row and j != 1) 
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')

#     print()



# C harifi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if (
#             (j == 1) or 
#             (i == 1 and j != col) or
#             (i == row and j != col)
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')

#     print()



# H harifi
# row = int(input('Enter the row: '))
# col = int(input('Enter the col: '))

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if (
#             (j == 1 or j == 5) or 
#             (i == ortaRow and j != col) 
#         ):
#             print('*', end=' ')
#         else:
#          print(' ', end=' ')

#     print()  




# Sonni topish uyini
# target = 5
# try_user = int(input('Nechta popitka: '))
# i = 0
# while i < try_user:
#     son = int(input('Son kiriting: '))
#     if son == target:
#         print('Siz yutdingiz!')
#         break
    
#     i += 1
     
# if i == try_user:
#     print('Siz yutqazdingiz!')



# Uy ishi
# 1
# row = 4
# col = 4

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#             print('*', end=' ')
#     print()  



# 2
# row = 4
# col = 4

# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if j == 1:
#             print('#', end=' ')
#         else:
#             print('', end=' ')
#         print('*', end=' ')       

#     print()  


# 3
# row = 4
# col = 4

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if j == 1 or i == 1:
#             print('#', end=' ')
#         else:
#             print('*', end=' ')

#     print()   



# # 4
# row = 4
# col = 4

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if j == 1 or i == 1 or j == col:
#             print('#', end=' ')
#         else:
#             print('*', end=' ')

#     print()   




# # 5
# row = 4
# col = 4

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if (j == 1 or i == 1) or (j == col or i == row):
#             print('#', end=' ')
#         else:
#             print('*', end=' ')

#     print()   



# # 6
# row = 4
# col = 4

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if (j == 1 or i == 1) or (j == col or i == row or i == ortaRow):
#             print('#', end=' ')
#         else:
#             print('*', end=' ')

#     print()   



# # 7
# row = 5
# col = 5

# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1

# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if i == j:
#             print('0', end=' ')
#         else:
#             print('*', end=' ')

#     print()   



# 8
# row = 5
# col = 5
#
# ortaRow = row // 2 + 1
# ortaCol = col // 2 + 1
#
# for i in range(1, row + 1):
#     for j in range(1, col + 1):
#         if i >= j:
#             print('0', end=' ')
#         else:
#             print('*', end=' ')
#
#     print()