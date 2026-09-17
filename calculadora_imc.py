# Programa base para calculadora de IMC.
# En este programa se almacenarán los datos del usuario.

# Nombre del usuario (string)
nombre = input("¿cuál es tu nombre?")

# Apellido paterno del usuario (string)
apellido_paterno = input("¿cuál es tu apellido paterno?")

# Apellido materno del usuario (string)
apellido_materno = input("¿cuál es tu apellido materno?")

# Edad del usuario (int)
edad = int(input("¿cuál es tu edad?"))

# Peso del usuario en kilogramos (float)
peso = float(input("¿cuál es tu peso?"))

# Estatura del usuario en metros (float)
estatura = float(input("¿cuál es tu estatura?"))

imc = peso / estatura ** 2
print(imc)

print("Bienvenido/a a la calculadora de IMC")

