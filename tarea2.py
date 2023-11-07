# se pide un programa que calcule el iva de una compra realizada por el usuario


print("+++binevenido al progrma para calcular el IVA de su compra+++")

def valorIVA(p):
    IVA= p*0.21
    return IVA
precio_compra= float((input("por favor ingrese el valor de su  compra:\n")))
IVA = valorIVA(precio_compra)

print ("Ingrese el valor de la compra es:",precio_compra)
print("el valor de la compra con IVA es:", (precio_compra + IVA))

