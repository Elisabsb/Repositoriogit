#mostrar se numero é par ou impar
from random import randint
numero = randint(1, 101)
resultado = numero % 2
if resultado == 0:
    print(f"o numero {numero} é par")
else:
    print(f"o numero {numero} é impar")
