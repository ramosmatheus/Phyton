# Cria Lista vazia
lista = []

#Outra forma de criar lista com tamanho 10
lista2 = [""]*10

#Adiconar um elemento na lsita

lista.append(5)
lista.append(18)
lista.append(32)
lista.append(45)
lista.append(55)
lista.append(56)
lista.append(57)
lista.append(85)

#Alterar valor lista
lista[3] = 44

print("Resultado da lista: ",lista)

#Calcular tamanho da lista

t = len(lista)
i = 0

while i < t:

    print("Na posição {} tem o valor {}.".format(i, lista[i]))
    i += 1

print("=================================================\n")
# Usando o for da maneira foreach
for x in lista:
    print("Valor da lista:", x)

print("=================================================\n")

# Uso do for normal
# len calcula tamanho da lista e range cria uma sequencia numerica de 0 ate o tamanho da lista
for i in range(len(lista)):
    print("Na posição {} tem o valor {}.".format(i, lista[i]))

print("=================================================\n")
# Criar de funções

def dobro(num):
    d = num * 2
    print("O dobro de {} é {}.".format(num, d))
    return d, num
a,b = dobro(5)
print("Os retornos são: {} e {}.".format(a, b))
