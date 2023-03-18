#1 Calcular emprestimo, perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar. Se a parcela passar de 30% do salario, emprestimo negado
casa = float(input("qual o valor da casa? "))
salario = float(input("quanto vc recebe? "))
anos = int(input("em quantos anos deseja pagar? "))
prestacao = (casa/(anos*12))
if prestacao > (30/100)*salario:
    print(f"sinto muito ,nao vai dar")
else:
    print(f"nossa, pague {prestacao, :.2} reais por mes")
print("muito obrigada por nos escolher")
