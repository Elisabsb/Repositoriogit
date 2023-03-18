#4 Escolher um número e mostrar sua tabuada
n = int(input("escolha o número que deseja saber seus multiplos: "))
repeat = int(input("quantas vezes repetir? "))
# print("{} x 1 = {}".format(n, n*1))
# print("{} x 2 = {}".format(n, n*2))
# print("{} x 3 = {}".format(n, n*3))
# print("{} x 4 = {}".format(n, n*4))
# print("{} x 5 = {}".format(n, n*5))
# print("{} x 6 = {}".format(n, n*6))
# print("{} x 7 = {}".format(n, n*7))
# print("{} x 8 = {}".format(n, n*8))
# print("{} x 9 = {}".format(n, n*9))
# print("{} x 10 = {}".format(n, n*10))


# jeito pequeno
for numero in range(1, repeat+1):
    print(f"{n} x {numero} = {n*numero}")
