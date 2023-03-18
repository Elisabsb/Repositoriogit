#024 ler o nome de uma cidade e se ela começa ou não com santo
cidade = input("ONDE QUE VC MORA? ").lower().strip()
print(cidade[:5] == "santo")
