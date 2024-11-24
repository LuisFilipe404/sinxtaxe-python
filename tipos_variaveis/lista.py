# Coleção de elementos ordenáveis e mutáveis

# Declaração
minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]

# Exibindo a lista
print("Minha lista de exemplo", minha_lista)

# Exibindo a lista individualmente
minha_lista[0] = "Python"
print("minha_lista[0]:", minha_lista[0])
print("minha_lista[5]:", minha_lista[5])
print("minha_lista[1:7]:", minha_lista[1:7])  # [2, 3, 4, 5, 'rocketseat', True]
print("minha_lista[:5]", minha_lista[:5])  # [1, 2, 3, 4, 5]
print("minha_list[2:]:", minha_lista[2:])  # [3, 4, 5, 'rocketseat', True, False]


# Métodos de listas

# Método append(): Adiciona um elemento ao final da lista
minha_lista.append("Luís")
print("Após append('Luís'):", minha_lista)

# Método index(): Retorna o índice do elemento
indice = minha_lista.index("Luís")
print("Índice de 'Luís':", indice)

# Método insert(): Adiciona um elemento em uma posição específica
minha_lista.insert(0, "Filipe")
print("Após insert(0, 'Filipe'):", minha_lista)

# Método pop(): Remove o último elemento da lista ou um elemento específico
elemento_devido = minha_lista.pop(3)
print("Após pop(3):", minha_lista)
print("Elemento removido:", elemento_devido)

# Método remove(): Remove um elemento específico
minha_lista.remove(True)
print("Após remove(True):", minha_lista)

minha_lista = [0, 1, 2, 3, 4, 5]

# Método sort(): Ordena a lista
minha_lista.sort()
print("Após sort():", minha_lista)
