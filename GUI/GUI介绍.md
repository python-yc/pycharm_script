# 1 GUI 介绍
- GraphicalUserInterface
- GUI for Python: Tkinter,wxPython,PyQt
- Tkinter:
    - 绑定的是TK GUI工具集，用途Python包装的Tcl代码
- PyGTK
    - Tkinter的替代品
- wxPython
    - 跨平台的Python GUI
- PyQt
    - 跨平台的
    - 商业授权可能有问题
    - 案例：Tkinter_eg
- 推荐资料
    - 辛星GUI，辛星Python       这个简洁明了，后面两个当字典用 
    - Python GUI Programming cookbook
    - Tkinter reference a GUI for Python
### tkinter 常用组件
## 1.1 组件的大致使用步骤
- 1.创建总面板   baseFrame=tkinter.Tk()
- 2.创建面板上的各种组件
    1.指定组件的父组件，即依附关系
    2.利用相应的属性对组件进行设置
    3.给组件安排布局
- 3.同步2相似，创建多个组件
- 4.最后启动总面板的消息循环    baseFrame.mianloop()
## 1.2
- 按钮
    Button          按钮组件
    RadioButton     单选框按钮
    CheckButton     选择按钮
    Listbox         列表框组件
- 文本输入组件
    Entry           单行文本框组件
    Text            多行文本框组件
- 标签组件
    Label           可以显示图片和文字
    Message         可以根据内容将文字换行
- 菜单
    Menu            菜单组件
    MenuButton      菜单按钮组件，可以使用Menu代替
- 滚动条
    scale           滑块组件
    Scrollbar       滚动组件
- 其他组件
    Canvas          画布组件
    Frame           框架组件，将多个组件编组
    Toplevel        创建子窗口容器组件
- 案例：Label_eg

## 1.3 组件布局
- 控制组件的摆放方式
- 三种布局：
    - pack：按照方位布局
    - place：按照坐标布局
    - grid：网络布局
- pack布局
    - 最简单，代码量最少，挨个摆放，默认从上到下，系统自动设置
    - 通用使用方式为：组件对象.pack(设置，，，，，)
    - side：停靠方位，可选为LEFT、TOP、RIGHT、BOTTOM
    - fill：填充方式，X、Y、BOTH、NONE
    - expande：YES/NO
    - anchor：N、S、E、W、CENTER
    - ipadx：x方向的内边距
    - ipady：y方向的内边距
    - padx：x方向的外边距
    - pady：y方向的外边距
    # 案例：pack_layout_eg
- grid布局
    - 给定的格子方式进行布局
    - 通用使用方式：组件对象.grid(设置，，，，，，)
    - sticky：N,S,W,E表示上下左右，用来决定组件从哪个方向开始
    - 支持ipadx、padx等参数，跟pack函数含义一样
    - 支持rowspan、columnspan，表示跨行、跨列数量
    # 案例：grid_layout_eg
- place布局
    - 明确方位的摆放
    - 相对位置布局，随意改变窗口大小会导致混乱
    - 使用place函数，分为绝对布局和相对布局，绝对布局使用x，y参数
    - 相对布局使用relx、rely、relheight、relwidth
## 1.4 消息机制
- 消息的传递机制
    - 自动发出事件/消息
    - 消息有系统负责发送到队列
    - 由相关组件进行绑定/设置
    - 后端自动选择感兴趣的事件并做出相应反应 
- 消息格式：
    - <[modifiter-]---type-[-detail]>   #尖括号和type的类型必须有，另外两个可以没有
    # Button即是有一个type类型
    - <Button-1>:Button表示一个按钮事件，1代表的是左键，2代表的是中键,3代表右键
    - <KeyPress-A>:键盘A键位
    - <Control-Shift-KeyPress-A>:同时按下Control，Shift和A三个键位
    - <F1>：F1键盘
    - [键位对应名称]
    (https://infohost.nmt.edu/tcc/help/tkinter/web/key-names.thml)
    - 案例event_eg
## 1.5 Tkinter的绑定
- bind_all:全局范围的绑定，默认是全局快捷键比如F1帮助文档
- bind_class:接受第三个参数，第一个是类名，第二个是事件，第三个操作
    - w.bind_class("Entry","<Control-V>",my_paste)
- bind:单独对一个实例绑定
- unbind:解绑，需要一个参数，即你要解绑那个事件
Entry：
    - 输入框，功能单一
    - entry["show"]="*"，设置遮挡字符
    - 案例entry_eg
### 1.6 菜单
- 1、普通菜单
- 第一个Menu类定义的书parent
- add_command 添加菜单项，如果菜单是顶层菜单，则从左向右添加，否则就是下拉菜单
    - label：指定菜单项名称
    - command：点击后相应的调用函数
    - acceletor：快捷键
    - underline：指定是否菜单信息下是否有横线
    - menu：属性指定使用哪一个作为顶级菜单
    - 案例common_menu_eg
- 2、级联菜单
- add_cascade：级联菜单，作用是引出后面的菜单
- add_cascade的menu属性：指明把菜单级联到哪个菜单上
- label：名称
- 过程：
    1.建立menu实例
    2.add_command
    3.add_cascade
    - 案例cascade_menu_eg
- 3、弹出式菜单
    - 弹出菜单也叫上下文菜单
    - 实现的大致思路
        1.建立菜单并向菜单添加各种功能
        2.监听鼠标右键（一般）
        3.如果右键点击，则根据位置判断弹出
        4.调用Menu的pop方法
    - add_separator 添加分隔符
    - 案例popup_menu_eg
#　1.7 canvas 画布
- 画布：可以自由的在上面绘制图形的一个小舞台
- 在画布上绘制对象，通常用create_xxx,xxx=对象类型，例如line，rectangle
- 案例canvas_eg

