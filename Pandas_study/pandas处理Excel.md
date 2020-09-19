# https://study.163.com/course/courseMain.htm?courseId=1006254007&_trace_c_p_k2_=ffb42b496bf74b79be97283426e4f49b

'''
数据处理思路流程：
1、关键数据抽取；   -- 想要看到的列
2、缺失值处理；     -- (data.isnull()).sum()    data((data.isnull()).sum())  data.dropna(how='all', inplace=True)
3、重复值处理；    -- 注意重复值要删的行，先对内容排序，这样有些部分重复的且有NaN的值会在后面
4、数据类型转换；   -- data.name.str.replace('元/米', '')
5、处理不合理数据；
6、绘图
'''

# 1、创建Excel并添加内容
df = pd.DataFrame({'ID': [1, 2, 3], 'Name':['Tim', 'Victor', 'Nick']})
不设置索引，默认有数字索引
df = df.set_index('ID')
df.to_excel('./output.xlsx')

# 索引和表头这样添加
dx = ['one', 'two', 'three', 'four']
arr2 = np.array(np.arange(12).reshape(4, 3))
df = pd.DataFrame(arr2, index=dx)
# 添加列名
df.columns = ['a', 'b', 'c']
# 2、读取Excel，如果表格前面有多余行，使用skiprows跳过，如果第一行有脏数据，header=1跳过
people = pd.read_excel('./people.xlsx', skiprows=None, header=0)
print(people.shape)
- 如果没有columns的名字，主动设定一个即可
- people.columns = ['ID', 'Type', 'Title', 'FirstName', 'MiddleName', 'LastName']
print(people.columns)
print(people)   # 注意将整个sheet打印
- 读取后进行保存
people.to_excel('xxx.xlsx')
# 3、自动填充excel
- dtype因为未给值时时NAN，不能直接给int类型，因此给个str行，也是整数
- usecols='C:F'；还可以usecols='C,D,E,F' 去除空列
books = pd.read_excel('./excel/Books.xlsx', skiprows=3,
                      usecols='C,D,E,F', index_col=None,
                      dtype={'ID': str, 'InStore': str, 'Date': str})
- 由于月份在excel中递增填充比较麻烦，因此给个单独函数
def add_month(d, md):
    yd = md // 12
    m = d.month + md % 12
    if m != 12:
        yd += m // 12
        m = m % 12
    return date(d.year + yd, m, d.day)


start = date(2018, 1, 20)
for i in books.index:
    # books.at[i, 'ID'] = i + 1         # dataframe的方式
    books['ID'].at[i] = i + 1
    books['InStore'].at[i] = 'YES' if i % 2 == 0 else 'NO'
    # books['Date'].at[i] = start + timedelta(days=i) # 日增
    # books['Date'].at[i] = date(start.year + i, start.month, start.day)  # 年增
    books['Date'].at[i] = add_month(start, i)   # 月增

print(books)
# 6、函数填充，计算列
例子func_calc_book006.py
核心部分
books['Price'] = books['ListPrice'] * books['Discount']
# 5、排序，多重排序
sort_007.py
核心部分
products.sort_values(by=['Worthy', 'Price'], inplace=True, ascending=False)
# 7、筛选过滤
sort_007.py
核心部分 apply()
- 条件过滤
students = students.loc[students['Age'].apply(age_18_to_30)].\
        loc[students['Score'].apply(level_a)]

- 由于有两行空的，执行时ValueError: cannot reindex from a duplicate axis
- 使用次函数查询重复轴索引，进行删除或修改即可
- print(students.index.duplicated())
# 9、数据可视化 -- 柱状图
histogram_009.py
核心部分 bar()
students = pd.read_excel('./excel/Students-009.xlsx')
- pandas 绘图
- students.plot.bar(x='Field', y='Number', color='purple', title='International')
- 使用plt绘图
# 注意如果列名时数字时，不能使用students.2017；只能使用students['2017']
plt.bar(students.Field, students.Number, color='purple')
- 将标签旋转90度,原因标签叠在一起
plt.xticks(students.Field, rotation='90')
- 添加坐标轴名
plt.xlabel('Field')
plt.ylabel('Number')
plt.title('International Students by Field', fontsize=16)
- 变迁完全显示，紧凑型布局(如果太长，标签会被阶段)
plt.tight_layout()
plt.show()
# 10、 制作分组柱图
group_histogram010.py
核心部分
students.plot.bar(x='Field', y=['2016', '2017'], color=['purple', 'red'],
                  title='International')

- 直接使用plt的方式，由于x都用的students.Field，结果会重叠起来，但是有颜色区分
- plt.bar(students.Field, students['2017'], label='2017')
- plt.bar(students.Field, students['2016'], label='2016')

students.plot.bar(x='Field', y=['2016', '2017'], color=['purple', 'red'],
                  title='International')

plt.title('International Students', fontsize=16, fontweight='bold')
# 11、叠加柱状图，水平柱状图
horizontal_histogram011.py
核心部分 barh()
users.plot.barh(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True, title='User Behavior')
# 12、饼图
p012.py
核心部分 pie()
students['2017'].plot.pie(fontsize=8)
# 13、折线图、叠加区域图
p013.py
核心部分
- 不叠加，未使用area
- weeks.plot(y=['Accessories', 'Bikes', 'Clothing', 'Components', 'Grand Total'])

- 使用叠加折线图绘制
weeks.plot.area(y=['Accessories', 'Bikes', 'Clothing', 'Components', 'Grand Total'])
# 14、散点图、直方图
p014.py
核心部分
- 列太长，默认输出时部分被隐藏，如果不要隐藏，进行配置
pd.options.display.max_columns = 777

- 散点图：scatter()
home_data.plot.scatter(x='price', y='sqft_living')
- 房屋面积直方图:hist()
home_data.sqft_living.plot.hist(bins=100)
plt.xticks(range(0, max(home_data.sqft_living), 5000), fontsize=8, rotation=90)
- 密度图: kde()
home_data.sqft_living.plot.kde()
plt.xticks(range(0, max(home_data.sqft_living), 500), fontsize=8, rotation=90)

### 数据分析
# pandas提供的一个重要函数corr()  每两列之间的相关性
print(home_data.corr())

- 行方向连接，左右连接
students = pd.concat([page_001, page_002], axis=1)
- 列方向连接，上下连接
students = pd.concat([page_001, page_002]).reset_index(drop=True)

# 16、多表联合
p016.py
核心部分
table = students.merge(scores, how='left', on='ID').fillna(0)
table = students.join(scores, how='left').fillna(0)
table.Score = table.Score.astype(int)
# 17 、数据校验、轴的概念
p017.py
核心部分
def score_validation(row):
    if not 0 <= row.Score <= 100:
        print(f'#{row.ID}\tstudent {row.Name} has an invalid score {row.Score}.')
students = pd.read_excel('./excel/Students-17.xlsx')
students.apply(score_validation, axis=1)
# 18、数据分割成两列
p018.py
核心部分
- 添加一个参数，直接将一个列表分成两列，expand=True
df = employees['Full Name'].str.split(expand=True)
employees['First Name'] = df[0]
employees['Last Name'] = df[1]

- 合并两列
- employees['full name'] = employees['First Name'] + ' ' + employees['Last Name']
# 19、求和、求平均、统计引导
p019.py
核心部分
temp = students[['Test_1', 'Test_2', 'Test_3']]

- 从左到右进行统计；默认为axis=0，从上到下
- result = temp.sum()
row_sum = temp.sum(axis=1)
row_mean = temp.mean(axis=1)
students['Total'] = row_sum
students['Average'] = row_sum
# 20、消除、定位重复数据
p20.py
核心部分
- 此处为单列;keep重复值保留前面的还是后面的，默认first
- students.drop_duplicates(subset='Name', inplace=True, keep='first')
- students.drop_duplicates(subset=['Name'], inplace=True, keep='last')

dupe = students.duplicated(subset='Name')       # bool
- 再进行过滤
- dupe = dupe[dupe == True]
- 因为dupe本身就是bool，所以可以简写为
dupe = dupe[dupe]
- 获取过滤的重复值的索引
dupe_inx = dupe.index       # Int64Index([20, 21, 22, 23, 24], dtype='int64')
- 定位重复数据
data = students.loc[dupe_inx]
# 21、行列互转
p21.py
核心部分
table = videos.transpose()
# 22、读取CSV、TSV、TXT中数据
p22.py
核心部分
"""csv/tsv/txt都是一种纯本文文件，所以读取方法一样read_csv"""
# 约定、csv以逗号分隔内容；tsv以table分隔；txt以非逗号和非table特殊字符，如| 分隔
# 23、透视表、分组、聚合
p23.py
核心部分
- 方法一：
orders['Year'] = pd.DatetimeIndex(orders['Date']).year
pt1 = orders.pivot_table(index='Category', columns='Year', values='Total', aggfunc=np.sum)
- 方法二：
orders['Year'] = pd.DatetimeIndex(orders['Date']).year
groups = orders.groupby(['Category', 'Year'])
s = groups['Total'].sum()
c = groups['ID'].count()
pt2 = pd.DataFrame({'Sum': s, 'Count': c})
# 24、线性回归、数据预测
p24.py
核心部分
- 斜率、截距
slope, intercept, r, p, std_err = linregress(sales.index, sales.Revenue)
- 期望值
exp = sales.index * slope + intercept
plt.scatter(sales.index, sales.Revenue)
plt.plot(sales.index, exp, color='purple')
plt.title(f'y={slope} * x + {intercept}')
# xticks 表示x轴上加
plt.xticks(sales.index, sales.Month, rotation=90)
plt.tight_layout()
plt.show()
# 25、条件格式--上
p25.py
核心部分
def low_score_red(s):
    color = 'red' if s < 20 else 'black'
    return f'color:{color}'
def highest_score_green(col):
    return ['background-color:lime' if s == col.max()
            else 'backgroud-color:white' for s in col]
students = pd.read_excel('./excel/Students-25-26.xlsx')
students.style.applymap(low_score_red, subset=['Test_1', 'Test_2', 'Test_3'])
students.style.applymap(low_score_red, subset=['Test_1', 'Test_2', 'Test_3'])\
    .apply(highest_score_green, subset=['Test_1', 'Test_2', 'Test_3'])
# 26、条件格式下
p26.py
核心部分
- 颜色深浅来表示数据的大小
color_map = sns.light_palette('green', as_cmap=True)
students = pd.read_excel('./excel/Students-25-26.xlsx')
students.style.background_gradient(color_map, subset=['Test_1', 'Test_2', 'Test_3'])
- 使用数据bar(矩形长度)来表示数据大小
students = pd.read_excel('./excel/Students-25-26.xlsx', index_col='ID')
students.style.bar(color='orange', subset=['Test_1', 'Test_2', 'Test_3'])
# 27、行操作集锦
# 删除空行
# df.dropna(axis=1, how='any')  # axis = 0、1, how = 'any'、 'all'
# 填空值
# df.fillna(value=0)
# 判断是否有空
# np.any(df.isnull()) == True     # 返回值单个结果：bool，不采用np判断，将返回所有单元格bool

row_operation.py
核心部分
- 直接修改单元格的值
students.at[39, 'Name'] = 'Bailey'
- 直接替换整行内容
stu = pd.Series({'ID':38, 'Name': 'kitty', 'Score': 115})
students.iloc[37] = stu
- 在第ID为20和21之间插入一行，danny同学，使用到切片方法
part1 = students[:20]
part2 = students[20:]
students = part1.append(stu, ignore_index=True).append(part2).reset_index(drop=True)
- 删除数据行，索引为0-2的行；参数inplace是为了不生成新的dataframe
students.drop(index=[0, 1, 2], inplace=True)
- 使用切片方式删除
students.drop(index=range(3,10), inplace=True)
students.drop(index=students[1:6].index, inplace=True)
# 28、列操作集锦
# 删除空列
# df.dropna(axis=1, how='any')  # axis = 0、1, how = 'any'、 'all'
# 填空值
# df.fillna(value=0)
# 判断是否有空
# np.any(df.isnull()) == True     # 返回值单个结果：bool，不采用np判断，将返回所有单元格bool
# 重新设置索引
# students = students.set_index('ID')

col_operation.py
核心部分
- 删除列
- students = students.drop(columns=['Age', 'Score'])
students = students.drop(columns=['Score'])
- 插入列
students.insert(1, column='Foo', value=np.repeat('foo', len(students)))
- 添加列名
students.columns = ['ID', 'Name', 'Score']
- 修改列名
students.rename(columns={'Foo': 'FOO', 'Name': 'NAME'}, inplace=True)
- row操作中有说到去空值，那种方式是采用定位到空值的inde，然后进行drop；这个更简单
students.dropna(inplace=True)
- 按条件查找删除
- missing = students.loc[students['Name'] == '']
- students.drop(index=missing.index, inplace=True)
- students.drop(students[students['ID'] == 'ID'].index, inplace=True)
# 29、链接sql server数据库
p29.py
核心部分
connection = pyodbc.connect('DRIVER=(SQL Server);SERVER=(local);'
                            'DATABASE=AdventureWorks;USER=sa;PASSWORD=123456')

engine = sqlalchemy.create_engine('mssql+pyodbc://sa:123456@(local)/AdventureWorks'
                                  '?driver=SQL+Server')
qurey = "select cout(FirstName) as Count from Person.person where FirstName='Tony'"
- 两个库连接数据库
df1 = pd.read_sql_query(qurey, connection)
df2 = pd.read_sql_query((qurey, engine))
# 30、复杂计算列
p30.py
核心部分
def get_circumcirecle_area(l, h):
    r = np.sqrt(l**2+h**2)/2
    return r**2*np.pi
def wrapper(row):
    return get_circumcirecle_area(row['Length'], row['Height'])

rects = pd.read_excel('./excel/Rectangles-30.xlsx', index_col='ID')
- 使用两个函数去返回或者后面直接使用lambda表达式
- rects['CA'] = rects.apply(wrapper, axis=1)
rects['CA'] = rects.apply(lambda row: get_circumcirecle_area(row['Length'], row['Height']), axis=1)
