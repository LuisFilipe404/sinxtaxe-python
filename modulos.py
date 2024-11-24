print("Exemplo de importação de módulo padrão:")
import math
from math import sqrt

raiz_quadrada = math.sqrt(25)
print(f"A raiz quadrada de 25 é {raiz_quadrada}")

raiz_quadrada = sqrt(25)
print(f"A raiz quadrada de 25 é {raiz_quadrada}")

print("Exemplo de importação de módulo customizado:")

import meu_modulo

mensagem = meu_modulo.saudacao("Filipe")

print(mensagem)
