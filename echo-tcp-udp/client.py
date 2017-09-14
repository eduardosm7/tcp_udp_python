import socket

def show():
    print("============================================================")
    print("Escolha um número para selecionar o tipo de protocolo")
    print("1. UDP")
    print("2. TCP")

def escolher():
    while True:
        try:
            protocolo = int(input(">"))
            if protocolo == 1 or protocolo == 2:
                print("============================================================")
                return protocolo
            else:
                print("Escolha um numero valido.")
        except:
            print("Escolha um numero valido.")

class Client:
    def __init__(self):
        self.HOST = '127.0.0.1'

    def start_udp(self):
        PORT = 5000

        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        print("Para encerrar, aperte Return numa linha vazia.")
        while True:
            msg = input(">")
            udp.sendto(msg.encode(), (self.HOST, PORT))
            if msg == "":
                print("============================================================")
                break
    
    def start_tcp(self):
        PORT = 5001
        
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.connect((self.HOST, PORT))
        
        print("====================Conexao estabelecida====================")
        print("Para encerrar a conexao, aperte Return numa linha vazia.")
        while True:
            msg = input(">")
            if msg == "":
                print("=====================Conexao encerrada======================")
                print("============================================================")
                tcp.close()
                break
            tcp.sendall(msg.encode())
            data = tcp.recv(1024).decode()
            print("Recebimento confirmado:", repr(data))

def main():
    show()
    protocolo = escolher()
    if protocolo == 1:
        try:
            Client().start_udp()
        except:
            print("Nao foi possivel se conectar ao servidor.")
            print("============================================================")
    elif protocolo == 2:
        try:
            Client().start_tcp()
        except:
            print("Nao foi possivel se conectar ao servidor.")
            print("============================================================")

if __name__ == "__main__":
    main()
