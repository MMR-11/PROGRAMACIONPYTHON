#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
import math
radio = float(input("Introduce el radio del cilindro: "))
altura = float(input("Introduce la altura del cilindro: "))
area_base = math.pi * radio ** 2
area_lateral = 2 * math.pi * radio * altura
area_total = 2 * math.pi * radio * (radio + altura)
volumen = math.pi * radio ** 2 * altura
print(f"Área de la base: {area_base:.2f}")
print(f"Área lateral: {area_lateral:.2f}")
print(f"Área total: {area_total:.2f}")
print(f"Volumen: {volumen:.2f}")