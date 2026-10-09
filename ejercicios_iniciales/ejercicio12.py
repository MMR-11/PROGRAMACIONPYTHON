#12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayory altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
lado = float(input("Introduce el lado del trapecio: "))
base_menor = float(input("Introduce la base menor: "))
base_mayor = float(input("Introduce la base mayor: "))
altura = float(input("Introduce la altura: "))
area = (base_menor + base_mayor) * altura / 2
perimetro = 2 * lado + base_menor + base_mayor
print(f"El área del trapecio es: {area}")
print(f"El perímetro del trapecio es: {perimetro}")
