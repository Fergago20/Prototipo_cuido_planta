from flask import Flask, request, jsonify, render_template
from controller.bluetooth import BluetoothLogica
from controller.logica import Logica
from controller.n8n import N8nLogica
import time


app = Flask(__name__)
bluetooth_logica = BluetoothLogica()
logica = Logica()
n8n = N8nLogica()  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/datos_actuales', methods=['GET'])
def datos_actuales():
    resultado = logica.guardar_datos()

    if  resultado[0] is False:
        return render_template('datos_actuales.html', datos=None, error=resultado[1])

    try:
        
        resultado = resultado[1]
        if len(resultado.split(',')) == 5:
            humedad, temperatura_ambiente, temperatura_objeto, humedad_suelo, fecha_revision = resultado.split(',')
            datos = {
                'humedad': humedad,
                'temperatura_ambiente': temperatura_ambiente,
                'temperatura_objeto': temperatura_objeto,
                'humedad_suelo': humedad_suelo,
                'fecha_revision': fecha_revision
            }
            return render_template('datos_actuales.html', datos=datos)
        else:
            return render_template('datos_actuales.html', datos=None, error="Datos incompletos o inválidos")
            
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
    fechaprimera = str(request.args.get('fechaprimera'))
    fechasegunda = str(request.args.get('fechasegunda'))
    datos_filtrados = logica.datos_filtrados_fecha(fechaprimera, fechasegunda)
    if datos_filtrados:
        return render_template('historial.html', datos=datos_filtrados)
    return render_template('historial.html', error='No se encontraron datos en el rango de fechas')

@app.route('/grafico', methods=['GET'])
def grafico():
    if 'fechaprimera' not in request.args or 'fechasegunda' not in request.args:
        return render_template('grafico.html', error='Por favor, ingrese las fechas para filtrar los datos.')
    datos = logica.datos_filtrados_fecha(str(request.args.get('fechaprimera')), str(request.args.get('fechasegunda')))
    if datos:
        print("Datos para el gráfico:", datos)
        return render_template('grafico.html', datos=datos)
    return render_template('grafico.html', error='No se encontraron datos para el gráfico')

@app.route('/enviar_datos', methods=['GET'])
def enviar_datos():
    # Obtener y validar los datos
    resultado = logica.guardar_datos()
    if not resultado[0]:
        return jsonify({'error': resultado[1]}), 400

    resultado = resultado[1]
    humedad, temperatura_ambiente, temperatura_objeto, humedad_suelo, fecha_revision = resultado.split(',')
    datos = {
        'humedad': humedad,
        'temperatura_ambiente': temperatura_ambiente,
        'temperatura_objeto': temperatura_objeto,
        'humedad_suelo': humedad_suelo,
        'fecha_revision': fecha_revision
    }


    # Enviar a N8N
    response = n8n.enviar_datos(datos)
    if response is None:
        return jsonify({'error': 'Failed to send data to n8n'}), 500

    return jsonify({
        'message': 'Datos enviados correctamente',
        'datos_enviados': datos,
        'respuesta_n8n': response
    }), 200


@app.route('/n8n', methods=['GET'])
def vista_n8n():
    return render_template('n8n.html')

@app.route('/exito_datos')
def exito_datos():
    return render_template('exito_datos.html')

@app.route('/error_datos')
def error_datos():
    return render_template('error_datos.html')

@app.route('/vigilante', methods=['GET'])
def vigilante():
    try:
        while True:
            resultado = logica.guardar_datos()
            if resultado[0]:
                datos = resultado[1]
                humedad, temperatura_ambiente, temperatura_objeto, humedad_suelo, fecha_revision = datos.split(',')
                datos_dict = {
                    'humedad': humedad,
                    'temperatura_ambiente': temperatura_ambiente,
                    'temperatura_objeto': temperatura_objeto,
                    'humedad_suelo': humedad_suelo,
                    'fecha_revision': fecha_revision
                }
                n8n.enviar_datos(datos_dict)
                return render_template('vigilante.html', datos=datos_dict)
            else:
                return render_template('error_datos.html', error="Datos inválidos o no disponibles")
            time.sleep(300)
    except Exception as e:
        return render_template('error_datos.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)