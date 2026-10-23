#19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son  iguales
#and=y or= o in= un numero dentro de los numeros que pongas ej: 12345 y para que me lea los numero por separado he de poner en la siguiente linea int.
numero1=int(input("introduce el primer numero:"))
numero2=int(input("introduce el segundo numero:"))
if numero1==numero2:
    print("los numeros que has introducido son iguales")
else:
    if numero1<numero2:
        print("el número:",numero2,"es mas grande que el numero:",numero1)
    else:
        print("el número:",numero1,"es mas grande que el numero:",numero2)