import os
os.environ["PGCLIENTENCODING"] = "LATIN1"  # importante para tu server en Windows

from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
    return response

def get_connection():
    try:
        return psycopg2.connect(
            host="10.79.0.78",
            database="TOA_TAS",
            user="postgres",
            password="root",
            port="5432"
        )
    except Exception as e:
        print("Error al conectar:", e)
        return None


@app.route("/api/estudiantes", methods=["GET"])
def get_estudiantes():
    conn = get_connection()
    if not conn:
        return jsonify({"error": "No se pudo conectar"}), 500

    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, cedula, nombres, apellidos, direccion, "fechaNacimiento" 
            FROM estudiantes
        """)  # Usar comillas dobles para respetar la columna exacta

        datos = cursor.fetchall()

        resultado = []
        for e in datos:
            resultado.append({
                "id": e[0],
                "cedula": str(e[1]),
                "nombres": e[2],  # no necesitamos str() si ya es texto
                "apellidos": e[3],
                "direccion": e[4],
                "fechaNacimiento": str(e[5]) if e[5] else None
            })

        return jsonify(resultado)

    except Exception as e:
        print("Error en endpoint:", e)
        return jsonify({"error": str(e)}), 500

    finally:
        conn.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5070)