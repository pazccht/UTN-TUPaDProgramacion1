# Ejercicio 1
edad = int(input("Por favor ingrese su edad: "))
if edad > 18:
    print ("Es mayor de edad")

# Ejercicio 2
nota = int(input("Por favor ingrese su nota: "))
if nota >= 6 :
    print ("Aprobado")
else :
    print ("Desaprobado")


# Ejercicio 3
numero = int(input("Por favor ingrese un número: "))
if numero % 2 == 0 :
    print ("Ha ingresado un número par")
else:
    print ("Por favor, ingrese un número par")

# Ejercicio 4
edad = int(input("Por favor ingrese su edad: "))
if edad < 12:
    print ("Niño/a.")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
elif edad >= 30:
    print("Adulto/a")

# Ejercicio 5
contraseña = input ("Ingrese una contraseña: ")
longitud_contraseña = len(contraseña)
if (longitud_contraseña >= 8 and longitud_contraseña <= 14):
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejercicio 6
import random
from statistics import mode, median, mean

numeros_aleatorios = [ random.randint(1, 100) for i in range(50) ]
print(f"6) Números aleatorios: {numeros_aleatorios}")
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
resultado = "N/A"
if media > mediana and mediana > moda:
    resultado = "Sesgo positivo o a la derecha"
elif media < mediana and mediana < moda:
    resultado = "Sesgo negativo o a la izquierda"
elif media == mediana and mediana == moda:
    resultado = "Sin sesgo"
print(f"Resultado: {resultado}")

# Ejercicio 7
vocales = ["a", "e", "i", "o", "u"]
frase = input ("Ingrese una frase: ")
ultimo_char = frase [-1].lower()
if ultimo_char in vocales:
    frase = frase + "!"
print (frase)

# Ejercicio 8
nombre = input ("Ingrese su nombre: ")
opcion = int(input("Ingrese una opción:\n 1: mayus\n 2: minus\n 3: capitalización\n"))
resultado = nombre
if opcion == 1:
    resultado = nombre.upper()
elif opcion == 2:
    resultado = nombre.lower()
elif opcion == 3:
    resultado = nombre[:1].upper()+nombre[1:]
print (resultado)

# Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud <3:
    categoria = "Muy leve"
elif magnitud >=3 and magnitud <4:
    categoria = "Leve"
elif magnitud >=4 and magnitud <5:
    categoria = "Moderado"
elif magnitud >=5 and magnitud <6:
    categoria = "Fuerte"
elif magnitud >=6 and magnitud <7:
    categoria = "Muy Fuerte"
elif magnitud >=7:
    categoria = "Extremo"
print(categoria)

#Ejercicio 10
hemisferios = [ "N", "S" ]
hemisferio = input("10) Ingrese su hemisferio: ").upper()
if (hemisferio not in hemisferios):
    print(f"Ingrese un hemisferio válido ({hemisferios})")
    exit()
print(f"Seleccionó hemisferio: {hemisferio}")
mes = int(input("Ingrese el mes del año (número): "))
dia = int(input("Ingrese el día (número): "))

hemisferio_norte = hemisferio == "N"
estacion = "N/A"
if (mes == 12 and dia >= 21 and dia <= 31) or (mes >= 1 and mes < 3) or (dia <= 20 and mes == 3):
    estacion = "Invierno" if hemisferio_norte else "Verano"
elif (mes == 3 and dia >= 21) or (mes > 3 and mes < 6) or (mes == 6 and dia <= 20):
    estacion = "Primavera" if hemisferio_norte else "Otoño"
elif (mes == 6 and dia >= 21) or (mes > 6 and mes < 9) or (mes == 9 and dia <= 20):
    estacion = "Verano" if hemisferio_norte else "Invierno"
elif (mes == 9 and dia >= 21) or (mes > 9 and mes < 12) or (mes == 12 and dia <= 20):
    estacion = "Otoño" if hemisferio_norte else "Primavera"
print(f"Estación: {estacion}")