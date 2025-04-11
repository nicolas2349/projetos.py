dtotal=int(input())

anos=dtotal//365
meses= (dtotal % 365) //30
dias= (dtotal % 365) %30

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")