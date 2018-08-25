import socket

"""
客户端： 创建TCP连接的时候。主动发起连接的是客户端
服务器：接受客户端的连接
"""

# 1 创建一个socket
# 参数1：指定协议   AF_INET ipv4   或者 AF_INET6 ipv6
# 参数2：SOCK_STREAM执行使用面向流的TCP协议
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# 2 建立连接  192.168.43.181
# 参数1：要连接服务器的ip
# 参数2：要连接的端口信息
sk.connect(('www.sina.com.cn', 80))

# 3发送数据 模拟发送浏览器的请求头
sk.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 4接受数据
data = []

while True:
    # 一次接受 1k
    tempData = sk.recv(1024)
    # 如果有数据
    if tempData:
        data.append(tempData)
        pass
    else:
        pass
    pass
    # 将数据转出字符串
dataStr = (b''.join(data)).decode('utf-8')
print(dataStr)

# 5 断开连接
sk.close()