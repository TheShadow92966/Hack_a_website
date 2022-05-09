import socket

site = input("Enter the website name you want to hack: ")
url = input("Enter the url of the website you want to hack: ")


mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((site, 80))
if "https" in url:
    print('OUTPU\n')
    cmd = 'GET url HTTPS/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        print(data.decode(), end = "")
    mysock.close()
else:
    print("OUTPUT\n")
    cmd = 'GET url HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        print(data.decode(), end = "")
    mysock.close()