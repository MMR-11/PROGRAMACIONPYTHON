#calcula area y longitud de un circulo: area=pi*r la la dos longitud=2pi*r
import math
diámetro=float(input("introduce el diámetro:"))
radio=diámetro/2
area=math.pi * (radio ** 2)
longitud= 2 * math.pi * radio
print("resultado round:",round(area,2))
print("resultado round:",round(longitud,2))
print("resultado roura:",round(area,2))
print("resultado roura:",round(longitud,2))
