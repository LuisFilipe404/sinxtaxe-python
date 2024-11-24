# if, elif, else

# Exemplo de if
idade = int(input("Quantos anos voce tem? "))
print("Exemplo de comando if")

if idade >= 18:
    print("Você é maior de idade")
elif idade >= 12:
    print("Você é adolescente")
else:
    print("Você é menor de idade")


mensagem = (
    "Pode tirar carteira de habilitação"
    if idade >= 18
    else "Você não pode tirar carteira de habilitação"
)

print(mensagem)
