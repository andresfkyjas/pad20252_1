def area_rectangulo(base :float ,alto :float) -> float:
    """Calcular el area del triangulo
    :param base: base del triangulo
    :param alto: altura del triagulo
    :return: area del triangulo
    """
    return base * alto

print("Area de 3x5",area_rectangulo(3,5))

class Carro():
    def __init__(self, name="",tipo_car=[],color="",num_puertas=0,tipo_combustible=[]):
        """_summary_

        Args:
            name (str, optional): _description_. Defaults to "".
            tipo_car (list, optional): _description_. Defaults to [].
            color (str, optional): _description_. Defaults to "".
            num_puertas (int, optional): _description_. Defaults to 0.
            tipo_combustible (list, optional): _description_. Defaults to [].
        """
        self.name = name
        self.tipo_car=tipo_car
        self.color=color
        self.num_puertas=num_puertas
        self.tipo_combustible=tipo_combustible

    def frenar(self,tipo=0):
        """_summary_

        Args:
            tipo (int, optional): _description_. Defaults to 0.

        Returns:
            _type_: _description_
        """
        if tipo ==1 :
            self.tipo_disco_freno="abs"
        else:
            self.tipo_disco_freno="disco"
        return self.tipo_disco_freno


    def __str__(self):
        return "NOMBRE : ",self.name ,"- TIPO : ", self.tipo_car,"- COLOR : ",self.color,"- # PUERTAS : ",self.num_puertas,self.tipo_combustible


type_car= ["camioneta"] 
color = "negro"
num_puertas=4
tipo_combustible=["gasolina"]
name ="mazda cx30"
carro_1 = Carro(color=color,name=name,num_puertas=num_puertas,tipo_combustible=tipo_combustible,tipo_car=type_car)

type_car= ["automovil"] 
color = "azul"
num_puertas=2
tipo_combustible=["gasolina"]
name ="Renauld 2025"

carro_2 = Carro(color=color,name=name,num_puertas=num_puertas,tipo_combustible=tipo_combustible,tipo_car=type_car)
print("#########################################################################")
print(carro_1.__str__())
print("#########################################################################")
print(carro_2.__str__())
print("#########################################################################")

carro_3 = Carro(color=color,name=name,tipo_combustible=tipo_combustible,tipo_car=type_car)
print(carro_3.__str__())
print("#########################################################################")
