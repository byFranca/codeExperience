"""
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
"""

N=int(input())
V100=0
V50=0
V20=0
V10=0
V5=0
V2=0
V1=0
print(f"{N}")
if 0<N and N<1000000:
    while N>=100:
        N=N-100
        V100=V100+1
    while N>=50:
        N=N-50
        V50=V50+1
    while N>=20:
        N=N-20
        V20=V20+1
    while N>=10:
        N=N-10
        V10=V10+1
    while N>=5:
        N=N-5
        V5=V5+1
    while N>=2:
        N=N-2
        V2=V2+1
    while N>=1:
        N=N-1
        V1=V1+1
    print(f"{V100} nota(s) de R$ 100,00")
    print(f"{V50} nota(s) de R$ 50,00")
    print(f"{V20} nota(s) de R$ 20,00")
    print(f"{V10} nota(s) de R$ 10,00")
    print(f"{V5} nota(s) de R$ 5,00")
    print(f"{V2} nota(s) de R$ 2,00")
    print(f"{V1} nota(s) de R$ 1,00")