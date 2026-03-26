import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

def atender_cliente(conn, addr):

    print(f"Cliente conectado:{addr}")
    
    request = conn.recv(1024).decode()
    print("Petición recibida:", request)

    body = "<html>"\
    "<body>"\
    "<h1>Hola desde mi servidor en Python - Steeven Toala</h1>"\
    "</body>"\
    "</html>"

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=UTF-8\r\n"
        f"Content-Length: {len(body.encode('UTF-8'))}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{body}"
    )
    conn.sendall(response.encode('UTF-8'))
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Servidor HTTP escuchando en {HOST}:{PORT}")

while True:
    conn, addr = server.accept()
    hilo = threading.Thread(target=atender_cliente,args=(conn, addr))
    hilo.start()
