import time
#Encontrar o maior valor na lista - Exemplo 1
lista = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maiorNumero = lista[0] #Recebeu o numero 17
for i in range(1, len(lista)):
    if lista[i] > maiorNumero:
        maiorNumero = lista[i]
print("Numero Maior da Lista:", maiorNumero)

time.sleep(3)