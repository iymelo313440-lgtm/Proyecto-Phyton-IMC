# Programa base para calculadora de IMC.
# En este programa se almacenarán los datos del usuario.
print("Bienvenido/a a la calculadora de IMC")

# Nombre del usuario (string)
nombre = input("¿cuál es tu nombre?").title()

# Apellido paterno del usuario (string)
apellido_paterno = input("¿cuál es tu apellido paterno?").title()

# Apellido materno del usuario (string)
apellido_materno = input("¿cuál es tu apellido materno?").title()

# Edad del usuario (int)
edad = int(input("¿cuál es tu edad?"))

# Peso del usuario en kilogramos (float)
peso = float(input("¿cuál es tu peso?"))

# Estatura del usuario en metros (float)
estatura = float(input("¿cuál es tu estatura?"))

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



