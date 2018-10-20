#coding=utf-8

import os
import sys
import sqlite3

def ingresar_cliente():
	os.system("cls")
	print "--------ingresar cliente----------"
	print " "

	var_dni = raw_input("ingrese dni: ")
	var_nombre = raw_input("ingrese nombre: ")
	var_pellido = raw_input("ingrese apellido: ")
	var_fec_nac = raw_input("ingrese fecha de nacimiento: ")
	var_direccion = raw_input("ingrese direccion: ")
	var_localidad = raw_input("ingrese localidad: ")
	var_telefono = raw_input("ingrese numero de telefono: ")
	var_telefono = int(var_telefono)


	con = sqlite3.connect("vaterinaria.db")

	sql = """INSERT INTO clientes(dni,nombre,apellido,fec_nac,direccion,localidad,telefono) 
	VALUES (var_dni,var_nombre,var_apellido,var_fec_nac,var_direccion,var_localidad,var_telefono)"""

	cursor = con.cursor()
	cursor.execute(sql)
	con.commit()
	con.close()

	print "su ingreso ha sido exitoso."
	print " "
	print "[m] volver al menu principal."
	print "[s] salir."

	opcion_cliente = raw_input("seleccione una opcion: ")

	if opcion_cliente == "m":
		menu_cliente()
	elif opcion_cliente == "s":
		sys.exit()

def consultar_cliente():
	os.system("cls")
	print "----------------consulta cliente----------------"
	print " "

	dni = raw_input("ingrese el dni: ")
	dni = int(dni)

	con = sqlite3.connect("vaterinaria.db")
	cursor = con.cursor()
	cursor.execute("SELECT * FROM clientes WHERE dni = +dni+ ")

	print "---------------\t\t-------------------"
	print "------------consulta: ----------------"
	print "---------------\t\t-------------------"

	for cliente in cursor:
		print cliente[0,1,2,3,4,5,6]
		print " "

	con.close()

	print "su consulta ha sido exitosa."
	print " "
	print "[m] volver al menu principal."
	print "[s] salir."

	opcion_cliente = raw_input("seleccione una opcion: ")

	if opcion_cliente == "m":
		menu_cliente()
	elif opcion_cliente == "s":
		sys.exit()

def modificar_cliente():
	dni = raw_input("ingrese el dni: ")
	dni = int(dni)

	con = sqlite3.connect("vaterinaria.db")
	cursor = con.cursor()
	cursor.execute("SELECT * FROM clientes WHERE dni = +dni+ ")

	for cliente in cursor:
		print cliente[0,1,2,3,4,5,6]
		print " "

	dni = raw_input("ingrese dni: ")
	dni = int(dni)
	nombre = raw_input("ingrese nombre: ")
	apellido = raw_input("ingrese apellido: ")
	fec_nac = raw_input("ingrese fecha de nacimiento: ")
	direccion = raw_input("ingrese direccion: ")
	localidad = raw_input("ingrese el peso: ")
	telefono = raw_input("ingrese numero de telefono: ")
	telefono = int(telefono)

	sql = "UPDATE clientes SET dni = +dni+ , nombre = +nombre+ , apellido = +apellido+ , fec_nac = +fec_nac+ , direccion = +direccion+ , localidad = +localidad+ , telefono = +telefono+ WHERE dni = +dni+ "

	cursor.execute(sql)
	con.commit()
	con.close()

	print "registro modificado exitosamente."
	print " "
	print "[m] volver al menu principal."
	print "[s] salir."

	opcion_cliente = raw_input("seleccione una opcion: ")

	if opcion_cliente == "m":
		menu_cliente()
	elif opcion_cliente == "s":
		sys.exit()


def eliminar_cliente():
	dni = raw_input("ingrese el dni: ")
	dni = int(dni)

	con = sqlite3.connect("vaterinaria.db")
	cursor = con.cursor()
	cursor.execute("SELECT * FROM clientes WHERE dni = +dni+ ")

	for cliente in cursor:
		print cliente[0,1,2,3,4,5,6]
		print " "

	sql = "DELETE FROM clientes WHERE dni = +dni+"

	cursor.execute(sql)
	con.commit()
	con.close()

	print "registro eliminado exitosamente."
	print " "
	print "[m] volver al menu principal."
	print "[s] salir."

	opcion_cliente = raw_input("seleccione una opcion: ")

	if opcion_cliente == "m":
		menu_cliente()
	elif opcion_cliente == "s":
		sys.exit()



def menu_cliente():
	os.system("cls")
	print "sitema de alta, baja, modificacion y consulta de pacientes"
	print " "
	print "[1] ingresar cliente"
	print "[2] eliminar cliente"
	print "[3] modificar cliente"
	print "[4] consulta cliente"
	print "[5] salir"
	print " "

	opcion_menu_cliente = raw_input("seleccione una opcion: ")
	opcion_menu_cliente = int(opcion_menu_cliente)
	if opcion_menu_cliente == 1:
		ingresar_cliente()
	elif opcion_menu_cliente == 2:
		eliminar_cliente()
	elif opcion_menu_cliente == 3:
		modificar_cliente()
	elif opcion_menu_cliente == 4:
		consultar_cliente()
	elif opcion_menu_cliente == 5:
		sys.exit()
	else:
		opcion_menu_cliente = raw_input("seleccione una opcion valida: ")
		menu_cliente()



def ingresar_paciente():
	os.system("cls")
	print "--------ingresar paciente----------"
	print " "

	nombre = raw_input("ingrese nombre del paciente: ")
	edad = raw_input("ingrese la edad: ")
	edad = int(edad)
	fec_nac = raw_input("ingrese fecha de nacimiento del paciente: ")
	raza = raw_input("ingrese la raza: ")
	peso = raw_input("ingrese el peso: ")
	dni_cliente = raw_input("ingrese el dni del dueño: ")
	observaciones = raw_input("reservado para reporte medico: ")

	con = sqlite3.connect("vaterinaria.db")
	cursor = con.cursor()
	cursor.execute("INSERT INTO pacientes(nombre,edad,fec_nac,raza,peso,dni_cliente,observaciones) value ('"+nombre+"' , '"+edad+"' , '"+fec_nac+"' , '"+raza+"' , '"+peso+"' , '"+dni_cliente+"' , '"+observaciones+"')")
	con.commit()
	con.close()

	print "su ingreso ha sido exitoso."
	print " "
	print "[m] volver al menu principal."
	print "[s] salir."

	opcion_paciente = raw_input("seleccione una opcion: ")

	if opcion_paciente == "m":
		menu_paciente()
	elif opcion_paciente == "s":
		sys.exit()

def consultar_paciente():
	os.system("cls")
	print "----------------consulta paciente----------------"
	print " "

	id_paciente = raw_input("ingrese el id del paciente: ")
	id_paciente = int(id_paciente)

	con = sqlite3.connect("vaterinaria.db")
	cursor = con.cursor()
	cursor.execute("SELECT * FROM pacientes WHERE id_paciente = +id_paciente+ ")

	print "---------------\t\t-------------------"
	print "------------consulta: ----------------"
	print "---------------\t\t-------------------"

	for paciente in cursor:
		print pacientes[0,1,2,3,4,5,6,7]
		print " "

	con.close()

	print "su consulta ha sido exitosa."
	print " "
	print "[m] volver al menu principal."
	print "[s] salir."

	opcion_paciente = raw_input("seleccione una opcion: ")

	if opcion_paciente == "m":
		menu_paciente()
	elif opcion_paciente == "s":
		sys.exit()

def modificar_paciente():
	id_paciente = raw_input("ingrese el id del paciente: ")
	id_paciente = int(id_paciente)

	con = sqlite3.connect("vaterinaria.db")
	cursor = con.cursor()
	cursor.execute("SELECT * FROM pacientes WHERE id_paciente = +id_paciente+ ")

	for paciente in cursor:
		print paciente[1,2,3,4,5,6,7]
		print " "

	nombre = raw_input("ingrese nombre del paciente: ")
	edad = raw_input("ingrese la edad: ")
	edad = int(edad)
	fec_nac = raw_input("ingrese fecha de nacimiento del paciente: ")
	raza = raw_input("ingrese la raza: ")
	peso = raw_input("ingrese el peso: ")
	dni_cliente = raw_input("ingrese el dni del dueño: ")
	observaciones = raw_input("reservado para reporte medico: ")

	sql = "UPDATE pacientes SET nombre= +nombre+ , edad = +edad+ , fec_nac= +fec_nac+ , raza= +raza+ , peso= +peso+ , dni_cliente= +dni_cliente+ , observaciones= +observaciones+ WHERE id_paciente= +id_paciente+ "

	cursor.execute(sql)
	con.commit()
	con.close()

	print "registro modificado exitosamente."
	print " "
	print "[m] volver al menu principal."
	print "[s] salir."

	opcion_paciente = raw_input("seleccione una opcion: ")

	if opcion_paciente == "m":
		menu_paciente()
	elif opcion_paciente == "s":
		sys.exit()


def eliminar_paciente():
	id_paciente = raw_input("ingrese el id del paciente: ")
	id_paciente = int(id_paciente)

	con = sqlite3.connect("vaterinaria.db")
	cursor = con.cursor()
	cursor.execute("SELECT * FROM pacientes WHERE id_paciente = +id_paciente+ ")

	for paciente in cursor:
		print paciente[1,2,3,4,5,6,7]
		print " "

	sql = "DELETE FROM pacientes WHERE id_paciente= +id_paciente+"

	cursor.execute(sql)
	con.commit()
	con.close()

	print "registro eliminado exitosamente."
	print " "
	print "[m] volver al menu principal."
	print "[s] salir."

	opcion_paciente = raw_input("seleccione una opcion: ")

	if opcion_paciente == "m":
		menu_paciente()
	elif opcion_paciente == "s":
		sys.exit()



def menu_paciente():
	os.system("cls")
	print "sitema de alta, baja, modificacion y consulta de pacientes"
	print " "
	print "[1] ingresar paciente"
	print "[2] eliminar paciente"
	print "[3] modificar paciente"
	print "[4] consulta paciente"
	print "[5] salir"
	print " "

	opcion_menu_paciente = raw_input("seleccione una opcion: ")
	opcion_menu_paciente = int(opcion_menu_paciente)
	if opcion_menu_paciente == 1:
		ingresar_paciente()
	elif opcion_menu_paciente == 2:
		eliminar_paciente()
	elif opcion_menu_paciente == 3:
		modificar_paciente()
	elif opcion_menu_paciente == 4:
		consultar_paciente()
	elif opcion_menu_paciente == 5:
		sys.exit()
	else:
		opcion_menu_paciente = raw_input("seleccione una opcion valida: ")
		menu_paciente(opcion_menu_paciente)



def menu_principal():
	os.system("cls")
	print "----------------------------- MENU PRINCIPAL --------------------------------"
	print " "
	print "Bienvenido al sistema general de 'animales sueltos' veterinaria"
	print " "
	print "[1] Clientes"
	print "[2] Pacientes"
	print "[3] Facturacion"
	print "[4] salir"
	print " "

	opcion_menu_principal = raw_input("seleccione una opcion: ")
	opcion_menu_principal = int(opcion_menu_principal)
	if opcion_menu_principal == 1:
		menu_cliente()
	elif opcion_menu_principal == 2:
		menu_paciente()
	#elif opcion_menu_cliente == 3:
	#	menu_facturacion()
	elif opcion_menu_principal == 4:
		sys.exit()
	else:
		print "seleccione una opcion valida: "	
		menu_principal()

menu_principal()