from flask import Blueprint, jsonify
from configdb import get_connection

sensors = Blueprint("sensors", __name__)

@sensors.route('/allSensors')
def get_all_sensors():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, activo, roto FROM sensor")
        results = cursor.fetchall()

        sensors = []
        for row in results:
            sensors.append({
                'id': row['id'],
                'activo': row['activo'],
                'roto': row['roto']
            })

        return jsonify({
            'success': True,
            'sensors': sensors
        }), 200
    except Exception as ex:
        return jsonify({
            'success': False,
            'description': 'Error',
            'error': str(ex)
        }), 500