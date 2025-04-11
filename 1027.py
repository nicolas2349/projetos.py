num1,num2,num3= map(int,input().split())
tds_nums=num1,num2,num3
nmaior=max(num1,num2,num3)
nmenor=min(num1,num2,num3)
soma=num1+num2+num3
nmeio=soma-nmaior-nmenor
print(nmenor)
print(nmeio)
print(nmaior)
print()
for n in tds_nums:
    print(n)