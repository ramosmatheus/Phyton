#Este é um comentário

'''
Comentário em bloco
- Três áspas simples ou três áspas duplas
'''

print("Hello World")

print("Phyton foda!")

#variavel
nome = "Matheus"

# Concatenação com o +
print("Olá "+ nome+" !")

#Entrada de dados pelo terminal. Por padrão toda entrada é String
nome = input("Digite seu nome: ")
print("Olá "+nome + ", seja bem vindo ao sistema!! :D")


#Quando trabalhamos com números, temos que converter a variável
idade = input("Digite sua idade: ")
idade = int(idade)
#idade = float(idade)


"""
Operadores
+
-
*
/

** Potência
2**3 = 8
3**2 = 9

** Raiz Quadrada
16**(1/2) = Raiz quadrada de 16
16**(1/3) = Raiz cúbica de 16
"""


print("A raiz é", 16**(1/4) )

"""
Condicionais

&& = and
ou = or
"""

a = 20
#a = int(a)

if a > 10 :
    print(a , " é maior que 10.")

elif a < 10:
    print(a , " é menor que 10.")
else:
    print(a , " é igual a 10")


"""
Laço de repetição WHILE
"""

x = 1
t = 8

while x <= 10:
    print(x, "x", t, "=", t*x)

    x += 1
