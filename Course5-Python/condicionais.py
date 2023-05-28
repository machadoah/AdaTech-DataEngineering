# > ESTRUTURAS CONSICIONAIS

"""
    if condição:
        comando1
        comando2
    else:
        comando1
"""

"""
    Imagine que coê queira imprimir "Aprovado(a)", caso o estudante tenha média maior ou igual a 7, ou
    "Reprovado(a)", caso a média seja inferior a 7
"""

def media(nota1, nota2):
    media = ((nota1 + nota2)/2)
    return media

nome = input("Olá querido aluno, tudo bem? \nMe informe seu primeiro nome: ")
presenca = float(input("Me sua porcentagem de presença, em decimal! (e.g. 75% = 0.75): "))

nota1 = float(input(f"caro {nome} me infome agora sua 1ª nota: "))
nota2 = float(input(f"UAU, me passe agora sua 2ª nota {nome}: "))

media = media(nota1, nota2)

print(f"{nome}, sua média foi de {media}")

if ((media >= 7) and (presenca >= 0.75)):
    print(f"Parabéns {nome} você foi aprovado(a)")
elif(media >= 5):
    print(f"{nome} você ainda pode ir para a recuperação, boa sorte!")
else:
    print(f"Que pena {nome} você foi reprovado(a)")