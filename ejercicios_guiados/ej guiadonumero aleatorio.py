#el usuario introduzca un número por teclado del 1 al 5 pero el ordenador piens aun número al azar. saber si ha adivinado o ha fallado.
import random
aleatorio=random.randint(1,5)
numero=input("introduce un numero del 1 al 5:")
if numero in "12345":
    numero=int(numero)
        if numero>1 or numero<5:
             print("el valor no entra e el rango")
        else:
            #!= es que no es igual y si pones random w3 en google te sladran opciones para hacer un numero ramdom
            if aleatorio==numero:
                print("has acertado")
            else: print("has fallado")

