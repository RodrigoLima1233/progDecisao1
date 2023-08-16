'''
8. Fazer um algoritmo que pergunte 3 números, e ao final, guarde na variável maior o maior destes 3 números
inseridos. O valor da variável maior deverá ser exibido ao final.
'''

num = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))
num3 = int(input("Informe o último número: "))

if ( num > num2 and num3):
    print(f"{num}")
else:
    if ( num2 > num and num3 ):
        print(f"{num2}")
    else:
        if (num3 > num and num2 ):
            print(f"{num3}")
