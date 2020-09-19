"""
# 6.2 TCP编程
- 面向连接的传输，即每次传输之前都需要先建立一个链接
- 客户端和服务器两个程序需要编写
- Server端的编写流程
    - 1.建立socket负责具体通信，这个socket其实只负责接受对方的请求
    - 2.绑定端口号和地址
    - 3.监听接入的访问socket
    - 4.接收访问的socket，可以理解接受访问即建立了一个通讯的连接通路
    - 5.接收对方的发送内容，利用接收到的socket接收内容
    - 6.如果有必要，给对方发送反馈信息
    - 7.关闭连接通路
"""

#socket模块负责socket编程
import socket

#模拟服务器的函数
def tcp_srv():
    #1.建立socket，建立socket，socket是负责具体通信的一个实例
    #需要用到两个参数
    #socket.AF_INET：使用ipv4协议
    #socket.SOCK_DGRAM：使用UDP通信
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2.绑定ip和port
    #127.0.0.1：这个ip地址代表的是机器本身
    #78998：自己指定一个端口号
    #地址是一个tuple类型，（ip，port）
    addr = ("127.0.0.1",8998)
    sock.bind(addr)

    #3.监听接入的访问socket
    sock.listen()

    while True:
        # 4.接受访问的socket，可以理解接受访问即建立了一个通讯的连接通路
        # accept返回的元组第一个元素赋值给skt，第二个赋值给addr
        skt, addr = sock.accept()
        # 5.接收对方的发送内容，利用接收到的socket接收内容
        # 500代表接收使用的buffersize
        #msg = skt.reveive(500)
        msg = skt.recv(500)
        # 接收到的是bytes格式内容
        #想得到str格式的需要进行解码

        rst = "Received msg:{0} from {1}".format(msg,addr)
        print(rst)
        # 6.如果有必要，给对方发送反馈消息
        skt.send(rst.decode())

        # 7.关闭连接通路
        skt.close()


if __name__ == '__main__':
    print("Starting server......")
    tcp_srv()
    print("Ending server......")







