""" programa que convierta una unidad de 
dias , horas , minutos y segundos a segundos"""
print("TRANFORMADOR DE TIEMPO EN SEGUNDOS")
while True:
    dia = int(input("por favor ingrese los dias: "))
    hora = int(input("por favor ingrese las horas: "))
    minutos = int(input("ingrese los minutos: "))
    segundos = int(input("ingrese los segundos: "))

    def convertir_a_segundo(a,b,c,d):
        segundos_totales= 0
        segundos_totales += segundos
        segundos_totales += minutos * 60
        segundos_totales += hora * 60 * 60
        segundos_totales += dia *24 * 60 *60
        return segundos_totales

    segundos_totales= convertir_a_segundo(dia, hora, minutos, segundos)
    print("la cantidad de segundos totales es de:", segundos_totales)

