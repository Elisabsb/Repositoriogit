#pedir um numero de 0 a 9999 e mostrar separado unidades, dezenas,centenas e milhares.
numero = int(input("digite um numero de 0 a 9999 "))
n = str(numero)
nseparado = str(n.split())
print(f"O número {numero} possui:")
print(f"unidades: {len(nseparado[0])}")
print(f"dezenas: {len(nseparado[1])}")
print(f"centenas: {len(nseparado[2])}")
print(f"milhares: {len(nseparado[3])}")
print(nseparado)
#DEU MERDA AAAAAAAAAAAA
