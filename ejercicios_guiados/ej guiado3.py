txt= "i love apples, apples are my favourite fruite"
"""contador=txt.count ("apples")
print(contador)"""
"""txt= "i love apples, apples are my favourite fruite"
indice=txt.find ("apples")
print(indice)"""
"""minusculas= txt.lower()
print(minusculas)
print(minusculas.count("apples"))"""
respuesta=input("introduce una letra:")
if respuesta.isumeric()==False:
    if respuesta.isupper()==True:
        print("es mayúscula")
    else:
        print("es minuscula")
else:
    print("el valor introducido no es una letra")
"""lower= para poner todo en minusculas y isupper para todo mayusculas,
d isumeric para numeros y isalpha es para letras"""