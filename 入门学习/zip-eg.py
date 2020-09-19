# zip - 压缩包
    #模块名zipfile
import zipfile

print("ZipFile的用法和结果如下")
#格式：zipfile.ZipFile(files[,mode[,compression[,allowZip64]]])
#创建一个ZipFile对象，表示一个zip文件。参数file表示文件路径或类文件对象
zf = zipfile.ZipFile("C:\\a.zip")
print(zf)
print("getinfo()的用法和结果如下")
#ZipFile.getinfo(name)
#获取zip文档内指定文件的信息。
# 返回一个zipfile.ZipInfo对象，包括文件的详细信息
rst =zf.getinfo("abc.jpg")
print(rst)
print("namelist()的用法和结果如下")
#格式：ZipFile.namelist()
#获取zip文档内所有文件的名称列表
print("extractall()的用法和结果如下")
#ZipFile.extractall([path[,members[,pwd]]])
#解压zip文档中所有文件到当前目录。参数members的默认值为zip文档内所有文件名称列表











