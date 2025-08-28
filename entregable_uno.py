
# procesador_bar.py
# -*- coding: utf-8 -*-
"""
Clase sencilla para estudiantes de 1er semestre (sin pandas).
Pasos:
  1) Lee "datos_in.txt" con: n cc_uno cc_dos
  2) Genera n datos (b y c) usando semillas cc_uno y cc_dos, guarda "datos_out.txt"
  3) Lee "datos_out.txt", agrega columna aleatoria "etiqueta" y genera "grafico_out.jpg"
     mostrando cuántos hay de cada etiqueta en gráfico de barras.
"""
import os
import math
import random
import matplotlib.pyplot as plt

class ProcesadorDatos:
    def __init__(self, ruta_in="datos_in.txt", ruta_out="datos_out.txt", ruta_img="grafico_out.jpg"):
        self.ruta_in = ruta_in
        self.ruta_out = ruta_out
        self.ruta_img = ruta_img

        # Variables a llenar desde el archivo de entrada
        self.n = None
        self.cc_uno = None
        self.cc_dos = None

        # Categorías para el paso 3
        self.categorias = ["anciano","anciana","mujer","hombre","niño","niña"]

    # 1) Leer archivo de entrada
    def leer_datos_entrada(self):
        if not os.path.exists(self.ruta_in):
            raise FileNotFoundError("No se encontró el archivo: " + self.ruta_in)

        with open(self.ruta_in, "r", encoding="utf-8") as f:
            contenido = f.read().strip()

        partes = contenido.split()
        if len(partes) < 3:
            raise ValueError("El archivo debe tener 3 valores: n cc_uno cc_dos")

        try:
            self.n = int(partes[0])
            self.cc_uno = int(partes[1])
            self.cc_dos = int(partes[2])
        except ValueError:
            raise ValueError("Los valores n, cc_uno y cc_dos deben ser enteros")

        print("n =", self.n)
        print("cc_uno =", self.cc_uno)
        print("cc_dos =", self.cc_dos)
        return "ok"

    # 2) Generar datos y guardarlos
    def generar_datos(self):
        """
        generar los datos i hasta n,
        b,c, y guardar en un archivo datos_out.txt
        """
        if self.n is None or self.cc_uno is None or self.cc_dos is None:
            raise RuntimeError("Primero ejecute leer_datos_entrada()")

        rng_b = random.Random(self.cc_uno)
        rng_c = random.Random(self.cc_dos)

        return "ok"

    # 3) Leer datos_out, agregar etiqueta y graficar
    def leer_y_graficar(self):
        if not os.path.exists(self.ruta_out):
            raise FileNotFoundError("No se encontró el archivo: " + self.ruta_out)

        # Leemos manualmente el CSV
        with open(self.ruta_out, "r", encoding="utf-8") as f:
            lineas = f.read().strip().splitlines()

        if not lineas or not lineas[0].startswith("i,b,c"):
            raise ValueError("El archivo no tiene el encabezado esperado 'i,b,c'")
        return "ok"


if __name__ == "__main__":
    proc = ProcesadorDatos()
    print("Paso 1:", proc.leer_datos_entrada())
    print("Paso 2:", proc.generar_datos())
    print("Paso 3:", proc.leer_y_graficar())