# # shutil 模块
import shutil

#copy() 复制文件
#格式：shutil.copy(源路径，目的路径)
#拷贝的同时可以给文件命名
print("copy的用法和结果如下")
rst = shutil.copy("C:\\img/5.jpg","C:\\abc.jpg")
print(rst)
print("copy2()的用法和结果如下")
# 递归删除文件夹
shutil.rmtree()
#copy2() 复制文件，保留元数据（文件信息）
#格式：shutil.copy2(源路径，目标路径)
#返回值：返回目标路径
#注意：copy和copy2的唯一区别在于copy2复制文件时尽量保留元数据
print("copyfile()的用法和结果如下")
#copyfile()将一个文件中的  内容  复制到另外一个文件当中
#格式：shutil.copyfile('源路径','目标路径')
#返回值：无
print("move()的用法和结果如下")
#move() 移动文件/文件夹
#格式：shutil.move(源路径，目标路径)
#rst = shutil.move("C:\\abc.jpg","C:\\a")
print(rst)
import os
if not os.path.exists("C:\\abc.jpg"):
    print("已经移动走了")
elif os.path.exists("C:\\a\\abc.jpg"):
    print("exit")
else:
    shutil.move("C:\\abc.jpg", "C:\\a")
print("# 归档make_archive()的用法和结果如下")
#make_archive() 归档操作
#格式:shutil.make_archive(归档后的文件或目录名，后缀，需要归档的文件夹)
#Windows相当于压缩，后缀的格式只有zip、tar、gztar
#返回值：归档后的地址
# rst = shutil.make_archive("C:\\a","zip","C:\\a - secondary")
# if os.path.exists('C:\a.zip'):
#     print("cunzai")
# print(rst)
print("unpack_archive()的用法和结果如下")
# #unpack_archive() 解包操作
# #格式：shutil.unpack_archive(归档文件地址,解包后的地址)，
# #返回值：解包后的地址

