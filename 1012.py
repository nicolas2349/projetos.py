A,B,C=map(float,input().split())

pi=3.14159

tri=(A*C)/2
cir=(C**2)*pi
trap=((A+B)*C)/2
qua=B**2
reta=A*B

print(f"TRIANGULO: {tri:.3f}")
print(f"CIRCULO: {cir:.3f}")
print(f"TRAPEZIO: {trap:.3f}")
print(f"QUADRADO: {qua:.3f}")
print(f"RETANGULO: {reta:.3f}")