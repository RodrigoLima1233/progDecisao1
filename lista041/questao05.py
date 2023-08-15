'''
5) Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno.
'''

nota = float(input("Informe a sua primeira nota: "))
nota1 = float(input("Informe a sua segunda nota: "))
not2 = float(input("Informe a sua terceira nota: "))
nota3 = float(input("Informe a sua quarta nota: "))

notaa = nota + nota1 + not2 + nota3

media = notaa / 4

if ( media > 5 ):
    print("Parabéns você foi aprovado")
else:
    print("Você ficou")