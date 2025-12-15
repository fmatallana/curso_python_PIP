"""
1. se instala fast api con pip3
2. se instala uvicorn con el siguiente comando pip3 install "uvicorn["standard"]
3. actualizar el requirements
4. se importa fastapi from fastapi import FastAPI
5. @app.get('/')
def get_list():
    return [1,2,3,4,5,6]

con el decorador "@app.get" se le dice en que parte del server retorne esto

6.lanzar el server con uvicorn

uvicorn main(en esa parte va el nombre del archivo de ejecucion):app(hace referencia al nombre de la variable en la que se agrego fastapi en el archivo main) --reload (esto significa que si se hace un cambio se recargara siempre)

7. DEVOLVER HTML
from fastapi.responses import HTMLResponse


@app.get('/contact', response_class = HTMLResponse)
def get_list():
    return """
<h1> Hola soy una pagina</h1>
<p> soy un parrafo </p>
"""


"""