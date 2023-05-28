# > Estrutura com contador

def produto(n1, n2):
    produto = n1 * n2
    return produto

numero = int(input("Me forneça o numero que você deseja imprimir a tabuada: "))
teto = int(input("Informe até quantas vezes o deseja multiplicar: "))

contador = 0

while contador <= teto:
    
    print(f"{numero} x {contador} = {produto(numero, contador)}")
    contador = contador + 1