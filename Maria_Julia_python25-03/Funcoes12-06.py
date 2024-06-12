import time

#parte 1
def hi_everybody(lista):
    for name in lista:
        print("Oi", name)

hi_everybody(["Tina", "Gabi", "Jão"])
#parte 2

def criar_lista(n):
    my_list = []
    for i in range(n):
        my_list.append(i)
    return my_list

print(criar_lista(10))

#parte 3

a = 1
 
def fun():
    global a
    a = 2
    print(a)
 
 fun()
a = 3
print(a)
 



time.sleep(3)