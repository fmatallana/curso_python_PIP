"""
se importa requests en el directorio y entorno que se desee

se crea una variable como la de la linea 5 de store.py para  saber de donde queremos obtener informacion

se pueden imprimir los estados de las request con print(r.status.code)

se puede imprimir la informacion con print(r.text)


de esta forma se puede convertir un tipo string a una lista para poder iterarlo y ver los elementos por su llave

categories = r.json()
    for category in categories:
        print(category["name"])
"""