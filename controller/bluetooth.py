import serial
import time
class BluetoothLogica:
    def __init__(self):
        self.puerto = 'COM15'
        self.baudrate = 9600
        self.ser = None

    def conectar(self):
        try:
            if self.ser is None or not self.ser.is_open:
                self.ser = serial.Serial(self.puerto, self.baudrate, timeout=2)
            return True, "Conexión establecida"
        except serial.SerialException as e:
            return False, str(e)

    def enviar_datos(self):
        estado, mensaje = self.conectar()
        if not estado:
            return False, mensaje
        try:
            self.ser.write('Solicitar datos'.encode('utf-8'))
            return True, "Datos enviados"
        except serial.SerialException as e:
            return False, str(e)

    def recibir_datos(self):
        estado, mensaje = self.conectar()
        if not estado:
            return False, mensaje

        enviado, mensaje_envio = self.enviar_datos()
        if not enviado:
            return False, mensaje_envio

        try:
            datos = self.ser.readline().decode('utf-8').strip()
            datos = datos + ',' + time.strftime('%Y-%m-%d-%H:%M:%S')
            return True, datos
        except serial.SerialException as e:
            return False, str(e)

    def cerrar_conexion(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            return True, "Conexión cerrada"
        return False, "No hay conexión abierta para cerrar"
