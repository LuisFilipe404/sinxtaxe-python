# Coleção não ordenada de par chave-valor

# Criando um dicionario de exemplo
pessoa = {
    "nome": "Luís",
    "idade": 22,
    "sexo": "masculino",
    "nacionalidade": "brasileiro",
}

print("Dicionário de exemplo:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Sexo:", pessoa["sexo"])
print("Nacionalidade:", pessoa["nacionalidade"])


pessoa["sobrenome"] = "Filipe"
print("Após adicionar sobrenome:", pessoa)

pessoa["idade"] = 23
print("Após alterar idade:", pessoa)

# Removendo um par chave valor
del pessoa["sobrenome"]

print("Após remover sobrenome:", pessoa)


# Métodos: keys(), values(), items()

chaves = list(pessoa.keys())
print("Chaves:", chaves)
print("Primeira chave", chaves[0])

valores = list(pessoa.values())
print("Valores:", valores)
print("Primeiro valor:", valores[0])

itens = list(pessoa.items())
print("Itens:", itens)
print("Primeira chave valor %s = %s" % (itens[0][0], itens[0][1]))
