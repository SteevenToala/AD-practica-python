from multiprocessing import Process, Queue
import time

def productor(q):
    for i in range(5):
        mensaje = f"Mensaje {i}"
        print(f"Productor envia: {mensaje}")
        q.put(mensaje)
        time.sleep(0.5)

def consumidor(q):
    for i in range(5):
        mensaje = q.get()
        print(f"Consumidor recibe: {mensaje}")

if __name__ == "__main__":
    q = Queue()

    p1 = Process(target=productor, args=(q,))
    p2 = Process(target=consumidor, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
