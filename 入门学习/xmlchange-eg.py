"""
import xml.etree.ElementTree as et

tree = et.parse(r'to_edit.xml')

root = tree.getroot()

for e in root.iter('Name'):
    name = stu.find('Name')

    fi name != None:
    name.set('test',name.text *2)

stu = root.find('Student')

#生成一个新的元素
e = et.Element('ADDer')
e.attrib = {'a','b'}
e.text = '我加的'

stu.append(e)

#把修改的内容写进文件，否则修改无效
tree.write('to_edit.xml')
"""
#==========================================================
import xml.dom.minidom

#在内存中创建一个空的文档
doc = xml.dom.minidom.Document()
#创建一个根节点Managers对象
root = doc.createElement('Managers')
#设置根节点的属性
root.setAttribute('company','xx科技')
root.setAttribute('address','生命科技小镇')
#将根节点添加到文档对象中
doc.appendChild(root)

managerList = [{'name':'joy','age':18,'sex':'boy'},
               {'name':'tom','age':22,'sex':'girl'},
               {'name':'ruby','age':23,'sex':'girl'}
               ]
for i in managerList:
    nodeManager = doc.createElement('Manager')
    nodeName = doc.createElement('name')
    #给子节点name设置一个文本节点，用于显示文本内容
    nodeName.appendChild(doc.createTextNode(str(i['name'])))

    nodeAge = doc.createTextNode('age')
    nodeAge.appendChild(doc.createTextNode(str(i['age'])))

    nodeSex = doc.createTextNode('sex')
    nodeSex.appendChild(doc.createTextNode(str(i['sex'])))

    #将各叶子节点添加到父节点Manager中
    #最后将Manager添加到根节点Managers中
    nodeManager.appendChild(nodeName)
    nodeManager.appendChild(nodeAge)
    nodeManager.appendChild(nodeSex)
    root.appendChild(nodeManager)
#开始写xml文档
fp = open('Manager.xml','w')
doc.writexml(fp,indent='\t',addindent='\t',newl='\n',encoding='utf-8')

#==========================================================

"""
import xml.etree.ElementTree as et

#在内存中创建一个空文件
etree = et.ElementTree()

e = et.Element('Student')

etree._setroot(e)

e_name = et.SubElement(e,'Name')
e_name.text = 'hahaha'

etree.write('v06.xml')      #保存在文件内
"""
