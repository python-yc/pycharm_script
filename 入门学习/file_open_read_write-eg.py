'''
- mode：表明文件有什么方式打开
    r ：以只读方式打开，文件不存在会报错
    w ：写方式打开，会覆盖已有文件，如果文件不存在会创建文件
    a ：append以追加方式打开，如果文件不存在创建文件
    x ：创建方式打开，如果文件存在，报错
    b ：binary，以二进制方式写入
    t ：文本方式打开
    + ：可读写
'''
'''
read:按字符从当前位置读取文件内容，若未指定读取长度，则会读取至结尾；
read(10):从光标所在位置读取10字符
readline:读取光标所在行
readlines：从光标所在行以  列表  形式读完文件内容
list(f):以打开的文件作为参数，创建列表
seek(offset,from)
    -移动文件的读取位置，也叫指针
    -from的取值范围：
    
        0:从文件头开始偏移
        1：从文件当前位置开始偏移
        2：从文件的末尾开始偏移
移动的单位是字节（byte），一个汉字也是一个字节，返回文件只针对当前位置

#with后的第一个r表示对后面引号内符号无特殊意义比如：\就是本身（推荐使用with）
with支持一次打开多个文件，格式如下
with open('file1','r') as f1, open('file2','r') as f2, open('file3','r') as f3
'''
#以写的方式打开
#文件打开后，不使用规范关闭，以免出现错误
f = open("C:\\a.txt","w")
f.close()
#with语句
#-with使用的技术是一种为上下文管理协议的技术（ContextManagementProtocol）
#-自动判断文件的作用域，自动关闭不在使用的打开文件句柄
with open(r"C:test01.txt",'w') as f:
    f.write("i love you !")
    f.write("我爱你中国，我的母亲!")
#下面语句块开始对文件f进行操作，不需要使用close函数，推荐使用with
#with后的第一个r好像可有可无
with open(r"C:test01.txt",'r') as f:
    #按行读取内容，括号内表示读取个数，虽然不加参数时表示行，但此时加参数后不是行数而是字节数
    strline = f.readline(3)
    #此循环保证能够完整读取文件直至结束，不为空即为真
    while strline:
        print(strline)
        strline = f.readline()

#seek案例
#打开文件后，从第5个字节开始读取，即打开后需要移动4个字节
with open(r"C:test01.txt",'r') as f :
    f.seek(4,0)
    strChar = f.read(10)
    print(strChar)

print("============以下是tell()的用法和结果===============")
#tell 函数：用来显示文件读写指针的当前位置，也是字节数
#加上 print(f.tell())
print("============一下是write()和writelines()的用法和结果===========")
'''
- write(str):把字符串写入文件
- writelines(str):把字符串按行写入文件
- 区别：
    write函数参数只能是字符串
    writelines参数可以是字符串，也可以是字符串序列
    - 案例open-eg
'''
l = ['1','2','3']
with open(r"C:test01.txt",'w') as f:
    f.write("loving life")
    f.write("harding more")
    f.writelines(l)

with open(r"C:test01.txt",'r') as f:
    print(f.readlines())

print("#####以下是序列化与反序列化的使用#####")
'''
##序列化 - pickle
- 也成为持久化，落地：把程序 运行中 的信息保存在磁盘上
##反序列化：序列化的逆过程
- pickle：python提供的序列化模块
- pickle.dump：序列化
- pickle.load：反序列化
'''
#序列化
import pickle

age = 19
with open("C:test01.txt",'wb') as f:
    pickle.dump(age,f)

#反序列化
with open("C:test01.txt",'rb') as f:
    age = pickle.load(f)
    print(age)

'''
# ##序列化-shelve
# - 持久化工具
# - 类似字典，用k,v保存数据，存取方式跟字典也类似
# - open，close
# - shelve 特殊性
- 不支持多个应用并行写入,但是可以多个一起读取
    为了解决这个问题，open的时候可以使用flag=r
- 写回问题
    shelve默认情况写会等待持久化对象进行任何修改
    解决方法：强制写回：writeback=True
'''
import shelve

#打开文件
#shv相当于一个字典
shv = shelve.open("C:\\shv\\shv.db")
shv["one"] = 1
shv["two"] = 2
shv["three"] = 3

shv.close()

print("############shelve读取案例######################")
shv = shelve.open("C:\\shv\\shv.db",flag="r")  #或者这样表达
#shv = shelve.open("C:\\shv\\shv.db")   可以不加flag参数
#此处并不是多个一起读取
try:
    print(shv["one"])
    print(shv["two"])
except Exception as e:
    print("居然有错误，很烦")
finally:
    shv.close()

shv = shelve.open("C:\\shv\\shv.db",writeback=True)
shv["one"] = {"eins":1,"zwei":2,"drei":3}
try:
    k1 = shv["one"]
    print(k1)
    k1["eins"] = 100
finally:
    shv.close()

shv = shelve.open("C:\\shv\\shv.db")
print(k1,"ooo")
shv.close()
