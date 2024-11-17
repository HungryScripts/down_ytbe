#!/usr/bin/env python3
#programa de codigo abierto 
#no me hago responsable del mal uso que se le de a esta herramienta

#use la libreria random para poder generar caracteres aleatorios en el script 
from random import randrange

#este es un pequeño aviso que deje por si no se entendia bien el uso del generador
print("AVISO \npara saber como utilizar correctamente este script debes de leer el archivo que tiene de nombre \'AYUDA\'")

#la clase llamada gen obtiene las entradas de datos que se coloquen y al final los coloca en una lista llamada list
class gen:
	var_1 = input("nombre $")
	var_2 = input("segundo nombre $")
	var_3 = input("tercer nombre $")
	var_4 = input("apellido $")
	var_5 = input("edad $")
	var_6 = input("pais $")
	var_7 = input("estado $")
	var_8 = input("numer de telefono $")
	list = [var_1,var_2,var_3,var_4,var_5,var_6,var_7,var_8]

#el print avisa y le pregunta al usuario si quiere continuar con la creacion del diccionario
print("los datos han sido procesados, si pulsa la tecla \'y\' se generara el diccionario de manera infinita asta que pare el proceso con ctrl + c")

#pregunta si el usuario quiere continuar y muestra las 2 opciones disponibles y lo guarda en una variable
camino = input("desea continuar? y/n $")

#este es if se ejecuta si en la variable camino esta el valor 'y'
if camino == "y":
	#bucle while que se ejecuta de manera infinita
	while True:
		#la variable list accede a la clase gen y luego a la lista y la guarda en la variable list
		list = gen.list
		#aqui se usa randrange para tomar un valor aleatorio de la lista ya mencionada
		op = randrange(len(list))
		op_2 = randrange(len(list))
		op_3 = randrange(len(list))
		op_4 = randrange(len(list))
		op_5 = randrange(len(list))
		op_6 = randrange(len(list))
		op_7 = randrange(len(list))
		op_8 = randrange(len(list))
		#no me acuerdo que hacian los [] :(
		unir = list[op]
		unir_2 = list[op_2]
		unir_3 = list[op_3]
		unir_4 = list[op_4]
		unir_5 = list[op_5]
		unir_6 = list[op_6]
		unir_7 = list[op_7]
		unir_8 = list[op_8]

		union = unir + unir_2 + unir_3 + unir_4 + unir_5 + unir_6 + unir_7 + unir_8

		print(union)
		diccionario = open("diccionario_de_contraseñas.txt", "a")
		diccionario.write(union)
		diccionario.close()
		diccionario = open("diccionario_de_contraseñas.txt", "a")
		diccionario.write(union)
		diccionario.close()
		diccionario = open("diccionario_de_contraseñas.txt", "a")
		diccionario.write(union)
		diccionario.close()
		diccionario = open("diccionario_de_contraseñas.txt", "a")
		diccionario.write(union)
		diccionario.close()
		diccionario.write(union)
		diccionario.close()
		diccionario = open("diccionario_de_contraseñas.txt", "a")
		diccionario.write(union)
		diccionario.close()