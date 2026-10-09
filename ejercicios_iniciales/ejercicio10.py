#10. Introduce por teclado dos números y muestre por pantalla la siguiente información:cociente, resto y si el dividendo es par o impar
dividendo=float(input("introduce el número dividendo:"))
divisor=float(input("introduce el número divisor:"))
cociente=dividendo//divisor
resto=dividendo%divisor
if dividendo%2==0: dividendo= print("dividendo es par")
else :dividendo= print("dividendo es impar")
print("el cociente de estos números es:", cociente)