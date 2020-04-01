import socket as sk
import time
serverPort = 21
serverSocket = sk.socket(sk.AF_INET, sk.SOCK_STREAM) 
serverSocket.bind(('', serverPort))
serverSocket.listen(10)

# accept() accepts client connection and creates temporary socket
connectionSocket, addr = serverSocket.accept()
time.sleep(1) #Wait a second.

#Servidor 220 Welcome to the Client.
connectionSocket.send('220 Welcome \r\n'.encode('utf-8'))
print('Connected to', addr,'!')

while 1:

    time.sleep(0.5) #Half-second timer

    recv = connectionSocket.recv(1024) #Awaits the Client's response;
    print(recv.decode('UTF-8')) #Prints the Client response on the terminal;
    part = recv.decode('UTF-8').split() #Wrap the message into strings for conditions;

    #Analyzes the first string of the customer's message and sends the requested.
    
    if (part[0] == 'AUTH'): #Try TLS ou SSL
        connectionSocket.send('502 TLS e/ou SSL not implemented\r\n'.encode('utf-8'))
        recv = ''

    if (part[0] == 'USER'): #Client sends User.
        connectionSocket.send('331 PASSWORD\r\n'.encode('utf-8'))
        recv = ''

    if (part[0] == 'PASS'): #Client sends Password
        connectionSocket.send('230 Logado!\r\n'.encode('utf-8'))
        recv = ''

    if (part[0] == 'SYST'): #File System.
        connectionSocket.send('215 UNIX emulated by FileZilla\r\n'.encode('utf-8'))
        recv = ''

    if (part[0] == 'FEAT'):
        connectionSocket.send('211-Features:\r\n'.encode('utf-8'))
        connectionSocket.send('MDTM\r\n'.encode('utf-8'))
        connectionSocket.send('REST STREAM\r\n'.encode('utf-8'))
        connectionSocket.send('SIZE\r\n'.encode('utf-8'))
        connectionSocket.send('MLST type*;size*;modify*;\r\n'.encode('utf-8'))
        connectionSocket.send('MLSD\r\n'.encode('utf-8'))
        connectionSocket.send('UTF8\r\n'.encode('utf-8'))
        connectionSocket.send('CLNT\r\n'.encode('utf-8'))
        connectionSocket.send('MFMT\r\n'.encode('utf-8'))
        connectionSocket.send('EPSV\r\n'.encode('utf-8'))
        connectionSocket.send('EPRT\r\n'.encode('utf-8'))
        connectionSocket.send('211 End\r\n'.encode('utf-8'))
        recv = ''

    if (part[0] == 'PWD'): #Lists the default directory.
        connectionSocket.send('257 "/" is current directory.\r\n'.encode('utf-8'))
        recv = ''
        
    if (part[0] == 'CWD'): #Enter the default directory.
        connectionSocket.send('250 CWD successful. "/" is current directory.\r\n'.encode('utf-8'))
        recv = ''

    if (part[0] == 'MLSD'): 
        connectionSocket.send('150 Opening data channel for directory listing of "/"\r\n'.encode('utf-8'))
        time.sleep(1)
        connectionSocket.send('226 Successfully transferred "/"\r\n'.encode('utf-8'))
        recv = ''

    if (part[0] == 'TYPE'):
        connectionSocket.send('200 Type set to A\r\n'.encode('utf-8'))
        recv = ''
        #part = ''

    if (part[0] == 'PASV'): #Entering Passive Mode
        connectionSocket.send('227 Entering Passive Mode (127,0,0,1,197,226)\r\n'.encode('utf-8'))
        recv = ''

    if (part[0] == 'LIST'):
        connectionSocket.send('\r\n'.encode('utf-8'))
        recv = ''
    
    if (recv == 'RETR test.txt'): #Request: RETR test.txt
        connectionSocket.send('150 Opening data channel for file download from server of "/test.txt"\r\n'.encode('utf-8'))
        time.sleep(1)
        connectionSocket.send('226 Successfully transferred "/test.txt"\r\n'.encode('utf-8'))
        recv = ''
    
    if (recv == 'STOR desktop.ini'): #Request: STOR desktop.ini
        connectionSocket.send('150 Opening data channel for file upload to server of "/desktop.ini"\r\n'.encode('utf-8'))
        time.sleep(1)
        connectionSocket.send('226 Successfully transferred "/desktop.ini"\r\n'.encode('utf-8'))
        recv = ''
   
        
  
