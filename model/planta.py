from datetime import datetime
class EstadoPlanta:
    def __init__(self):
        self.datos= {}

    def obtener_datos(self, humedad, temperatura_ambiente, temperatura_objeto, humedad_suelo, fecha_revision):

        self.datos = {
            'humedad': humedad,
            'temperatura_ambiente': temperatura_ambiente,
            'temperatura_objeto': temperatura_objeto,
            'humedad_suelo': humedad_suelo,
            'fecha_revision': fecha_revision
        }

    def retornar_datos(self):
        lista_datos = [
            self.datos['humedad'],
            self.datos['temperatura_ambiente'],
            self.datos['temperatura_objeto'],
            self.datos['humedad_suelo'],
            self.datos['fecha_revision']
        ]
        return lista_datos
    