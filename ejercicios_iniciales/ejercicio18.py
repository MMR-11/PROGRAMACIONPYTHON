#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.
adultos=(input("introduce el número de adultos que asistirán;"))
menores=(input("introduce el número de menores que asistirán;"))
entrada_de_menores=menores+12*50/100
entrada_de_adultos=adultos+12*10/100
print("el precio a pagar de adulto es de:",entrada_de_adultos)
print("el precio a pagar de menores es de:",entrada_de_menores)