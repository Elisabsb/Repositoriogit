#escreva um programa que gere um numero aleatorio entre 0 e 5 e o usuario deve tentar descobrir qual o numero escolhido e escrever venceu ou perdeu
import random
numaleatorio = random.randint(0, 5)
resposta = int(input("ME FALE QUAL O NUMERO QUE O PC ESCOLHEU ENTRE 0 E 5! "))
if resposta == numaleatorio:
    print("EITA COMO LACRAA")
elif resposta > 5:
    print("EU MANDEI APENAS ATE 5")
else:
    print(f"o numero era {numaleatorio}")
