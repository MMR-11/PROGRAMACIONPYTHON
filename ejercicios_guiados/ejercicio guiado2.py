#una tienda aplica el 10% de descuento a un producto y depués se le aplica el iva del 21%
precio=float(input("añade un precio de un producto:"))
descuento=precio-precio*10/100
precioiva=descuento+descuento*21/100
print(f"el producto con precio¨{precio}tiene un descuento de {descuento}y un total de {precioiva}")
print("el producto con precio",precio, "tiene un descuento de",descuento,"y un total de",precioiva)
preciototal=precio * (1-10/100) * (1+21/100)
print("nuevo resultado",round(preciototal,2))