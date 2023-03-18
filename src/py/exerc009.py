    #6 Saber a largura e altura de uma parede em metros e falar a quantidade de tinta necessária (1lt pinta 2m²)
lar = float(input("Qual a largura da parede em metros? "))
alt = float(input("Qual a altura da parede em metros? "))
print("A parede tem {}m² de area e utilizará {} litros de tinta".format(lar*alt, (lar*alt)/2))
