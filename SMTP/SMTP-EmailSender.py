import socket as sk
import base64 as b64
import ssl

print ('\nFollow the instructions below to send an email.\n')
remetente = input("Sender's email:")
senha = input("Senha: ")
destino = input("Recipient's Email:")
msg = input("Message to be sent:")

clientSocket=sk.socket(sk.AF_INET,sk.SOCK_STREAM)
clientSocket.connect(('smtp.gmail.com',587))
recv=clientSocket.recv(1024)
print(recv.decode('utf-8'))

clientSocket.sendall(bytes('HELO gmail.com\r\n', 'utf-8'))
recv=clientSocket.recv(1024)
print(recv.decode('utf-8'))

clientSocket.send('STARTTLS\r\n'.encode('utf-8'))
recv=clientSocket.recv(1024)
print (recv.decode('utf-8'))

secureclientSocket=ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)

secureclientSocket.sendall(bytes('HELO gmail.com\r\n','utf-8'))
recv = secureclientSocket.recv(1024)
print(recv)

secureclientSocket.sendall(bytes('AUTH LOGIN\r\n', 'utf-8'))
recv=secureclientSocket.recv(1024)
print(recv)

encriptar = remetente

encriptar = b64.b64encode(bytes(encriptar, 'utf-8')) + bytes('\r\n','utf-8')
secureclientSocket.sendall(encriptar)

encriptar = senha

encriptar = b64.b64encode(bytes(encriptar, 'utf-8')) + bytes('\r\n','utf-8')
secureclientSocket.sendall(encriptar)

secureclientSocket.sendall(bytes('MAIL FROM: <'+ remetente + '>\r\n', 'utf-8'))
recv=secureclientSocket.recv(1024)

print(recv.decode('utf-8'))
secureclientSocket.sendall(bytes('RCPT TO: <'+ destino + '>\r\n', 'utf-8'))
recv=secureclientSocket.recv(1024)
print(recv.decode('utf-8'))
secureclientSocket.send('DATA'.encode('utf-8')+'\r\n'.encode('utf-8'))
recv=secureclientSocket.recv(1024)
print(recv.decode('utf-8'))
secureclientSocket.sendall(bytes(msg + '\r\n.\r\n', 'utf-8'))
recv=secureclientSocket.recv(1024)
print (recv.decode('utf-8'))
secureclientSocket.send('QUIT'.encode('utf-8')+'\r\n'.encode('utf-8'))
recv=secureclientSocket.recv(1024)
print (recv.decode('utf-8'))

secureclientSocket.close()
clientSocket.close()