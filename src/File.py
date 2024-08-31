# version 1.1.0
import csv
import json
import os

from .constants import STRUCT


class File:
    def __init__(self, name) -> None:
        self.name = name
        if not self.exists():
            self.save_data(STRUCT)

    def exists(self):
        return os.path.exists(self.name)

    def delete(self):
        if os.path.exists(self.name):
            os.remove(self.name)
        else:
            return False

    def save_data(self, data):
        with open(self.name, "w") as file:
            json.dump(data, file, indent=4)

    def extract_data(self):
        with open(self.name) as file:
            data = json.load(file)
        return data

    def to_csv(self, data):

        # Escribir los datos de 'expenses' en un archivo CSV
        with open("expenses.csv", mode="w", newline="") as archivo_csv:
            # Obtener los nombres de las columnas
            columnas = data[0].keys()
            # Crear el escritor de CSV
            writer = csv.DictWriter(archivo_csv, fieldnames=columnas)

            # Escribir la cabecera
            writer.writeheader()
            # Escribir las filas
            writer.writerows(data)
