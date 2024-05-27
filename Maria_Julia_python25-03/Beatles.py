import time
beatles = []
print("tamanho da lenta:",len(beatles))
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print("PARTE 2:", beatles)

tamanhoLista = len(beatles)
for i in range(tamanhoLista//2):
    primeiroMembro = str(input("digite Stu Sutcliffe para adicionar ele na lista:"))
    beatles.append(primeiroMembro)
    segundoMembro = str(input("digite Pete Best para adicionar ele na lista:"))
    beatles.append(segundoMembro)
print("PARTE 3:",beatles)

del beatles[-1]
del beatles[-1]
print("PARTE 4:", beatles)

beatles.insert(0, "Ringo Starr")
print("PARTE 5:",beatles)
time.sleep(5)