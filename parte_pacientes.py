#coding=utf-8

import os
import sys
import sqlite3

def ingresar_paciente():
	os.system("cls")
	print ("--------ingresar paciente----------")
	print (" ")

	nombre = raw_input("ingrese nombre del paciente: ")
	edad = raw_input("ingrese la edad: ")
	edad = int(edad)
	fec_nac = raw_input("ingrese fecha de nacimiento del paciente: ")
	raza = raw_input("ingrese la raza: ")
	peso = raw_input("ingrese el peso: ")
	dni_cliente = raw_input("ingrese el dni del dueño: ")
	observaciones = raw_input("reservado para reporte medico: ")

	con = sqlite3.connect("pacientes.s3db")
	cursor = con.cursor()
	cursor.execute("INSERT INTO pacientes(nombre,edad,fec_nac,raza,peso,dni_cliente,observaciones) value ('"+nombre+"' , '"+edad+"' , '"+fec_nac+"' , '"+raza+"' , '"+peso+"' , '"+dni_cliente+"' , '"+observaciones+"')")
	con.commit()
	con.close()

	print ("su ingreso ha sido exitoso.")
	print (" ")
	print ("[m] volver al menu principal.")
	print ("[s] salir.")

	opcion_paciente = raw_input("seleccione una opcion: ")

	if opcion_paciente == "m":
		menu_paciente()
	elif opcion_paciente == "s":
		sys.exit()

def consultar_paciente():
	os.system("cls")
	print ("----------------consulta paciente----------------")
	print (" ")

	id_paciente = raw_input("ingrese el id del paciente: ")
	id_paciente = int(id_paciente)

	con = sqlite3.connect("pacientes.s3db")
	cursor = con.cursor()
	cursor.execute("SELECT * FROM pacientes WHERE id_paciente = +id_paciente+ ")

	print ("---------------\t\t-------------------")
	print ("------------consulta: ----------------")
	print ("---------------\t\t-------------------")

	for paciente in cursor:
		print (pacientes[0,1,2,3,4,5,6,7])
		print (" ")

	con.close()

	print ("su consulta ha sido exitosa.")
	print (" ")
	print ("[m] volver al menu principal.")
	print ("[s] salir.")

	opcion_paciente = raw_input("seleccione una opcion: ")

	if opcion_paciente == "m":
		menu_paciente()
	elif opcion_paciente == "s":
		sys.exit()

def modificar_paciente():
	id_paciente = raw_input("ingrese el id del paciente: ")
	id_paciente = int(id_paciente)

	con = sqlite3.connect("pacientes.s3db")
	cursor = con.cursor()
	cursor.execute("SELECT * FROM pacientes WHERE id_paciente = +id_paciente+ ")

	for paciente in cursor:
		print (paciente[1,2,3,4,5,6,7])
		print (" ")

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

	print ("registro modificado exitosamente.")
	print (" ")
	print ("[m] volver al menu principal.")
	print ("[s] salir.")

	opcion_paciente = raw_input("seleccione una opcion: ")

	if opcion_paciente == "m":
		menu_paciente()
	elif opcion_paciente == "s":
		sys.exit()


def eliminar_paciente():
	id_paciente = raw_input("ingrese el id del paciente: ")
	id_paciente = int(id_paciente)

	con = sqlite3.connect("pacientes.s3db")
	cursor = con.cursor()
	cursor.execute("SELECT * FROM pacientes WHERE id_paciente = +id_paciente+ ")

	for paciente in cursor:
		print (paciente[1,2,3,4,5,6,7])
		print (" ")

	sql = "DELETE FROM pacientes WHERE id_paciente= +id_paciente+"

	cursor.execute(sql)
	con.commit()
	con.close()

	print ("registro eliminado exitosamente.")
	print (" ")
	print ("[m] volver al menu principal.")
	print ("[s] salir.")

	opcion_paciente = raw_input("seleccione una opcion: ")

	if opcion_paciente == "m":
		menu_paciente()
	elif opcion_paciente == "s":
		sys.exit()



def menu_paciente():
	os.system("cls")
	print ("sitema de alta, baja, modificacion y consulta de pacientes")
	print (" ")
	print ("[1] ingresar paciente")
	print ("[2] eliminar paciente")
	print ("[3] modificar paciente")
	print ("[4] consulta paciente")
	print ("[5] salir")
	print (" ")

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

menu_paciente()