import numpy as np
import json
import pandas as pd
from openpyxl import Workbook
from pathlib import Path

class DataGenerator:
    """
    Clase para generar, leer y escribir datos en formatos JSON, TXT y XLSX
    """

    def __init__(self):
        pass

    def _validar_limites(self, inferior, superior):
        if not (isinstance(inferior, (int, float)) and isinstance(superior, (int, float))):
            raise ValueError("Los límites deben ser numéricos (int o float).")
        if inferior >= superior:
            raise ValueError("El límite inferior debe ser menor que el límite superior.")

    def generar_datos_completos(self, n, categorias, x=4, limite_inferior=1, limite_superior=100):
        self._validar_limites(limite_inferior, limite_superior)

        columna_categorica = np.random.choice(categorias, size=n)
        columna_enteros = np.random.randint(int(limite_inferior), int(limite_superior), size=n)
        columna_decimales = np.random.uniform(0, 1, size=n)
        columna_reales = np.random.normal(0, 1, size=n)

        columnas = [columna_categorica, columna_enteros, columna_decimales, columna_reales]
        nombres = ["categoria", "enteros", "decimal", "reales"]

        data = np.column_stack(columnas[:x])
        self.column_names = nombres[:x]
        return data

    def escribir_datos(self, data, tipo='json', ruta='datos_salida'):
        Path(ruta).parent.mkdir(parents=True, exist_ok=True)
        if tipo == 'json':
            with open(f"{ruta}.json", 'w') as f:
                json.dump(data.tolist(), f)
        elif tipo == 'txt':
            np.savetxt(f"{ruta}.txt", data, fmt='%s')
        elif tipo == 'xlsx':
            columnas = getattr(self, 'column_names', [f"col_{i}" for i in range(data.shape[1])])
            df = pd.DataFrame(data, columns=columnas)
            df.to_excel(f"{ruta}.xlsx", index=False)

    def leer_datos(self, tipo='json', ruta='datos_salida'):
        if tipo == 'json':
            with open(f"{ruta}.json", 'r') as f:
                return np.array(json.load(f))
        elif tipo == 'txt':
            return np.loadtxt(f"{ruta}.txt", dtype=str)
        elif tipo == 'xlsx':
            df = pd.read_excel(f"{ruta}.xlsx")
            return df.to_numpy()