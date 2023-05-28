# > DICIONÁRIO

"""
    Se faz possivel criar um label associado a um valor
"""

# criando dicionarios vazios
dicionario = {}
dicionario = dict() 

dicionario = { 'nome': 'Antonio', 'idade': 19, 'altura': 1.77, 'curso': 'Análise de Sistemas' }

print(dicionario['idade']) # acessa a idade

# Adicionando elementos em um dicionario

dicionario['faculdade'] = 'Fatec-PG'
print(dicionario)

# Se for criado duas labels iguais elas são sobrescritas

# Iterando sobre um dicioario

for chave in dicionario:
    print(chave, dicionario[chave]) # percorre as chaves, elementos
    
# Testando a existencia de uma chave

print("peso" in dicionario)
print("altura" in dicionario)