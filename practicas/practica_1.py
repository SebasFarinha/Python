#Promedio y nota
notas = []
for x in range(1,4):
    #Validar QUE LA NOTA ESTE ENTRE 1 Y 5
    nota = int(input(f"Ingrese la nota {x}: "))
    while (nota < 0) or (nota > 5):
        
        print("Nota no valida")
        nota = int(input(f"Ingrese la nota {x}: "))
    else:
        
        notas.append(nota)






#Calcular el promedio
suma = 0
for x in range (3):
    suma +=notas[x]
promedio = suma / 3

print("El promedio de notas: ", promedio)
print("Estado: ")
if (promedio > 1.7):
    print("Aprobado")
else:
    print("Reprobado")