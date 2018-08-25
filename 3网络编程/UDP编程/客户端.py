"""
TCP 建立可靠的连接，并且通信双方都可以通过流的方式发送数据
相对于 TCP 来说
UDP 是不需要建立连接的。只要知道对方的IP和端口号就能直接给其发送数据包
但是能不能到达就不知道了
虽然 UDP 传输是不可靠的 。但是相比 TCP来说  速度快 。
对于要求不高的数据可以使用 UDP (比如广播)
"""
import socket

# 参数1：指定协议   AF_INET ipv4   或者 AF_INET6 ipv6
# 参数2：SOCK_STREAM执行使用面向流的TCP协议
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);
udp.sendto('这个是数据'.encode('utf-8'), ('192.168.60.1', 8899))
data = udp.recv(1024).decode('utf-8')
print("服务器说：", data)
