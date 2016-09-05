import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))

print('bind udp on 999...')
while True:
    print('aaaaaaaa')
    data, addr = s.recvfrom(1024)
    print('aaaaaaaaaaaaaaaaaaaaa')
    print('received from %s:%s.' % addr)
    s.sendto(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'), addr)
