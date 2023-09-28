alumnos_lista=[]
while True:
    try:
        cantidad_alumnos= int(input("Ingrese el número de alumnos a ingresar: "))
        while cantidad_alumnos<=0:
            cantidad_alumnos= int(input("Vuelva a ingresar el número de alumnos a ingresar: "))
        for i in range(cantidad_alumnos):
            try:
                nombre= input(f'Ingrese el nombre del alumno {i+1}: ')
                notas= []
                for j in range (3):
                    nota= float(input(f"Ingrese las nota {j+1} del alumno {nombre}: "))
                    notas.append(nota)
                alumno={"Alumno": nombre, "Notas": notas}
                alumnos_lista.append(alumno)
            except ValueError:
                nombre= (input("Vuelva a ingresar el nombre del alumno: "))
        break
    except ValueError:
       print("Vuelva a ingresar el número de alumnos a ingresar")
for alumno in alumnos_lista:
    print(f"Alumno: {alumno['Alumno']}")
    print(f"Notas: {alumno['Notas']}")
