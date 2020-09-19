"""
题目：输出指定格式的日期。
程序分析：使用 datetime 模块。
"""

import datetime

if __name__ == '__main__':
    # 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
    print(datetime.date.today().strftime('%Y-%m-%d'))

    # 创建日期对象
    miyazakiBirthDay = datetime.date(1941,1,5)

    print(miyazakiBirthDay.strftime('%d%m%Y'))

    #日期算数运算
    miyazakiBirthNextDay = miyazakiBirthDay + datetime.timedelta(days=1)

    print(miyazakiBirthNextDay.strftime('%Y-%m-%d'))

    #日期替换
    miyazakiFirstBirthDay = miyazakiBirthDay.replace(year=miyazakiBirthDay.year+1)

    print(miyazakiFirstBirthDay.strftime('%Y-%m-%d'))







