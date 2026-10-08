#print"5. Programa que pida cinco palabras y muestre una frase con las cinco. Modifica el código para que entre palabra y palabra haya una coma."
variable1= (input("introduce una palabra para formar una frase:"))
variable2= (input("introduce una palabra:"))
variable3= (input("introduce una palabra:"))
variable4= (input("introduce una palabra:"))
variable5= (input("introduce una palabra:"))
print("la frase sin comas es:", variable1+variable2+variable3+variable4+variable5)
resultado= ",".join(variable1+variable2+variable3+variable4+variable5)
print("la frase que has creado con comas es:", resultado)

print(variable1+","+)