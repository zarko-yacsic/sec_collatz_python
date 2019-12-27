
- Descripción del desarrollo : 

Se desarrolló una API (Usando Python 3.7 y el microframework Flask), la cual devolverá la secuencia Collatz de un número entero dado.

	Esta secuencia se calcula de la siguiente manera:
	- Si el número es par, se divide por dos
	- Si es impar se multiplica por 3, y se le suma 1
	- Seguir la secuencia hasta llegar a 1

	Ejemplo :
	- La secuencia de 6 sería : 6,3,10,5,16,8,4,2,1
	* * * * * * * * * 

	Validaciones :
	- Se valida que el input corresponda únicamente a un número entero, y que sea mayor a cero
	- Si no cumple, la API devuelve el respectivo mensaje de error.
	* * * * * * * * * 

	Formato salida :
	- Ejemplo 1 (Cuando el número es un entero válido) 
	salida = [
			{
				"status" : "OK",
				"valor_input" : 6,
				"secuencia_collatz" : [6,3,10,5,16,8,4,2,1]
			}
		]

	- Ejemplo 2 (Cuando el número no es un entero válido) 
	salida = [
			{
				"status" : "ERROR",
				"mensaje" : "Se debe ingresar un número entero válido."
			}
		]
	* * * * * * * * * 


- Módulos Python requeridos :
	- Flask
	- flask_restful
	- jsonify


- Pruebas del desarrollo :
Se generó un archivo llamado 'test_get.py' para ejecutar pruebas con la herramienta PYTEST.



- Reporte de Pruebas :
Se generó un archivo llamado 'reporte_test.xlsx' que describe cada una de las pruebas realizadas con PYTEST y sus resultados.








