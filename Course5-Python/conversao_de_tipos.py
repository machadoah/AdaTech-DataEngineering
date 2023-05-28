# CONVERSÃO DE TIPOS

idade = '19'
numero1 = '10'
numero2 = '20'

print(f"Imprimindo concatenação {numero1 + numero2}") # Realiza a concatenação dos textos!

numero1 = int(numero1) # convertendo string em int
numero2 = int(numero2)

idade_numerica = int(idade)

print(f"Soma dos numeros {numero1 + numero2}")

print(f"Ano passado você tinha {idade_numerica - 1} anos!")

print(idade, type(idade))
print(idade_numerica, type(idade_numerica))