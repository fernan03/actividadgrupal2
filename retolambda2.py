persona = {}

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
ocupacion = input("Ingrese su ocupacion: ")

crearpersona = lambda nombre,edad,ocupacion: {nombre,edad,ocupacion}

print(crearpersona(nombre,edad,ocupacion))