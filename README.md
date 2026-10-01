# Calculadora de IMC

# Descripción del programa
La calculadora de IMC es un programa desarrollado en Python que solicita al usuario sus datos personales, edad, pero y estatura para calcular su índice de masa corporal IMC. El programa presenta los datos de manera organizada y valida las entredas del usuario para evitar campos vacíos y errores en los datos numéricos.

# Requisitos
-Tener Python instalado.
-Contar con el archivo ´calculadora_imc.py´.
-Utilizar un entorno de desarrollo como visual studio code o una terminal.

# Instrucciones de ejecución
1. Abrir el archivo ´calculadora_imc.py´.
2. Ejecutar el programa desde visual studio code o desde la terminal.
3. Introducir el nombre y los apellidos cuando sean solicitados.
4. Introducir la edad como un número entero.
5. Introducir el peso y la estatura utilizando valores numéricos.
6. El programa mostrará los datos ingresados y el resultado del IMC.

# Datos que solicita el programa
| Dato | Tipo de dato |
|---|---|
| Nombre | `str` |
| Apellido paterno | `str` |
| Apellido materno | `str` |
| Edad | `int` |
| Peso | `float` |
| Estatura | `float` |

# Validaciones implementadas
El Programa incorpora validaciones para evitar que el usuario continúe con campos vacíos.

El peso y la estatura se reciben como texto y se intenta realizar su conversión a ´float´mediante ´try/except´. Si la conversión no es posible, se muestra un mensaje de error y se solicita nuevamente el dato.

# Refelxión personal
Durante eñ Bootcamp he aprendido la importancia que tiene cada elemento al momento de programar. Los puntos, las comas, los paréntesis, las comillas y cada carácter son importantes para que el programa pueda ejecutarse correctamente. Incluso una sola letra puede cambiar el contexto de una instrucción y generar un error.
Al principio me costaba un poco identificar cuáles eran las variables y estructuras adecuadas para resolver los retos. Sin embargo, a medida que fui aprendiendo y practicando, cada concepto se volvió más comprensible y me resultó más fácil identificar qué herramienta utilizar en cada situación.
Todavía me falta mucho por aprender y practicar, pero considero que ahora comprendo las bases necesarias para continuar avanzando en Python y seguir desarrollando mis habilidades de programación.
