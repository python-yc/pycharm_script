import socket

"""
- Client端流程
    - 1.建立通信的socket
    - 2.发送内容到指定服务器
    - 3.接受服务器给定的反馈内容
"""
def clientFunc():
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    text = "I love you !"

    #发送的数据必须是bytes格式
    data = text.encode()

    #发送，("127.0.0.1",7852)这个可以用变量代替，与服务端的形式那样
    sock.sendto(data,("127.0.0.1",7852))

    data, addr = sock.recvfrom(300)

    data = data.decode()

    print(data)

if __name__ == '__main__':
    clientFunc()


