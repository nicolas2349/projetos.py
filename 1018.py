def nota(N):
    print (N)
    
    notas=[100,50,20,10,5,2,1]
    
    for nota1 in notas:
        quant=N // nota1
        print(f"{quant} nota(s) de R$ {nota1},00")
        N %= nota1
N=int(input())
if 0<N<1000000:
    nota(N)