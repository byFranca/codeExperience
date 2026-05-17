"""
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.
"""
NUMEROS=[]
PAR=0
IMPAR=0
POS=0
NEG=0
for i in range(5):
    N=int(input())
    NUMEROS.append(N)

for i in range(len(NUMEROS)):
    if NUMEROS[i]%2==0:
        PAR=PAR+1
    else:
        IMPAR=IMPAR+1


    if NUMEROS[i]>0:
        POS=POS+1
    
    if NUMEROS[i]<0:
        NEG=NEG+1

print(f"{PAR} valor(es) par(es)")
print(f"{IMPAR} valor(es) impar(es)")
print(f"{POS} valor(es) positivo(s)")
print(f"{NEG} valor(es) negativo(s)")