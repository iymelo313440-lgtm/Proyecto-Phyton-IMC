# Programa base para calculadora de IMC.
# En este programa se almacenarán los datos del usuario.
print("Bienvenido/a a la calculadora de IMC")

# Nombre del usuario (string)
nombre = input("¿cuál es tu nombre?").title()
while nombre == "":
    print("Error: el nombre no puede estar vacío.")
    nombre = input( "¿Cuál es tu nombre?").title()

# Apellido paterno del usuario (string)
apellido_paterno = input("¿cuál es tu apellido paterno?").title()
while apellido_paterno == "":
    print( "Error: el apellido paterno no puede estar vacio.")
    apellido_paterno = input( "¿Cuál es tu apellido paterno?").title()

# Apellido materno del usuario (string)
apellido_materno = input("¿cuál es tu apellido materno?").title()
while apellido_materno == "":
    print( "Error: el apellido materno no puede estar vacio.")
    apellido_materno = input( "¿Cuál es tu apellido materno?").title()

# Edad del usuario (int)
edad = input("¿cuál es tu edad?")
while not edad.isdigit():
    print( "Error: la edad debe ser un número.")
    edad = input( "¿Cuál es tu edad?")
edad = int(edad)


# Peso del usuario en kilogramos (float)
peso = input("¿cuál es tu peso?")
while True:
    try:
        peso = float(peso)
        break
    except:
        print( "Error: el peso debe ser un número.")
        peso = input( "¿Cuál es tu peso?")


# Estatura del usuario en metros (float)
estatura = input("¿cuál es tu estatura?")
while True:
    try:
        estatura = float(estatura)
        break
    except:
        print( "Error: la estatura debe ser un número.")
        estatura = input( "¿Cuál es tu estatura?")


imc = peso / estatura ** 2
print(f"""
Nombre: {nombre}
Apellido paterno: {apellido_paterno}
Apellido materno: {apellido_materno}
Edad: {edad}
Peso: {peso} kg
Estatura: {estatura} m
IMC: {imc:.2f}
""")



