#9. programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas
variable1= float(input("introduce un número de segundos:"))
minutos=variable1/60
horas=variable1/3600
print ("el número de minutos es:", minutos,"y el número de horas es:",round(horas,2))