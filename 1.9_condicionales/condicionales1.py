#ejercicio 1 del 1.9
num1 = int(input("Ingrese primer numero"))
num2 = int(input("Ingrese el segundo numero"))
if num1 > num2:
    if num1 % 2 == 0 :
        print( num1, "es mayor, y es un numero par")
    else:
       print(num1, "es mayor, y es un numero impar")
elif num1 < num2:
    if num2 % 2 == 0 :
         print( num2, "es mayor, y es un numero par")
    else:
       print(num2, "es mayor, y es un numero impar")
else:
    print("Los numeros son iguales")
