"""27. Mejora el programa anterior para controlar que el valor introducido es una letra y en
caso de introducir un número, aparezca un aviso por pantalla"""
letra=input("introduce una letra:")
if letra.isalpha():
    if letra.isupper()==True:
        print("la letra es mayúscula")
    elif letra.isupper()==False:
        print("la letra es minúscula")
if letra.isnumeric()==True:
    print("el valor introducido es un numero")
else:
    print("la letra es mayúscula ¿? ")