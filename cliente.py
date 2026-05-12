from entidad import Entidad
from excepciones import ClienteError


class Cliente(Entidad):

    def __init__(self, nombre, correo, telefono):
        self.set_nombre(nombre)
        self.set_correo(correo)
        self.set_telefono(telefono)

    def set_nombre(self, nombre):
        if not nombre.strip():
            raise ClienteError(
                "El nombre no puede estar vacío"
            )

        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_correo(self, correo):
        if "@" not in correo:
            raise ClienteError("Correo inválido")

        self.__correo = correo

    def get_correo(self):
        return self.__correo

    def set_telefono(self, telefono):
        if not telefono.isdigit():
            raise ClienteError(
                "El teléfono debe contener solo números"
            )

        self.__telefono = telefono

    def get_telefono(self):
        return self.__telefono

    def mostrar_info(self):
        return (
            f"Cliente: "
            f"{self.__nombre} - "
            f"{self.__correo}"
        )