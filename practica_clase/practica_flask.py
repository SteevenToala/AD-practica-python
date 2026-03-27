from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_connection():
    """Conexión a PostgreSQL"""
    try:
        connection = psycopg2.connect(
            host="10.79.0.78",
            database="TOA_TAS",
            user="postgres",
            password="root",
            port="5432"
        )
        return connection
    except Exception as e:
        print("Error al conectar:", e)
        return None


@app.route("/api/estudiantes", methods=["GET"])
def get_estudiantes():
    try:
        conn = get_connection()
        if not conn:
            return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

        cursor = conn.cursor()

        # Forzar encoding correcto
        cursor.execute("SET client_encoding TO 'LATIN1'")

        cursor.execute("""
            SELECT id, cedula, nombres, apellidos, direccion, fecha_nacimiento 
            FROM estudiantes
        """)

        estudiantes = cursor.fetchall()

        cursor.close()
        conn.close()

        estudiantes_list = []
        for e in estudiantes:
            estudiantes_list.append({
                "id": e[0],
                "cedula": str(e[1]),
                "nombres": str(e[2]),
                "apellidos": str(e[3]),
                "direccion": str(e[4]),
                "fecha_nacimiento": str(e[5]) if e[5] else None
            })

        return jsonify(estudiantes_list)

    except Exception as e:
        print("Error en endpoint:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5070, debug=False)