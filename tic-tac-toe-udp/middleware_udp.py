from velha import *
import socket
import time

class Server:
    def __init__(self):
        self.HOST = ''
        self.PORT = 5000
        self.conexoes = []
        self.infolist = []
        self.started = False
        self.ok = []
        
    def enviar_todos(self, mensagem):
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp.sendto((mensagem).encode(), (self.infolist[0][0],int(self.infolist[0][1])))
        udp.sendto((mensagem).encode(), (self.infolist[1][0],int(self.infolist[1][1])))
        
    def validar_turno(self,addr,turno):
        if turno == 1 and self.conexoes[0] == addr:
            return True
        elif turno == -1 and self.conexoes[1] == addr:
            return True
        else: return False

    def inicializar(self):
        
        player_count = 1
        
        print("Servidor UDP rodando!")

        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp.bind((self.HOST, self.PORT))

        while player_count <= 2:
            data, addr = udp.recvfrom(1024)
            if data:
                info = (data.decode()).split(" ")
                self.infolist.append(info)
                time.sleep(0.5)
                if addr not in self.conexoes:
                    player_count += 1
                    msg = "Aguardando o outro player..."
                    udp.sendto(msg.encode(), (info[0],int(info[1])))
                print("(UDP)", addr, "-", data.decode())
        
        a = Velha()
        
        self.enviar_todos("\n>Fique digitando em ambos os clientes qualquer coisa: ")
        print(self.conexoes)
        
        while True:
            data, addr = udp.recvfrom(1024)
            if data:
                if addr[1] not in self.conexoes and len(self.conexoes) < 2:
                    self.conexoes.append(addr[1])
                elif data.decode() != "ok" and len(self.conexoes) == 2:
                    if self.validar_turno(addr[1],a.turno) == True:
                        self.started = True
                        jogada = a.jogar(data.decode())
                        if jogada == False:
                            self.enviar_todos(a.board_string())
                            self.enviar_todos("0")
                            self.ok = []
                        elif jogada == 1:
                            self.enviar_todos(a.board_string())
                            self.enviar_todos("1")
                            break
                        elif jogada == 2:
                            self.enviar_todos(a.board_string())
                            self.enviar_todos("2")
                            break
                        elif jogada == 3:
                            self.enviar_todos(a.board_string())
                            self.enviar_todos("3")
                            break
                    else:
                        self.enviar_todos("OBSERVE DE QUEM EH A VEZ DE JOGAR!")
                if data.decode() == "ok" and self.started == True:
                    time.sleep(0.5)
                    if len(self.ok) == 2:
                        self.ok = []
                    if addr[1] not in self.ok:
                        self.ok.append(addr[1])
                    else: 
                        self.enviar_todos("999")
                        print("CONEXAO PERDIDA COM UM DOS PLAYERS")
                        break

                

def main():
    Server().inicializar()
    
if __name__ == "__main__":
    main()
    quit()