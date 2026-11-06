#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif. 
letra=input("introduce una letra:")
if letra.isalpha():
    if letra.isupper()==True:
        print("la letra es mayúscula")
    elif letra.isupper()==False:
        print("la letra es minúscula")
if letra.isnumeric()==True:
    print("el valor introducido es un numero")
if not letra.isalnum():
    print("el valor introducido es un simbolo")
else:
    print("la letra es mayúscula ¿? ")