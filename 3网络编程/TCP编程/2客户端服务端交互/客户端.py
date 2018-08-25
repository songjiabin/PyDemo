import socket

# 1 创建一个socket
# 参数1：指定协议   AF_INET ipv4   或者 AF_INET6 ipv6
# 参数2：SOCK_STREAM执行使用面向流的TCP协议
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# 2 建立连接  192.168.43.181
# 参数1：要连接服务器的ip
# 参数2：要连接的端口信息
sk.connect(('192.168.43.181', 8080))

while True:
    data = input("请输入给服务器发送的数据")
    sk.send(data.encode("utf-8"))
    info = sk.recv(1024)
    print(("服务器的数据是:%s" % (info.decode('utf-8'))))
    pass


