n1,n2,n3 = map (int, input().split())
d=(n1+n2+abs(n1-n2))/2

maior=(d+n3+abs(d-n3))/2

print(f"{int(maior)} eh o maior")