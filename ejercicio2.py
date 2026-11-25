"""Una tienda online utiliza códigos para identificar sus productos. Estos códigos pueden
contener letras, números y guiones. Crea un programa que solicite al usuario un código de
producto."""
cod=input("introduce el código:")
codespa=cod.strip()
codmayus=cod.upper()
codminus=cod.lower()
codcarac=len(codespa)
codguines=cod.count("_")
codpala=codminus.find("tec")
codfinaliz=cod.endswith("25")
print("el código en mayúsculas es:",codmayus,)
print("el código en minúsculas es:",codminus,)
print("los carácteres del código són:",codcarac,)
print("los guiones del código son:",codguines,)
if codpala != -1:
    print("el código si que contiene tec")
else:
    print("el código no que contiene tec")
if codfinaliz==True:
    print("colección25: si ")
else:
    print("colección25: no")