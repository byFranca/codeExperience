"""
Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos.

Entrada
A entrada contém um número indeterminado de inteiros. A entrada será encerrada quando um valor negativo for lido.

Saída
A saída contém um valor correspondente à média de idade dos indivíduos.

A média deve ser impressa com dois dígitos após o ponto decimal.
"""
idades=[]
total=0
j=0
n=int(input())

while n>=0:
    idades.append(n)
    n=int(input())

for i in range(len(idades)):
    total=total+idades[i]
    j=j+1

media=total/j
print(f"{media:.2f}")