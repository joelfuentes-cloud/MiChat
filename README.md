# Chat Dockerizado con Python y Redis

Este proyecto es una aplicación de chat mediante contenedores. Utiliza un servidor web y una base de datos en memoria para gestionar los mensajes,
es una aplicación de chat construida bajo una arquitectura de microservicios utilizando contenedores Docker, la aplicación permite conectarse a una interfaz web, 
y compartir mensajes instantáneos.

## 🛠️ Tecnologías utilizadas

* **Python 3.11**: Lógica del servidor y API.
* **Flask**: Framework web para la interfaz y el manejo de rutas.
* **Redis**: Base de datos NoSQL para el almacenamiento rápido de mensajes.
* **Docker & Docker Compose**: Para la orquestación y despliegue de los servicios.

## Características

* **Historial en tiempo real**: Los mensajes se guardan en Redis y se actualizan automáticamente cada 2 segundos.
* **Persistencia**: Gracias a los volúmenes de Docker, los mensajes no se pierden aunque detengas los contenedores.

## Instalación y Despliegue

Para ejecutar este proyecto, solo necesitas tener instalado [Docker Desktop](https://www.docker.com/products/docker-desktop/).

1.  **Clona este repositorio** o descarga los archivos `app.py`, `Dockerfile` y `docker-compose.yml`.
2.  **Abre una terminal** en la carpeta del proyecto.
3.  **Lanza la aplicación** con el siguiente comando: docker-compose up -d
4. **Habre tu navegador** y pon http://localhost:5000
```bash
