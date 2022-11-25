from setuptools import setup

setup (
    name = "paquete_calcalculos",
    version = "1.0",
    description = "breve explicación de las funciones del paquete",
    author= "nombre del autor",
    packages=["calculos","calculos.calculos_generales"] # ruta donde se encuentra el paquete que queremos distribuir
    # resto de datos no obligatorios
    author_email= "correo del autor",
    url="web de referencia",
)