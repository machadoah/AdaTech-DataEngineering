# > Estrutura de dados (LISTAS)

# Antes 
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

# Com listas
notas = [7.9, 9.7, 8.2]

# Criando Listas
lista = [] # Cria uma lista vazia
lista = list() # Cria uma lista vazia 

lista = [26, 'Antonio', True, 3.1415]

lista_de_listas = [10, [1,2,3]] # o 1º elemento é um elemento, a 2º é outra lista

# Indexação e Slices

print(lista[0]) # Imprime o 1º elemento

# Slices

lista = ["Corinthians", "São Paulo", "Flamengo", "Santos", "Palmeiras", "Vasco"]

print(lista[0:3]) # elementos do indices 0,1,2
print(lista[:]) # lista inteira
print(lista[2:5:2]) # inicia no indice 2, vai até 4, pulando de 2 em 2

# > Iteração com For

# 1. Utilizando os elementos

for elemento in lista:
    print(elemento)
    
# 2. Utilizando os índices

print(f"Comprimento da lista é {len(lista)}")

for i in range(len(lista)):
    print(lista[i])