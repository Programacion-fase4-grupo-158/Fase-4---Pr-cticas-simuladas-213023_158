from servicio import Servicio
from excepciones import ServicioError


class ReservaSala(Servicio):

    def __init__(self, nombre, precio_base, capacidad):
        super().__init__(nombre, precio_base)
        self.capacidad = capacidad

    def validar_parametros(self):
        if self.capacidad <= 0:
            raise ServicioError("Capacidad inválida")

    def calcular_costo(self, horas=1, impuesto=0):
        return (self.precio_base * horas) + impuesto

    def describir_servicio(self):
        return f"Reserva de sala con capacidad para {self.capacidad} personas"

    def mostrar_info(self):
        return self.describir_servicio()