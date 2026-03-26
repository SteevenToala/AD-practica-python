from flask import Flask, jsonify
import pyodbc
import pdb

app = Flask(__name__)

def get_connection():
    return pyodbc.connect(
        "DRIVER={OBDC Driver 17 for SQL Server};"
        "SERVER=10.79.0.78;" #ip del SQLServer
        "DATABASE=AppDistribuidasDB_P;"
        "UID=sa;"
        "PWD=sa;"
        "TrustServerCertificate=yes;"
    )

@app.route('/api/productos', methods=['GET'])
def get_productos():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, precio FROM productos")
        rows = cursor.fetchall()
        productos = []
        for row in rows:
            productos.append({
                'id': row.Id,
                'nombre': row.Nombre,
                'precio': row.Precio
            })
        
        cursor.close()
        conn.close()
        return jsonify(productos) , 200
    except Exception as e:
        return jsonify(
                {
                'error': "error al obtener productos",
                'details': str(e)
                }
            ), 500
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=500, debug=False)
