#54 leia 7 anos de nascimento e mostra quais sao de maior e quais de menor
for x in range(0, 7):
    data = int(input("Digite um ano de nascimento"))
    for z in range(1):
        if data <= 2005:
            print(f"Os que nasceram em {data} são maiores de idade")
        else:
            print(f"naisceu em {data} é de menor!")
print("é isto")
