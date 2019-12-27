import urllib.request
import json, sys, re


# Funcion principal :
# (Devuelve los valores de la secuencia Collatz, en un string, separados por coma)
def obtenerSecuenciaCollatz(valor = None):
	if valor == None:
		valor = input("Ingrese un número entero : ")
	valor = filtrarValor(valor);	
	url = "http://localhost:5000/secuencia_collatz/" + str(valor)
	respuesta = urllib.request.urlopen(url)
	data = json.loads(respuesta.read())	
	if data[0]["status"] == "OK":
		salida = ','.join(map(str, data[0]["secuencia_collatz"]))
	else:
		salida = data[0]["status"] + ": "  + data[0]['mensaje']
	return(salida)


# Función para filtrar valor a enviar :
def filtrarValor(valor):
	valor = str(valor)
	valor = valor.strip()
	valor = re.sub('[^a-zA-Z0-9]','-', valor)
	valor = re.sub('-{2,}', '-', valor)
	return valor.lower()

