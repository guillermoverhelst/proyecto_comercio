# proyecto_comercio

* Si es la primera vez, ejecuta el comando 'python manage.py migrate' en la carpeta raiz del proyecto (.../tienda_enfasis_r/proyecto_comercio)

* Carpeta settings configurada para cualquier equipo

* Siempre que bajes los cambios genera tu nueva 'secret key' de la siguiente manera:

Nota: Desde la consola del IDE

1)navegar hasta la ruta: ".../tienda_enfasis_r/proyecto_comercio"

2)Ejecuta el comando: "python manage.py shell"

3)En la consola de python escribe y ejecuta:
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())

4)Copiar la secret key y pegarla en el archivo settings.py que esta en la ruta: ".../tienda_enfasis_r/proyecto_comercio/aplicación_comercio/" y guardar el archivo

NOTA: MUY IMPORTANTE BORRAR LA SECRET KEY ANTES DE HACER UN PUSH.