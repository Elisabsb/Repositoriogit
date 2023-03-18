#somar só os multiplos impares de 3 indo de 1 ate 500
soma = 0
for cont in range (1, 501, 2):
    if cont % 3 == 0:
        soma = soma + cont
print(f"a soma disso tudo da {soma}")
