import socket
import threading

HOST = "localhost"
PORT = 5000

def cliente(id_cliente):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    mensaje = f"Hola desde cliente {id_cliente}"
    s.send(mensaje.encode())
    respuesta = s.recv(1024).decode()
    print(f"Cliente {id_cliente} recibe: {respuesta}")
    s.close()

hilos = []

for i in range(5):
    t = threading.Thread(target=cliente, args=(i,))
    t.start()
    hilos.append(t)


for t in hilos:
    t.join()
