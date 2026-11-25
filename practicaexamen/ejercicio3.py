"""Una empresa de alquiler de bicicletas quiere comprobar si un cliente puede alquilar una
bicicleta eléctrica."""
edad=int(input("introduce tu edad:"))
carnet=input("¿dispones de carnet de conducir?responde con si o no")
tarjeta=input("¿tienes tarjeta de socio de la empresa? responde con si o no")
carnets=carnet.strip
tarjetas=tarjeta.strip
if edad<18:
    print("no puede alquilar la bicicleta: edad insuficiente")
if carnets=="no" and tarjetas=="no":
    print("No puede alquilar: no cumple los requisitos adicionales")
if edad >=18 and (carnets=="si" or tarjetas=="si"):
    print("puedes alquilar la bicicleta")

    