import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))   #80 is port address
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()  # \r\n stands for "return in new line" 
#\r\n is twice bcoz after the get request if the blank line exist then it indictes its the end of req and nomore headers
# encoded bcoz it should be in " UTF8 "
mysock.send(cmd)

while True:  # loop is to wait until it receives all the data 
    data = mysock.recv(512) #here 512 is no of character 
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()