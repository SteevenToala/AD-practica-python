import socket
import threading

HOST = "10.79.15.91"
PORT = 5080

def atender_cliente(conn, addr):
    print(f"Cliente conectado desde:", addr)
    data = conn.recv(1024)

    print(f"Mensaje de {addr}: {data.decode()}")
    conn.send(f"Hola cliente, {addr}, mensaje recibido".encode())
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Servidor multicliente escuchando en {HOST}:{PORT}...")

while True:
    conn, addr = server.accept()
    hilo = threading.Thread(target=atender_cliente,args=(conn, addr))
    hilo.start()