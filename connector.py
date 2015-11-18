import ssl
import socket
import logging


class connector:

    def __init__(self,host,port):
        self.host = host
        self.port = port


    def connect(self,host,port):
        try: 
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sslsock = ssl.wrap_socket(self.sock)
        except socker.error as e:
            raise e
        try:
            self.sslsock.connect((host,int(port)))
        except socket.error as e: 
            raise e


    def send(self,request):
        try:
            self.sslsock.send(request + '\r\n')
            print request
        except socket.error as e:
            raise e


    def send_request(self,request):
        """ Sends a request and saves the response in object's field """
        self.connect(self.host,self.port)
        self.send(request)
        try:
            self.response = self.sslsock.recv(4096)
        except socket.error as e:
            raise e
        self.close()


    def response_should_be(self,pattern):
        if self.response.startswith(pattern):
            print self.response
            return self.response
        else:
            msg = "Response doesn't start with %s" % pattern + "\nResponse: " + self.response
            raise AssertionError(msg)


    def close(self):
        self.sock.close()
