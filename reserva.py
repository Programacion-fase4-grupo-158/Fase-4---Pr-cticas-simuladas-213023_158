from excepciones import ReservaError


class Reserva:

    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):
        try:
            if self.duracion <= 0:
                raise ReservaError("Duración inválida")

            self.servicio.validar_parametros()
            costo = self.servicio.calcular_costo(self.duracion)
            self.confirmar()

            return f"Reserva procesada correctamente. Costo: {costo}"

        except Exception as e:
            raise ReservaError("Error al procesar la reserva") from e