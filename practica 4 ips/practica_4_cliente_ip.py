import socket
import threading

HOST = "10.79.10.120"
PORT = 5000

def cliente(id_cliente):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    
    mensaje = f"Hola desde cliente {id_cliente} Steeven Toala"
    s.send(mensaje.encode())
    
    respuesta = s.recv(1024).decode()
    print(f"Cliente {id_cliente} Steeven Toala recibe: {respuesta}")
    
    s.close()


# Crear y ejecutar hilos correctamente
hilos = []

for i in range(1, 2):  # puedes cambiar el 2 por más clientes
    t = threading.Thread(target=cliente, args=(i,))
    hilos.append(t)
    t.start()

# Esperar a que todos terminen
for t in hilos:
    t.join()