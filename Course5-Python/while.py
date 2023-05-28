import random

inicio = 0
fim = 10

numero_sorteado = random.randint(inicio, fim) # Será sorteado um numero aleatorio y | 0 <= y <= 10

numero_escolhido = int(input("Informe um número entre 0 e 10: "))

while((numero_sorteado != numero_escolhido)):
    print("Você errou! Tente novamente.")
    
    numero_escolhido = int(input("Informe outro número entre 0 e 10: "))

print(f"Parabéns, você acertou o número sorteado foi {numero_sorteado}!!")