# el profesora nececita contabilizar cuantos alumnos aprueban y cuantos desaprueban
# el profesor tiene 6 alumnos 
# el profesor debe ingresar las notas
# y el programa debe separa e imprimir las aprobadas y desaprobadas.

profesor = str(input("Profesor(a), ingrese su nombre: "))
alumnos = int(input(f"Ingrese el numero de alumnos: "))

contador = 1

aprobado = 0
reprobado = 0

while contador <= alumnos:
    nota = int(input(f"ingresa la nota del alumno {contador}: "))
    
    if nota <= 10:
        reprobado += 1
    else:
        aprobado += 1

    contador +=1

print(f"##### PROFESOR(A): {profesor} #####")
print(f"Alumnos en total: {alumnos}")
print(f"---------------------------")
print(f"los aprovados son: {aprobado}")
print(f"los reprovados son: {reprobado}")
