#7 Mostrar o preço de um produto e quanto ele ficará com 5% de desconto
p = float(input("Qual o valor do produto? "))
print("esse produto ficará por {} reais com o desconto".format((-p*5)/100+p))
