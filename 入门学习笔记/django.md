# 1、 Django系统
- 环境
    - python3.6
    - django1.8
- 参考资料
    - django架站的16堂课     --书本
# 1.1 环境搭建
- anaconda+pycharm
- anaconda使用
    - conda list：显示当前环境安装的包
    - conda env list：显示安装的虚拟环境列表
    - conda create -n env_name python=3.6
    - 激活conda的虚拟环境
        - (Linux)source activate env_name
        - (win)activate env_name
    - pip install django==1.8
# 1.2 后台需要的流程
# 创建第一个django程序
- django-admin startproject python_django       路径：C:\Users\Administrator\python_django(被剪切到D盘了)
## 两种启动方式：
    - 1、命令行启动
        cd  C:\Users\Administrator\python_django
        python manage.py runserver
    - 2、pycharm 启动
        - 需要配置(anaconda)
        - 将相应的文件粘贴到此路径下，可以在此处显示（比如你创建的文件在C盘内）
        - 运行manage.py文件
        - 然后在菜单下面一行的右上角运行处，点击正在运行的文件进行编辑，然后在
        Script params 后面输入runserver保存即可。然后再运行manag.py文件就可以出现对应信息
# 2.1 路由系统-urls
- 创建app
    - app：负责一个具体业务或者一类具体业务的木块
    - 在python_django内创建一个名为teacher的app文件夹 
    cd  C:\Users\Administrator\python_django
    python manage.py startapp teacher
- 路由
    - 按照具体的请求url，导入到相应的业务处理模块的一个功能
    - django的信息控制中枢
    - 本质上是接受的URL和相应的处理模块的一个映射
    - 在接受URL请求的匹配上使用re（正则）
    - URL的具体格式urls.py中所示
- 需要关注两点：
    1、 接受的URL是什么，即如何用re对传入URL进行匹配
    2、 已知URL匹配到哪个处理模块
- url匹配规则
    - 从上往下一个一个对比
    - url格式是分级格式，则按照级别一级一级往下比对，主要对应url包含子url的额情况
    - 子url一旦被调用，则不会返回到主url
        - `/one/two/three/`
    - 正则以r开头，表示不需要转义，注意尖号(^)：开头和美元符号($)：结尾
        - '/one/two/three/' 配对 r'^one/' (注意：第一个不需要加/，路由会自动去掉url中的第一个/)
        - '/oo/one/two/three' 不配对 r'^one/'
        - '/one/two/three'  配对 r'three/$'   (注意：末尾的/不能省略)
        - '/oo/one/two/three/oo'    不配对 r'three/$'
        - 开头不需要有反斜杠
        - 如果从上向下都没有找到合适的匹配内容，则报错
# 2.2 正常映射
- 把某一个符合re的url映射到事物处理函数中去
    - 举例如下：
        '''
        from showeast import views as sv
        
        urlpatterns = [
            url(r'^admin/',admin.site.urls),
            url(r'^normalmap/',sv.normalmap),
        ]
        '''
# 2.3 URL 中带参数映射
- 在事件处理代码中需要由URL传入参数，形如/myurl/param中的param
- 参数都是字符串形式，如果需要整数等形式需要自行转换
- 通常的形式如下：
    '''
    /serarch/page/432   中的432需要经常变换
    '''
# 2.4 URL在app中处理
- 如果所有应用URL都集中在python_django/urls.py中，可能导致文件的臃肿
- 可以把urls具体功能逐渐分散到每个app中
    - 从django.conf.urls 导入 include
    - 注意此时re部分的写法
    - 添加include导入
- 使用方法：
    - 确保include被导入
    - 写主路由的开头url
    - 写子路由
    - 编写views函数
- 同样可以使用参数
# 2.5 URL 中的嵌套参数
- 抽取某个参数的一部分
    - 例如URL /index/page- ，需要捕获数字3作为参数
    '''
    url(r'index_1/(page-(\d+)/)?$',sv.myindex_1),   #不太好
    url(r'index_2/(?:page-(?P<page_number>\d+)/)?$',sv.myindex_2),  #好
    '''
    - 上述例子会得到两个参数，但?: 表明忽略此参数(page-这么多忽略)
# 2.6 传递额外参数
- 参数不仅仅来自于URL，还可能是我们自己定义的内容
'''
url(r'extrem/$',sv.extreParam,{'name':"xiaohong'}),
'''
- 附加参数同样适用于include语句，此时对include内所有都添加
# 2.7 URL的反向解析
- 防止硬编码
- 本质上是对每一个URL进行命名
- 以后在编码代码中使用URL的值(这样在url参数改变时，值可以使用同一个不影响结果)，原则上都应该使用反向解析
# 3 views 视图
# 3.1 视图概述
- 视图即视图函数，接收web响应的事物处理函数，
- 响应指符合http协议要求的任何内容，包括json、strong、html等
- 本章忽略事物处理，重点在如何返回处理结果上
# 3.2 其他简单视图
- django.http给我们提供很多和HttpResponse类似的简单视图，
通过查看django.http代码我们知道，
- 此类视图使用方法基本类似，可以通过return语句直接返回给浏览器
- Http404为Exception子类，所以需要raise使用
- 是否显示debug信息在setting文件里面进行设置DEBUG的值（True或者False）
# 3.3 HttpResponse详解
- 方法
    - init：使用网页内容实例化HttpResponse对象
    - write(content)：以文件的方式写
    - flush()：以文件的方式输出缓存区
    - set_cookie(key,value='',max_age=None,expires=None)：设置Cookie
        - key,value都是字符串类型
        - max_age是一个整数，表示在指定秒数后过期
        - expires是一个datetime或timedelta对象，会话将在这个指定的日期/时间过期，
        - max_age与expires二选一(这两个在填时只能选到一个)
        - 如果不指定过期时间，则两个星期后过期
    - delete_cookie(key)：删除指定的key的Cookie，如果key不存在则什么也不发生
# 3.4 HttpResponseRedirect
- 重定向，服务器端跳转
- 构造函数的第一个参数用来指定重定向的地址
- 案例tulingxueyuan/teacher_app/views.py
    '''
    python
    # 在east/urls中添加以下内容
    url(r'^v10_1/',views.v10_1),
    url(r'^v10_2/',views.v10_2),
    url(r'^v11/',views.v11,name="v11"),
    '''
    '''
    python
    # tulingxueyuan/teacher_app/views中添加以下内容
    def v10_1(request):
        return HttpResponseRedirect("/v11")
    
    def v10_2(request):
        return HttpResponseRedirect(reverse("v11"))
        
    def v11(request):
        return HttpResponse("哈哈，这是v11的访问返回呀")
    '''
# 3.5 Request对象
- Request介绍
    - 服务器接收到http协议的请求后，会根据报文创建HttpRequest对象
    - 视图函数的第一个参数是HttpRequest对象
    - 在django.http模块中定义了HttpRequest对象的API
- 属性
    - 下面除非特别说明，属性都是只读的
    - path：一个字符串，表示请求的页面是完整路径，不包含域名
    - method：一个字符串，表示请求使用的HTTP方法，常用值包括："GET","POST"
    - encoding：一个字符串，表示提交的数据的编码方式
        - 如果为None则表示使用浏览器的默认设置，一般为utf-8
        - 这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码
    - GET：一个类似于字典的对象，包含get请求方式的所有参数
    - POST：一个类似于字典的对象，包含post请求方式的所有参数
    - FILES：一个类似于字典的对象，包含所有的上传文件
    - COOKIES：一个标准的Python字典，包含所有的cookie，键和值都为字符串
    - session：一个既可以读又可以写的类似于字典的对象，表示当前的会话，
        - 只有当django启用会话的支持时才可用，
        - 详细内容见"状态保持"
- 方法
    - is_ajax()：如果请求是通过XMLHttpRequest发起的，则返回True
- QueryDict对象
    - 定义在django.http.QueryDict
    - request对象的属性GET、POST都是Query类型的对象
    - 与Python字典不同，QueryDict类型的对象用来处理同一个键带有多个值的情况
    - 方法get()：根据键获取值
        - 只能获取键的一个值
        - 如果一个键同时拥有多个值，获取最后一个值
    - 方法getlist()：根据键获取值
        - 将键的值以列表返回，可以获取一个键的多个值
- GET属性
    - QueryDict类型的对象
    - 包含get请求方式的所有参数
    - 与url请求地址中的参数对应，位于?后面
    - 参数的格式是键值对，如key=value1
    - 多个参数之间，使用&连接，如key1=value1&key2=value2
    - 键是开发人员定下来的，值是可变的
    - 案例tulingxueyuan/teacher_app/views/v8_get
    ##访问时的格式类似这样127.0.0.1:8000/v8/?k1='liu'&k2='xiaoming'
- POST属性
    - QueryDict类型的对象    #与dict的区别，dict值只有一个，QueryDict值可以有多个，是checkbox
    - 包含post请求方式的所有参数
    - 与from表单中的控件对应
    - 表单中控件必须有name属性，name为键，value为值
        - checkbox存在一键多值的问题
    - 键是开发人员定下来的，值是可变的
    - 案例tulingxueyuan/teacher_app/views/v9_post
        - setting中设置模板位置
        """
        我们直接添加一个html文件，需要在setting文件中设置如下：
        1、INSTALLED_APPS中添加对应文件，如：'teacher_app',
        2、TEMPLATES的DIRS中添加模板包名，如：os.path.join(BASE_DIR,"templates")
        3、下面一行注释掉会把相应的安全中间件关掉，这样可以显示get_post的内容
        TEMPLATES中注释掉，#'django.middleware.csrf.CsrfViewMiddleware',
        """
        - 设置get页面的urls和函数
        '''
        python
        # tulingxueyuan/urls.py
        # 需要在路由文件中添加两个路由
        url(r'^v9_get/',views.v9_get),
        url(r'^v9_post/',views.v9_post),
        # 方法在tulingxueyuan/teacher_app/views中添加
        '''
# 3.6 手动编写视图
- 实验目的：
    - 利用django快捷函数手动编写视图处理函数
    - 编写过程中理解视图运行原理
- 分析：
    - django把所有请求信息封装入request
    - django通过urls模块把相应请求跟事件处理函数连接起来，
    并把request作为参数传入
    - 在相应的处理函数中，我们需要完成两部分
         - 处理业务
         - 把结果封装并返回，我们可以使用简单HttpResponse，同样也
         - 本案例不介绍业务处理，把木管集中在如何渲染结果并返回
    - render(request,template_name[,context][,context_instance][,content_type])
        - 使用模板和一个给定的上下文环境，返回一个渲染过的HttpResponse对象
        - request：django的传入请求
        - template_name ：模板名称
        - conetext、content_instance：上下文环境
    - render_to_response：可以理解为render的升级版（具体找百度）
# 3.7 系统内建视图
    - 系统内建视图，可以直接使用(也可以通过自己写的替换)
    - 404
        - defaults.page_not_fund(request,template='404.html')
        - 系统引发Http404时触发
        - 默认传request_path变量给模板，即导致错误的URL
        - DEBUG=True则不会调用404，取而代之是调试信息
        - 404视图会被传递一个RequestContext对象并可以访问模板上下文处理器提供的变量
    - 500（server error）
        - defaults.server_error(request,template_name="500.html")
        - 需要DEBUG=False，否则不调用
    - 403(HTTP Forbidden) 视图
        - defaults.permission_denied(request,template_name='403.html)
        - 通过PermissionDenied触发
    - 400(bad request) 视图
        - defaults.bad_request(request,templae_name='400.html')
        - DEBUG=False
# 3.8 基于类的视图
- 对比基于函数的视图的优势和区别：
    - HTTP方法的method可以有各自的方法，不需要使用条件分支来解决
    - 可以使用OOP技术（例如Mixin）
- 概述
    - 核心是允许使用不同的实例方法来响应不同的HTTP请求方法，而避开条件分支实现
    - as_vies函数作为类的可调用入库，该方法创建一个实例并调用dispatch方法，按照请。。
    方法没有定义，则引发HttpResponseNotAllowed
- 类属性使用
    - 在类定义时直接覆盖
    - 在调用as_view的时候直接作为参数使用，例如：
    '''
    urlpatterns = [
        url(r'^about/',GreetingView.as_view(greeting="G'day")),
    ]
    '''
- 对于基类的视图的扩充大致有三种方法，Mixin、装饰as_view、装饰dispatch
- 使用Mixin
    - 多继承的一种形式，来自弗雷的行为和属性组合在一起
    - 解决多继承问题
    - View的子类只能单继承，多继承会导致不可预期问题
    - 多继承带来的问题：
        - 结构复杂....
# 105 课 6-6 models

# 3.9.1 Models 模型
- ORM
    - ObjectRelationMap：把面向对象思想转换成数据库思想
    - 类对应表格
    - 类中的属性对应表中的字段
    - 在应用的models.py文件中定义class
    - 所有使用ORM的class都必须是models.Model的子类
    - class中的所有属性对应表格中的字段
    - 字段的类型都必须使用，model.xxx不能使用python中的类型
    - 在django中，Models负责跟数据库交互
- django连接数据库
    - 自带默认数据库Sqlite3
        - 关系型数据库
        - 轻量级
    - 建议开发用Sqlite3，部署用mysql之类数据库
    - 切换数据库在settings.py中进行设置
    - # django 连接mysql
        
        DATABASES = {
            'default' : {
                'ENGINE' : 'django.db.backends.mysql',
                'NAME' : '数据库名称',
                'PASSWORD' : '数据库密码',
                'HOST' : '127.0.0.1',
                'PORT' : '3306',
            }
        }
    - 需要在项目文件下的__init__文件中导入pymysql包
        '''
        # 在主项目的__init__文件中  
        import pymysql
        pymysql.install_as_MySQLdb()
        '''
# 3.9.2 models 类的使用
- 定义和数据库表映射的类
    - 在应用中的models.py文件中定义class
    - 所有需要使用ORM的class都必须是models.Model的子类
    - class中的所有属性对应表格中的字段
    - 字段的类型都必须使用，model.xxx不能使用python中的类型
- 字段常用参数
    1. max_length：规定数值的最大长度
    2. blank：是否允许字段为空，默认不允许
    3. null：在DB中控制是否保存为null，默认为false
    4. default：默认值
    5. unique：唯一
    6. verbose_name：假名
    - 案例在teacher_app/models.py中
- 数据库的迁移(python3没有就用python)
    1.在命令行中，生成数据迁移的语句（生成sql语句）
        python3 manage.py makemigreations
    2.在命令行中，输入数据迁移的指令
        python3 manage.py migrate
        ps:如果前一种出现没有变化或者报错，可以尝试强制迁移
        # 强制迁移命令
        python3 manage.py makemigrations 应用名
        python3 manage.py migrate 应用名
    3.对于默认数据库，为了避免出现混乱，如果数据库中没有数据，可以先删除相关文件，自带的sqlite3数据库删除
# 106 课 6-7 models
## 3.9.3 查看数据库的数据
1.启动命令行：python manage.py shell (or python3)
ps:注意点：对orm的操作分为静态函数和非静态函数两种，静态是指在内存中只有一份
2.在命令行中导入对应的映射类
     from 应用.models import 类名
3.使用objects属性操作数据库.objects 是模型中实际和数据库进行交互的
4.查询命令
    - 类名.objects.all() 查询数据库表中的所有内容，返回的结果是一个QueryDict类型
    - 类名.objects.filter(条件)
    使用时如：
        from teacher_app.models import Teacher
        # 实例化对象
        t = Teacher()
        t.name = "xiaoming"
        t.age = 18
        # 保存数据（如果查询不到，需要退出当前shell，再进入）
        t.save()
        ta = Teacher.objects.all()
        # 然后在命令行输入ta回车即可看到对应信息
        # 这样进行使用对数据进行过滤
        ta = Teacher.objects.filter(age=30)
# 3.9.4 常用的查找方法
1. 通用查找格式：属性名__(下面的内容) = 值 
- gt：大于、gte：大于等于、lt：小于、lte：小于等于、range：范围、year：年份、isnull：是否为空
ta = Teacher.objects.filter(age__lt=30) # 形式解释这样的，有=这个符号
ta
2.查找等于指定的格式：属性名 = 值
3.模糊查找：属性名__(使用下面的内容) = 值
- exact：精确等于、iexact：不区分大小写、contains：包含、startwith：以..开头、endwith：以..结尾
# 108 课 6-8 models
## 3.9.5 数据库的创建形式
- 数据库表关系
    - 1:1 OneToOne
        - 建立关系，在模型任意一边即可，使用OneToOneField("另一个类的类名")
    - 1:N OneToMany
    - N:N ManyToMany
# 110 课 模板
## 4.1 模板系统
- 模板：一组相同或者相似的页面，在需要个性化的地方进行留白，需要的时候只是用数据填充就可以使用
- 步骤：
    1.在settings中设置LTEMPALTES
    2.在templates目录下编写并调用
## 模板-变量
- 变量的表示方法：{{var_name}}
- 在系统调用模板的时候，会用相应的数据查找相应的变量名称，如果找到，则渲染，否则跳过。
- 案例django_tem/tpl/templates/two.html
## 模板-标签
- 1.for标签：[% for .. in ..  %]
- 用法：
    {% for .. in .. %}
        循环语句
    {% endfor %}
- 案例django_tem/tpl/templates/three，显示班级成绩

- 2.if标签
- 用来判断条件
- 案例django_tem/tpl/templates/four

- 3.csrf标签
- csrf：跨站请求伪造
- 在提交表单的时候，表单页面需要加上{% csrf_token %}
- 案例five_get,five_post
# 112 课 session_分页_类视图_admin
## 4.1 session
- 为了应对HTTP协议的无状态性
- 用来保存用户比较敏感的信息
- 属于request的一个属性
- 常用操作
    - request.session.get(key,defaultValue)
    - request.session.clear():清除全部
    - request.session[key] = value：赋值
    - request.session.flush()：删除当前会话且清除会话的cookie
    - del request.session[key]:也是删除值，很少使用
## 4.2 分页
- django提供现成的分页器用来对结果进行分页
- from django.core.paginator import Paginator
## 4.3 基于类的视图
- 可以针对http协议不同的方法创建不同的函数
- 可以使用Mixin等oop技术
- Mixin
    - 把来自父类的行为或者属性组合在一起
    - 解决多重继承的问题
- ListView
## 4.4.1 admin
- 案例 - teach_session
- settings中填入app
- 创建Admin
- 打开urls.py
- 创建超级用户
    #如果打不开admin网址，先执行1，反之直接执行2
    1.python manage.py makemigrations
      python manage.py migrate
    2.python manager.py createsuperuser
    ## 已创建超级用户 yucai/yucai123
    
    # 修改models后再次迁移执行：
     1/python manage.py makemigrations session_app
     2/python manage.py migrate session_app
    # 同时在那个对应关系中添加了default参数，不然有个报错
    """You are trying to add a non-nullable field 'room' to student without a default; we can't do that (the
database needs something to populate existing rows)"
- 配置settings文件
## 4.4.2 绑定管理模型

## 4.4.3 设置admin管理类
- 实现方式
    - ModelAdmin
    - 装饰器
- 修改页面显示数量：list_per_page = int_number
- 操作选项框在上还是下：actions_on_top/button = True/False
- 控制列表中显示的内容；list_display=[]
- 搜索search_fields = []
- 分组fieldsets = ((),())
- 将函数作为列显示,如：（models中Teacher类下定义了一个curTime函数）
    - 函数必须返回值
    - 设置short_descraption作为显示内容
    - 排序使用admin_order_field = string
