import time
numeros = [111, 7, 2, 1]
print(len(numeros))
#Adicionando mais um numero à lista
numeros.append(52)
print(len(numeros))

print(numeros)
#inserir um novo valor em um respecitivo numero (parametros do insert é a posição e o novo numero)
numeros.insert(0, 222)
print(len(numeros))
print(numeros)

#acrescenta um numero no ultimo passando-o para frente assim tornando o penultimo 
numeros.insert(-1, 12)
print(numeros)
print(len(numeros))

#acrescenta um numero no penultimo passando-o para frente assim tornando o anti-penultimo 
numeros.insert(-2, 20)
print(numeros)
print(len(numeros))
time.sleep(5)
