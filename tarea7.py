print("####CALCULADORA####")
def suma (a,b):
    return a + b 
def resta (a,b):
    return a - b
def multiplicacion (a,b):
    return a * b
def potencia (a,b):
    return a ** b
def division (a,b):
    if b == 0:
        print ("no se puede divider por cero")
    else:
        return a / b

num_1= float(input("ingrese el primer numero: "))
num_2= float(input("ingrese el segundo numero: "))

print("----menu de operaciones----")
print ("1-suma")
print ("2-resta")
print ("3-multiplicacion")
print ("4-potencia")
print ("5-division")

opc = int(input("ingrese la opcion que desea: "))

if opc == 1:
    print(num_1, "+", num_2, "=", suma(num_1,num_2))
elif opc == 2:
    print(num_1, "-", num_2, "=", resta(num_1,num_2))
elif opc == 3:
    print(num_1, "*", num_2, "=", multiplicacion(num_1,num_2))
elif opc == 4:
    print(num_1, "**", num_2, "=", potencia(num_1,num_2))
elif opc == 5:
    print(num_1, "/", num_2, "=", division(num_1,num_2))
else:
    print("ingrese una opcion valida")
