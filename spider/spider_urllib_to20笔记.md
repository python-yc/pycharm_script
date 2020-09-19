# 爬虫准备工作
- 参考资料
    - python网络数据采集·图灵工业出版
    - 精通Python爬虫框架scrapy·人民邮电出版社
    - [Python3网络爬虫](http://blog.csdn.net/c406495762/article/details/72858983)
    - [Scrapy官方教程](http://scrapy-chs.readthedos.io/zh_CN/0.24/intro/tutorial.html)
- 前提知识
    - url
    - http协议
    - web前端 html,css,js
    - ajax
    - re, xpath
    - xml

# 1 爬虫简介
- 爬虫定义：网络爬虫（又被称为网页蜘蛛，网络机器人，在FOAF社区中间，更经常成为网页追逐者）
是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本
另外一些不常使用的名字还有蚂蚁，自动索引，模拟程序或者蠕虫
- 两大特征：
    - 能按作者要求下载数据或者内容
    - 能自动在网络上流窜
- 三大步骤
    - 下载网页
    - 提取正确的信息
    - 根据规则自动跳到另外的网页上执行上两步内容
- 爬虫分类
    - 通用爬虫
    - 专用爬虫（聚焦爬虫）
- Python网络包简介
    - python2.x：urllib、urllib2、urllib3、httplib、httplib2、requests
    - python3.x：urllib、urllib3、httplib2、requests

# 2 urllib
- 包含模块
    - urllib.request：打开和读取urls
    - urllib.error：包含urllib.request产生的常见错误，使用try捕捉
    - urllib.parse：包含解析url的方法
    - urllib.robotparse：解析robots.txt文件
    - 案例一simple_urllib_1.py

- 网页编码问题解决
    - chardet   可以自动检测网页编码格式，但是可能有误
    - 需要安装 pip install chardet
    - 案例simple_urllib_2_chardet.py

# 2.1 urllib中request模块
- urlopen 的返回对象
    - 案例simple_urllib_3_rsp.py
    # 具有的一下函数
    - geturl(): 返回请求对象的url
    - info()：请求返回对象的meta信息
    - getcode()：返回的http code

- requese.data的使用
    - 访问网络的两种方法
        - get
            - 利用参数给服务器传递信息
            - 参数为dict，然后用parse编码，如：parse.urlencode(qs)
            - 案例simple_urllib_4_parse.py
        - post
            - 一般向服务器传递参数使用
            - post是把信息自动加密处理
            - 我们如果想使用post信息，需要用到data参数
            - 使用post 意味着Http的请求头可能需要更改：
                - Conten-Type:application/x-www(json) form-urlencode  ## form-data中的kw就是keyword的缩写
                - Content-Length:数据长度
                - 简而言之，一旦更改请求方法，请注意其他请求头部信息相适应
            - urllib.parse.urlencode可以将字符串自动转换成上面的
            - 案例simple_urllib_5_post1.py
            - 为了更多的设置请求消息，单纯的通过urlopen函数已经不太好用了
            - 需要利用request.Request 类
            - 案例simple_urllib_5_post2.py    

# 2.2 urllib中error 模块
- urllib.error

- URLError产生的原因：
    - 没网、服务器连接失败、不知道定制服务器
    - 是OSError的子类
    - 案例simple_urllib_6_urlerror.py

- HTTPError, 是URLError的一个子类
- 案例simple_urllib_7_httperror.py

- URLError和HTTPError两者区别
    - HTTPError是对应的HTTP请求的返回错误码，如果返回的错误码是400以上的，则引发HTTPError
    - URLError对应的一般是网络出现的问题，包括url问题
    - 关系区别OSError-URLError-HTTPError

- UserAgent
    - UserAgent: 用户代理，简称UA，属于headers的一部分，服务器通过UA来判断访问者的身份
    - 常见的UA值，使用的时候可以直接复制粘贴，也可以用浏览器访问的时候抓包
    如：Chrome（可以直接在网页F12获取复制）
    - Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36
- 设置UA可以通过两种方式：
    - headers
    - 案例simple_urllib_8_header1.py
    - add_header
    - 案例simple_urllib_8_header2.py

- ProxyHandler处理（代理服务器）
    - 分公有代理和私有代理两种，私有代理收费
    - 使用代理IP，是爬虫的常用手段
    - 获取代理服务地址
        - www.xicidaili.com
        - www.goubanjia.com
    - 代理用来隐藏真实访问，代理也不允许频繁访问某一个固定网站，所以代理一定要很多
    - 基本使用步骤：
        1、设置代理地址
        2、创建ProxyHandler
        3、创建Opener
        4、安装Opener
    - 案例simple_urllib_9_proxy.py

- cookie & session
    - 由于http协议的无记忆性，人们为了弥补这个缺憾，所以采用的一个补充协议
    - cookie是发给用户（即http浏览器）的一段信息，session是保存在服务器上的对应的
       一半信息，用来记录用户信息
    
    - cookie和session的区别
        - 存放位置不同
        - cookie不安全
        - session会保存在服务器上一定时间，会过期
        - 单个cookie保存数据不超过4k，很多浏览器限制一个站点最多保存20个
    
    - session的存放位置
        - 存在服务器端
        - 一半情况，session是放在内存中或者数据库中
        - 没有cookie登录
        - 案例simple_urllib_10_nocookie.py(没有cookie的登录会跳转到登录界面)
    
    - 使用cookie登录
        - 直接把cookie赋值下来，然后手动放入请求头
        - 案例simple_urllib_10_usecookie.py
        
# http模块包含一些关于cookie的模块，通过他们，我们可以自动使用cookie
    - CookieJar
        - 管理存储cookie，向传出的http请求添加cookie
        - cookie存储在内存中，CookieJar实例回收后将消失
    - FileCookieJar(filename, delayload=None, policy=None):
        - 使用文件管理cookie
        - filename保存cookie的文件
    - MozillaCookieJar(filename, delayload=None, policy=None):
        - 创建与mocilla浏览器cookie.txt兼容的FileCookieJar实例
    - LwpCookieJar(filename, delayload=None, policy=None):
        - 创建与livwww-perl标准兼容的Set-Cookie3格式的FileCookieJar实例
    - 他们的关系是：CookieJar-->FileCookieJar-->MozillaCookieJar & LwpCookieJar

## 利用cookiejar访问人人网，案例simple_http_11_usecookiejar.py
        - 自动使用cookie登录，大致流程：
        - 1、打开登录页面后自动通过用户名密码登录
        - 2、自动提取反馈回来的cookie
        - 3、利用提取的cookie登录个人页面

    - handler 是Handler的实例，常用参看案例11代码
        - 用来处理复杂的请求
            # 生成cookie管理器
            cookie_handler = request.HTTPCookieProcessor(cookie)
            # 创建http请求管理器
            http_handler = request.HTTPHandler()
            # 创建https管理器
            https_handler = request.HTTPSHandler()

    - 创立handler后，使用opener打开，打开后相应的业务由相应的handler处理
    - cookie作为一个变量，打印出来
    - 案例simple_http_12_printcookie.py
        - cookie的属性
            - name：名称
            - value：值
            - domain：可以访问此cookie的域名
            - path：可以访问此cookie的页面路径
            - expires：过期时间
            - size：大小
            - Http字段
## MozillaCookieJar(一般使用这个类) - 用于保存cookie（称为落地，即保存在计算机内）
    - 案例simple_http_13_filecookiejar.py
## cookie的读取（即保存依次，以后直接读取这个文件即可）
    - 案例simple_http_14_readcookie.py
## SSL
    - SSL证书就是指遵守SSL安全套阶层协议服务器数字证书(SecureSocketLayer)
    - 美国网景公司开发
    - CA(CertifacateAuthority)是数字证书认证中心，就是发放、管理、废除数字证书的收信人的第三方机构
    - 遇到不信任的SSL证书，需要单独处理，一行代码(ssl._create_default_https_context = ssl._create_unverified_context)
    - 案例simple_http_15_ssldeal.py
## js加密
    - 有的反爬虫策略采用js对需要传输的数据进行加密处理（通常是md5值）
    - 经过加密，传输的就是密文，但是
    - 加密函数或者过程一定是在浏览器完成，也就是一定会把代码（js代码）暴露给使用者
    - 通过阅读加密算法，就可以模拟出加密过程，从而达到破解
    ## 在线代码格式化（http://tool.oschina.net/codeformat/js）
    - 案例simple_urllib_17_dealjs1.py
    - 案例simple_urllib_17_dealjs2.py

## ajax
    - 异步请求
    - 一定会有url，请求方法，可能有数据
    - 一般使用json格式
    - 案例，爬豆瓣电影数据simple_ajax_18_douban.py
    
## Requests-献给人类的模块（非常好用）
- HTTP for Humans，更简洁，更友好
- 继承了urllib的所有特征
- 底层使用的是urllib3
- 开源地址：https://github.com/requests/requests
- 中文文档：http://docs.python-requests.org/zh_CN/latest/index.html
- (有时间读读此文档，很优秀，这个不是python自带的，要想使用，自行安装)
### 使用1、get请求
    - requests.get()
    - requests.request("get", url)
    - 可以带有headers和params
    - 案例simple_requests_19_get1.py
- get返回内容
    - 案例simple_requests_19_get2.py
    - 返回属性可以通过采用断点然后debug进行查找，属性在rsp内，所有属性均可以打印
    - 常见属性rsp.text、rsp.content、rsp.url、rsp.encoding、rsp.status_code、rsp.cookie
- post
    - rsp = requests.post(url, data=data)
    - 案例simple_requests_20_post.py
    - data、headers要求dict类型，比request要方便多了

## proxy
- 此处只大致说一下代码，就没有演示
    proxies = {
        "http": "address of proxy",
        "https": "address of proxy"
    }
    rsp = requests.request("get", "http:xxxx", proxies=proxies)
    - 代理有可能报错，如果使用人数多，考虑安全问题，可能会强行关闭

- 用户验证
    - 代理验证
        # 可能需要HTTP basic Auth 可以这样
        # 格式为  用户名:密码@代理地址:端口地址
        proxy = { "http": "china:123456@162.168.1.123:6666" }
        rsp = requests.get("http:/www.baidu.com", proxies=proxy)
    - web客户端验证
        - 如果遇到web客户端严重，需要添加auth=(用户名, 密码)
            auth=("test1", "123456") # 授权信息
            rsp = requests.get("http://www.baidu.com", auth=auth)
- requests处理cookie
    - requests可以自动处理cookie信息
    
        rsp = requests.get("http://xxx")
        # 如果对方服务器给传送过来cookie信息，则可以通过反馈cookie属性得到
        # 返回一个CookieJar实例
        cookiejar = rsp.cookies
        
        # 可以将cookiejar转换成字典
        cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
- session
    - 与服务器端session是不一样的东西
    - 模拟一次会话，从客户端浏览器连接服务器开始，到客户端浏览器断开
    - 能让我们跨请求保持某些参数，比如在同一个session实例发出的 所有请求之间保持cookie
    
        # 创建session对象，可以保持cookie值
        ss = requests.session()
        headers = {"User-Agent": "xxxxxxxxxx" }
        data = { "name": "xxxxxxxxxxx" }
        # 此时，由创建的session管理请求负责发出请求
        ss.post("http://www.baidu.com", data=data, headers=headers)
        rsp = ss.get("http://www.baidu.com")

- https请求验证ssl整数
    - 参数verify负责表示是否需要验证ssl证书，默认是True
    - 如果不需要验证ssl整数，则设置成False表示关闭
        rsp = requests.get("https://www.baidu.com", verify=False)
        # 如果用verify=True访问12306，会报错，因为它证书有问题（自己做的）
        












