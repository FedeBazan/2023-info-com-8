'''
7-Escribe un programa que pida al usuario una palabra y determine si es un
palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a
izquierda).'''
palabra = input("Escribe una palabra: ")
es_palindromo = True
for i in range(len(palabra)//2):
    if palabra[i] != palabra[-i-1]:
        es_palindromo = False
        break
if es_palindromo:
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")
