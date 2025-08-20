import serial
import time

class BluetoothLogica:
    def __init__(self):
        self.puerto = "COM5"   
        self.baudrate = 9600
        self.ser = None

    def conectar(self):
        try:
            if self.ser is None or not self.ser.is_open:
                self.ser = serial.Serial(self.puerto, self.baudrate, timeout=2)
            return True, f"Conexión establecida en {self.puerto}"
        except serial.SerialException as e:
            print("No conectado")
            return False, f"Error al conectar: {e}"

    def enviar_datos(self, mensaje="Solicitar datos"):
        estado, mensaje_conexion = self.conectar()
        if not estado:
            return False, mensaje_conexion
        try:
            self.ser.write(mensaje.encode("utf-8"))
            return True, "Datos enviados"
        except serial.SerialException as e:
            return False, str(e)

    def recibir_datos(self):
        estado, mensaje_conexion = self.conectar()
        if not estado:
            return False, mensaje_conexion
        enviado, mensaje_envio = self.enviar_datos()
        if not enviado:
            return False, mensaje_envio
        try:
            datos = self.ser.readline().decode("utf-8", errors="ignore").strip()
            datos = datos + "," + time.strftime("%Y-%m-%d-%H:%M:%S")
            return True, datos
        except serial.SerialException as e:
            return False, str(e)

    def cerrar_conexion(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
            return True, "Conexión cerrada"
