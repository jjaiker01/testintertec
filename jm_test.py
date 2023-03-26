"""Code Challenge Instructions
“In the programming language of your choice, write a program that parses a sentence and replaces each word with the following: first letter, number of distinct characters between first and last character, and last letter. Words are separated by spaces or non-alphabetic characters and these separators should be maintained in their original form and location in the answer. 

Examples: 
1.	“Smooth” becomes “S3h” 
2.	“Space separated” becomes “S3e s5d” 
3.	“Dash-separated” becomes “D2h-s5d” 
4.	“Number2separated” becomes “N4r2s5d” """

import re

def contar_repetidos(cadena):
    return int(len(set(x for x in cadena if cadena.count(x) > 1)))

def contar_norepetidos(cadena):
    return int(len(set(x for x in cadena if cadena.count(x) == 1)))

def resultado(cadena):
    salida=[]
    for letras in cadena:
        primero = letras[0:1]
        ultimo = letras[-1]
        n1 = str(contar_repetidos(letras[1:len(letras)-1]) + contar_norepetidos(letras[1:len(letras)-1]))
        salida.append(f"{letras}: {primero}{n1}{ultimo}")
    return salida

def limpia1(x):
    return re.split('[^\w+]', x)

def limpia2(x):
    return re.split('[\d]+', x)

def change_list(x):
    lista_changed = ' '.join(x)
    return lista_changed

def format_list(x):
    x = x.split(' ')
    return x

def validate(x):
    nueva = [s for s in x if s != '']
    return nueva


lista_palabras = [
    'a',
    'abc',
    'mbca',
    'hbcaaccad',
    'Smooth',
    'Space separated',
    'Dash-separated',
    'Number2separated',
    'Ma3Bue4no',
    'example*life',
    ''
]

lista = validate(lista_palabras)
lista = change_list(lista)
cadena1=limpia1(lista)
lista = change_list(cadena1)
cadena2=limpia2(lista)
lista = change_list(cadena2)
cadena3=format_list(lista)
print (resultado(cadena3))