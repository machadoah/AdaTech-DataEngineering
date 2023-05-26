soma = 0

quantidadeNotas = int(input("Informe a quantidade de notas: "))

for i in range(1, quantidadeNotas + 1):
    nota = float(input(f"Informe sua {i}ª nota: "))
    soma += nota

media = soma / quantidadeNotas

print(f"A média do aluno foi de {media}")
    
    