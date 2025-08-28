import numpy as np

class NumpyEjercicios:
    """
    Clase para aplicar ejercicios con NumPy.
    
    Ofrece funciones agrupadas por categorías para facilitar el aprendizaje de operaciones con arreglos NumPy,
    incluyendo:
        - Creación de arreglos (placeholders)
        - Inspección de propiedades
        - Operaciones matemáticas
        - Comparaciones y lógica booleana
        - Funciones agregadas
        - Indexado y manipulación de arrays

    Todas las funciones validan los datos de entrada y muestran la entrada, salida, tipo y forma de los resultados.
    """

    def _validar_datos(self, datos):
        """
        Valida que los datos no sean None y que sean de tipo np.ndarray.

        Parámetros:
        - datos: objeto a validar

        Excepciones:
        - ValueError: si los datos son None
        - TypeError: si los datos no son un ndarray de NumPy
        """
        if datos is None:
            raise ValueError("Los datos no pueden ser None")
        if not isinstance(datos, np.ndarray):
            raise TypeError("Los datos deben ser un array de NumPy")

    def _mostrar_entrada_salida(self, entrada, salida):
        """
        Imprime datos de entrada y salida, así como su tipo y forma.

        Parámetros:
        - entrada: datos antes del procesamiento
        - salida: resultado de la operación

        Retorna:
        - salida: el mismo resultado que recibe como parámetro
        """
        print("\n📥 Entrada:\n", entrada)
        print("📤 Salida:\n", salida)
        print("📐 Tipo:", type(salida), "| Forma:", getattr(salida, 'shape', 'escalar'))
        return salida

    # --- Initial Placeholders ---
    def placeholder_zeros(self, x=0, y=0):
        """
        Crea una matriz de ceros de tamaño (x, y).
        """
        return self._mostrar_entrada_salida(f"np.zeros(({x},{y}))", np.zeros((x, y)))

    def placeholder_ones(self):
        """
        Crea una matriz de unos de tamaño (2, 4).
        """
        return self._mostrar_entrada_salida("np.ones((2,4))", np.ones((2, 4)))

    def placeholder_full(self):
        """
        Crea una matriz (3x3) llena con el valor 7.
        """
        return self._mostrar_entrada_salida("np.full((3,3),7)", np.full((3, 3), 7))

    def placeholder_identity(self):
        """
        Crea una matriz identidad de tamaño 4x4.
        """
        return self._mostrar_entrada_salida("np.eye(4)", np.eye(4))

    # --- Inspección de Arreglos ---
    def inspeccionar_shape(self, datos):
        """
        Devuelve la forma (dimensiones) del arreglo.
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, datos.shape)

    def inspeccionar_ndim(self, datos):
        """
        Devuelve el número de dimensiones del arreglo.
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, datos.ndim)

    def inspeccionar_size(self, datos):
        """
        Devuelve el número total de elementos del arreglo.
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, datos.size)

    def inspeccionar_dtype(self, datos):
        """
        Devuelve el tipo de datos (dtype) de los elementos del arreglo.
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, datos.dtype)

    # --- Aritmética ---
    def suma_array(self, datos, valor=0):
        """
        Suma un valor escalar a todos los elementos del arreglo.
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, datos + valor)

    def multiplicacion_elemento(self, datos, valor=0):
        """
        Multiplica cada elemento del arreglo por un valor escalar.
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, datos * valor)

    def raiz_cuadrada(self, datos):
        """
        Calcula la raíz cuadrada de los valores absolutos del arreglo.
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, np.sqrt(np.abs(datos)))

    def logaritmo_natural(self, datos):
        """
        Aplica logaritmo natural a (1 + valor absoluto de cada elemento).
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, np.log1p(np.abs(datos)))

    # --- Comparaciones ---
    def comparar_mayores_50(self, datos):
        """
        Compara si los elementos son mayores a 50.
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, datos > 50)

    def comparar_igual_a_10(self, datos):
        """
        Verifica qué elementos son exactamente iguales a 10.
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, datos == 10)

    def comparar_array(self, datos):
        """
        Compara el arreglo con una copia para verificar igualdad.
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, np.array_equal(datos, datos.copy()))

    def comparar_menores_20(self, datos):
        """
        Verifica qué elementos son menores que 20.
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, datos < 20)

    # --- Funciones Agregadas ---
    def suma_total(self, datos):
        """
        Calcula la suma total de todos los elementos.
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, datos.sum())

    def media_columna(self, datos):
        """
        Calcula el promedio de cada columna.
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, np.mean(datos, axis=0))

    def maximo_global(self, datos):
        """
        Encuentra el valor máximo de todo el arreglo.
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, np.max(datos))

    def desviacion_estandar(self, datos):
        """
        Calcula la desviación estándar de todos los elementos.
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, np.std(datos))

    # --- Subsetting, Slicing, Indexing ---
    def seleccionar_fila_0(self, datos):
        """
        Devuelve la primera fila del arreglo.
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, datos[0])

    def seleccionar_columna_1(self, datos):
        """
        Devuelve la segunda columna (índice 1).
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, datos[:, 1])

    def seleccionar_por_rango(self, datos):
        """
        Devuelve las filas 1 y 2 completas del arreglo.
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, datos[1:3, :])

    def seleccion_booleana(self, datos):
        """
        Devuelve elementos mayores a 50 usando indexado booleano.
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, datos[datos > 50])

    # --- Manipulación de Arreglos ---
    def transponer(self, datos):
        """
        Transpone el arreglo (filas por columnas).
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, datos.T)

    def aplanar(self, datos):
        """
        Convierte el arreglo en un vector 1D.
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, datos.ravel())

    def concatenar_con_otra(self, datos):
        """
        Concatena el arreglo con otro del mismo tamaño lleno de unos.
        """
        self._validar_datos(datos)
        otra = np.ones_like(datos)
        return self._mostrar_entrada_salida(datos, np.concatenate((datos, otra), axis=0))

    def insertar_valores(self, datos):
        """
        Inserta el valor 99 en la columna 1 para cada fila del arreglo.
        """
        self._validar_datos(datos)
        return self._mostrar_entrada_salida(datos, np.insert(datos, 1, 99, axis=1))
