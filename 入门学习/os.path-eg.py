# #os.path模块，与路径相关
import os.path as op

print("abspath的用法和结果如下")
#abspath() 将路径转化为绝对路径   --abselute
#格式：os.path.abspath('路径')
#返回值：路径的绝对形式
absp = op.abspath(".")
print("当前绝对路径为：",absp)
print("basename()的用法和结果如下")
#basename()获取路径中的文件名部分
#格式：os.path.basename(路径)
#返回值：文件名字符串
bn = op.basename("C:\\img/5.jpg")
print(bn)
print("join的用法和结果如下")
#join()将多个路径拼合成一个路径
#格式：os.path.join(路径1，路径2......)
#返回值：组合后的新路径字符串
bn = op.join("C:\\img", "cookie")
print(bn)
#dirname()获取路径中除最后部分的路径
# os.path.dirname(路径1)
# 返回值：字符串
print(op.dirname(bn))
print("spilt的用法和结果如下")
#spilt() 将路径切割为文件夹部分和当前文件部分
#spilt还能根据相应的分隔符（分隔符为，。等等）切割内容
#格式：os.path.spilt(路径)
#返回值：路径和文件名组成的元组
t = op.split("C:\\img/tupian/dir/5.jpg")
print(t)
print("isdir的用法和结果如下")
#isdir() 检查是否是目录
#格式：os.path.isdir(路径)
#返回值：布尔值
rst = op.isdir("C:\\img/5.jpg")
print(rst)
print("exists的用法和结果如下")
#exists() 检测文件或者目录是否存在
#格式：os.path.exists(路径)
#返回值：布尔值
e = op.exists("C:\\img")
print(e)

