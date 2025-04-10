#cpf = [5,6,9,3,9,2,7,3,8,5,9]
# cpf = [5,6,9,3,9,2,7,3,8,5,9]
cpf_entrada = str(input("digite seu cpf:"))
cpf = []
for p in cpf_entrada:
    if p in '0123456789':
        v1 = int(p)
        cpf.append(v1)

soma = (cpf[0])*10,(cpf[1])*9,(cpf[2])*8,(cpf[3])*7,(cpf[4])*6,(cpf[5])*5,(cpf[6])*4,(cpf[7])*3,(cpf[8])*2
mult = sum(soma)
res = mult%11

DV_1=0
if (res<2):
    DV_1 = 0
else:
    DV_1= 11-res

    

soma = (cpf[0])*11,(cpf[1])*10,(cpf[2])*9,(cpf[3])*8,(cpf[4])*7,(cpf[5])*6,(cpf[6])*5,(cpf[7])*4,(cpf[8])*3,(cpf[9])*2
mult2 = sum(soma)
res2 = mult2%11

DV_2=0
if (res2<2):
    DV_2 = 0
else:
    DV_2= 11-res2

if (DV_1== cpf[-2] and DV_2==cpf[-1]):
    print ("CPF VALIDO!")
else:
    print ("CPF INVALIDO!")  