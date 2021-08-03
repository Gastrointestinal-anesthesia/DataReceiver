import socket

class MonitorSocket:
    # 创建套接字 socket
    TCPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, port):
        self.__port = port
        # 绑定本地信息 bind
        self.TCPServerSocket.bind(("", port))
        # 让默认的套接字由主动变为被动 listen
        self.TCPServerSocket.listen(128)
        # 等待客户端的链接 accept
        self.ClientSocket, clientAddr = self.TCPServerSocket.accept()
        print(clientAddr)

    def __del__(self):
        self.TCPServerSocket.close()
        self.ClientSocket.close()
        print("Connection deinit on port %d" % self.__port)

    def ReceiveAPackage(self):
        return self.ClientSocket.recv(1024)
