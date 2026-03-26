import socket

HOST = "10.79.15.91"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Servidor escuchando en {HOST}:{PORT}...")

conn, addr = server.accept()
print("Conectado por:", addr)

data = conn.recv(1024)
print("Mensaje recibido:", data.decode())

conn.send("Hola desde el servidor".encode())

conn.close()
server.close()