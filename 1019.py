N=int(input())

horas= N//3600
minu=(N%3600) //60
seg= N%60

print(f"{horas}:{minu}:{seg}")
