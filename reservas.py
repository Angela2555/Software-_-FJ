
# Incorpora Cliente y servicio.
from Entidades import Cliente
from servicios import Servicio

# Carga la clase para manejo de excepciones.
from Excepciones import ManejoExcepciones

# Clase para controlar las reservas.
class Reserva:

# Agenda los datos de la reserva.
    def __init__(self, identificador, cliente, servicio, duracion):

# Comprueba que el tiempo asignado sea mayor a 0.
        if duracion <= 0:
            raise ValueError("La duracion debe ser mayor a cero.")

        self.identificador = identificador
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion

# Almacena el estado de la reserva.
        self.estado = "Pendiente"

# Ejecuta la validacion de la reserva.

    def confirmar_reserva(self):
        if self.estado == "Cancelada":
            raise ValueError("No se puede confirmar una reserva cancelada.")

        self.estado = "Confirmada"
# Guarda el registro de la reserva confirmada.
        ManejoExcepciones("Evento").registrar_log("Reserva confirmada.")

        return self.estado

# Anula la reserva solicitada.
    def cancelar_reserva(self):
        if self.estado == "Cancelada":
            raise ValueError("La reserva ya esta cancelada.")

        self.estado = "Cancelada"
    

# Almacena el registro de la reserva cancelada.
        ManejoExcepciones("Evento").registrar_log("Reserva cancelada.")

        return self.estado

# Tramita la reserva solicitada.
       
    def procesar_reserva(self):
        try:
            # Verifica que la reserva este confirmada.
            if self.estado != "Confirmada":
                raise ManejoExcepciones("La reserva debe estar confirmada.")

            # Verifica que los datos del servicio sean correctos.
            if not self.servicio.validar_servicio():
                raise ManejoExcepciones("Los datos del servicio no son validos.")
            
# Evalua el precio de la reserva.
            costo = self.servicio.calcular_costo()

        except ManejoExcepciones as error:
# Notifica y guarda el error.
            print(error)
            ManejoExcepciones("Error").registrar_log(str(error))
            return None

        else:
            # Almacena el estado de reserva confirmda.
            ManejoExcepciones("Evento").registrar_log("Reserva procesada.")
            return costo

        finally:
# Registra el cierre del intento  de procesar la reserva.
            ManejoExcepciones("Evento").registrar_log("Finalizo el intento de procesar la reserva.")

   