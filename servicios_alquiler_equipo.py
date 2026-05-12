from servicio import Servicio
from excepciones import ServicioError


class AlquilerEquipo(Servicio):

    def __init__(self, nombre, precio_base, tipo_equipo):
        super().__init__(nombre, precio_base)
        self.tipo_equipo = tipo_equipo

    def validar_parametros(self):
        if not self.tipo_equipo:
            raise ServicioError("Tipo de equipo inválido")

    def calcular_costo(self, dias=1, descuento=0):
        return (self.precio_base * dias) - descuento

    def describir_servicio(self):
        return f"Alquiler de equipo tipo {self.tipo_equipo}"

    def mostrar_info(self):
        return self.describir_servicio()