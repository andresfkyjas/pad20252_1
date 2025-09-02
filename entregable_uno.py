
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
        self.categorias = ["perro","gato","caballo","gallina"]

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

        # Generamos líneas de CSV manualmente
        lineas = []
        lineas.append("i,b,c")  # encabezado
        esc_b = math.log10((self.cc_uno % 10000) + 10)
        esc_c = math.log10((self.cc_dos % 10000) + 10)

        for i in range(1, self.n + 1):
            # Ruido uniforme para b en [-1,1]
            ruido_b = (rng_b.random() * 2.0) - 1.0
            # Aproximación a normal(0,1) con 12 uniformes - 6
            ruido_c = sum(rng_c.random() for _ in range(12)) - 6.0

            b = (i * 0.5) + ruido_b * esc_b
            c = (math.sqrt(i)) + ruido_c * esc_c

            # Guardamos con 6 decimales para legibilidad
            lineas.append(f"{i},{b:.6f},{c:.6f}")

        with open(self.ruta_out, "w", encoding="utf-8") as f:
            f.write("\n".join(lineas))

        # Verificación: archivo existe y tiene n filas + 1 (encabezado)
        if not os.path.exists(self.ruta_out):
            raise IOError("No se pudo crear el archivo de salida")

        with open(self.ruta_out, "r", encoding="utf-8") as f:
            total_lineas = sum(1 for _ in f)

        if total_lineas != self.n + 1:
            raise IOError("El archivo de salida no tiene la cantidad correcta de filas")

        return "ok"

    # 3) Leer datos_out, agregar etiqueta y graficar
    def leer_y_graficar(self):
        if not os.path.exists(self.ruta_out):
            raise FileNotFoundError("No se encontró el archivo: " + self.ruta_out)

        # Leemos manualmente el CSV
        with open(self.ruta_out, "r", encoding="utf-8") as f:
            lineas = f.read().strip().splitlines()

        if not lineas or lineas[0].strip() != "i,b,c":
            raise ValueError("El archivo no tiene el encabezado esperado 'i,b,c'")

        # Parseamos
        i_vals = []
        b_vals = []
        c_vals = []
        for linea in lineas[1:]:
            partes = linea.split(",")
            if len(partes) < 3:
                continue
            i_vals.append(int(partes[0]))
            b_vals.append(float(partes[1]))
            c_vals.append(float(partes[2]))

        # Agregar etiqueta aleatoria y re-escribir archivo con nueva columna
        rng_cat = random.Random((self.cc_uno or 0) ^ (self.cc_dos or 0))
        etiquetas = [rng_cat.choice(self.categorias) for _ in i_vals]

        # Re-escribir con la nueva columna
        with open(self.ruta_out, "w", encoding="utf-8") as f:
            f.write("i,b,c,etiqueta\n")
            for i, b, c, e in zip(i_vals, b_vals, c_vals, etiquetas):
                f.write(f"{i},{b:.6f},{c:.6f},{e}\n")

        # Graficar líneas simples
        plt.figure()
        plt.plot(i_vals, b_vals, label="b")
        plt.plot(i_vals, c_vals, label="c")
        plt.xlabel("i")
        plt.ylabel("valor")
        plt.title("Series generadas b y c")
        plt.legend()
        plt.tight_layout()
        plt.savefig(self.ruta_img, dpi=200)
        plt.close()

        if not os.path.exists(self.ruta_img) or os.path.getsize(self.ruta_img) == 0:
            raise IOError("No se pudo generar la imagen")

        return "ok"


if __name__ == "__main__":
    proc = ProcesadorDatos()
    print("Paso 1:", proc.leer_datos_entrada())
    print("Paso 2:", proc.generar_datos())
    print("Paso 3:", proc.leer_y_graficar())