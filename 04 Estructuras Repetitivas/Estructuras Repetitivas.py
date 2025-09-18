# 1)
print("1)")
for i in range (101):
    print (i)

# 2)
num = input ("2) Ingrese un número entero: ")
aux = float (num)
digitos = 0
if 0==num:
    digitos=1
while aux >= 1:
    aux = aux / 10
    digitos += 1
print ("{num} tiene {digitos} dígitos")

# 3)
num1 = input ("3) Ingrese un número: ")
num2 = input ("Ingrese otro número: ")
total = 0
for i in range (num1 +1, num2):
    total +=i
print (f"La suma entre {num1} y {num2} es {total}")

# 4)
suma = 0
while True:
        num = int(input("Ingrese un número: "))
        if num == 0:
            break
        suma += num
print("El resultado de la suma es:", suma)

# 5)
print ("Adivine el número entre 0 y 9:")
import random
resultado = random.randint(0, 9)
intentos = 0
ingresado = -1
while (ingresado != resultado):
    ingresado = int(input("Ingrese un número: "))
    intentos += 1
print (f"¡Ganaste! El número era: {resultado}. Y la cantidad de intentos fue: {intentos}")

# 6)
for i in range (101, 0, -1):
     if i % 2 == 0:
          print (i)

# 7)
num = int(input ("Ingrese un número entero: "))
total = 0
for i in range (0, num):
     total += i
print(f"La suma entre (0;{num}) es {total}")

# 8)
cantidad = 10
pares = 0
negativos = 0
for i in range (cantidad):
     num = int(input(f"Ingrese un número {i+1} de {cantidad}: "))
     if num % 2 == 0:
        pares += 1
        if num < 0:
             negativos += 1
print (f"Pares: {pares}. Impares: {cantidad - pares}. Negativos: {negativos}. Positivos: {cantidad - negativos}")

# 9) 
import statistics
cantidad = 10
nums = [None] * cantidad
for i in range (cantidad):
     nums[i] = int(input(f"Ingrese número {i+1} de {cantidad}: "))
print(f"La media de {nums} es {statistics.mean(nums)}")

# 10)
num = str(int(input("Ingrese un número entero: ")))
longitud = len(num)
mun = ""
for i in range (longitud):
     mun += num [longitud - i -1]
print (f"{num} -> {mun}")