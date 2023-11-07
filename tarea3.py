# programa que calcule la tabla de multiplicar de 
# cualquier numero entero dado por el usuario desde 0 al 12

print("---tabla de multiplicar---")
def tabla_de_multiplicar(n1,n2):
    return str(n1) + "*" + str(n2) + "=" + str(n1*n2)

n= int(input("ingrese un numero entero para ver su tabla de multiplicar:"))

for i in range(0, 13):
    print(tabla_de_multiplicar(n,i))
