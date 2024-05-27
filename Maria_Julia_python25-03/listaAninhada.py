import time
#Criando uma lista dentro de outra lista usando o for
lista = [[x for x in range(4)]for i in range(5)]
print(lista)

#Nova organização
lista = [5, 3, 1, 2, 4]

#Organizar em ordem crescente (atualiza as posições)
lista.sort()
print(lista)

#Organizar em ordem decrescente (atualiza as posições)
lista.reverse()
print(lista) 

print(lista[3])
time.sleep(5)