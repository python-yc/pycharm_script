addrbook1 = {}
addrbook2 = {}

def read_address():
    '''
    read address from txt
    :return: 
    '''
    file1 = open("C:/address_book1.txt")
    lines1 = file1.readlines()  #列表
    for line in lines1:
        line = line.strip()            #去空白
        content = line.split(',')    #分割样式：[小明,电话]
        addrbook1[content[0]] = content[1]
    file1.close()

    with open("C:/address_book2.txt") as file2:
        lines2 = file2.readlines()  #列表
        for line in lines2:
            line = line.strip()            #去空白
            content = line.split(',')    #分割样式：[小明,电话]
            addrbook2[content[0]] = content[1]

def merge_address():
    lines = []
    header = "姓名\t      电话\t        邮箱\n"
    lines.append(header)
    for key in addrbook1.keys():
        line = ''
        if key in addrbook2.keys():
            line += '\t'.join([key,addrbook1[key],addrbook2[key]])
            line += '\n'
        else:
            line += '\t'.join([key,addrbook1[key],"*************"])
            line += '\n'
        lines.append(line)

    for key in addrbook2.keys():
        line = ''
        if key not in addrbook1.keys():
            line += '\t'.join([key,"*************",addrbook2[key]])
            line += '\n'
        lines.append(line)

    with open("C:/new_address_book1.txt",'w',encoding='utf-8') as newfile:
        newfile.writelines(lines)

if __name__ == '__main__':
    read_address()
    merge_address()
    print(addrbook1)
    print(addrbook2)



