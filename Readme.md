# Proyecto Manejador de Horarios

Este proyecto es una aplicación web creada con Django para gestionar horarios de clases en un entorno educativo. Los usuarios pueden crear ciclos, aulas, cursos y asignar cursos a aulas para organizar los horarios.

## Requisitos

Antes de comenzar, asegúrate de tener los siguientes requisitos instalados:

- **Python 3.10 o superior**  
  - **En Windows**: Descárgalo desde [python.org](https://www.python.org/downloads/) e instálalo. Asegúrate de marcar la opción "Add Python to PATH" durante la instalación.
  - **En Linux**: Usa el siguiente comando:
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```

- **Django 4.x**
  - **Instalar en ambos sistemas** (Windows/Linux) dentro de un entorno virtual:
    ```bash
    pip install django
    ```

- **PostgreSQL** (o el gestor de base de datos que prefieras)  
  - **En Windows**: Descarga e instala PostgreSQL desde [postgresql.org](https://www.postgresql.org/download/windows/).
  - **En Linux**: Usa el siguiente comando:
    ```bash
    sudo apt update
    sudo apt install postgresql postgresql-contrib
    ```

## Instalación

1. **Clona este repositorio**:
   
   Abre una terminal y ejecuta los siguientes comandos para clonar el repositorio y acceder al directorio del proyecto:
   ```bash
   git clone <repositorio-url>
   cd <nombre-del-repositorio>

2. **Crea un entorno virtual**:   
    - ## En Linux o macOS:
    python3 -m venv env
    source env/bin/activate

    - ## En Windows:
    python -m venv env
    .\env\Scripts\activate
    
3. **Instala las dependencias**:       
    pip install -r requirements.txt

3. **Configura la base de datos**: 
    psql -U postgres
    CREATE DATABASE parcial_fundamentos;
    
    - ## En el archivo settings.py:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'parcial_fundamentos',
            'USER': 'nombre_de_usuario',
            'PASSWORD': 'tu_contraseña',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

    python manage.py migrate
    

4. **Crear usuario admin**:
    python manage.py createsuperuser
    ## Seguir las instrucciones

5. **Correr el proyecto**:
    python manage.py runserver