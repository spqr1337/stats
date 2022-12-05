import math

#declaração de variáveis
lista1 = []
lista2 = []
a = int(input("Entre com o número de elementos que deseja inserir: "))
media1 = media2 = soma1 = soma2 = soma3 = 0

#inserção da primeira e segunda lista.
for i in range(a):
    b = float(input(f"Entre com o elemento {i+1} da primera lista: "))
    lista1.append(b)
    c = float(input(f"Entre com o elemento {i+1} da segunda lista: "))
    lista2.append(c)

#calculando a média de cada uma das listas.
for j in range(len(lista1)):
    media1 += lista1[j]
media1 = media1/len(lista1)
for k in range(len(lista2)):
    media2 += lista2[k]
media2 = media2/len(lista2)

#somatorio da parte de cima.
for m in range(a):
    soma1 += (lista1[m]-media1)*(lista2[m]-media2)

#somatorio da parte de baixo.
for n in range(a):
    soma2 += (lista1[n]-media1)**2
    soma3 += (lista2[n]-media2)**2

#calculando o coeficiente de pearson
ccp = soma1 / ((math.sqrt(soma2))*(math.sqrt(soma3)))
ccpa = abs(ccp)
if ccpa>1:
    txt = "muitoforte"
elif ccpa<0.3:
    txt = "desprezível"
elif ccpa<0.5:
    txt = "fraca"
elif ccpa<0.7:
    txt = "moderada"
elif ccpa<0.99:
    txt = "forte"
if ccp>0:
    txt2 = "diretamente"
else:
    txt2 = "inversamente"
print(f"O valor da correlação é {round (ccp, 2)}, o que indica que ela é uma correlação {txt} e {txt2} proporcional.")