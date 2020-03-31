import socket

HOST = ''              # Server IP Address
PORT = 15000           # Server port

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((HOST, PORT))
tcp.listen(1)

print ('\nConnection OK ')

while True:
    connection, client = tcp.accept()
    print ('Connection made by', client)

    msg = connection.recv(1024)
     
    file=msg.decode('utf-8')
    print (file)
    
    m = file.split('\r\n',10)
    file_n = m[0].split(' ',3);
    file_n[1] = file_n[1].replace('/','')
    print (file_n[1])
    file_name = file_n[1]
    
    try:
        f=open(file_name, 'r')
        str = f.read()
        l = len(str)
        f.close()
        connection.sendall(bytearray("HTTP/1.1 200 OK\n","ascii"))
        connection.sendall(bytearray("\n","ascii"))
        connection.sendall(bytearray(str,"ascii"))
    except IOError:
        connection.send('HTTP/1.1 404 Not Found\r\nServer: LocalHost HTTP server\r\nContent-Type: text/html\r\n\r\n<html>\r\n<head>\r\n<title>Error!</title></head ><body><h1>\r\n404 Not Found \r\n</h1></body></html>\r\n'.encode('utf-8'))
        print('\nThe requested file does not exist.')                    

    print ('Connection terminated by ', client)
    connection.close()
