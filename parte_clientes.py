#coding=utf-8

import os
import sys
import sqlite3

def ingresar_cliente():
	os.system("cls")
	print ("--------ingresar cliente----------")
	print (" ")

	var_dni = input("ingrese dni: ")
	var_nombre = input("ingrese nombre: ")
	var_apellido = input("ingrese apellido: ")
	var_fec_nac = input("ingrese fecha de nacimiento: ")
	var_direccion = input("ingrese direccion: ")
	var_localidad = input("ingrese localidad: ")
	var_telefono = input("ingrese numero de telefono: ")
	var_telefono = int(var_telefono)


	con = sqlite3.connect("C:\\UTILES\\codigopython\\vaterinaria.db")

	sql = 'INSERT INTO clientes(dni,nombre,apellido,fec_nac,direccion,localidad,telefono) VALUES ('+str(var_dni)+',"'+str(var_nombre)+ '","'+str(var_apellido)+'","'+str(var_fec_nac)+'","'+str(var_direccion)+'","'+str(var_localidad)+'",'+str(var_telefono)+')'

	cursor = con.cursor()
	cursor.execute(sql)
	con.commit()
	con.close()

	print ("su ingreso ha sido exitoso.")
	print (" ")
	print ("[m] volver al menu principal.")
	print ("[s] salir.")

	opcion_cliente = input("seleccione una opcion: ")

	if opcion_cliente == "m":
		menu_cliente()
	elif opcion_cliente == "s":
		sys.exit()

def consultar_cliente():
	os.system("cls")
	print ("----------------consulta cliente----------------")
	print (" ")

	dni = input("ingrese el dni: ")
	dni = int(dni)

	con = sqlite3.connect("C:\\UTILES\\codigopython\\vaterinaria.db")
	cursor = con.cursor()
	cursor.execute("SELECT * FROM clientes WHERE dni="+ str(dni))

	print ("------------consulta: ----------------")

	for cliente in cursor:
		print ("Nombre:" + str(cliente[1]))
		print ("Apellido:" + str(cliente[2]))
		print ("Fecha de Nacimiento:" + str(cliente[3]))
		print ("Direccion:" + str(cliente[4]))
		print ("Localidad:" + str(cliente[5]))
		print ("Telefono:" + str(cliente[6]))
		print (" ")

	con.close()

	print ("su consulta ha sido exitosa.")
	print (" ")
	print ("[m] volver al menu principal.")
	print ("[s] salir.")

	opcion_cliente = input("seleccione una opcion: ")

	if opcion_cliente == "m":
		menu_cliente()
	elif opcion_cliente == "s":
		sys.exit()

def modificar_cliente():
	dni = input("ingrese el dni: ")
	dni = int(dni)

	con = sqlite3.connect("C:\\UTILES\\codigopython\\vaterinaria.db")
	cursor = con.cursor()
	cursor.execute("SELECT * FROM clientes WHERE dni=" +str(dni))

#	for cliente in cursor:
#		print (cliente[0,1,2,3,4,5,6])
#		print (" ")

#	dni = input("ingrese dni: ")
#	dni = int(dni)
	nombre = input("ingrese nombre: ")
	apellido = input("ingrese apellido: ")
	fec_nac = input("ingrese fecha de nacimiento: ")
	direccion = input("ingrese direccion: ")
	localidad = input("ingrese el peso: ")
	telefono = input("ingrese numero de telefono: ")
	telefono = int(telefono)

	sql = "UPDATE clientes SET dni = "+str(dni)+" , nombre= "+str(nombre)+ ", apellido ="+str(apellido)+" , fec_nac ="+str(fec_nac)+" , direccion ="+str(direccion)+" , localidad ="+str(localidad)+" , telefono ="+str(telefono)+ " WHERE dni="+str(dni)

	cursor.execute(sql)
	con.commit()
	con.close()

	print ("registro modificado exitosamente.")
	print (" ")
	print ("[m] volver al menu principal.")
	print ("[s] salir.")

	opcion_cliente = input("seleccione una opcion: ")

	if opcion_cliente == "m":
		menu_cliente()
	elif opcion_cliente == "s":
		sys.exit()


def eliminar_cliente():
	dni = input("ingrese el dni: ")
	dni = int(dni)

	con = sqlite3.connect("C:\\UTILES\\codigopython\\vaterinaria.db")
	cursor = con.cursor()
	cursor.execute('SELECT * FROM clientes WHERE dni='+str(dni))

#	for cliente in cursor:
#		print (cliente[0,1,2,3,4,5,6])
#		print (" ")

	sql = "DELETE FROM clientes WHERE dni="+str(dni)

	cursor.execute(sql)
	con.commit()
	con.close()

	print ("registro eliminado exitosamente.")
	print (" ")
	print ("[m] volver al menu principal.")
	print ("[s] salir.")

	opcion_cliente = input("seleccione una opcion: ")

	if opcion_cliente == "m":
		menu_cliente()
	elif opcion_cliente == "s":
		sys.exit()



def menu_cliente():
	os.system("cls")
	print ("sitema de alta, baja, modificacion y consulta de pacientes")
	print (" ")
	print ("[1] ingresar cliente")
	print ("[2] eliminar cliente")
	print ("[3] modificar cliente")
	print ("[4] consulta cliente")
	print ("[5] salir")
	print (" ")

	opcion_menu_cliente = input("seleccione una opcion: ")
	#opcion_menu_cliente = int(opcion_menu_cliente)
	if opcion_menu_cliente == "1":
		ingresar_cliente()
	elif opcion_menu_cliente == "2":
		eliminar_cliente()
	elif opcion_menu_cliente == "3":
		modificar_cliente()
	elif opcion_menu_cliente == "4":
		consultar_cliente()
	elif opcion_menu_cliente == "5":
		sys.exit()
	else:
		opcion_menu_cliente = input("seleccione una opcion valida: ")
		menu_cliente()

def menu_principal():
	os.system("cls")
	print ("----------------------------- MENU PRINCIPAL --------------------------------")
	print (" ")
	print ("Bienvenido al sistema general de 'animales sueltos' veterinaria")
	print (" ")
	print ("[1] Clientes")
	print ("[2] Pacientes")
	print ("[3] Facturacion")
	print ("[4] salir")
	print (" ")

	opcion_menu_principal = input("seleccione una opcion: ")
	#opcion_menu_principal = str(opcion_menu_principal)
	if opcion_menu_principal == "1":
		menu_cliente()
	elif opcion_menu_principal == "2":
		#eliminar_cliente()
		print ("######## Deberia mostrar el menu de pacientes ######## ")
	elif opcion_menu_principal == "3":
		#modificar_cliente()
		print ("######## Deberia mostrar el menu de facturacion ######## ")
	elif opcion_menu_principal == "4":
		#consultar_cliente()
		sys.exit()
	else:
		opcion_menu_principal = input("seleccione una opcion valida: ")
		menu_cliente()


menu_principal()




















