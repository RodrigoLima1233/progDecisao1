'''
3) Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número é par ou
é ímpar.
'''

num = int(input("Indique um número: "))
div = num % 2

if ( div == 0 ):
    print(f"{num} é par")

else:
    print("Este número é ímpar")

