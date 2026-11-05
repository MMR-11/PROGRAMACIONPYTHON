#22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
nota=float(input("introduce un número:"))
if nota in (1,2,3,4,5,6,7,8,9,10):
    if nota<5:
        print("has sacado un",nota,"y has supendido")
    else:
        print("has sacado un",nota,"y has aprovado")
else: print("la nota que has introducido no está dentro de 0 y 10")