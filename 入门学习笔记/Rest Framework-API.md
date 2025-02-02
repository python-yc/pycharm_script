# 114 课 API介绍
## 1 REST
- 前后端分离
- API-ApplicationProgrammingInterface
    - 为了应对千变万化的前端需求
- REST:RepresationsStateTrans
    - 2000 Fieding博士提出
    - RESTful：遵守REST规范的技术设计的软件可以称为RESTful
- REST规范：
    - URL代表一个资源，一个资源应该是一个名词
    - 动作有HTTP的method方法提供
    - URL应该包含版本信息，版本信息也可以放在HTTP协议中
    - 过滤信息，使用URL的参数代表过滤
    - 返回值：每一个返回代码都有具体特定含义
    - 返回格式：推荐固定具体格式
        code：xxx；msg：xxx；data：xxx。
        先查看code情况；msg中有相应信息，如报错；正常在data中提取数据
- DjangoRestFramework(DRF)
    - https://qlmi.github.io/Django-REST-framework-documentation/
    - 安装：pip install djangorestframework==3.7
    - 版本问题：version3.7是基于1.xx版本django，之后是2.xx版本django
    - django_filter依赖djangorestframework 3.7
- DRF的主要任务
-案例 TlxyDRF
    - django-admin startproject TlxyDRF
    - python manage.py startapp case01
    - 配置settings
    - 配置urls
    - 创建三个模型：Student，Teacher，ClassRoom
    - 创建序列化器
    - 创建视图集合
## 2 序列化（serializer）
- 序列化：把系统运行中的一些实例等转换成一种可直接表示出来的格式，用来保存，传输等；
- 反序列化：序列化的反操作
- pickle、file、xml、json
# 2.1 序列化/反序列化-DRF
- 实验步骤
- 创建project serializer_drf
- 创建app MySer
- settings
# 2.2 serializer的类型参数
- read_only：仅用于序列化输出
- write_only：反序列化输入
- allow_null：允许传入None
- validators：使用验证器
# 2.3 创建serializer对象/使用
- 构造方法
    Serializer(instance=None,data=empty,#**kwarg)
# 3 反序列化
- 验证
    - is_valid：
        - 验证数据是否合法，返回boolean
        - 在使用从外部传入的数据之前，必须  使用  此函数进行验证
        - 如果验证失败，返回数据错误异常
    - validated_data:
        - 经过验证后的数据，存入此结构
# 4 视图
- DRF的视图从处理任务、处理流程等与django基本一致
- 此视图基本是django视图的扩展
    - Request
        - 把请求解析成一个request实例
        - 属于DRF的，与django的HttpRequest不太一样，大致相同
        - 在得到Request之前有一个Parse对传入的数据请求进行解析
        - data属性
            - 请求数据体，类似于django的request.POST，request.FILES
            - 在DRF中主要指的是json
        - query_params
            - 所有传入的关键字都在这里
            
            api.tulingxueyuan.com/student/?name='xiao'
            # 使用案例
            # 在请求参数里查找name值，添加了get后，如果查到则返回，否则返回默认值None
            name = self.request.query_params.get('name',None)
        - user
            - 登录后的用户信息都在user中
            - 如果没有登录，则是anonymous（匿名用户）
            - 可以用判断来判断用户是否登录成功
    - Response
        - rest_framework.response.Response
        - 用Renderer渲染器对返回内容进行渲染
        
        # 在settings中设置
        REST_FRAMEWORK = {
            'DEFAUTL_RENDERER_CLASSES': ( #默认响应渲染类
                'rest_framework.renderers.JSONRenderer',  #json渲染
                'rest_framework.renderers.BrowsableAPIRenderer', #可浏览的渲染接口
            )
        }
    - 返回的构造方式 status 是http中的状态码
        - returen Response(data,status=None,template_name=None,headers=None,content_type=None)
- 视图类
- APIView
    - rest_framework.views.APIView
    - 是django中View的子类
    - 与View有不同的地方
        - 传入传出数据用的是drf的请求和反馈类
        - 会引发并处理APIException
        - 在dispatch之前，会进行身份验证，权限检查，流量控制
    - 支持的属性有
        - authentication_classes：列表或者元组，身份验证类
        - permission_classes：权限验证
        - throttle_classes：流量控制
    - 对API的访问提供了一些方便
        - HTTP-Method + 名词
        - 默认对HttpMethod常用的方法提供了支持
    - API工具
        - Chrome  ---Postman
        - Firefox   ---RESTClient
    - GenericAPIView
        - APIView的子类
        - 支持的属性
            - queryset：查询结果集
            - serializer_class：视图使用的序列化器
            - panination_class：分页控制器
            - filter_backends：过滤器后端
            - lookup_field：查询条件字段，默认为pk
        - get_queryset：返回查询结果集集合，经常需要重写
        - get_serializer_class：得到序列化器类
        - get_serializer：得到序列化器
- ListModelMixin
    - list(request,*args,**kwargs)
- CreateModelMixin
    - create(request,*args,**kwargs)
- RetrieveModelMixin    -- 查询
    - retrieve(request,*args,**kwargs)
- DestroyModelMixin
    - destroy(request,*args,**kwargs)
- ViewSet
    - 把一系列操作打包放入一个类中
    - list：GET
    - retrieve：GET + id
    - destroy：DELETE
    - update:UPDATE
    - create:POST





