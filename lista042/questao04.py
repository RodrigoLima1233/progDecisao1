'''
4. Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana.
'''

num = int(input("Informe um número de 1 a 7: "))

if ( num == 1 ):
    print(f"{num} esse dia é Domingo")
else:
    if ( num == 2 ):
        print(f"Dia {num} é segunda-feira")
    elif ( num == 3 ):
        print(f"Dia {num} é terça-feira")
    elif ( num == 4):
        print(f"Dia {num} é quarta-feira")
    elif ( num == 5 ):
        print(f"Dia {num} é quinta-feira")
    elif ( num == 6 ):
        print(f"Dia {num} é sexta-feira")
    elif ( num == 7 ):
        print(f"Dia {num} é sábado")
    else:
        if ( num > 7 ):
            print("Número inválido")
        else:
            if ( num == 0 ):
                print("Número inválido")