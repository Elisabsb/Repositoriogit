#programa que le velocidade de carro e se passar 80km/h calcular multa de 7 reais por km ultrapassado.
from random import randint
kmh = randint(76, 120)
if kmh > 80:
    multa = (kmh-80)*7
    print(f"vc ta em outra dimensão indo a {kmh}km/h??? tome {multa} reais de multa")
else:
    print(f"acelerao ai, ta a {kmh}km/h")
