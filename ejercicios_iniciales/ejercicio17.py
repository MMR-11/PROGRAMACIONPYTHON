#17. Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.
peso=float(input("introduce el peso en kilogramos:"))
estatura=float(input("introduce tu estatura en metros:"))
imc=peso//(estatura**2)
print("si pesas",peso,"y mides",estatura,"su imc es de:",(round)(imc,2))
if imc>25: print("usted tiene sobrepeso")
