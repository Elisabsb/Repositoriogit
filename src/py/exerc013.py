#sortear 1 de 4 nomes
from random import choices
f1 = input("nome 1")
f2 = input("nome 2")
f3 = input("nome 3")
f4 = input("nome 4")
esco = choices([f1, f2, f3, f4], k=1)
print("o filme escolhido foi {}".format(esco))
