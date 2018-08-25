import socket

# 1 创建一个socket
# 参数1：指定协议   AF_INET ipv4   或者 AF_INET6 ipv6
# 参数2：SOCK_STREAM执行使用面向流的TCP协议
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# 绑定IP端口
sk.bind(('192.168.43.181', 8080))

# 监听
sk.listen(10)

print('服务器启动......')

# 等待连接
# 客户端socket 客户端的地址
# 在这里写的话 只能接受一个连接
clientSocket, clientAddress = sk.accept()

print('服务器连接成功......%s:' % str(clientAddress))

while True:
    data = clientSocket.recv(1024)
    print(data.decode('utf-8'))
    clientSocket.send(("收到了你的消息%s" % (data.decode('utf-8'))).encode('utf-8'))
    pass
