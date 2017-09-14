import socket
import os
import threading
import time

class Client:
    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 5000
        self.acabou = False
        self.porta = ""
        self.teste = ""
        self.started = False

    def limpar(self):                                         #limpa o console
        os.system('cls' if os.name == 'nt' else 'clear')
		
    def input_ip(self):
        self.HOST = input(">Insira aqui o IP do servidor: ")
        self.teste = input(">Insira seu IP: ")
        self.porta = input(">Insira uma porta VALIDA (diferente de 5000): ")
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp.sendto((self.teste+" "+self.porta).encode(),(self.HOST, self.PORT))
        
    def send_udp(self):
       
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        while True:
            msg = input()
            udp.sendto(msg.encode(), (self.HOST, self.PORT))
    
    def receive_udp(self):
        
        print("Servidor UDP rodando!")

        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp.bind((self.teste, int(self.porta)))

        while True:
            data, addr = udp.recvfrom(1024)
            if data:
                if (data.decode() != "0") and (data.decode() != "1") and (data.decode() != "2") and (data.decode() != "3") and (data.decode() != "OBSERVE DE QUEM EH A VEZ DE JOGAR!") and (data.decode() != "999"):
                    self.limpar()
                    print(data.decode())
                else:
                    if data.decode() == "0":
                        self.started = True
                    if data.decode() == "1":
                        print("\nPLAYER 1 GANHOU!\n(Ctrl+C para sair)")
                        self.acabou = True
                        break
                    if data.decode() == "2":
                        print("\nPLAYER 2 GANHOU!\n(Ctrl+C para sair)")
                        self.acabou = True
                        break
                    if data.decode() == "3":
                        print("\nDEU VELHA!\n(Ctrl+C para sair)")
                        self.acabou = True
                        break
                    if data.decode() == "OBSERVE DE QUEM EH A VEZ DE JOGAR!":
                        print("\n"+data.decode())
                        if self.started == True:
                            udp.sendto("ok".encode(), (self.HOST, self.PORT))
                    if data.decode() == "999":
                        self.limpar()
                        print("CONEXAO PERDIDA COM O OUTRO PLAYER\n(Ctrl+C para sair)")
                        break
    
def main():
    b = Client()
    
    b.input_ip()
    
    t1 = threading.Thread(None,b.receive_udp)
    t1.start()
    
    while b.acabou == False:
        time.sleep(1)
        b.send_udp()
    
        
if __name__ == "__main__":
    main()

        