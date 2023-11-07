"""comprobar si una palabra o frase es polindrona.
tener en cuenta que no se diferencia los espacios ni las mayusculas y tildes"""
print(" programa para determinar si una palabra o frase es polindrono")

def espolindromo (palabra):
    palabra = palabra.lower()
    palabra = palabra.replace(" ","")
    palabra = palabra.replace ("á","a")
    palabra = palabra.replace ("é","e")
    palabra = palabra.replace ("í","i")
    palabra = palabra.replace ("ó","o")
    palabra = palabra.replace ("ú","u")
    a = 0
    b = len(palabra) -1
    for i in range(0, len(palabra)):
        if palabra[a] == palabra[b]:
            a += 1
            b -= 1
        else:
            return False
    return True

palabra= input("Por favor ingrese una palabra o frase:\n")
if espolindromo(palabra):
    print("es espolindromo")
else:
    print("no es polindromo")



