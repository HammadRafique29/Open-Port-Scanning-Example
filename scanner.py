import socket
import threading
from queue import Queue

target = '192.168.2.107'

open_ports = []
threads = []
queue = Queue()


def fill_port_queue(port_list):
    for port in port_list:
        queue.put(port)


def scan():
    while not queue.empty():
        port = queue.get()
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            open_ports.append(port)
        except:
            pass


def threading_scan():
    for i in range(500):
        thread = threading.Thread(target=scan)
        threads.append(thread)


def start_threads():
    for thread in threads:
        thread.start()


def wait_for_threads():
    for thread in threads:
        thread.join()


ports = range(4000, 5010)
fill_port_queue(ports)
threading_scan()
start_threads()
wait_for_threads()

for i in open_ports:
    print('Open ports are {}'.format(i))
