#declarando variaveis

var_inteira = 10
var_texto = 'exemplo'

print(var_inteira)

print('_____________________________')

#_________________________________________
# estrutura de seleção composta

i = 10

if i > 10:
    print('Item é maior que 10')

elif i == 10:
    print('Item é igual a 10')
    
else:
    print('Item é menor que 10')

print('_____________________________')
#____________________________________________
#laços de repetição - for e while

for posicao, x in enumerate(range(0,10)):
    print(posicao, x)

print('_____________________________')
#____________________________________________
#listas em python

lista_nomes = ['Antonia', 'Rangel', 'Ana']

print(lista_nomes) 

for item in lista_nomes: #lista item por item da lista
    print(item)

print('_____________________________')

for posicao, item in enumerate(lista_nomes): #lista item por item e sua posicao
    print(posicao, item)

print('_____________________________')

lista_nomes.sort() #coloca os item em ordem crescente

for posicao, item in enumerate(lista_nomes):
    print(posicao, item)

print('_____________________________')

#_______________________________________________________
#dicionarios
dicionario = {'nome': 'Alex', 'sobrenome': 'Araujo'}

print(dicionario)

print('_____________________________')

#________________________________________________________
#
