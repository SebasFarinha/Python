#Ejercicio del 1.10
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    if (b==0):
        print("NO SE PUEDE DIVIDIR POR CERO!!!!")
    else:
        return a/b
def raiz(radicando,indice):
    return radicando *(1/indice)



#Prueba, solo se imprime en calculadora.py
if __name__ == "__main__":
    print("La suma de 2 y 8 = ", suma(2,8))
    print("La resta de 2 y 8 = ", resta(2,8))
    print("La multiplicacion de 2 y 8 = ", multiplicacion(2,8))
    print("La division de 2 y 8 = ", division(2,8))
    print("La raíz de 2 con indice 8 = ", raiz(2,8))