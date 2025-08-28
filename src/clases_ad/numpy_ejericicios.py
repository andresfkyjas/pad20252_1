import numpy as np
import json
import pandas as pd
from openpyxl import Workbook
from pathlib import Path

class NumpyEjercicios:
    """
    Clase para aplicar ejercicios con NumPy, incluyendo validación, trazabilidad de entrada/salida
    y ejemplos agrupados por categoría funcional.
    """

    def _validar_datos(self, datos):
        if datos is None:
            raise ValueError("Los datos no pueden ser None")
        if not isinstance(datos, np.ndarray):
            raise TypeError("Los datos deben ser un array de NumPy")

    def _mostrar_entrada_salida(self, entrada, salida):
        print("\n📥 Entrada:\n", entrada)
        print("📤 Salida:\n", salida)
        print("📐 Tipo:", type(salida), "| Forma:", getattr(salida, 'shape', 'escalar'))
        return salida
    
    # Initial Placeholders
    def placeholder_zeros(self, x=0,y=0):
        return self._mostrar_entrada_salida("np.zeros(({},{}))".format(x,y), np.zeros((x, y)))

    def placeholder_ones(self):
        return self._mostrar_entrada_salida("np.ones((2,4))", np.ones((2, 4)))

    def placeholder_full(self):
        return self._mostrar_entrada_salida("np.full((3,3),7)", np.full((3, 3), 7))

    def placeholder_identity(self):
        return self._mostrar_entrada_salida("np.eye(4)", np.eye(4))
    
    # inspeccionar arreglos
    def inspeccionar_shape(self, datos):
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, datos.shape)

    def inspeccionar_ndim(self, datos):
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, datos.ndim)

    def inspeccionar_size(self, datos):
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, datos.size)

    def inspeccionar_dtype(self, datos):
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, datos.dtype)