from dataclasses import replace

print("Olá, bem vindo/a/e à calculadora de média.")
aluno=input("Digite o nome do aluno: ")


#notasqtd = int(input("Primeiro, digite a quantidade de notas a serem inseridas: "))

mediaMin=float(input("Digite a média mínima para aprovação: ").replace(',','.'))

mediaMin = round(mediaMin,2)

nota1=float(input(f"{aluno}. Digite a primeira nota: ").replace(',','.'))
nota2=float(input(f"{aluno}. Digite a segunda nota: ").replace(',','.'))

media= (nota1+nota2)/2

if(media>=mediaMin):
    print(f"O Aluno {aluno} foi aprovado com a média {media}!!! Parabéns {aluno}")
else:
    print(f"O Aluno {aluno} foi reprovado com a média {media}")