#um programa que lê um numero real e mostre na tela apenas a parte inteira (antes da virgula)
import math
from random import triangular
num = float(triangular(0, 98))
inte = math.floor(num)
print("o munero {} tem como inteiro {}".format(num, inte))