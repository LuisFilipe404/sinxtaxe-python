print("For utilizando lista")
lista = [1, 2, 3, 4, 5]

for elemento in lista:
    print(elemento)

print("For utilizando tupla")

tupla = (1, 2, 3, 4, 5)

for elemento in tupla:
    print(elemento)

print("For utilizando dicionário")

pessoa = {
    "nome": "Luís",
    "idade": 22,
    "sexo": "masculino",
    "nacionalidade": "brasileiro",
}

for chave, valor in pessoa.items():
    print(chave, valor)


# range(): retorna um intervalo numérico em formato de lista
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(0, 10)))

print("For utilizando range")

for numero in range(5):
    print("Número", numero)

print("Utilizando range com len")

lista = [1, 2, 3, 4, 5]

for indice in range(0, len(lista)):
    print("Indice", indice, "Valor", lista[indice])

# enumerate()
lista_enumerate = ["a", "b", "c", "d", "e"]

for indice, valor in enumerate(lista_enumerate):
    print("Indice", indice, "Valor", valor)
