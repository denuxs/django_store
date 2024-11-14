# Django Fake Store API

Simple API REST para tienda online (En desarrollo)

API Doc: https://denlop.pythonanywhere.com/swagger

Frontend: https://amazing-crumble-40f260.netlify.app

* username: admin@localhost.com
* password: endurance

### Features

* Categorias
* Productos
* Usuarios
* Autenticación JWT

### Paquetes

* Python 3+
* Django 5
* Django Rest Framework
* Simple JWT
* Sqlite
* Swagger

### Instalar

Crear un entorno virtual con virtualenv e instalar paquetes

```
virtualenv venv
source venv/bin/activate

pip install -r requirements.txt
```

### Ejecutar la app

```
python manage.py migrate
python manage.py runserver
```

### TO DO

* bugfix api swagger register
* Unit testing