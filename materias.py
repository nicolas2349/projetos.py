alunos = {}
materias = ["portugues", "matematica", "ciencia", "geografia", "ingles"]

while(True):
        aluno = input(f"digite o nome do aluno: ")
        media = []
        for i in range (1,5):
            print (f"{i}° BIMESTRE")
            notas=[]
            for a in range(0,5):
                nota= float(input(f"digite a nota do aluno em {materias[a]}: ")) 
                notas.append(nota)
            media.append(notas)
        alunos[aluno] = media
        
        opc = input("Deseja Continuar? [S] [N] ")[0].upper()
    
        if(opc=="N"):
         break
print (materias[0],materias[1],materias[2],materias[3],materias[4])
print ("-------------------------------------------- -")
print("nome do aluno",*alunos)
print ("1° bimestre",*media)