import random
import math

#declarando variáveis
a = int(input("Entre com o número de variáveis que você deseja: "))
b = int(input("Entre com o limite inferiror para gerar os números aleatórios: "))
c = int(input("Entre com o limite superior para gerar os números aleatórios: "))
lista = []
moda = []
media = var = 0

#definindo a função mediana
def mediana(lista):
    global median
    oddeven = len(lista)//2
    if len(lista)%2==0:
        half = (lista[oddeven-1]+lista[oddeven])/2
        median = half
    else:
        median = lista[oddeven]
        
#difinindo a função moda
def modal(lista, moda):
    #sem isso não funciona não pergunta por quê.
    for i in range(a):
        moda.append(1)
    #moda
    for i in range(len(lista)):
        e = lista[i]
        for j in range(len(lista)):
            if e==lista[j]:
                f = moda[j]+1
                moda[j] = f
    #removendo o +1 do começo
    for i in range(len(moda)):
        f = moda[i]-1
        moda[i] = f

#definindo a impressão da moda
def imp_moda(moda):
    global g
    g = e = 0
    for k in range(len(moda)):
        if moda[k]>e:
            e = moda[k]
            g = k
            
    
#gerando a amostra
for i in range(a): 
    d = random.randint(b, c)
    lista.append(d)
lista.sort() #ordem crescente

#calculando a média
for i in range(len(lista)):
    media += lista[i]
media = media/len(lista)
print("Valor médio: ", media)

#chamando a mediana
mediana(lista)
print("Mediana da série: ", median)

#moda
modal(lista, moda)
#impressão da moda
imp_moda(moda)
print(f"Moda: O número {lista[g]} apareceu {moda[g]} vezes.")

# Variânça
for i in range(len(lista)):
    var += (lista[i]-media)**2
var = var/len(lista)
print("Variânça: ", var)

#Desvio Padrão PARA VARIÁVEIS ALEATÓRIAS DISCRETAS
dp = var*len(lista)
dp = (1/len(lista))*var
dp = math.sqrt(dp)
print("Desvio padrão: ", dp)

#Coeficiente de variação
cv = dp/media
print("Coeficiente de variação: ", cv)

#Margem de erro
me = 1.96*(dp/math.sqrt(len(lista)))
me *= 100
round(me, 2)
print(f"A margem de erro para essa amostra é de {me}%.")