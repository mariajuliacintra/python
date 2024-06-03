import time
#Encontrar o maior valor na lista - Exemplo 1
lista = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maiorNumero = lista[0] #Recebeu o numero 17
for i in range(1, len(lista)):
    if lista[i] > maiorNumero:
        maiorNumero = lista[i]
print("Numero Maior da Lista:", maiorNumero)

#Exemplo 2
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 18]
maior = my_list[0]
for i in my_list:
    if i > maior:
        maior = i
print("Valor Maior2:", maior)

# exemplo 3
ultimaLista = my_list[:]
mel = ultimaLista[0]
for i in ultimaLista[1:]:
    if i > mel:
      mel = i
print(mel)

#Encontrar a localização de um determinado elemento dentro de uma lista
frutas = ["abacaxi", "maçã", "pêra", "mamão", "uva", "melancia"]
elemento = "melancia"
achado = False

for i in range(len(frutas)):
    achado = frutas[i] == elemento
    if achado:
        break

if achado:
    print("Elemento encontrado no indice:", i)
else:
    print("Elemento não encontrado!!!")

time.sleep(3)