# > FUNÇÕES

# 1. O que são funçoes e por que uriliza-las?

"""
print() # imprime uma mensagem
input() # retorna um valor informado pelo usuário
len() # retorna a quantidade de elementos da lista
"""

# 2. Criando funções

# Função inicial

def saudacao():
    print("Seja bem-vindo(a)!")
    print("É um prazer ter você por aqui! ❤️")

saudacao() # Imprime

# Função com parâmetro

def saudacao(nome, curso):
    print(f"Seja bem-vindo {nome}!")
    print(f"É um prazer ter você por aqui, fazendo parte do curso de {curso}! ❤️")
    
saudacao("Antonio", "Orintação a Objetos com Java")

# Função com parâmetro default
    # Por padrão dado parametro recebe um valor pre-definido

def saudacao(nome, curso="Python"):
    print(f"Seja bem-vindo {nome}!")
    print(f"É um prazer ter você por aqui, fazendo parte do curso de {curso}! ❤️")
    
saudacao("Antonio")

# Função com retorno

def soma(numero1, numero2):
    soma = numero1 + numero2
    
    return soma

numero1 = 7
numero2 = 5

print(f"A soma de {numero1} + {numero2} é {soma(numero1, numero2)}")