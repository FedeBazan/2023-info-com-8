'''
4-Escribe un programa que imprima los números pares del 1 al 100.
'''
print('##Numeros pares del 1 al 100##')
for i in range(1,100):
    if i%2==0:
        print(f'{i}',end=', ')
else:
    print('100.')