"""Una empresa de mensajería necesita calcular la distancia entre dos puntos de un mapa
para organizar sus entregas.
Crea un programa que solicite al usuario las coordenadas de dos puntos:"""
import math 
coordenada1x=float(input("introduce la cordenada x del primer numero:"))
coordenada1y=float(input("introduce la cordenada y del segundo numero:"))
coordenada2x=float(input("introduce la cordenada x del primer numero:"))
coordenada2y=float(input("introduce la cordenada y del segundo numero:"))
distancia_de_cordenadas= math.sqrt((coordenada2x - coordenada1x)**2 + (coordenada2y - coordenada1y)**2)
print("la distancia de los dos puntos del mapa es:",distancia_de_cordenadas)