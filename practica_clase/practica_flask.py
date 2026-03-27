from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

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


def limpiar(valor):
    if valor is None:
        return None
    try:
        return str(valor)
    except:
        try:
            return valor.encode('latin1').decode('utf-8', errors='ignore')
        except:
            return ""


@app.route("/api/estudiantes", methods=["GET"])
def get_estudiantes():
    conn = get_connection()
    if not conn:
        return jsonify({"error": "No se pudo conectar"}), 500

    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, cedula, nombres, apellidos, direccion, fecha_nacimiento 
            FROM estudiantes
        """)

        datos = cursor.fetchall()

        resultado = []
        for e in datos:
            resultado.append({
                "id": e[0],
                "cedula": limpiar(e[1]),
                "nombres": limpiar(e[2]),
                "apellidos": limpiar(e[3]),
                "direccion": limpiar(e[4]),
                "fecha_nacimiento": str(e[5]) if e[5] else None
            })

        return jsonify(resultado)

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": str(e)}), 500

    finally:
        conn.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5070)