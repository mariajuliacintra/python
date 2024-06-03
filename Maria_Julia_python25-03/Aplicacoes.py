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

#Exemplo 4 - Conferidor de aposta na loteria
sorteados = [5, 11, 9, 42, 3, 49]
apostados = [3, 7, 11, 42, 34, 49]
acertos = 0

for numero in sorteados:
    if numero in apostados:
        acertos += 1 
print("Numeros de acertos:", acertos)

#Remoção de numeros repetidos em uma lista 
lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print("lista original:", lista)
#Lista de apoio
vistos = []
#Iterar pela lista original de trás para frente
for i in range(len(lista)-1,-1,-1):
    #Se o numero já esta na lista "vistos" removelo da lista original
    if lista[i] in vistos:
        del lista[i]
    else:
        #Caso contrario adiciona a lista "vistos"
        vistos.append(lista[i])
print("Lista modificada:", lista)


#Listas Avançadas
#2 D - listas aninhadas bidimensionais
tabela=[[":(", ":)", ":|", ";-;"], [";-;", ":|", ":)", ":("], [":|", ":)", ";-;", ":("]]
print(tabela[0][3])

#3D - Matriz Tridimensional
cubo = [[[":(", "y", "z"], [":)", "y", "z"], [":|", "y", "z"]],
        [["amor", "ódio", "caridade"], ["paz", "esperança", "férias"], ["tina", "prior", "pp"]],
        [["restinga", "patrocinio", "rifaina"], ["amazonense", "fluminense", "santos"], ["pizza", "lasanha", "pastel"]]]
print(cubo)
print(cubo[1])
print(cubo[1][0])
print(cubo[1][0][2])
time.sleep(3) 