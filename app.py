from flask import Flask, request, jsonify, render_template
from controller.bluetooth import BluetoothLogica
from controller.logica import Logica
app = Flask(__name__)
bluetooth_logica = BluetoothLogica()
logica = Logica()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/datos_actuales', methods=['GET'])
def datos_actuales():
    resultado = logica.guardar_datos()

    if isinstance(resultado, tuple) and resultado[0] is False:
        return render_template('datos_actuales.html', datos=None, error=resultado[1])

    try:
        humedad, temperatura_ambiente, temperatura_objeto, humedad_suelo, fecha_revision = resultado.split(',')
        datos = {
            'humedad': humedad,
            'temperatura_ambiente': temperatura_ambiente,
            'temperatura_objeto': temperatura_objeto,
            'humedad_suelo': humedad_suelo,
            'fecha_revision': fecha_revision
        }
        return render_template('datos_actuales.html', datos=datos)
    except Exception as e:
        return render_template('datos_actuales.html', datos=None, error="Error al procesar los datos: " + str(e))


@app.route('/historial', methods=['GET'])
def historial():
    datos = logica.obtener_datos()
    if datos:
        return render_template('historial.html', datos=datos)
    return render_template('historial.html', error='No se encontraron datos')

@app.route('/historial_filtrado', methods=['GET'])
def historial_filtrado():
    fechaprimera = request.args.get('fechaprimera')
    fechasegunda = request.args.get('fechasegunda')
    datos_filtrados = logica.datos_filtrados_fecha(fechaprimera, fechasegunda)
    if datos_filtrados:
        return render_template('historial.html', datos=datos_filtrados)
    return render_template('historial.html', error='No se encontraron datos en el rango de fechas')

@app.route('/grafico', methods=['GET'])
def grafico():
    datos = logica.estado()
    if datos:
        return render_template('grafico.html', datos=datos)
    return render_template('grafico.html', error='No se encontraron datos para el gráfico')

if __name__ == '__main__':
    app.run(debug=True)