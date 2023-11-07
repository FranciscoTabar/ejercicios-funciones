""" programam que valide si la contraseña ingresada es segura.
una contraseña segura :
mas de 8 caracteres 
al menos una mayuscula
tiene al menos un numero"""
print("¿como saber si su contraseña es segura?")
def comprobar_contrasenia(password):
    largo= False
    mayus= False
    numer= False
    if len(password)>8 :
        largo= True
    for i in range(len(password)):
        if password[i].isupper():
            mayus= True
        if password[i].isnumeric():
            numer=True
    if largo and mayus and numer:
        return True
    else:
        return False

password = input("Por favor ingrese su contraseña: ")
verificacion = comprobar_contrasenia(password)
if verificacion:
    print("LA CONTRASEÑA ES SEGURA!!")
else:
    print("la contraseña NO es segura!!")





