"""30. Realiza un programa que controle si la longitud de una frase introducida por teclado es
igual, menor o mayor de 11 caracteres. Utiliza elif"""
Texto=input("introduce un texto:")
longitud_texto=len (Texto)
if longitud_texto==11:
    print("el texto tiene 11 carácteres")
elif longitud_texto>11:
    print("el texto tiene mas de 11 carácteres")
elif longitud_texto<11:
    print("el texto tiene menos de 11 carácteres")