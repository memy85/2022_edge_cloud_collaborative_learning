
import socket


class Sender:
    
    def __init__(self, my_ip_address, receiver_ip_address, port):
        self.ip_address = my_ip_address
        self.receiver_ip_address = receiver_ip_address
        self.port = port
    
    def send_function(self, data):
        pass
    
    @call
    def socket_open(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.ip_address, self.port))
        
    
    def send_signal(self):
        '''
        By given status, the Manager will call the Sender to send a signal to other devices.
        If there is a match, it returns a connection enabled signal to the Mananger.
        '''
        pass
        
    
    
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('172.30.1.55', 9000)) # ip주소, 포트번호 지정 
server_socket.listen(4) # 클라이언트의 연결요청을 기다리는 상태 
client_socket, addr = server_socket.accept() # 연결 요청을 수락함. 그러면 아이피주소, 포트등 데이터를 return 
print(client_socket, "has connected")
data = client_socket.recv(65535) # 클라이언트로 부터 데이터를 받음. 출력되는 버퍼 사이즈. (만약 2할 경우, 2개의 데이터만 전송됨) 
print("받은 데이터:", data.decode())

if "__name__" == "__main__":
    