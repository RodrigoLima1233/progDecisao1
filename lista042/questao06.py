'''
6. Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final o algoritmo
deverá exibir na tela a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior
que o ano atual, o cálculo de idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela:
“Dados inseridos estão incorretos”.
'''

nasc = int(input("Informe o ano de seu nascimento: "))
ano = int(input("Informe seu ano atual: "))

sub: int = ano - nasc

print(f"Você tem {sub} anos de idade")

if ( ano > 2023 ):
        print("Dados inseridos estão incorretos")