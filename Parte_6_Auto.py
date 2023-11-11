import requests
import csv
import sys

print('url',sys.argv[1])

url = sys.argv[1]

def descargar_datos(url):
  respuesta = requests.get(url)
  nombre_archivo = url.split("/")[-1]
  with open(nombre_archivo, "w") as archivo:
    escritor = csv.writer(archivo)
    contenido = respuesta.content.decode("utf-8")
    lista = contenido.splitlines()
    for linea in lista:
      escritor.writerow(linea.split(","))
  return nombre_archivo