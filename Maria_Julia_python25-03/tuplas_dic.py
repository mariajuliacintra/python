import time 
#tupla é uma lista que não da para fazer alterações ou seja esse tipo de codigo com ela não dará certo
#tupla[0] = 100 (tentando mudar o valor da posição 0 para 100) (ERRO!!!)
# tupla = tuple()
tupla = (1)
tupla = (1,)
tupla = 1, 2, 3

#print(tupla)
#print(tupla[1])

#manipulando dicionários:
dic = {"semMundial":"Palmeiras", "1Mundial":"Corinthinas", "2Mundiais":"SãoPaulo"}
print(dic['semMundial'])

notas = {"Mat":5, "LP":10, "EF":8}
print(notas)
print(notas["EF"])

#print(dir(notas)) #lista as funcionalidade/metodos que pode ser aplicado com "notas"

print(notas.values())  #metodo para exiber somente o conteudo dentro do dicionário SAIDA: (dict_values([5, 10, 8]))
print(notas.keys()) #vai exibir o indices que foram definidos na criação do dicionário SAIDA: (dict_keys(['Mat', 'LP', 'EF']))
print(len(notas))#vai exibir o tamanho do dicionário

for disciplina in notas.keys():
    print(disciplina)
time.sleep(3)