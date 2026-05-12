import logging

from cliente import Cliente
from reserva import Reserva
from excepciones import ClienteError, ServicioError, ReservaError

from servicios.reserva_sala import ReservaSala
from servicios.alquiler_equipo import AlquilerEquipo
from servicios.asesoria import AsesoriaEspecializada


# Configuración de logs
logging.basicConfig(
    filename="logs/sistema.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


clientes = []
servicios = []
reservas = []


print("\n===== INICIO DEL SISTEMA =====\n")


# OPERACIÓN 1
try:
    cliente1 = Cliente("Juan Perez", "juan@gmail.com", "123456789")
    clientes.append(cliente1)
    print(cliente1.mostrar_info())
except ClienteError as e:
    logging.error(e)


# OPERACIÓN 2
try:
    cliente2 = Cliente("Maria", "correo_invalido", "987654321")
    clientes.append(cliente2)
except ClienteError as e:
    print(e)
    logging.error(e)


# OPERACIÓN 3
try:
    sala = ReservaSala("Sala Premium", 100, 20)
    servicios.append(sala)
    print(sala.mostrar_info())
except ServicioError as e:
    logging.error(e)


# OPERACIÓN 4
try:
    equipo = AlquilerEquipo("Portátil", 80, "Laptop")
    servicios.append(equipo)
    print(equipo.mostrar_info())
except ServicioError as e:
    logging.error(e)


# OPERACIÓN 5
try:
    asesoria = AsesoriaEspecializada("Consultoría", 150, "Python")
    servicios.append(asesoria)
    print(asesoria.mostrar_info())
except ServicioError as e:
    logging.error(e)


# OPERACIÓN 6
try:
    reserva1 = Reserva(cliente1, sala, 3)
    reservas.append(reserva1)
    print(reserva1.procesar())
except ReservaError as e:
    print(e)
    logging.error(e)


# OPERACIÓN 7
try:
    reserva2 = Reserva(cliente1, equipo, -2)
    reservas.append(reserva2)
    print(reserva2.procesar())
except ReservaError as e:
    print(e)
    logging.error(e)


# OPERACIÓN 8
try:
    cliente3 = Cliente("Carlos", "carlos@gmail.com", "telefono")
    clientes.append(cliente3)
except ClienteError as e:
    print(e)
    logging.error(e)


# OPERACIÓN 9
try:
    sala_invalida = ReservaSala("Sala Error", 100, -10)
    sala_invalida.validar_parametros()
except ServicioError as e:
    print(e)
    logging.error(e)


# OPERACIÓN 10
try:
    reserva3 = Reserva(cliente1, asesoria, 2)
    reservas.append(reserva3)
    print(reserva3.procesar())
    except ReservaError as e:
    print(e)
    logging.error(e)
finally:
    print("\nSistema ejecutado correctamente")