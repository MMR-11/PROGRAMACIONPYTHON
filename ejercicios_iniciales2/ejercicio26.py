"""26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si
está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición."""
letra=input("introduce una letra:")
if letra.isalpha():
    if letra.isupper():
        print("la letra es mayúscula")
    elif not letra.isupper():
        print("la letra es minúscula")
else:
    print("la letra es mayúscula ¿?")