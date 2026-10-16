#el usuario introduzca un número por teclado del 1 al 5 pero el ordenador piens aun número al azar. saber si ha adivinado o ha fallado.
import random
aleatorio=random.randint(1,5)
numero=int(input("introduce un numero del 1 al 5:"))
if numero>=1 or numero<5:
    print("has introducido un valor incorrecto")

if aleatorio==numero: 
    print("has acertado")
else:
    print("has fallado")