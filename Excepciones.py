
# Clase para manejo de excepciones.
class ManejoExcepciones(Exception):
    

# Guarda el mensaje de falla.
    def __init__(self, mensaje):
        super().__init__(mensaje)

 # Almacena todos los errores relevantes en el archivo de logs.
    def registrar_log(self, mensaje):
        with open("logs.txt", "a", encoding="utf-8") as archivo:
            archivo.write(mensaje + "\n")


