# Servidor web

import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_socket.bind(('localhost',8080))
server_socket.listen(1)
print("Servidor ejecutandose.....")

conn, addr =  server_socket.accept()
print("Esperando conexiones en el puerto" ,{addr})

data = conn.recv(1024)
print("Mensaje recibido:",data.decode())

conn.sendall(b"Hola desde el servidor!")
conn.close()