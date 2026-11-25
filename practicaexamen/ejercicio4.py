"""Un parque de atracciones ha creado una promoción especial. Cada visitante recibe un
número aleatorio que determina el tipo de premio que puede conseguir.
Crea un programa que realice el siguiente sorteo."""
import random
aleatorio=random.randint(1,100)
edad=(input("introduce tu edad"))
if not edad.isalpha():
    print("error")
elif int(edad)<=100 or int(edad)>=1:
    print("error")
else:
    if aleatorio >=1 or aleatorio<=10:
        print("premio especial, entrada gratuita")
    elif aleatorio >=11 or aleatorio<=30:
         print("premio de un descuento de 50%")
    elif aleatorio >=31 or aleatorio<=60:
            print("premio de un descuento de 20%")
    elif aleatorio >=61 or aleatorio<=100:
            print("no ha conseguido ningúun premio")