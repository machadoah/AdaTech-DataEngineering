# > MÉTODOS DE LISTAS

lista = [1, 3, 12, 8, 2]

print(f"Lista original: {lista}")

## > MÉTODOS PARA ADICIONAR ELEMENTOS

# append (adiciona um elemento no final da lista)

lista.append(3)

print(f"Depois do append: {lista}")

# insert (define o indice onde vai ser adiconado e o elemento )

lista.insert(2, 10)

print(f"Depois do insert: {lista}")

# extend (juntar duas listas)

lista2 = [1, 2, 3]

lista.extend(lista2) # Adiciona os elementos de lista2 no final de lista

print(f"Depois do extend: {lista}")

## > MÉTODOS PARA REMOVER ELEMENTOS

# pop (remove um elemento de dado indice, ou se não especificar a posião, remove o ultimo)

lista.pop()

print(f"Depois do pop(): {lista}")

lista.pop(0)

print(f"Depois do pop(0): {lista}")

# remove (remove o elemento que você deseja remover)
    # remove apensar o 1º

lista.remove(3)

print(f"Depois do remove: {lista}")

## > MÉTODOS DE LOCALIZAÇÃO NA LISTA

# count (passando como parametro o elementos, imprime quantas vezes o elemento se repete na lista)

print(f"A quantidade de numeros 2 na lista é de {lista.count(2)} vezes")

# index (passando como paramentro o elemento, devolve o indice dele na lista)

## > ORDENAÇÃO

print(f"Qual o indice do elemento 12 é {lista.index(12)}")

# sort (ordena)
print(f"Lista antes do sort: {lista}")

lista.sort()
# lista.sort(reverse=True) -> (Realiza a ordenação decrescente)

print(f"Lista depois do sort: {lista}")
