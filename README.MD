Examen de evaluación para peopleOne

Se usa una arquitectura monolítica

Cómo instalar
Sobre un python2.7.x ejecutar pip -r [archivo requirements]
Para inicializar la aplicación se debe ejecutar primero dos comandos:
python manage.py createsuperuser --settings [settings que van a ocupar (default: desarrollo)]
python manage.py population_script --settings [settings que van a ocupar (default: desarrollo)]

en la url existe una url llamada /api
/api/users
/api/services
/api/areas
/api/items

se ha probado en un ubuntu de 64 bits
python 2.7.x
django 1.8.x


lista de pendientes y mejoras
hacer transaccional la operación de borrado
realizar las operaciones de cada api en el front