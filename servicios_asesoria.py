from servicio import Servicio
from excepciones import ServicioError


class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, precio_base, especialidad):
        super().__init__(nombre, precio_base)
        self.especialidad = especialidad

    def validar_parametros(self):
        if not self.especialidad:
            raise ServicioError("Especialidad inválida")

    def calcular_costo(self, horas=1, impuesto=0, descuento=0):
        return ((self.precio_base * horas) + impuesto) - descuento

    def describir_servicio(self):
        return f"Asesoría especializada en {self.especialidad}"

    def mostrar_info(self):
        return self.describir_servicio()