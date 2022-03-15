#Built-in Data Types

#Tipos de dados:
'''
Text Type: str
Numeric Types: int, float, complex
Sequence Types: list, tuple, range
Mapping Type: dict
Set Types: set, frozenset
Boolean Type: bool
Binary Types: bytes, bytearray, memoryview
'''

string = "Hello World"
numero = 20
numero_flutuante = 20.5
complexo = 1j
lista = ["maça", "banana", "cereja"]
tupla = ("maça", "banana", "cereja")
numero_em_range = range(6)
dicionario = {"nome" : "Keren", "ano" : 20}
set_frutas = {"maça", "banana", "cereja"}
frozen_set_frutas = ({"maça", "banana", "cereja"})
booleano = True
set_bytes = b"Hello"

print(type(string))
print(type(set_frutas))
print(type(dicionario))
print(type(booleano))

