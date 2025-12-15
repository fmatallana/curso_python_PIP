"""
con los venv se pueden aislar dependencias y modulos para cada proyecto

lo unico que hay global es la version de python

hay proyectos en los que la version de python es diferente y lo que hace docker es aislar todo, proyectos, dependencias y la version de python


USAR DOCKER

instalarlo y asegurarse que use wsl (viene por defecto)

crear un documento llamado Dockerfile en el modulo que se necesite

dentro de Dockerfile escribir

FROM python:3.12

esto le dice al contenedor que use esta version de python

WORKDIR /app para crear una carpeta dentro del contenedor

COPY requirements.txt /app/requirements.txt una buena practica es copiar el requirements en el contenedor, el archivo de la izquierda es el local y el de la derecha el que se creara en el contenedor 


instalar dependencias, no aplicar cache y hacer actualizaciones del gestos de paquetes con upgrade

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


COPIAR TODO EL CONTENIDO DEL MODULO 

COPY . /app (app es el nombre de la carpeta en local)

se crea un archivo docker-compose.yml

se crea para declarar como y desde donde se inicializa el contenedor

services:
 app-csv:
  build: lo que se le indica aca es, va a construir un servicio
    context: . desde la carpeta en la que se esta ubicado
    dockerfile: Dockerfile y en la carpeta que esta ubicado debe buscar el archivo Dockerfile

    
para que esto funcione el contenedor debe estar encendido y se hace de la siguiente manera

agregar esta linea en el dockerfile

CMD ["bash", "-c", "while true; do sleep 1; done"]

para que empiece a construir se debe correr este comando en terminal, dentro de la carpeta que se necesita

docker-compose build antes de ejecutar este comando docker debe estar abierto

docker-compose up -d con este comando se lanza el contenedor

docker-compose ps asi se ven los contenedores activos

ocker-compose exec app-csv bash asi se puede ingresar a desarrollar con el contenedor

  volumes:
  - .:/app

esto sirve para poder enlazar el sistema de archivos y el contenedor
"""