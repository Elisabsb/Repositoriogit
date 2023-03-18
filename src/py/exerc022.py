#022 crie um programa que leia o nome completo e mostre o nome com todas as letras maiusculas, minusculas,
# quantas letras tem desconsiderando espaço e quantas tem o primeiro nome.
nome = input("Qual o seu nome? ").strip()
print(f"o nome em maiusculo {nome.upper()}")
print(f"o nome em minusculo {nome.lower()}")
separado = nome.split()
print(f"seu nome tem {len(nome) - nome.count(' ')} letras")
print(len(separado[0]))
