#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10
numero1=int(input("introduce un numero emtre el 0 y el 10:"))
numero2=int(input("introduce el segundo numero entre el 0 y el 10:"))
if str(numero1) in "1,2,3,4,5,6,7,8,9,10" or str(numero2) in "1,2,3,4,5,6,7,8,9,10":
    if numero1==numero2:
        print("los numeros que has introducido son iguales")
    else:
        if numero1<numero2:
            print("el número:",numero2,"es mas grande que el numero:",numero1)
        elif numero1>numero2:
            print("el número:",numero1,"es mas grande que el numero:",numero2)
else: print("el número que has introducido no esta dentro del rango")