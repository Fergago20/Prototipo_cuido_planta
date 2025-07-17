from model.archivos import GuardarArchivos
from model.planta import EstadoPlanta
from controller.bluetooth import BluetoothLogica

class Logica:
    def __init__(self):
        self.archivos = GuardarArchivos()
        self.estado_planta = EstadoPlanta()
        self.bluetooth_logica = BluetoothLogica()

    def guardar_datos(self):
        datos = self.bluetooth_logica.recibir_datos()
        if datos[0] is False:
            return False, "No se recibieron datos del dispositivo Bluetooth"
        datos = datos[1]
        datos = datos.replace("'", "").replace("[", "").replace("]", "").replace(" ", "")
        humedad, temperatura_ambiente, temperatura_objeto, humedad_suelo, fecha_revision = datos.split(',')
        self.estado_planta.obtener_datos(humedad, temperatura_ambiente, temperatura_objeto, humedad_suelo, fecha_revision)
        datos = str(self.estado_planta.retornar_datos())
        datos = datos.replace("'", "").replace("[", "").replace("]", "").replace(" ", "")
        datos = ',' + datos
        print(datos)
        self.archivos.guardar(datos)
        return datos

    def obtener_datos(self):
        datos = self.archivos.cargar()
        if datos:
            valores = datos.split(',')
            valores= valores[1:]
            largo = len(valores) // 5
            return [
                {
                    'humedad': valores[i * 5],
                    'temperatura_ambiente': valores[i * 5 + 1],
                    'temperatura_objeto': valores[i * 5 + 2],
                    'humedad_suelo': valores[i * 5 + 3],
                    'fecha_revision': valores[i * 5 + 4]
                } for i in range(largo)
            ]
            
        
    def estado(self):
        return self.estado_planta.retornar_datos()
    
    def datos_filtrados_fecha(self, fechaprimera, fechasegunda ):
        datos = self.obtener_datos()
        if datos:
            return [dato for dato in datos if fechaprimera <= dato['fecha_revision'] <= fechasegunda]
            