#Técnicas para deixar as váriaveis mais fácil para ser entendida:

#Camel Case
'''Cada palavra, exceto a primeira, começa com letra maiuscula'''
variavelNome = "Keren"

#Pascal Case
'''Cada palavra começa com letra maiuscula'''
VariavelNome = "Keren"

#Snake Case
'''Cada palavra é separada por um underline'''
variavel_nome = "Keren"


#Vários valores relacionadas com várias variáveis
'''Python permite relacionar valores com várias variáveis em uma linha'''
a, b, c = "Aprendendo", "Python", "Online"
#printando 
print(a)
print(b)
print(c)

#printando em uma linha
print(a,b,c)

#Um único valor relacionada com várias variáveis
'''É possível relacionar o mesmo valor para várias variáveis em uma linha'''
a = b = c = "Python"
print(a)
print(b)
print(c)

#Descompactar uma coleção
'''Se possui uma coleção de coisas numa lista, tupla ou outro, Python permite extrair valores em variáveis into variables.'''

frutas = ["maçã", "banana", "cereja"]
x, y, z = frutas
print(x)
print(y)
print(z)

#Output variáveis
x = "Aprender Python é legal"
print(x)

x = "Aprender"
y = "Python"
z = "é legal"
print(z, y, z)

