# Declaração

nome_completo = "Luís Filipe"

nome_completo_aspas = """
  Luís
  Filipe
"""

nome_completo_quebra = "Luís \
Filipe"

nome = "Luis"
sobrenome = "Filipe"

# Formatação
print("Nome completo (1a forma):", nome_completo)
print("Nome completo (2a forma): " + nome_completo_aspas)
print("Nome completo (3a forma): ", +"Luís " + "Filipe")
print("Nome completo (4a forma): %s" % nome_completo_quebra)
print("Nome completo (5a forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (6a forma): {nome} {sobrenome}")
print("Nome completo (7a forma): {} {}".format(nome, sobrenome))
