"""
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.
"""

X=int(input())
cont=0
while cont<6:
    if X%2==0:
        X=X+1
    else:
        print(f"{X}")
        X=X+1
        cont=cont+1