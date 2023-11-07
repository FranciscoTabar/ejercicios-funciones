""" programa para calcular IMC de una persona dado su peso y estatura. Luego, indicar su nivel de pero asi:
IMC                 CLASIFICACION
<18.5               ->bajo peso
18.5 - 24.9         ->normal
25.0 - 29.9         ->sobrepeso
30.0 - 34.9         ->obesidad I
35.0 - 39.9         ->obesidad II
40.0 - 49.9         ->obesidad III
>50.0               ->obesidad IV
"""

print("PROGRAMA PARA CALCULAR ES ICM DEL PASIENTE")
def calcularIMC(a,b):
    IMC= a/(b*b)
    return IMC
def nivel_de_peso (IMC):   
    if IMC <18.5:
        return "bajo peso"
    elif 18.5<=  IMC <=24.9:
        return "peso Normal"
    elif 25.0<=  IMC <=29.9:
        return "Sobrepeso"
    elif 30.0<=  IMC <=34.9:
        return "Obesidad I"
    elif 35.0<=  IMC <=39.9:
        return "Obesidad II"
    elif 40.0<=  IMC <=49.9:
        return "Obesidad III"
    elif IMC >50.0:
       return "Obesidad IV"


peso= float(input("ingrese su peso (Kg): "))
estatura= float(input("ingrese su estatura en (metro): "))
print("Su nivel de peso es:", nivel_de_peso(calcularIMC(peso,estatura)))