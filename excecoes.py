print("exemplo de captura de exceção")

try:
    numero = input("Digite um número inteiro:")
    resultado = 10 / int(numero)
    print(resultado)
except ZeroDivisionError:
    print("Erro: divisão por zero")
    raise ZeroDivisionError("Divisão por zero")
except Exception as e:
    print(f"Erro: {e}")
else:  # Executado se não ocorrer exceção
    print("Executado com sucesso")
finally:
    print("Sempre executado")
