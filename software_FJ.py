
# Importa la clase Cliente.
from Entidades import Cliente

# Importa las clases de los servicios.
from servicios import ReservaHabitacion, AlquilerEquipo, ConsultoriaEspecializada

# Importa la clase Reserva.
from reservas import Reserva

# Carga la clase para manejo de excepciones.
from Excepciones import ManejoExcepciones

# Crea las listas de almacenamiento de informacion.
clientes = []
servicios = []
reservas = []



# Genera registro de cliente.
cliente1 = Cliente(
    1,
    "Maria Lopez",
    "10256897",
    "Maria@gmail.com",
    "3104567890",
    "Cra 6 n 10-20 Bogota"
)

# guarda en la lista un cliente.
clientes.append(cliente1)


# crear cliente sin nombre.
try:
    cliente2 = Cliente(
        2,
        "",
        "1056897852",
        "luis@gmail.com",
        "3101234567",
        "cra 2B 5-10 Bogota"
    )

except ValueError as error:
# Muestra el error del registro.
    print(error)
# Creacion incorrecta del correo del cliente .
try:
    cliente3 = Cliente(
        3,
        "Felipe Diaz",
        "92865432",
        "felipegmail.com",
        "3121454560",
        "cra 12 26-40 Medellin"
    )

except ValueError as error:
# Muestra el error del registro.
    print(error)

# Verifica el manejo de errores al ingresar numero de noches incorrecto.
reserva_incorrecta = ReservaHabitacion(4, "Habitacion sencilla", 100000, 0)

# Verifica los datos de la reserva incorrecta.
print(reserva_incorrecta.validar_servicio())


# Muestra la informacion del cliente.
print(cliente1.mostrar_informacion())


# Crea una reserva de habitacion.
reserva1 = ReservaHabitacion(1, "Habitacion sencilla", 11000, 3)

# Agrega la resrva al listado de habitaciones.
servicios.append(reserva1)

# Muestra el costo total de la habitacion.
print(reserva1.calcular_costo())

# calcula costo con ivas y porcentaje de descuento
print(reserva1.calcular_costo(19, 15))

# Visualiza la informacion de la habitacion.
print(reserva1.describir_servicio())

# Verifica los datos de la habitacion.
print(reserva1.validar_servicio())


# Crea un alquiler de equipo.
alquiler1 = AlquilerEquipo(2, "Computador", 80000, 4)

# Guarda el alquiler de equipo en la lista correspondiente de servicios.
servicios.append(alquiler1)

# Visualiza el costo total del alquiler.
print(alquiler1.calcular_costo())

# Calcula el costo con IVA y descuento.
print(alquiler1.calcular_costo(19, 15))

# Muestra la informacion del alquiler de equipo.
print(alquiler1.describir_servicio())

# Valida los datos del alquiler.
print(alquiler1.validar_servicio())


# Registra una consultoria especializada.
consultoria1 = ConsultoriaEspecializada(3, "Asesoria de software", 95000, 5)

# Almacena la consultoria en la lista que corresponde.
servicios.append(consultoria1)

# Muestra el costo total de la consultoria con iva y descuento.
print(consultoria1.calcular_costo())

# Calcula el costo con IVA y descuento.
print(consultoria1.calcular_costo(19, 15))


# Muestra la informacion de la consultoria.
print(consultoria1.describir_servicio())

# Revisa los datos de la consultoria.
print(consultoria1.validar_servicio())


# Crea una reserva para el cliente.
reserva_cliente1 = Reserva(1, cliente1, reserva1, 3)

# Guarda la reserva del cliente en la lista que corresponde.
reservas.append(reserva_cliente1)

# Confirma la reserva.
print(reserva_cliente1.confirmar_reserva())

# Procesa la reserva y muestra el costo.
print(reserva_cliente1.procesar_reserva())

# Cliente cancela la reserva
print(reserva_cliente1.cancelar_reserva())


# Verifica una reserva pendiente.
reserva_cliente1.estado = "Pendiente"
print(reserva_cliente1.procesar_reserva())


# Prueba el manejo de excepciones.
try:
    raise ManejoExcepciones("Error de prueba.")

except ManejoExcepciones as error:
    print(error)

# Registra un evento en el archivo de logs.
registro = ManejoExcepciones("Prueba del registro de eventos.")
registro.registrar_log("Sistema ejecutado correctamente.")

# Prueba de excepcion encadenada.
try:
# Intenta convertir un texto en un numero.
    try:
        numero = int("hola")

    except ValueError as error:
# Genera una excepcion propia a partir del error original.
        raise ManejoExcepciones("No se pudo convertir el dato.") from error

except ManejoExcepciones as error:

# Muestra la excepcion original.
    print(error)
    ManejoExcepciones("Error").registrar_log(str(error))

#Muestra los datos guardados en las listas.
print("Clientes registrados:", len(clientes))
print("Servicios registrados:", len(servicios))
print("Reservas registradas:", len(reservas))

# Recorre los servicios almacenados en la lista.
for servicio in servicios:

# Muestra la descripcion de cada servicio.
    print(servicio.describir_servicio())

# Calcula el costo de cada servicio.
    print(servicio.calcular_costo())

# Ejecuta una prueba con ingreso de un precio incorrecto.
print("Iniciando prueba de precio incorrecto")

try:
    servicio_incorrecto = ReservaHabitacion(5, "Habitacion sencilla", 0, 2)
except ValueError as error:
    print(error)

# Ejecuta una prueba con ingreso de un servicio sin nombre.
try:
    servicio_sin_nombre = ReservaHabitacion(6, "", 100000, 2)
except ValueError as error:
    print(error)