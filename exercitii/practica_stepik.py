import math

#TODO ------------------------------------------------

# input().split()
# ceva = input("Introdu cateva cuvinte: ").split()
# print(ceva)
#TODO ------------------------------------------------
#
#
# lst_int = list(map(int, input("Introdu:").split()))
# print(lst_int)
#TODO ------------------------------------------------
#
#
# lista = list(map(int, input("Introdu cateva valori").split()))
# print(*lista)
#TODO ------------------------------------------------
#
# name = 'stas'
# surname = 'mrd'
# patronimic = 'vladimir'
# print(name, surname, patronimic, sep = '\n')
# print(name, surname, patronimic, end = ' ')
# print(name, surname)
# print(f"Numele = {surname}\nPrenumele ={name}\nPatronimic ={patronimic}")
#
#
#TODO ------------------------------------------------
#
# a,b = map(int,input("Introdu laturile unui celor 2 catete ale triunghiului:").split())
# c = math.sqrt(a**2 + b**2)
# print(f"Rezultat = {c}")
#
#TODO ------------------------------------------------

# math.pi = float(input())
# print(round(math.pi, 3))

#TODO ------------------------------------------------

# width = int(input())
# height = int(input())
#
# sq = width * height
# pr = 2 * (width + height)
#
# print("Площадь прямоугольника равна sq", sq)
# print("Периметр прямоугольника равен pr", pr)

#TODO ------------------------------------------------

# s = 0
# i = 0
# n = -10
#
# while i > n:
#     i-=1
#     s-=1
#     print(s)

#TODO ------------------------------------------------

# pass_true = '12345'
# ps = ''
# while ps != pass_true:
#     if ps != pass_true:
#         ps = input('Introdu parola corecta: ')
# else:
#     print('Parola corecta!')

#TODO ------------------------------------------------

# n = 20
# i = 1
# while i < n:
#     if i % 2 == 0:
#         print(i)
#     i+=1

#TODO ------------------------------------------------
# 5.1 || EX 4

# n,m = map(int,input().split())
# rs = ''
# while n<=m:
#     if n<=m:
#         rs += str(n**2) + ' '
#     n+=1
# print(rs)

#TODO ------------------------------------------------
# 5.1 || EX 5

#price = float(input())
# result = ''
# i = 2
# while i<=10:
#     result += f'{(price*i):.1f}' + ' '
#     i+= 1
#
# print(result)
#TODO ------------------------------------------------
# 5.1 || EX 6

# n = int(input())
# i=1
# s=0
# while i <= n:
#     s=s+(1/i)
#     i+=1
# print(f'{s:.3f}')
#TODO ------------------------------------------------
# 5.1 || EX 7

# rs = 0
# while (inp := int(input())) != 0:
#     rs +=inp
#
# print(rs)

#TODO ------------------------------------------------
# 5.1 || EX 7

# msg = input()
# while '--' in msg:
#     msg = msg.replace('--','-')
# print(msg)
#TODO ------------------------------------------------
# 5.1 || EX 8

# n = list(map(int,input()))
# i = 0
# result = 1
# while i<len(n):
#     result = result * n[i]
#     i=i+1
# print(result)
#TODO ------------------------------------------------
# 5.1 || EX 9

# n = int(input())
# a,b = 1,1   # am luat din comments
# i = 0
# result = '1'
# while len(result.split(' ')) < n:
#     i+=2
#     a,b = b,a+b # am luat din comments
#     result += " "+str(a)
# print(result)
#TODO ------------------------------------------------
# 5.1 || EX 10

# n = int(input())
# a = 1
# i = 3
# while i<n:
#     a =a*2
#     i += 3
# print(a)
#TODO ------------------------------------------------
# 5.1 || EX 11

# n = int(input())
# i = 1
# dep = 1000
# while i <= n:
#      dep += (dep*0.05)
#      i+=1
# print(round(dep,2))
#TODO ------------------------------------------------
# 5.1 || EX 12

# n,m = map(int, input().split())
# i = n
# result = ''
# while  i<=m:
#     if (i % 2)!=0:
#         result += str(i) + ' '
#     i += 1
# print(result)
#TODO ------------------------------------------------
# 5.1 || EX 13

number = 100
result = ''
while number < 1000:
    if number % 3 == 0 and number % 47 == 43:
        result += str(number) + ' '
    number += 1
print(result)
#TODO ------------------------------------------------