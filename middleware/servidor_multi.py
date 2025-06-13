from socket import socket,AF_INET,SOCK_STREAM
from multiprocessing import Process, Queue
import time
import sys

port = int(sys.argv[1])


def worker(task_queue):
    while True:
        if not task_queue.get():
            conn, addr = task_queue.get()
            print(f"Procesando la solicitud de {addr}")
            try:
                data = conn.recv(1924)
                print(f"Mensaje recibido de {addr}:{data.decode()}")
                time.sleep(1)
                conn.sendall(b"Respuesta del servidor")
            except Exception as e:
                print(f"error en el cliente{addr}:{e}")
        else:
            time.sleep(0.1)


def start_server(host='localhost', port=port, num_worker=10):
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((host,port))
    server_socket.listen(1)
    print(f"Servidor escuchando en {host}:{port}")

    task_queue = Queue()

    workers = [Process(target = worker,args=(task_queue,))]
    for w in workers:
        w.start()

    try:
        while True:
            conn, addr = server_socket.accept()
            print(f"Cliente conectado: {addr}")
            task_queue.put((conn,addr))
    except KeyboardInterrupt:
        print("Servidor detenido manualmente")
    finally:
        server_socket.close()
if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("El uso del comando es:")
        else:
            start_server(port=port)
