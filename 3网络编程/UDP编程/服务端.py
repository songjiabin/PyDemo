import socket

# 参数1：指定协议   AF_INET ipv4   或者 AF_INET6 ipv6
# 参数2：SOCK_STREAM执行使用面向流的TCP协议
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
udp.bind(('192.168.60.1', 8899))

while True:
    data, address = udp.recvfrom(1024)
    print('客户端口说', data.decode())
    udp.sendto("收到".encode('utf-8'),address)
    pass
