import socket
import threading

class Server:
    def __init__(self):
        self.HOST = ''

    def start_udp_server(self):
        PORT = 5000
        
        print("Servidor UDP rodando!")

        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp.bind((self.HOST, PORT))

        while True:
            data, addr = udp.recvfrom(1024)
            if data:
                print("(UDP)", addr, "-", data.decode())

    def start_tcp_server(self):
        PORT = 5001
        
        print("Servidor TCP rodando!")
        
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        tcp.bind((self.HOST, PORT))
        tcp.listen(50)

        def connect():
            print("(TCP) Conexao estabelecida por", addr)

            while True:
                data = conn.recv(1024)
                if data:
                    print("(TCP)", addr, "-", data.decode())
                else:
                    print("(TCP) Conexao de", addr, "encerrada.")
                    break
                conn.sendall(data)
        
        while True:
            conn, addr = tcp.accept()
            threading.Thread(None,connect).start()
            

def main():
    t1 = threading.Thread(None,Server().start_tcp_server)
    t1.start()
    t2 = threading.Thread(None,Server().start_udp_server)
    t2.start()

if __name__ == "__main__":
    main()
