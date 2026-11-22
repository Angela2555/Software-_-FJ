
# Incorpora las herramientas necesarias para crear las clases abstractas.
from abc import ABC, abstractmethod

# trasfiere datos de la clase para almacenar errores.
from Excepciones import ManejoExcepciones

# Clase abstracta de los servicios.
class Servicio(ABC):

# Almacena los datos de los servicios.
    def __init__(self, identificador, nombre, precio):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        if not nombre:
           raise ValueError("El nombre del servicio es obligatorio.")


        self.identificador = identificador
        self.nombre = nombre
        self.precio = precio

# Metodo para calcular el valor del servicio.
    def calcular_costo(self, impuesto=0):
        return self.precio + (self.precio * impuesto / 100)

# Muestra detalles del servicio.
    @abstractmethod
    def describir_servicio(self):
        pass

# Analiza los datos del servicio solicitado.
    @abstractmethod
    def validar_servicio(self):
        pass


# Clase para diligenciar la reserva de habitacion.
class ReservaHabitacion(Servicio):

# Guarda los datos de la reserva solicitada.
    def __init__(self, identificador, nombre, precio, noches):
        super().__init__(identificador, nombre, precio)
        self.noches = noches

# Calcula el costo total de la reserva solicitada con impuestos y descuentos.
    def calcular_costo(self, impuesto=0, descuento=0):
        total = self.precio * self.noches
        total = total + (total * impuesto / 100)
        total = total - (total * descuento / 100)
        return total

    
# Visualiza los detalles de la reserva de habitacion.
    def describir_servicio(self):
        return f"Reserva de habitacion: {self.nombre}, {self.noches} noches."

# Analiza los datos de la reserva.
    def validar_servicio(self):
        try:
            if self.noches <= 0:
                raise ValueError("La cantidad de noches debe ser mayor a cero.")
            return True

        except ValueError as error:
            print(error)
            ManejoExcepciones("Error").registrar_log(str(error))
            return False

# Clase para el alquiler de equipos.
class AlquilerEquipo(Servicio):

# Almacena los datos del alquiler.
    def __init__(self, identificador, nombre, precio, cantidad_dias):
        super().__init__(identificador, nombre, precio)
        self.cantidad_dias = cantidad_dias

# Calcula el precio total del alquiler con impuestos y descuento.
    def calcular_costo(self, impuesto=0, descuento=0):
        total = self.precio * self.cantidad_dias
        total = total + (total * impuesto / 100)
        total = total - (total * descuento / 100)
        return total

# Visualiza los datos del alquiler de equipos.
    def describir_servicio(self):
        return f"Alquiler de equipo: {self.nombre}, {self.cantidad_dias} dias."

# Valida que los datos se ingresen correctamente.
    def validar_servicio(self):
        try:
            if self.cantidad_dias <= 0:
                raise ValueError("La cantidad de dias debe ser mayor a cero.")
            return True

        except ValueError as error:
            print(error)
            ManejoExcepciones("Error").registrar_log(str(error))
            return False

# Clase para los servicios de consultoria especializada.
class ConsultoriaEspecializada(Servicio):

# Almacena los datos de la consultoria especializada.
    def __init__(self, identificador, nombre, precio, horas):
        super().__init__(identificador, nombre, precio)
        self.horas = horas

# Calcula el valor total de la consultoria con descuento e impuestos
    def calcular_costo(self, impuesto=0, descuento=0):
        total = self.precio * self.horas
        total = total + (total * impuesto / 100)
        total = total - (total * descuento / 100)
        return total
    
# Muestra los datos de la misma.
    def describir_servicio(self):
        return f"Consultoria especializada: {self.nombre}, {self.horas} horas."

# Verifica que los datos sean correctos.
    def validar_servicio(self):
        try:
            if self.horas <= 0:
                raise ValueError("La cantidad de horas debe ser mayor a cero.")
            return True

        except ValueError as error:
            print(error)
            ManejoExcepciones("Error").registrar_log(str(error))
            return False
