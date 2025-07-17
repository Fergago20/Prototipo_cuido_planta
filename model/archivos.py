class GuardarArchivos:
    def __init__(self):
        self.nombre_archivo = 'datos.txt'

    def guardar(self, datos):
        with open(self.nombre_archivo, 'a') as archivo:
            archivo.write(datos)

    def cargar(self):
        try:
            with open(self.nombre_archivo, 'r') as archivo:
                return archivo.read()
        except FileNotFoundError:
            return None