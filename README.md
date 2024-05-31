pasos para la reproduccion:
1. crear la base de con el nombre "myproject"
2. ir a la carpeta sap y en settings buscar DATABASE y cambiar la credenciales de coneccion por la de su base de datos.
3. dentro de carpeta sap hacer el "makemigrations" para crear archivos de migración del modelo, esto se realiza con el siguiente comando: python manage.py makemigrations.
4. ahora realizar el "migrate" que se usa para migrar todo los pendientes a la base de datos y se actualizen o creen las tablas necesarias para el proyecto, esto se realiza con el siguiente comando: python manage.py migrate.
5. por ulimo crear un superusuario en django para poder entrar al apartado administrable de la web, este usuario se crea con el siguiente comando: python manage.py createsuperuser, una vez corrido este comando le da un usuario y una contraseña.
6. ya puede visualizar el proyecto ejecutando el siguiente comando: python manage.py runserver.
