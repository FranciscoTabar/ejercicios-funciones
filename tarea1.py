"""se pide un programa que calcule la nota final del alumno sabiendo que la 
primera y segunda nota corresponden al 30% y la tercer nota al 40% de la 
calificacion final"""
print(----"calculo de nota final----")
n1= float(input("ingrese el valor de la primera nota:"))
n2= float(input("ingrese el valor de la segunda nota:"))
n3= float(input("ingrese el valor de la tercera nota:"))

def calcular_nota (n1, n2, n3):
    return (n1*0.3) + (n2*0.3) + (n3*0.4)

nota_final= calcular_nota ( n1, n2, n3)

print( "la nota final del estudiante es :", round(nota_final,2))

