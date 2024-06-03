import time

#Biblioteca para retornar um número inteiro aleatório 
from random import randint as rd 
sorteado = rd(-100, 100)#Sorteia um numero de -100 á 100
#print(sorteado)

#Criando uma lista de numeros inteiros aleatórios
lista = [rd(1, 6)for i in range(1,11)]
lista2 = [x for x in range (1, 11)]
lista3=["Rolo Compressor!!!" for i in range(1,4)]
# print(lista)
# print(lista2)
# print(lista3)

#Criando uma list PAR
par = [i for i in range(10) if i%2 == 0]
#print(par)

#Povoando uma lista com "input"
#listaUsuario = [(input("Digite um número:")for p in range (5)]
#print(listaUsuario)

#Utilizando o método split (cada palavra se torna um elemento da lista)
nome = "Mickey Mouse"
# print(nome)
# print(nome.split())#Momentaneamente "separou" as palavras e colocou na lista
# print(nome)

#Aplicando o split com 'input'
#notas = [n for n in input("Notas:").split()]
#print(notas)

# notas2 = [float(n) for n in input("Notas:").split(",")]
# print(notas2)

#lista com diferentes informações
listaMista = [17, 70.5, "Sem Mundial", True]
# print(listaMista)

#Manipulação / Fatiamento de Listas
veiculos1 = ["carro", "bicicleta", "moto"]
# print("Veiculos 1:", veiculos1)

#copiando todo o conteudo de uma lista para outra
veiculos2 = veiculos1[:]

del veiculos1[2]
# print()
# print("Veiculos 1:", veiculos1)
# print("veiculos 2:", veiculos2)

#Copiando parte do conteúdo de uma lista
veiculos3 = veiculos2[0:1]
# print("Veiculos 3:", veiculos3)

#Copiando parte do conteudo, incluindo o último elemento 
veiculos4 = veiculos2[1:-1]
# print("veiculos 4:", veiculos4)

veiculos5 = veiculos2[-1:1] #Indice negativo sempre em ultimo lugar, se não será exibido uma lista vazia
# print("Veiculos 5:", veiculos5)

#Outras maneiras de fatiamento (omissão do start ou do end)
my_list = ["A", "B", "C", "D", "E", "F"]
# print(my_list)
nem_list = my_list[:3]
# print(nem_list)
nem_listFim = my_list[3:]
# print(nem_listFim)

#Apagando conteudo de listas
del my_list[1:3]
# print(my_list)
del my_list[:]#Apaga todo o conteudo
# print(my_list)

del my_list

#Testando se alguns itens existem em uma lista ou não para isso, usamos palavras chaves in e not in
naosei = ["A", 'B', 18, 15]
print("A" in naosei)
print("C" not in naosei)
print(15 not in naosei)
time.sleep(3)