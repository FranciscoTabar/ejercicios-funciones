""" programa que calcula el nuevo salario de un trabajador si 
obtubo un incremento del x% """


print("¿quierees saber cual es tu nuevo salario?")
salario_actual = float(input("por favor ingrese su salario actual: ")) 
incremento = float(input("ingrese el porcentaje del aumento de su salario:"))

def calculo_salario(salario, x):
    nuevo_salario = salario + (salario * (x/100))
    return nuevo_salario

nuevo_salario = calculo_salario(salario_actual, incremento)
print("el nuevo salario es de :", nuevo_salario)
