'''
9) Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou
nulo.
'''

num = int(input("Informe um número: "))

if ( num > 0 ):
    print(f"{num} é positivo")

elif ( num == 0 ):
    print(f"{num} é nulo")

elif ( num < 0 ):
    print(f"{num} é negativo")
