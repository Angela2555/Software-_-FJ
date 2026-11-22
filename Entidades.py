# sirve para crear clases abstractas
from abc import ABC, abstractmethod

# registra errores al crear clientes.
from Excepciones import ManejoExcepciones

# clase base de la cual heredan las demas clases
class Entidad(ABC):

#empieza cada entidad con un codigo y lo guarda
    def __init__(self, identificador):
        self.identificador = identificador

#las clases hijas implementan este metodo segun sus propias caracteristicas
    @abstractmethod
    def mostrar_informacion(self):
        pass

# Clase para el registro de clientes del sistema.
class Cliente(Entidad):
    
# Registra y guarda los datos personales del cliente.
    def __init__(self, identificador, nombre, documento, correo, telefono, direccion):

# Comprueba que todos los campos tengan informacion.
        try:
            if not all([nombre, documento, correo, telefono, direccion]):
                raise ValueError("Todos los datos del cliente son obligatorios.")

        except ValueError as error:
            ManejoExcepciones("Error").registrar_log(str(error))
            raise


# Verifica que los datos esten ingresados correctamente.
        try:
            if "@" not in correo or "." not in correo:
                raise ValueError("El correo electronico no es valido.")

        except ValueError as error:
            ManejoExcepciones("Error").registrar_log(str(error))
            raise


# Verifica que se digiten solo numeros.
        try:
            if not telefono.isdigit():
                raise ValueError("El telefono debe contener solo numeros.")

        except ValueError as error:
            ManejoExcepciones("Error").registrar_log(str(error))
            raise
        
        super().__init__(identificador)
        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo
        self.__telefono = telefono
        self.__direccion = direccion

# Metodo para visualizar los datos del cliente.
    def mostrar_informacion(self):
        return (f"Nombre: {self.__nombre}, "
                f"Documento: {self.__documento}, "
                f"Correo: {self.__correo}, "
                f"Telefono: {self.__telefono}, "
                f"Direccion: {self.__direccion}")
    









