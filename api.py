from flask import Flask, jsonify
from flask_restful import Resource, Api


# Recursos de la API...
class SecuenciaCollatz(Resource):

	# GET para valor de entrada...
	def get(self, valor):
		valor = self.validarEntero(valor)
		if valor == False:
			salida = [
				{
					"status" : "ERROR",
					"mensaje" : "Se debe ingresar un número entero válido."
				}
			]
		else:
			if valor < 0:
				salida = [
					{
						"status" : "ERROR",
						"mensaje" : "Se debe ingresar un número entero mayor a cero."
					}
				]
			else:
				salida = self.obtenerSecuencia(valor)
		return jsonify(salida)



	# Validar que input sea un numéro entero...
	def validarEntero(self, numero):
		try:
			entero = int(numero)
			return entero
		except ValueError:
			return False



	# Obtener la secuencia Collatz del número ingresado...
	def obtenerSecuencia(self, numero):
		x = numero
		secuencia = [x]
		while secuencia[-1] > 1:
			if x % 2 == 0:
				n = int(x / 2)
				secuencia.append(n)
			else:
				n = int(3 * x + 1)
				secuencia.append(n)
			x = secuencia[-1]
		salida = [
			{
				"status" : "OK",
				"valor_input" : numero,
				"secuencia_collatz" : secuencia
			}
		]
		return salida


# Crear nueva instancia y agregar recurso GET...
app = Flask(__name__)
api = Api(app)
api.add_resource(SecuenciaCollatz, "/secuencia_collatz/<valor>")


if __name__ == '__main__':
	app.run(debug = True)


