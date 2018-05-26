#!/usr/local/python3/bin/python3  
# -*- encoding:utf-8 -*-
# Filename: python3_learn_man.py
# Author  : litao
# Python  : 3.6
# Time    : 2018/4/22 21:14
# Version : 1

def 更新日志():
    log_2018_05_22 = '''
        补充了字典的一点内容，补充了类的应用笔记。开始socket编程。'''
    log_2018_05_22 = '''
        基本完成面向对象，补充hashlib,序列化模块。
        '''
    log_2018_05_19 = '''
        完善面向对象的高级用法.补充元类，类的特殊成员.
        '''
    log_2018_05_18 = '''
        完善面向对象的高级用法.开始类的特殊方法,补充反射,类方法,静态方法.
        '''
    log_2018_05_12 = '''
        完善面向对象的高级用法.
        '''
    log_2018_05_11 = '''
        完善面向对象的三大特性.
        '''
    log_2018_05_08 = '''
        完善字符串格式化精讲.面向对象开始.
        '''
    log_2018_05_06 = '''
        完善time模块.
        '''
    log_2018_05_05 = '''
        补充functools.partial方法.补充函数的属性、回调函数.分离出闭包.添加subprocess,commands模块.
        '''
    log_2018_05_03 = '''
        完成sys模块.完善一些知识点.
        '''
    log_2018_05_02 = '''
        添加与生成器有关的模块方法.完成os模块,完成datetime模块.完善一些知识点.
        '''
    log_2018_05_01 = '''
        完善一些知识点,完成re正则、random随机模块.完成namedtuple,补充字符串的对齐,format函数
        '''
    log_2018_04_31 = '''
        完善一些知识点包括数学运算,序列相关的内置函数,完成流程控制,完成一些常用模块,补充使用技巧模块.
        '''
    log_2018_04_30 = '''
        补充一些知识点
        '''
    log_2018_04_29 = '''
        基本完成函数部分.
        '''
    log_2018_04_28 = '''
        完成内置函数.
        '''
    log_2018_04_27 = '''
        完成数据类型,进行文件操作,和函数.
        '''
    log_2018_04_26 = '''
        逐个测试所有方法.
        '''
    log_2018_04_22 = '''
        第一次编写,将博客的内容迁移到这里.
        '''

def 更新备忘录():
    '''
    常用模块二，hashlib
    补充类的描述符，类的特殊成员。类的题目
    python书籍补充.
    python2实例手册补充.
    补充模块 http://www.cnblogs.com/Eva-J/articles/7291842.html
    '''

def 说明():
    '''
    作者:涛
    仅用于自学python3.
    请使用"pycharm"打开此文档, "Ctrl+Shift+NumPad+/-"将函数展开或折叠后方便查阅
    错误在所难免, 还望指正！
    不定期更新地址:https://github.com/332000640/python3_learn_man
    '''

def 基础():
    '''python3的基础知识'''
    '''约定变量名全部大写代表常量'''

    def 生态工具():

        模块方法 = '''
            help('modules')   # 查看python所有模块  命令行下:python -c "help('modules')"
            for i in dir(os):print(i)   # 模块的方法
            help(os.path)               # 方法的帮助
            '''

    def pip的使用():
        '''
        pip install 库名              安装包和依赖包
        pip uninstall 库名            卸载安装包
        pip list                     查看已经安装的第三方库
        pip list --outdated          查哪些包需要更新
        pip install 库名=版本号       安装任意版本则可加上版本号
        pip show 库名                查看安装库的详细信息
        pip show --files            查看已安装的包
        pip install --upgrade 库名   pip升级包
        pip --help                  查看帮助
        pip install --download=/path 库名    将第三方库及依赖下载到path,只下载不安装
        pip download                下载软件包
        pip check                   检查软件包的依赖是否完整
        pip search                  查找软件包
        pip wheel                   打包软件到wheel格式
        pip completion --bash >> ~/.profile  命令补全
        pip install -i https://pypi.douban.com/simple/ flask  使用-i 指定镜像源.
        修改pip配置文件,指定镜像源
        cat pip.conf
        [global]
        index-url = https://pypi.douban.com/simple/
        下载到本地:  从requirements.txt读取软件与版本.
        pip install --download=`pwd` -r requirements.txt
        本地安装:
        pip install --no-index -f file://`pwd` -r requirements.txt
        可以先用pip download pymysql,再用pip install pymysql*.whl 本地安装
        '''

    def 关键字():

        查看关键字 = '''
            import keyword
            keyword.iskeyword(str)       # 字符串是否为python关键字
            keyword.kwlist               # 返回pytho所有关键字
            ['False','None','True','and','as','assert','break','class','continue','def','del','elif','else','except','finally',\
             'for','from','global','if','import','in','is','lambda','nonlocal','not','or','pass','raise','return','try', 'while','with','yield']
             '''

    def 数据类型():
        '''数字,字符串,列表,元组,字典,集合'''

        共性 = '''
            除数字类型不能使用for循环遍历外,其他的均可遍历
            for i in obj:print(i)
            除字典,数字不能使用 + * 号拼接外,其他的均可拼接
            'abc'+'def'         'abc'*3
            [1,2,3]+[4,5,6]     [1,2,3]*3
            (1,2,3)+(4,5,6)     (1,2,3)*3
            '''

        数据的分解操作 = '''
            只要对象是可迭代的,就可以就行分解操作.
            a,_,b,_='1234'   丢弃操作
            a,*_,b='1234'    分解操作
            '''

        def 数字():

            特性 = '''
                只能存放一个值
                一经定义,不可更改直接访问
                分类:整型,布尔,浮点,复数
                整型(Int)
                通常被称为是整型或整数,是正或负整数,不带小数点.Python3整型是没有限制大小的,可以当作 Long类型使用,所以Python3没有 Python2的Long类型.
                浮点型(float)
                浮点型由整数部分与小数部分组成,浮点型也可以使用科学计数法表示
                复数(complex)
                复数由实数部分和虚数部分构成,可以用a + bj, 或者complex(a, b)表示, 复数的实部a和虚部b都是浮点型.
                '''

            算术运算符 = '''
                +    加     - 两个对象相加
                -    减     - 得到负数或是一个数减去另一个数
                *    乘     - 两个数相乘或是返回一个被重复若干次的字符串
                /    除     - x 除以y
                %    取模   - 返回除法的余数
                **   幂     - 返回x的y次幂
                //   取整除  - 返回商的整数部分
                '''

            比较运算符 = '''
                ==  等于      - 比较对象是否相等
                !=  不等于    - 比较两个对象是否不相等
                >   大于      - 返回x是否大于y
                <   小于      - 返回x是否小于y.返回1表示真,返回0表示假.
                >=  大于等于   - 返回x是否大于等于y.
                <=  小于等于  - 返回x是否小于等于y.
                '''

            赋值运算符 = '''
                =    简单的赋值运算符
                +=   加法赋值运算符
                -=   减法赋值运算符
                *=   乘法赋值运算符
                /=   除法赋值运算符
                %=   取模赋值运算符
                **=  幂赋值运算符
                //=  取整除赋值运算符
                '''

            逻辑运算符 = '''
                在没有()的情况下,not优先级高于 and,and优先级高于or,即优先级关系为() >not > and > or ,同一优先级从左往右计算.
                x or y      x为真,值就是x,x为假,值是y.其中一个为真,就返回为真的值,如果两个都为真,就返回第一个.
                x and y     x为真,值是y, x为假,值是x.在第一个值为真的时候,就看第二个值,第二值为真,就为真,第二个值为假,就为假.第一个值为假,直接返回第一个值,即,为假.
                x and y     布尔"与" - 如果 x 为 False,x and y 返回 False,否则它返回 y 的计算值.
                x or y      布尔"或" - 如果 x 是 True,它返回 x 的值,否则它返回 y 的计算值.
                not x       布尔"非" - 如果 x 为 True,返回 False .如果 x 为 False,它返回 True.
                '''

            成员运算符 = '''
                in 如果在指定的序列中找到值返回True,否则返回False.x在y序列中, 如果x在y序列中返回True.
                not in 如果在指定的序列中没有找到值返回True,否则返回False.
                '''

            身份运算符 = '''
                is 是判断两个标识符是不是引用自一个对象x is y, 类似id(x) == id(y), 如果引用的是同一个对象则返回True,否则返回False
                is not 是判断两个标识符是不是引用自不同对象,x is not y,类似id(a) != id(b).如果引用的不是同一个对象则返回结果True,否则返回False.
                数据类型是不允许改变的, 这就意味着如果改变数字数据类型的值,将重新分配内存空间
                '''

            删除 = '''
                del  变量名  # 删除一些数字对象的引用
                '''

            类型转换 = '''
                int()       # 将数字组成的字符重转换为数字类型
                float()     # 将整数和字符串转换成浮点数.
                data = 10.bit_length()  # 当十进制用二进制表示时,最少使用的位数
                conjugate()     # 复数
                from_bytes()
                res = int.from_bytes(x)  # 把bytes类型的变量x,转化为十进制整数,并存入res中.其中bytes类型是python3特有的类型
                to_bytts()      # 是int.from_bytes的逆过程,把十进制整数,转换为bytes类型的格式
                complex(x)      # 将x转换到一个复数,实数部分为x,虚数部分为0.
                complex(x, y)   # 将 x 和 y 转换到一个复数,实数部分为 x,虚数部分为 y.x 和 y 是数字表达式在整数除法中,除法(/)总是返回一个浮点数,如果只想得到整数的结果,丢弃可能的分数部分,可以使用运算符 //
                abs(x)          # 返回数字的绝对值,如abs(-10) 返回 10
                ceil(x)         # 返回数字的上入整数,如math.ceil(4.1) 返回 5
                floor(x)        # 返回数字的下舍整数,如math.floor(4.9)返回4
                max(x1, x2, ...)# 返回给定参数的最大值,参数可以为序列.
                min(x1, x2, ...)# 返回给定参数的最小值,参数可以为序列.
                modf(x)         # 返回x的整数部分与小数部分,两部分的数值符号与x相同,整数部分以浮点型表示.
                pow(x, y)       # x ** y运算后的值.
                round(x,[,n])      # 返回浮点数x的四舍五入值,如给出n值,则代表舍入到小数点后的位数.
                sqrt(x)         # 返回数字x的平方根.
                choice(seq)     # 从序列的元素中随机返回一个元素,比如import random; random.choice(range(10)),从0到9中随机挑选一个整数.
                randrange([start, ]stop[, step]) # 从指定范围内,按指定基数递增的集合中返回一个随机数,基数缺省值为1
                random()        # 随机返回下一个实数,它在[0, 1)范围内.import random;random.random()
                seed([x])       # 改变随机数生成器的种子seed.如果你不了解其原理,你不必特别去设定seed,Python会帮你选择seed.
                shuffle(lst)    # 将序列的所有元素随机排序
                uniform(x, y)   # 随机生成下一个实数,它在[x, y] 范围内.
                '''

        def 字符串():

            字符串表达 = '''
                引号包含的都是字符串类型,单引双引没有区别
                三引号允许一个字符串跨多行,字符串中可以包含换行符、制表符以及其他特殊字符.自始至终保持一小块字符串的格式是所谓的WYSIWYG(所见即所得)格式的.
                在Python3中,所有的字符串都是Unicode字符串
                \       (在行尾时)表示续行符
                \\      反斜杠符号
                \'      单引号
                \"      双引号
                \n      换行
                \v      纵向制表符
                \t      横向制表符
                \r      回车(退到行首不换行)
                '''

            字符串格式化 = '''
                %s后面可以是数字类型.但 %d后面必须是数字类型的.
                print('abdc %s sdfsdf' % 'aaa')  # %2s表示占用两个字符的位置
                %d 格式化整数.
                %f 格式化浮点数字,可指定小数点后的精度.如 %0.2f 表示保留小数点后两位.

                msg = 'my name is %(name)s, age is %(age)s' % {"name": "lisi", "age": "18"} # 使用字典的方式
                msg = 'my name is %(name)s, age is %(age)s' % vars()                        # 还可以这样写,或者用 globals()
                msg = 'name:{},age:{},sex:{}'.format('haiyan', 18, 'girl')                  # 按顺序
                msg = 'name:{0},age:{1},sex:{0}'.format('aaaaaa', 'bbbbbb')                 # 按索引
                msg = 'name:{x},age:{y},sex:{z}'.format(x='haiyan', y='18', z='women')      # 赋值的方式
                msg = 'name:{x},age:{y},sex:{z}'.format_map({'x':'haiyan', 'y':'18', 'z':'women'})  # 使用format_map 传入字典
                更多内容见 字符串格式精讲.
                字符串拼接
                直接写 a='hello' 'word'   这样就会拼接在以前 a:   'helloword'
                '''

            字符串的对齐 = '''
                text = "hello"
                ljust,rjust,center接收一个可选的填充字符.
                text.ljust(20)
                text.rjust(20,'-')
                text.center(20)
                format函数可以完成对齐字符串.利用 > 右对齐、 < 左对齐、 ^ 居中对齐.这里不是字符串的format方法.是format函数.通过在对齐符前面指定填充符.
                format(text,'>20')
                format(text,'<20')
                format(text,'^20')
                format(text,'->20')
                format(text,'#<20')
                format(text,'*^20')
                format函数还可以对 浮点数操作
                x=1.2345
                format(x,'>10.2f')
                '''

            字符编码 = '''
                sys.getdefaultencoding()        # 获取系统编码
                python3默认编码为unicode,在unicode中,一个字符就是两个字节.python3,有两种数据类型,bytes和unicode. 字符串是unicode类型,bytes是bytes类型.
                bytes.decode(encoding="utf-8", errors="strict")  # Python3 中没有 decode 方法,但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象,这个 bytes 对象可以由 str.encode() 来编码返回.
                'test'.encode(encoding='UTF-8', errors='strict')  # 以 encoding 指定的编码格式编码字符串,errors 默认为 'strict',触发UnicodeError 也可指定'ignore',忽略,或者'replace' 将未知编码替换成？.
                例:            
                str='i an 特斯拉'
                unicode--->gbk
                uni_to_gbk=str.encode('gbk')  # 编码为gbk  encode是编码方法,括号中为目的编码.
                uni_to_gbk                    # 此时uni_to_gbk 是 b 字节类型.encode在编码的同时会把中文转成字节bytes类型.gbk用俩个字节表示一个中文字符.utf-8用三个字节表示一个中文字符.
                gbk--->unicode
                uni_to_gbk.decode('gbk')      # 解码为unicode   decode是解码方法,在括号中指定原来的编码.    
                ss='李四'
                b1=ss.encode()                # 默认解码为utf8,将unicode 解码为bytes类型,解码格式为utf8.encode 就是将unicode转换成bytes,utf8格式.
                #b1.decode('utf8')            # 括号里指定b1的格式.将b1 格式转成utf8.
                d1=b1.decode('utf8')          # 将bytes类型的utf8格式编码为Unicode,decode编码,并指定b1的是什么格式.
                g1=ss.encode('gbk')
                by=bytes(ss,'utf8')           # 另一种类型转换的方法,用bytes函数,将unicode转成utf8编码的bytes类型.
                st=str(by,'utf8')             # 用str函数将utf8编码的bytes类型转成unicode.后面指定,by的当前格式.   
                '''

            字符串方法 = '''
                'test'.count('t',beg,end)        # 返回 str 在 string 里面出现的次数,可以指定查找开始和结束的位置.
                'test'.startswith(str, beg,end) 
                    检查字符串是否是以 str 开头,可以指定查找开始和结束的位置,返回bool值.
                    startswith可以接收多个后缀匹配,但多个匹配项必须放在一个元组里面.
                    strs=['mysql.db','zabbix.py','run.bat','test','haproxy.cfg','nginx.log']
                    [s for s in strs if s.startswith(('my','ha','ng','za'))]
                'test'.endswith('t', beg, end)
                    检查字符串是否以指定的字符串结束,可以指定查找开始和结束的位置,返回bool值.
                    endswith可以接收多个后缀匹配,但多个匹配项必须放在一个元组里面.
                    strs=['mysql.db','zabbix.py','run.bat','test','haproxy.cfg','nginx.log']
                    [s for s in strs if s.endswith(('.db','.bat','.cfg','.log'))]
                'te\tst'.expandtabs(tabsize=8)                   # 把字符串 string 中的 tab 符号转为空格,tab 符号默认的空格数是 8 ,也可以指定其他空格数.
                'test'.find(str,beg,end)                         # 检测 str 是否包含在字符串中,可以指定查找开始和结束的位置,正常返回开始的索引值,未找到返回-1.
                'test'.index(str, beg,end)                       # 跟find()方法一样,只不过如果str不在字符串中会报一个异常.
                'test'.upper()      # 转换字符串中的小写字母为大写.
                'test'.isalnum()    # 如果字符串至少有一个字符并且所有字符都是字母或数字则返回True, 否则返回False.
                'test'.isdigit()    # 如果字符串只包含数字则返回 True 否则返回 False.
                'test'.islower()    # 如果字符串中包含至少一个区分大小写的字符,并且所有这些(区分大小写的)字符都是小写,则返回 True,否则返回 False.
                'test'.isnumeric()  # 如果字符串中只包含数字字符,则返回 True,否则返回 False.
                'test'.isspace()    # 如果字符串中只包含空白,则返回 True,否则返回 False.
                'test'.istitle()    # 如果字符串是标题化的(见 title())则返回 True,否则返回 False.
                'test'.isupper()    # 如果字符串中包含至少一个区分大小写的字符,并且所有这些(区分大小写的)字符都是大写,则返回 True,否则返回 False.
                'test'.split(str="t", num)    # 以 str 为分隔符截取字符串,可以指定分割次数.默认以空格分割.也可以以其他的字符分割,分割完成后,如果没有指定分割符,或者分隔符为None,任何以空格为分隔符的结果中的空字符串,将从结果中删除.
                ' sdf '.split()     # 返回 ['sdf']
                ' sdf '.split(' ')  # 返回['', 'sdf', '']
                'test'.strip()      # 在字符串上执行 lstrip()和 rstrip(),默认去掉两边的空格,可以指定多个字符,如: 'abcdef'.strip('abef'),返回:cd .尽可能的匹配.
                 len('test')         # 返回字符串长度.
                'test'.ljust(6,'*') # 返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串,fillchar 默认为空格.
                'test'.lower()      # 转换字符串中所有大写字符为小写.
                'test'.lstrip()     # 截掉字符串左边的空格或指定字符.
                'test'.replace('t', 'T',2)  # 把 将字符串中的 str1 替换成 str2,也可以指定替换次数.有返回值,返回替换后的字符串.
                'test'.maketrans()          # 创建字符映射的转换表,对于接收两个参数的最简单的调用方式,第一个参数是字符串,表示需要转换的字符,第二个参数也是字符串表示转换的目标.
                 max('test')     # 返回字符串 str 中最大的字母.
                 min('test')     # 返回字符串 str 中最小的字母.
                'test'.capitalize()     # 将字符串的第一个字符转换为大写.
                'test'.isalpha()        # 如果字符串至少有一个字符并且所有字符都是字母则返回True, 否则返回False.
                'test'.rfind(str, beg, end)   # 类似于 find()函数,不过是从右边开始查找.
                'test'.rindex(str, beg, end)  # 类似于 index(),不过是从右边开始.
                'test'.rjust(7,'*')     # 返回一个原字符串右对齐,并使用fillchar(默认空格)填充至长度 width 的新字符串.
                'test'.rstrip()         # 删除字符串字符串末尾的空格.
                'test'.swapcase()       # 将字符串中大写转换为小写,小写转换为大写
                'test'.title()          # 返回"标题化"的字符串,就是说所有单词都是以大写开始,其余字母均为小写(见 istitle())
                'test'.translate('test', deletechars="")    # 根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
                'test'.zfill(9)         # 返回长度为 width 的字符串,原字符串右对齐,前面填充0
                'test'.isdecimal()      # 检查字符串是否只包含十进制字符,如果是返回 true,否则返回 false.
                'test'.splitlines(True) # 按照行('\r', '\r\n', \n')分隔,返回一个包含各行作为元素的列表,如果参数 keepends 为 False,不包含换行符,如果为 True,则保留换行符.
                '+'.join([1,2,3])       # join,以指定的字符并将一个容器类型的数据.接收一个可迭代对象,返回拼接后的字符串.可以直接将生成器表达式作为参数传入到join,不用加圆括号.join 里面可以直接传入生成器.
                'test {}'.format('2')   # 用于字符串格式化,详见字符串格式化.
                'test {name}'.format_map({'name':'lisli})  # 用于字符串格式化,与format不同的是format_map接收的是一个映射关系,如字典,字典的键是字符中的指定名字,键是你要传入的值.
                '''

            索引与切片 = '''
                a = 'ABCDEFGHIJK'
                print(a[0])
                print(a[3:5:2])
                print(a[-1:-4:-1])
                print(a[::-1])
                '''

        def 列表():
            '''
                列表的数据项不需要具有相同的类型
                创建一个列表,用逗号分隔的不同的数据项,使用方括号括起来,
                或用list()的方法创建列表
                '''

            列表的方法 = '''
                len(list)               # 列表元素个数
                max(list)               # 返回列表元素最大值  
                max(list)               # 返回列表元素最大值  
                min(list)               # 返回列表元素最小值 
                list(tuple)             # 将元组转换为列表  
                list.append(obj)        # 在列表末尾添加新的对象  无返回值
                list.count(obj)         # 统计某个元素在列表中出现的次数 无返回值
                list.extend(seq)        # 在列表末尾一次性追加另一个序列中的多个值(用新列表扩展原来的列表) 无返回值
                list.index(obj)         # 从列表中返回某个值第一个匹配项的索引位置
                list.insert(index, obj) # 将对象插入列表,指定插入位置 
                list.pop(obj=list[-1])  # 移除列表中的一个元素(默认最后一个元素),并且返回该元素的值
                list.remove(obj)        # 移除列表中某个值的第一个匹配项 无返回值
                list.reverse()          # 反向列表中元素,无返回值,改变列表本身,但reversed()不改变列表本身,返回反向的列表,列表中不能出现不同类型的数据.
                list.sort([func])       # 对原列表进行排序,无返回值 ,改变列表本身,但sorted()不改变列表本身,返回反向的列表,列表中不能出现不同类型的数据.可以用key=func 来指定一个可调用对象来进行排序,只接受单个参数的函数.
                list.clear()            # 清空列表 无返回值 
                list.copy()             # 复制列表 无返回值,属于浅拷贝
                del                     # 语句可以删除列表中的元素,也可以在内存空间删除整个列表.
                '''

        def 元组():
            '''
                元组的元素不能修改.元组使用小括号.即使元组中有一个元素,也需要使用逗号分割.可以使用tuple()函数创建
                '''

            元组的方法 = '''
                即使没有圆括号,python也能识别除元组,如  a=1,2,3,4
                del             # 语句来删除整个元组,不能删单个元素 
                len(tuple)      # 计算元组元素个数.     
                max(tuple)      # 返回元组中元素最大值.     
                min(tuple)      # 返回元组中元素最小值.     
                tuple(list)     # 将列表转换为元组.
                sorted(tuple)   # 如果使用sorted对元组进行排序,返回的是一个列表
                '''

        def 字典():
            '''
                可变容器模型,且可存储任意类型对象. 键必须是唯一的,但值则不必. 值可以取任何数据类型,但键必须是可哈希的,不可变的,如字符串,数字或元组.
                字典虽然是无序的,但字典的顺序是固定的.
                字典的keys(),items()支持常见的集合操作,求并集,交集,差集,不必转成集合.它们都是唯一的,而values()不支持集合操作.
                '''

            字典的方法 = '''
                len(dict1)          # 计算字典元素个数,即键的总数.     
                str(dict1)          # 输出字典,以可打印的字符串表示.
                eval(str1)          # 将字符串类型的字典转换成字典,返回字典         
                dict1.clear()       # 删除字典内所有元素 
                dict1.copy()        # 返回一个字典的浅复制 
                dict1.fromkeys(seq,[val])       # 创建一个新字典,以序列seq中元素做字典的键,val为字典所有键对应的初始值  如:dic1=dict().fromkeys([1,2,3,4,5],'test') 
                dict1.get(key, default=None)    # 返回指定键的值,如果值不在字典中返回default值 
                key in dict1                    # 如果键在字典dict里返回true,否则返回false 
                dict1.items()                   # 以列表返回可遍历的(键, 值) 元组数组 
                dict1.keys()                    # 以列表返回一个字典所有的键 
                dict1.setdefault(key, default=None)     # 和get()类似, 但如果键不存在于字典中,将会添加键并将值设为default,有返回值,无论key在不在字典里,都返回key相应的值.有则返回值,无则返回default.
                dict1.update(dict2)
                    把字典dict2的键/值对更新到dict里  无返回值.
                    字典的update可以用一个zip对象来升级
                    a=[1,2,3,4]
                    b=['a','b','c','d']
                    c={}
                    c.update(zip(a,b))
                    c -----> {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
                dict1.values()                  # 以列表返回字典中的所有值 
                dict1.pop(key,[default])        # 删除字典给定键 key 所对应的值,返回值为被删除的值.key值必须给出. 否则,返回default值.是有返回值的. 
                dict1.popitem()                 # 随机返回并删除字典中的一对键和值(一般删除末尾对). 是有返回值的.
                del                             # 能删单一的元素也能清空字典. 
                '''

            有序字典 = '''
                from collections import OrderedDict
                当对字典做迭代时,会严格安装字典的初始添加顺序进行
                '''

            字典的应用 = '''
                字典的键与键值对的元素集合是可以和普通集合一样进行求交集和并集的.
                但是字典的值的元素集合不行.
                a={'a':1,'b':2,'c':3,'d':4}
                b={'b':2,'c':3}
                a.keys() & b.keys() -----> {'b', 'c'}  求a,b 键的交集
                a.keys() - b.keys() -----> {'a', 'd'}  求a,b 键的差集
                a.keys() | b.keys() -----> {'a', 'b', 'c', 'd'} 求a,b 键的并集
                a.keys() - ['a','c'] -----> {'b', 'd'}  可以直接与列表求交集，并集
                a.items() & b.items() -----> {('b', 2), ('c', 3)}  求a,b 项的交集
                a.items() - b.items() -----> {('a', 1), ('d', 4)}  求a,b 项的差集
                a.items() | b.items() -----> {('a', 1), ('b', 2), ('c', 3), ('d', 4)}  求a,b 项的并集
                '''

        def 集合():
            '''
                集合是一个无序的,不重复的数据组合,基本功能是成员关系测试和删除重复元素.关系测试,测试两组数据之前的交集、差集、并集等关系,创建一个空集合必须用set().
                set([obj]) 可变集合:ojb必须是支持迭代的,由obj中的元素创建集合,否则创建一个空集合
                frozenset([obj]) 不可变集:执行方式与set()方法相同,但它返回的是不可变集合
                集合里面的元素必须是可哈希的.字典不能作为集合的元素
                '''

            集合的使用 = '''
                s | t
                s.union(t)          # 求并集
                s & t
                s.intersection(t)   # 求交集
                s - t
                s.difference(t)     # 求差集
                s ^ t
                s.symmetric_difference(t)   # 对称差集,a和b中不同时存在的元素
                s <= t
                s.issubset(t)               # 测试是否 s 中的每一个元素都在 t 中
                s >= t
                s.issuperset(t)             # 测试是否 t 中的每一个元素都在 s 中
                len(s)          # 集合s中元素个数
                obj in s        # 成员测试
                obj not in s    # 非成员测试
                s == t          # 等价测试
                s != t          # 不等价测试
                s.copy()        # 赋值操作:返回s的(浅复制)副本
                s.update(t)     # 将t中的成员添加s,t 必须是一个可迭代对象,类似于列表的extend()方法.
                s.add(obj)      # 将obj添加到s
                s.remove(obj)   # 删除操作
                s.discard(obj)  # 丢弃操作:remove() 的友好版本,如果s中存在ojb,从s中删除它
                s.pop()         # 移除并返回s中的任意一个值
                s.clear()       # 移除s中的所有元素a'v'a'a
                '''

    def 流程结构():

        if判断 = '''
            在没有()的情况下not 优先级高于 and,and优先级高于or,即优先级关系为( )>not>and>or,同一优先级从左往右计算.
            通过使用 and or not 实现多重条件约束
            
            if not 条件 and 条件 or 条件:
                pass
            elif not 条件 and 条件 or 条件:
                pass
            else:
                pass
            '''

        循环 = '''        
            while 条件:
                pass
            else:
                pass
            
            for 变量 in 可迭代对象:
                pass
            else:
            
            break: 跳出当前循环.
            continue: 跳出本次循环
            
            else 作用是指,当循环正常执行完,中间没有被break 中止的话,就会执行else后面的语句
            如果执行过程中被break,就不会执行else的语句
            '''

        三元运算 = '''
            r = 值1 if 条件 else 值2
            n = x if x > y else y
            如果 if 后面的条件成立,就返回 if 前面的值1,否则返回 else 后面的值2,r就等于返回值.
            三元运算还可以和推导式配合使用.详见推导式.
            '''

    def 文件操作():

        参数说明 = '''
            open(name,mode,encoding)
            with open(name,'r') as f,open(name1,'w') as f1:
            参数说明:
            name : 文件名称的字符串.
            mode : 打开文件的模式,默认文件访问模式为只读(r).
            encoding : 默认的打开方式r ,默认的打开编码是操作系统的默认编码
            不同模式打开文件的完全列表:
            模式	描述
            r	以只读方式打开文件.文件的指针将会放在文件的开头.这是默认模式.
            rb	以二进制格式打开一个文件用于只读.文件指针将会放在文件的开头.这是默认模式.
            r+	打开一个文件用于读写.文件指针将会放在文件的开头.
            rb+	以二进制格式打开一个文件用于读写.文件指针将会放在文件的开头.
            w	打开一个文件只用于写入.如果该文件已存在则将其覆盖.如果该文件不存在,创建新文件.
            wb	以二进制格式打开一个文件只用于写入.如果该文件已存在则将其覆盖.如果该文件不存在,创建新文件.
            w+	打开一个文件用于读写.如果该文件已存在则将其覆盖.如果该文件不存在,创建新文件.
            wb+	以二进制格式打开一个文件用于读写.如果该文件已存在则将其覆盖.如果该文件不存在,创建新文件.
            a	打开一个文件用于追加.如果该文件已存在,文件指针将会放在文件的结尾.也就是说,新的内容将会被写入到已有内容之后.如果该文件不存在,创建新文件进行写入.
            ab	以二进制格式打开一个文件用于追加.如果该文件已存在,文件指针将会放在文件的结尾.也就是说,新的内容将会被写入到已有内容之后.如果该文件不存在,创建新文件进行写入.
            a+	打开一个文件用于读写.如果该文件已存在,文件指针将会放在文件的结尾.文件打开时会是追加模式.如果该文件不存在,创建新文件用于读写.
            ab+	以二进制格式打开一个文件用于追加.如果该文件已存在,文件指针将会放在文件的结尾.如果该文件不存在,创建新文件用于读写.
            x   对不存在的文件执行写入操作,如果文件已存在会报错.FileExistErroe.
            xb  
            '''

        属性与方法 = '''
            f.read(3) 文件打开方式为文本模式时,代表读取3个字符.文件打开方式为b模式时,代表读取3个字节.
            f.readline() 一行一行读  每次只读一行,不会自动停止
            f.readlines([size]) 返回包含size字符的列表,size 未指定则返回全部行,只有字符个数超过本行的范围,返回下一行.
            for line in f: print line #通过迭代器访问,一行一行读  从第一行开始 每次读一行 读到没有之后就停止
            f.write("hello\n") #如果要写入字符串以外的数据,先将他转换为字符串.
            f.tell() 返回一个整数,表示当前文件指针的位置(就是到文件头的比特数).
            f.seek(偏移量,[起始位置]) 用来移动文件指针. 偏移量:单位:比特,可正可负.起始位置:0-文件头,默认值;1-当前位置;2-文件尾,1和2必须在b模式下进行,但无论哪种模式,都是以bytes为单位移动的
            f.truncate()  截断必须是写模式,但是不能用w或w+等方式打开,因为那样直接清空文件了,所以truncate要在r+或a或a+等模式下测试效果,截取文件到最大size字节,默认为当前文件位置
            f.close()                     # 关闭文件
            f.fileno()                    # 返回文件的描述符
            f.flush()                     # 刷新文件的内部缓冲区
            f.isatty()                    # 判断file是否是一个类tty设备
            f.next()                      # 返回文件的下一行,或在没有其他行时引发StopIteration异常
            f.seek(off, whence=0)         # 在文件中移动文件指针,从whence(0代表文件起始,1代表当前位置,2代表文件末尾)偏移off字节
            f.tell()                      # 返回当前在文件中的位置
            f.writelines(seq)             # 向文件写入字符串序列seq;seq应该是一个返回字符串的可迭代对象
            f.close() 关闭文件
            f.closed          # 表示文件已被关闭,否则为False
            f.encoding        # 文件所使用的编码  当unicode字符串被写入数据时,它将自动使用file.encoding转换为字节字符串;若file.encoding为None时使用系统默认编码
            f.mode            # Access文件打开时使用的访问模式
            f.name            # 文件名
            fe.newlines       # 读取行分隔符,未读取到行分隔符时为None,只有一种行分隔符时为一个字符串,当文件有多种类型的行结束符时,则为一个包含所有当前所遇到的行结束符的列表
            f.softspace       # 为0表示在输出一数据后,要加上一个空格符,1表示不加
            '''

def 函数():
    '''python3 函数详解'''

    def 内置函数():

        作用域相关 = '''
            globals() # 函数会以字典类型返回当前位置的全部全局变量.可以这样用 globals().get(func)()  就可以调用函数.
            locals()  # 会以字典类型返回当前位置的全部局部变量. 获取执行本方法所在命名空间内的局部变量的字典
            '''

        字符串执行 = '''
            eval()      
                用来执行一个字符串表达式,并返回表达式的值.eval(def_name) 里面可以直接跟函数名.返回的是函数对象(内存地址) 用eval(def_name)() 执行.用于将字典格式的字符串转换为字典. 
            exec()      
                执行储存在字符串或文件中的 Python 语句,相比于 eval,exec可以执行更复杂的 Python 代码. 
            compile()   
                函数将一个字符串编译为字节代码. 
            '''

        输入输出 = '''
            print(*objects, sep=' ', end='\n', file=sys.stdout,flush=False) 
                打印输出 可以一次输出多个对象.输出多个对象时,需要用 , 分隔.
                sep -- 用来间隔多个对象,默认值是一个空格.
                end -- 用来设定以什么结尾.默认值是换行符 \n,我们可以换成其他字符串.
                file -- 要写入的文件对象.file是一个文件描述符,
                with open('test.txt','a+') as f:
                    print('hello,world',file=f)
            input()
                函数接收一个标准输入数据,返回为 string 类型.
            '''

        内存相关 = '''
            hash()
                用于获取取一个对象(字符串或者数值等)的哈希值.
            id()
                用于获取对象的内存地址.
            '''

        文件操作 = '''
            open()
                用于打开一个文件,创建一个 file 对象,相关的方法才可以调用它进行读写.详见文件操作. 
            '''

        模块相关 = '''
            __import__
                用于动态加载类和函数. 如果一个模块经常变化就可以使用 __import__() 来动态载入. 
            '''

        帮助 = '''
            help()
                用于查看函数或模块用途的详细说明. 输入q退出
            '''

        调试相关 = '''
            callable()
                用于检查一个对象是否是可调用的.如果返回True,object仍然可能调用失败；但如果返回False,调用对象ojbect绝对不会成功. 
                对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True 
            '''

        查看内置属性 = '''
            dir()
                不带参数时,默认查看全局空间内的属性,返回当前范围内的变量、方法和定义的类型列表;带参数时,返回参数的属性、方法列表.如果参数包含方法__dir__(),该方法将被调用.如果参数不包含__dir__(),该方法将最大限度地收集参数信息.
            '''

        数字类型 = '''
            int() ***** 
                用于将一个字符串或数字转换为整型. 
            loat()
                将整数和字符串转换成浮点数. 
            complex()
                用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数.如果第一个参数为字符串,则不需要指定第二个参数
            '''

        进制转换 = '''
            hex()
                用于将10进制整数转换成16进制,以字符串形式表示.返回的是一个字符串. 
            oct()
                将一个整数转换成8进制字符串.
            bin()
                一个整数 int 或者长整数 long int 的二进制表示. 
            '''

        数学运算 = '''
            abs()
                函数返回数字的绝对值. 
            min()
                返回给定参数的最小值,参数可以为序列.也可以不是序列.返回的是值.
                min也可以接收序列的元素为元组进行比较,以元组的第一个元素为比较依据,如果第一个元素相等,以第二个元素为依据.以此类推
                例: min((3,'a'),(1,'b'),(1,'a')) 返回 (1, 'a'),可以用key=func 指定一个函数来根据函数返回的值来比较.
                生成器表达式可以作为单独的参数传入到min,不需要在加圆括号,例如: min(x for x in range(10))
            max()
                返回给定参数的最大值,参数可以为序列.也可以不是序列.返回的是值.
                max也可以接收序列的元素为元组进行比较,以元组的第一个元素为比较依据,如果第一个元素相等,以第二个元素为依据.以此类推
                例: max((3,'a'),(1,'b'),(1,'a')) 返回 (3, 'a'),可以用key=func 指定一个函数来根据函数返回的值来比较.
                生成器表达式可以作为单独的参数传入到max,不需要在加圆括号,例如: max(x for x in range(10))
            sum(iterable,start)
                对系列进行求和计算.参数必须是可迭代的数字集,可以指定开始值.
                sum 可以接收两个参数,第一个式可迭代对象,第二个参数是,从哪个值开始计算总和,不是指可迭代对象的索引,返回值: iterable的和加上start的值,start默认等于 0 .
                生成器表达式可以作为单独的参数传入到sum,不需要在加圆括号,例如: sum(x for x in range(10))
            round()
                返回浮点数x的四舍五入值.可以指定精确到小数点以后几位.默认是取整,也就是小数点以后0位.也可以为负数,相应的取 十位,百位,千位.
                round(1.23,1) -----> 1.2
                round(-1.27,1) -----> -1.3
                round(1.2536,3) -----> 1.254
                round(12536,-2) -----> 12500
            pow(x,y)
                方法返回 xy(x的y次方) 的值.
            divmod(x,y)
                返回x除y的商和余数的元组.
            '''

        序列相关 = '''
            list()
                用于将元组转换为列表.
            tuple()
                函数将列表转换为元组.
            sorted(reverse=False)
                对所有可迭代的对象进行排序操作,通过reverse参数可以反向排序.这里的方向排序是返回一个列表,而reversed()函数返回的是一个迭代器.
                也可以接收序列的元素为元组进行比较,以元组的第一个元素为比较依据,如果第一个元素相等,以第二个元素为依据.以此类推
                可以使用 key=func 的方式指定一个用于排序的函数.key指定一个接收一个参数的函数,这个函数用于从每个元素中提取一个用于比较的关键字.默认值为None
                可以使用 reverse=True,来进行反转.
                sort 与 sorted 区别: 
                sort 是应用在 list 上的方法,sorted 可以对所有可迭代的对象进行排序操作. 
                list 的 sort 方法返回的是对已经存在的列表进行操作,而内建函数 sorted 方法返回的是一个新的 list,而不是在原来的基础上进行的操作.
            reversed()
                返回一个反转的迭代器. 接收一个序列,返回的是一个迭代器.不带关键字参数,没有key= 关键字
                也可以接收序列的元素为元组进行比较,以元组的第一个元素为比较依据,如果第一个元素相等,以第二个元素为依据.以此类推
            slice()
                实现切片对象,主要用在切片操作函数里的参数传递.
                如: l=[1,2,3,4]
                a=slice(1,3,1)  依次是起始值,结束值,步长  可以通过 a.start、a.stop、a.step 得到这三个值.
                l[a]
                a.indices(len)  接收一个可迭代对象的长度.
                如果,如果给定的len大于slice的结束值stop,就返回(start,stop,step),如果如果给定的len小于slice的结束值stop,就返回(start,len,step),总之避免IndexError异常.
                s='abcdefghijklmn'
                for i in range(*a.indices(len(s))):
                    print(s[i])
                返回  bc
            str()
                将对象转化为适于人阅读的形式. 
            format()
                字符串格式化的功能.见字符串对齐.
            bytes()
                返回一个新的 bytes 对象,该对象是一个 0 <= x < 256 区间内的整数不可变序列.它是 bytearray 的不可变版本. 
            bytearray()
                法返回一个新字节数组.这个数组里的元素是可变的,并且每个元素的值范围: 0 <= x < 256.
            memoryview()
                返回给定参数的内存查看对象(Momory view). 所谓内存查看对象,是指对支持缓冲区协议的数据进行包装,在不需要复制对象基础上允许Python代码访问
            ord()
                是 chr() 函数(对于8位的ASCII字符串)或 unichr() 函数(对于Unicode对象)的配对函数,它以一个字符(长度为1的字符串)作为参数,返回对应的 ASCII 数值,或者 Unicode 数值,如果所给的 Unicode 字符超出了你的 Python 定义范围,则会引发一个 TypeError 的异常. 
            chr()
                用一个范围在 range(256)内的(就是0～255)整数作参数,返回一个对应的字符.
            ascii()
                类似 repr() 函数, 返回一个表示对象的字符串, 但是对于字符串中的非 ASCII 字符则返回通过 repr() 函数使用 \x, \u 或 \U 编码的字符.  
            repr()
                将对象转化为供解释器读取的形式.
            dict()
                用于创建一个字典.
            set()
                创建一个无序不重复元素集,可进行关系测试,删除重复数据,还可以计算交集、差集、并集等.要求集合的元素必须是可哈希的.
            frozenset()
                返回一个冻结的集合,冻结后集合不能再添加或删除任何元素.要求集合的元素必须是可哈希的.
            len()
                返回对象(字符、列表、元组等)长度或项目个数. 
            enumerate()
                用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列,同时列出数据和数据下标,一般用在 for 循环当中.
                返回的是一个enumreate对象实例,是一个迭代器,返回连续的元组.元组是由一个索引值,和next(调用所传入序列)的值.组成
            all()
                用于判断给定的可迭代参数 iterable 中的所有元素是否不为 0、''、False 或者 iterable 为空,如果是返回 True,否则返回 False.可以直接将生成器表达式作为参数传入到all,不用加圆括号.
            any()
                用于判断给定的可迭代参数 iterable 是否全部为空对象,如果都为空、0、false,则返回 False,如果不都为空、0、false,则返回 True. 可以直接将生成器表达式作为参数传入到any,不用加圆括号.
            zip()
                函数用于将可迭代的对象作为参数,将对象中对应的元素打包成一个个元组,然后返回由这些元组组成的列表.如果各个迭代器的元素个数不一致,则返回列表长度与最短的对象相同. 
                zip可以接受多余2个的序列.zip创建的只是一个迭代器.使用list强转.
            filter()
                用于过滤序列,过滤掉不符合条件的元素,返回由符合条件元素组成的新列表.
                该接收两个参数,第一个为函数,第二个为序列,序列的每个元素作为参数传递给函数进行判断,然后返回 True 或 False,最后将返回 True 的元素放到新列表中.
                filter 返回的是一个迭代器. 
            map()
                会根据提供的函数对指定序列做映射.第一个参数 function 以参数序列中的每一个元素调用 function 函数,返回包含每次 function 函数返回值的新列表. 
            '''

        反射相关 = '''
            delattr()
                函数用于删除属性. 
            setattr()
                对应函数 getatt(),用于设置属性值,该属性必须存在.
            getattr()
                函数用于返回一个对象属性值. 
            hasattr()
                用于判断对象是否包含对应的属性. 
            '''

        迭代与生成器 = '''
            range()
                返回的是一个可迭代对象(类型是对象),而不是列表类型, 所以打印的时候不会打印列表.
            next()
                迭代器的下一个项目.
            iter()
                用来生成迭代器.将可迭代对象转化为迭代器.iter可以接收一个无参的可调用对象,以及一个结束值.当使用这种方法时,iter()会重复调用可调用对象.
                直到返回的值与结束值相等.
                import sys
                f=open('/etc/passwd')
                for cond in iter(lambda:f.read(10),''):
                    n=sys.stdout.write(cond)
            '''

        定义类方法 = '''
            classmethod()
                修饰符对应的函数不需要实例化,不需要 self 参数,但第一个参数需要是表示自身类的 cls 参数,可以来调用类的属性,类的方法,实例化对象等.
            staticmethod()
                返回函数的静态方法.
            property()
                作用是在新式类中返回属性值.如果你只有第一个参数则返回对象的类型,三个参数返回新的类型对象.
            '''

        判断类关系 = '''
            isinstance()
                接受一个类型,如:list、dict、str、tuple、bytes等等.
                来判断一个对象是否是一个已知的类型,类似 type().
                isinstance() 与 type() 区别: 
                type() 不会认为子类是一种父类类型,不考虑继承关系. 
                isinstance() 会认为子类是一种父类类型,考虑继承关系. 
                如果要判断两个类型是否相同推荐使用 isinstance(). 
                isinstance也可以接收一个元组
                isinstance (a,(str,int,list))    # 是元组中的一个返回 True
            issubclass(class, classinfo)
                用于判断参数 class 是否是类型参数 classinfo 的子类.
            '''

        其他方法 = '''
            vars()
                返回对象object的属性和属性值的字典对象.
            object()
                所有类的基类.
            super()
                函数是用于调用父类(超类)的一个方法. super 是用来解决多重继承问题的,直接用类名调用父类方法在使用单继承的时候没问题,但是如果使用多继承,会涉及到查找顺序(MRO)、重复调用(钻石继承)等种种问题. 
                详见 面向对象中super的解释   
            type()
                判断一个数据的类型.
            bool()
                用于将给定参数转换为布尔类型,如果没有参数,返回 False.bool 是 int 的子类.
            '''

    def 自定义函数():

        函数定义 = '''
            def 关键字 函数名(设定与变量相同):
                函数的第一行语句建议使用三引号字符串—用于存放函数说明.可以使用  函数名.__doc__  调用.
                函数体
                return 结束函数,选择性地返回一个值给调用方.不带表达式的return相当于返回 None. 返回多个值,将多个值放在元组中返回.
                return 后面可以跟逻辑判断和短路逻辑 
                如: return a > 0 and a   
                return b > 0 or 0
                return a if a > 0 else 4
                return a or b
                return a and b
                return a,b,c  可以返回多个值,但值之间必须由','分割.
                '''

        函数的参数 = '''
            函数创建时:
            默认参数. 必须在位置参数后面.
            动态参数 *args,**kwargs 
            位置参数,*args,默认参数,**kwargs
            函数使用时
            位置参数.形参与实参必须一一对应,按顺序传入.
            关键字参数.必须一一对应,不分顺序.
            混合参数.一一对应 且 关键字参数必须在位置参数后面.
            顺序:位置参数,*args,关键字参数,**args
            *args 后面可以再跟一个参数,但传参时*args的参数必须以关键的方式指定.
            def add(*args,num):
                print(sum(args)+num)
            add(1,2,3,4,num=5)

            a=[1,2,3]
            b='test'
            [1,2,3] 是 List 类型,"test" 是 String 类型,而变量 a 是没有类型,a仅仅是一个对象的引用),可以是指向任何类型对象. 
            在 python 中,strings, tuples, 和 numbers 是不可变类型,而 list,dict 等则是可变类型. 
            不可变类型:变量赋值 a=5 后再赋值 a=10,这里实际是新生成一个 int 值对象 10,再让 a 指向它,而 5 被丢弃,不是改变a的值,而是a指向了10. 
            可变类型:变量赋值 l=[1,2,3,4] 后再赋值 l[2]=5 则是将 list l 的第三个元素值更改,本身l没有动,只是其内部的一部分值被修改了. 
            python 函数的参数传递: 
            不可变类型:如 整数、字符串、元组.如fun(a),传递的只是a的copy,没有影响a对象本身.比如在 fun(a)内部修改 a 的值,只是修改另一个复制的对象,不会影响 a 本身. 
            可变类型:如 列表,字典.如 fun(l),则是将 l 的引用传过去,修改后fun外部的la也会受影响.
            传入函数的和函数返回的都是同一个对象的引用.
            函数的默认参数应该是不可变类型的.如果一定要使用可变类型的,在函数外部声明 _no_value=object()  将_no_value作为默认参数的值传入函数.在函数里判断 if 默认参数 is _no_value:默认参数=？
            object()是一个内存地址,独特的私有实例,可以用这个特殊值判断用户是否提供了参数.
            如果函数的默认参数是可变类型的话,应该把None作为默认值.
            def spam(a,b=None):
                if b is None:    # 这里只能用is,不能用 if not b:这种语句,如果b=其他布尔值是false的参数呢？
                    b=list()
            默认参数的赋值只会在函数定义的时候绑定一次.
            x=42
            def spam(a,b=x):
                print(a,b)
            spam(1) -----> 1,42
            x=23
            spam(1) -----> 1,42
            默认值在函数定义时就已经确认好了.默认值应该时不可变类型的.
            '''

        函数作用域 = '''
            全局作用域:全局名称空间,内置名称空间. 
            局部作用域:局部名称空间 
            变量与值的加载顺序:内置命名空间(程序运行前加载)->全局命名空间(程序运行中:从上到下加载)->局部命名空间(程序运行中:调用时才加载) 
            变量与值的取值顺序:局部名称空间 ---> 全局名称空间 ----> 内置名称空间 
            global 关键字用来在函数或其他局部作用域中使用全局变量.但是如果不修改全局变量也可以不使用global关键字.如果更改一个全局变量,要先声明,后更改.
            nonlocal 关键字用来在函数或其他作用域中使用外层(非全局)变量.外部必须有这个变量,在内部函数声明nonlocal变量之前不能再出现同名变量.
            '''

        函数的特性 = '''
            函数名本质上就是函数的内存地址的引用
            可以互相赋值. 
            函数名可以当成函数的参数 
            可以当成容器类数据类型的参数 
            函数名可以当成函数的返回值 
            函数是第一类对象
            第一类对象:可在运行期创建,可用作函数参数或返回值,可存入变量的实体.
            '''

        函数的注解 = '''
            函数的注解没有任何的语法意义.只会保存在函数的__annotations__属性中.
            def test(x:int,y:int) -> int:
                print(x)
                print(y)

            test(1,2)
            '''

        函数的文档字符串 = '''
            通常函数的第一句话,会使用文档字符串,用于描述函数的用途
            可以通过__doc__属性获取.
            在装饰器中,可能获取不到.
            解决方法如下:
            1,手动编写
            def wrap(func):
                def call(*args,**kwargs):
                    return func()
                call.__doc__ = func.__doc__
                call.__name__ = func.__name__
                return call
            2,使用functools.wraps函数,详见下面的装饰器.
            '''

        函数的属性 = '''
            可以给函数添加任意属性
            def add():
                pass
            add.num=1
            add.msg='test'
            函数的属性保存在函数的 __dict__ 属性中.
            如果函数在装饰器中,可能获取不到.
            1,手动编写
            def wrap(func):
                def call(*args,**kwargs):
                    return func()
                call.__doc__ = func.__doc__
                call.__name__ = func.__name__
                call.__dict__.update(func.__dict__)
                return call
            2,使用functools.wraps函数,详见下面的装饰器.
            '''

    def 装饰器():
        '''为已存在的功能添加额外的功能,只在初始化脚本的时候执行一次.本质是函数, 用于装饰其他函数'''

        闭包 = '''
            闭包: 内层函数对外层函数非全局变量的引用,叫做闭包 
            闭包的好处:如果python 检测到闭包,函数的局部作用域不会随着函数的结束而结束 
            判断是不是闭包print(内层的函数名.__closure__) 
            '''

        通用语法 = '''
            普通装饰器
            def wapper(func):
                def inner(*args,**kwargs):
                    --- 附加功能 ---
                    ret=func(*args,**kwargs)
                    --- 附加功能 ---
                    return ret
                return inner

            @wapper   #相当于test=wapper(test)
            def test(num):
                print(num)

            带参数的装饰器
            def para(*args,**kwarg):
                def wapper(func):
                    def inner(*args,**kwargs):
                        --- 附加功能 ---
                        ret=func(*args,**kwargs)
                        print(num)
                        --- 附加功能 ---
                        return ret
                    return inner
                return wapper

            @para(3)    通过执行para,把装饰器返回.
            def test(num):
                print(num)

            装饰器返回被装饰函数的属性
            import functools
            functools.warps 通过对装饰器内层函数的装饰,被装饰函数的属性传递给外层函数.

            def outer(func):
                @functools.wraps(func)   #加在最内层函数正上方
                def inner(*args,**kwargs):
                    --- 附加功能 ---
                    ret=func(*args,**kwargs)
                    --- 附加功能 ---
                    return ret
                return inner

            多个装饰器装饰一个函数
            def w2(func):
                def inner2():
                    print('w2 ,before func')
                    func()
                    print('w2 ,after func')
                return inner2
            def w1(func):
                def inner1():
                    print('w1 ,before func')
                    func()
                    print('w1 ,after func')
                return inner1

            @w2
            @w1
            def f():
                print('in f')

            f()
            解:
            w2装饰w1,被w2装饰后的w1去装饰f,f作为参数传给w1,返回inner1,将inner1作为参数传递给w2,w2的inner2中的fun就是inner1,inner1中的func是f.
            inner2包含inner1,inner1包含f.  w1=w2(w1),f=w1(f),f=w2(w1(f))
            inner2()
                inner1()
                    f()
                inner1()
            inner2()
        '''

    def 闭包():
        闭包的定义 = '''
            闭包: 内层函数对外层函数非全局变量的引用,叫做闭包 
            闭包的好处:如果python 检测到闭包,函数的局部作用域不会随着函数的结束而结束 
            判断是不是闭包print(内层的函数名.__closure__)
            一般来讲,在闭包内层定义的变量,对外部来说是隔离的. 
            '''

        闭包的应用 = '''
            例1:详见装饰器
            例2:
            访问定义在闭包内的的变量,通过存取函数,将变量最为函数的属性附加到闭包,提供对内层函数的访问的支持.
            def sample():
                n=0
                def func():
                    print(n)
                def get_n():
                    return n
                def set_n(v):
                    nonlocal n
                    n=v
                func.get_n=get_n
                func.set_n=set_n
                return func

            f=sample()
            f() -----> 0
            f.set_n(10)
            f() -----> 10
            f.get_n() -----> 10
            '''

    def 迭代器生成器():

        迭代器 = '''
            凡是可以使用for循环取值的都是可迭代的
            可迭代协议 :内部含有__iter__方法的都是可迭代的
            迭代器协议 :内部含有__iter__方法和__next__方法的都是迭代器
            iter()函数将一个可迭代的对象,转化为迭代器.
            迭代器的三个方法:
            __length_hint__()   # 获取迭代器中元素的个数
            __setstate__()      # 根据索引值指定从哪里开始迭代
            __next()__()        # 一个一个取值,在for循环中,就是在内部调用了__next__方法
            迭代器的优势:
                节省内存
                取一个值就能进行接下来的计算 ,而不需要等到所有的值都计算出来才开始接下来的运算 —— 快
            迭代器的特性:
                惰性运算
        '''

        生成器 = '''
            一个包含yield关键字的函数就是一个生成器函数.yield可以为我们从函数中返回值,但是yield又不同于return.
            生成器和迭代器本质上是一样的
            yield函数
                执行生成器函数 会得到一个生成器 不会执行这个函数中的代码
                有几个yield,就能从中取出多少个值
            生成器表达式
                生成器表达式也会返回一个生成器 也不会直接被执行
                for循环里有几个符合条件的值生成器就返回多少值
            每一个生成器都会从头开始取值,当取到最后的时候,生成器中就没有值了
                一个生成器只能用一次
            return的执行意味着程序的结束,调用生成器函数不会得到返回的具体的值,而是得到一个可迭代的对象.
            每一次获取这个可迭代对象的值,就能推动函数的执行,获取新的返回值.直到函数执行结束.
            生成器函数的调用不会触发代码的执行,而是会返回一个生成器(迭代器).generator object.
            需要使用next()函数或生成器函数的__next__()方法,才会执行一次生成器.

            生成器.send()方法,相当于,先发送给生成器一个值,然后再执行next()方法,所以在使用send()之前,要先执行一次next().如果不先执行一次next(),send()发送的值将无变量接收.
            会报错.
            生成器用来解决 内存问题 和程序功能之间的解耦,是实现迭代器的一种手段
            '''

        生成器实例 = '''
            实例:
            def test(num=0):
                while True:
                    print(num)
                    num = yield num

            t=test()
            n=next(t)       # 打印0,返回0
            n=t.send(n+1)   # 传递1给num,打印1,返回1
            n=t.send(n+1)   # 传递2给num,打印2,返回2

            使用装饰器预激活生成器
            def init(func):
                def inner(*args,**kwargs):
                    ret = func(*args,**kwargs)
                    next(ret)  # 预激活
                    return ret
                return inner

            yield from 用法
            如果本身就是循环一个可迭代的,且要把可迭代数据中的每一个元素都返回 可以用yield from
            def test():
                yield from range(10) 
            for n in test():print(i)

            从生成器中取值,next send、循环、数据类型的强制转化
            第一种: next  随时都可以停止 最后一次会报错
            print(next(g))
            第二种:for循环 从头到尾遍历一次 不遇到break、return不会停止
            for i in g:print(i)
            第三种:list tuple 数据类型的强转  会把所有的数据都加载到内存里 非常的浪费内存
            print(list(g))

            实现tail -f 命令
            import time
            def tail(file):
                with open(file) as f:
                    f.seek(0,2)
                    while True:
                        line=f.readline()
                        if bool(line) == False:
                            time.sleep(0.1)
                            continue
                        yield line

            '''

        推导式 = '''
            推导式里面可以跟三元运算,可以有多个 for 循环,每个for循环里面可以跟三元运算
            生成器表达式:  庞大数据量的时候 使用生成器表达式
            (i**2 for i in range(10))
            (i**2 for i in range(10) if i%2==0 )
            列表推导式:
            [i**2 for i in range(10)]
            [i**2 for i in range(10) if i%2==0]
            [(x,y,z) for x in range(10) if x%2==0 for y in range(10,20) if y%2==0 for z in range(20,30) if z%2==0] 
            字典推导式:
            {k:v for item in [('a':1,'b':2)]}
            字典推导式也可以通过创建元组序列,利用dict() 函数来完成.效率不高
            dict((k,v) for k,v in [('a',1),('b',2)] if v > 0)
            集合推导式:  自带去重功能
            {i**2 for i in range(10)}
            三元运算在推导式中的使用
            list1 = [1,-2,3,-1,2,3,-4,6]
            [i if i > else 0 for i in list1]    三元运算必须放在 for 循环的前面
            [i for i in list1 if i > 0]         如果只有if语句,if 必须放在 for 循环后面.
            '''

    def 递归函数():

        递归的定义 = '''
            在一个函数里调用这个函数本身,这种使用函数的方式就叫做递归.
            递归的最大深度:997
            修改递归最大深度
            import sys; sys.setrecursionlimit(100000)
            递归必须有一个明确的结束条件
            每进入更深层次的递归时,问题的规模应由所减小
            '''

        二分查找算法 = '''
            def search(seque,num,start=None,end=None):
                start=0 if start is None else start
                end=len(seque) if end is None else end
                index=(end-start)//2+start  #相除之后再加上开始的索引才是在原列表里的真实位置
                if start <= end:
                    if num < seque[index]:
                        return search(seque,num,start=start,end=index-1)  #这里的索引不是切片的所引,是比较的索引,没有用的切片.
                    elif num > seque[index]:
                        return search(seque,num,start=index+1,end=end)
                    elif num == seque[index]:
                        return index
                else:
                    return None
            l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
            search(l,43)
            '''

        斐波那契数列 = '''
            def fibo(num,tmp_list=[0,1]):
                if len(tmp_list) <= num:
                    tmp_list.append(tmp_list[-1] + tmp_list[-2])
                    return ff(num,tmp_list)
                else:
                    return tmp_list
            '''

        阶乘 = '''
            def fac(n):
                if n == 1:return 1
                return n*fac(n-1)
        '''

    def 匿名函数():

        定义 = '''
            功能简单的函数
            函数名 = lambda 参数 :返回值
            lambda表达式中的变量,不是定义的时候去绑定,而是运行的时候去绑定.
            lambda可以定义默认参数,如果要给lambd传入外部的变量,lambda x,y=n:x+y  这样就把n传进去了.
            '''

        匿名函数应用 = '''
            1、排序字符串列表
            lis=['13','2','63','44','15','96']
            sorted(lis,key=lambda i:int(i))

            2、使用迭代
            for f in [lambda x,y=n:x+y for n in range(5)]:
                print(f(0))

            3、将(('a','b'),('c','d')) 变成 [{'a':'c'},{'b':'d'}]
            list(map(lambda t:{t[0]:t[1]},zip(('a','b'),('c','d'))))

            4,过滤除偶数
            a=[1, 4, 6, 7, 9, 12, 17]
            b=filter(lambda x:x if x%2==0 else False,a)
            '''

    def 回调函数():

        回调函数的定义 = '''
            编程分为两类:
            系统编程,所谓系统编程,简单来说,就是编写库.
            应用编程,利用写好的各种库来编写具某种功用的程序,也就是应用.
            在这里我们把调用回调函数的函数,称为中间函数.把调用中间函数的函数称为起始函数.
            回调机制提供了非常大的灵活性.在回调中,用某种方式,把回调函数像参数一样传入中间函数.
            在传入一个回调函数之前,中间函数是不完整的.通过传入不同的回调函数,来决定、改变中间函数的行为.这就比简单的函数调用要灵活.
            回调函数可以携带额外的状态.
            中间函数和回调函数是回调的两个必要部分,给中间函数传入什么样的回调函数,是在起始函数里决定的.
            回调有两种:
            阻塞式回调和延迟式回调.两者的区别在于:阻塞式回调里,回调函数的调用一定发生在起始函数返回之前；
            而延迟式回调里,回调函数的调用有可能是在起始函数返回之后.待完善.
            '''

        回调函数的举例 = '''
            例1:
            def f1(x):
                return x*2**1

            def f2(x):
                return x*2**2

            def f3(x):
                return x*2**3

            #中间函数
            #接受一个函数作为参数
            def main(func,num):
                return 1+func(num)

            #起始函数
            def start():
                print(main(f1,3)) -----> 7
                print(main(f2,3)) -----> 13
                print(main(f3,3)) -----> 25
                print(main(lambda x:x*5,3))  -----> 16

            例2:
            def add(*args):
                return sum(args)

            def echo(msg):
                print(msg)

            def apply(func,*args,callback):
                ret=func(*args)
                callback(ret)

            apply(add,1,2,3,4,echo)

            使用闭包在回调函数里附加其他信息.
            def make():
                seq=0
                def handler(ret):
                    nonlocal seq
                    seq += 1
                    print('{} for {}'.format(seq,ret))
                return handler

            handler=make()
            apply(add,1,2,3,4,callback=handler) -----> 1 for 10
            apply(add,6,7,8,callback=handler) -----> 2 for 21
            apply(add,11,12,13,14,callback=handler) -----> 3 for 50
            因为闭包的特性,seq的值不会随函数的调用完毕而丢弃.
            '''

def 类与对象():

    def 面向对象():

        面向对象思想 = '''
            面向过程:面向过程的程序设计的核心是过程(流水线式思维),过程即解决问题的步骤.
            优点:极大地降低了写成学的复杂度,只需要顺着执行的步骤,堆叠代码即可
            缺点:一套流水线或者流程就是用来解决一个问题,如果修改代码就都得改变
        
            面向对象:面向对象的程序设计语言必须有描述对象及其相互之间关系的语言成分.
            这些程序设计语言可以归纳为以下几类:
                系统中一切事物皆为对象；
                对象是属性及其操作的封装体；
                对象可按其性质划分为类,对象成为类的实例；
                实例关系和继承关系是对象之间的静态关系；
                消息传递是对象之间动态联系的唯一形式,也是计算的唯一形式；方法是消息的序列.
            优点:解决了程序的扩展性.对某一个对象单独修改,会立刻反映到整个体系中,如对游戏中一个人物参数的特征和技能修改都很容易.
            缺点:可控性差,无法向面向过程的程序设计流水线式的可以很精准的预测问题的处理流程与结果,面向对象的程序一旦开始就由对象之间的交互解决问题,无法预测最终结果.
            类:
            具有相同或相似性质的对象的抽象就是类.因此,对象的抽象是类,类的具体化就是对象,也可以说类的实例是对象.
            类具有属性,它是对象的状态的抽象,用数据结构来描述类的属性.
            类具有操作,它是对象的行为的抽象,用操作名和实现该操作的方法来描述.
            实例化就是类到对象的过程.
            一组数据结构和处理它们的方法组成对象(object),
            把相同行为的对象归纳为类(class),
            通过类的封装(encapsulation)隐藏内部细节,
            通过继承(inheritance)实现类的特化(specialization)／泛化(generalization),
            通过多态polymorphism)实现基于对象类型的动态分派(dynamic dispatch).
            '''

        类与对象= '''
            类的两种作用:属性引用和实例化
            对象是关于类而实际存在的一个例子,即实例
            对象/实例只有一种作用:属性引用 
            
            class person:
                role='man'
                def __init__(self,name,age):
                    self.name = name
                    self.age = age
                def talk(self):
                    print('hehe')
            person.role     # 查看类属性
            person.talk     # 查看类方法,是内存地址
            
            obj=person('lisi',22)       # 实例化,等于在执行person.__init__()
            obj.name                    # 查看属性
            obj.talk()                  # 调用方法
            
            实例化:类名加括号就是实例化,会自动触发__init__函数的运行,可以用它来为每个实例定制自己的特征.
            self:在实例化时自动将对象/实例本身传给__init__的第一个参数.
            __init__中self实际是对象本身,__init__ 隐式的return 返回self,即对象本身.
            注意:def  __init__(self):   这句话可以写也可以不写,只要有参数参进来的时候就必须得写.
    　　     def  方法名(self):这里的self必须得写.
            '''

        类的属性 = '''
            查看定义的类的属性
            dir(类名):返回的是一个名字列表
            类名.__dict__:返回的是一个字典,key为属性名,value为属性值
            
            类有两种属性:静态属性和动态属性
            静态属性就是直接在类中定义的变量
            动态属性就是定义在类中的方法
            在类中,用变量表示静态属性,用函数表示动态属性,因而具有相同的属性和功能的,就是‘类’.
            
            特殊的类属性
            类名.__name__     # 类的名字(字符串)
            类名.__doc__      # 类的文档字符串
            类名.__base__     # 类的第一个父类
            类名.__bases__    # 类所有父类构成的元组
            类名.__dict__     # 类的字典属性
            类名.__module__   # 类定义所在的模块
            类名.__class__    # 实例对应的类(仅新式类中)
            '''

        面向对象的组合用法 = '''
            组合指的是,在一个类中以另外一个类的对象作为静态属性,称为类的组合
            class C1:
                def f1(self,args):
                    print(args)
                    args+=1
                    return args
                    
            class C2:
                def __init__(self):
                    self.func=C1()
                    
            obj1=C2()
            obj1.func.f1(1)
            
            # 计算圆的面积周长
            from math import pi
            class Circle:
                def __init__(self,r):
                    self.r=r
                def area(self):
                    return self.r**2*pi
                def perimeter(self):
                    return self.r*pi*2
            # 计算圆环的周长
            class Ring:
                def __init__(self,r1,r2):
                    self.r1=Circle(r1)  #组合 self的r1属性就是Circle(r1)的一个对象.
                    self.r2=Circle(r2)  
                def area(self):
                    return self.r2.area()-self.r1.area()
                def perimeter(self):
                    return self.r1.perimeter()+self.r2.perimeter()
            
            h1=Ring(4,10)
            h1.area()      -----> 263.89378290154264
            h1.perimeter() -----> 87.96459430051421
            '''

        类成员的修饰符 = '''
            公有成员,在任何地方都能访问
            私有成员,只有在类的内部才能方法
            私有成员和公有成员的定义不同:私有成员命名时,前两个字符是下划线.(特殊成员除外,例如:__init__、__call__、__dict__等)
            class C:
             
                def __init__(self):
                    self.name = '公有字段'
                    self.__foo = "私有字段"
            
            私有成员和公有成员的访问限制不同:
            静态字段
                公有静态字段:类可以访问；类内部可以访问；派生类中可以访问
                私有静态字段:只能在类内部可以访问；

            class C:
                name = "公有静态字段"
                __name = "私有静态字段"
                
                def func1(self):
                    print (C.name)
                def func2(self):
                    print(C.__name)
            
            class D(C):
                def show1(self):
                    print (C.name)
                def show2(self):
                    print(C.__name)
            
            C.name         # 类可以访问 公有静态字段
            C.__name       # 类不能访问 私有静态字段 -----> 错误
            c = C()
            c.func1()      # 类内部可以访问 公有静态字段
            c.func2()      # 类内部可以访问 私有静态字段
            
            d = D()
            d.show1()      # 子类中可以访问 公有静态字段
            d.show2()      # 子类中不能访问 私有静态字段
            
            公有字段和私有字段
            方法、属性的访问于上述方式相似,即:私有成员只能在类内部使用
            如果想要强制访问私有字段,可以通过 【对象._类名__私有字段明 】访问(如:obj._C__foo),不建议强制访问私有成员.
            *** 更多内容见:封装
            '''

        类与对象的命名空间 = '''
            创建一个类就会创建一个类的名称空间,用来存储类中定义的所有名字,这些名字称为类的属性.
            其中类的数据属性是共享给所有对象的
            而类的动态属性是绑定到所有对象的
            创建一个对象/实例就会创建一个对象/实例的名称空间,存放对象/实例的名字,称为对象/实例的属性
            在obj.name会先从obj自己的名称空间里找name,找不到则去类中找,类也找不到就找父类...最后都找不到就抛出异常
            '''

    def 面向对象三大特性():
        '''
        面向对象的三大特性是指:封装、继承和多态.
        Python 2.x中默认都是经典类,只有显式继承了object才是新式类.
        Python 3.x中默认都是新式类,不必显式的继承object
        新式类对象可以直接通过__class__属性获取自身类型
        新式类增加了__slots__内置属性, 可以把实例属性的种类锁定到__slots__规定的范围之中
        新式类增加了__getattribute__方法
        '''

        封装 = '''
            封装:隐藏对象的属性和实现细节,仅对外提供公共访问方式.
            
            好处:
                1. 将变化隔离； 
                2. 便于使用；
                3. 提高复用性； 
                4. 提高安全性；
            
            封装原则:
                1. 将不需要对外提供的内容都隐藏起来；
                2. 把属性都隐藏,提供公共方法对其访问.
            
            私有变量和私有方法
            在python中用双下划线开头的方式将属性隐藏起来(设置成私有的)
            
            私有变量
            其实这仅仅这是一种变形操作
            类中所有双下划线开头的名称如__x都会自动变形成:_类名__x的形式:
            
            class A:
                __N=0               #类的数据属性就应该是共享的,但是语法上是可以把类的数据属性设置成私有的如__N,会变形为_A__N
                def __init__(self):
                    self.__X=10     #变形为self._A__X
                def __foo(self):    #变形为_A__foo
                    print('from A')
                def bar(self):
                    self.__foo()    #只有在类内部才可以通过__foo的形式访问到.
            
            A._A__N是可以访问到的,即这种操作并不是严格意义上的限制外部访问,仅仅只是一种语法意义上的变形
            这种自动变形的特点:
            1.类中定义的__x只能在内部使用,如self.__x,引用的就是变形的结果.
            2.这种变形其实正是针对外部的变形,在外部是无法通过__x这个名字访问到的.
            3.在子类定义的__x不会覆盖在父类定义的__x.
              因为子类中变形成了:_子类名__x,而父类中变形成了:_父类名__x.
              即双下滑线开头的属性在继承给子类时,子类是无法覆盖的.
            
            这种变形需要注意的问题是:
            1.这种机制也并没有真正意义上限制我们从外部直接访问属性,知道了类名和属性名就可以拼出名字:_类名__属性,然后就可以访问了,如a._A__N
            2.变形的过程只在类的内部生效,自定义的赋值操作,不会变形
            3.在继承中,父类如果不想让子类覆盖自己的方法,可以将方法定义为私有的
            a=A()
            a.__dict__ -----> {'_A__X': 10}             # 自动变形
            a.__y=2                                     # 自定义的赋值操作
            a.__dict__ -----> {'_A__X': 10, '__y': 2}   # 没有变形
            
            把fa定义成私有的,即__fa
            class A:
                def __fa(self):                         # 在定义时就变形为_A__fa
                    print('from A')
                def test(self):
                    self.__fa()                         # 只会与自己所在的类为准,即调用_A__fa,实际调用的是 self._A__fa()
            
            class B(A):
                def __fa(self):                         # 实际调用的是 self._B__fa()
                    print('from B')
            b=B()
            b.test() -----> from A    # test调用的是 self._A__fa()
            
            class foo:
                def __init__(self,name,age):
                    self.name=name
                    self.age=age
            self 是一个形式参数.
            当执行 obj1 = Foo('lisi', 18 ) 时,self 等于 obj1.
            当执行 obj2 = Foo('nana', 78 ) 时,self 等于 obj2.
            所以,内容其实被封装到了对象 obj1 和 obj2 中,每个对象中都有 name 和 age 属性.
            
            调用被封装的内容时,有两种情况:
            通过self间接调用被封装的内容
            通过 对象.属性名 的方式直接调用被封装的内容,对象的属性和方法.
            obj1 = Foo('lisi', 18 )
            obj1.name -----> 'lisi'     # 直接调用obj1对象的name属性
            obj1.age  -----> 18         # 直接调用obj1对象的age属性

            class foo:
                def __init__(self,name,age):
                    self.name=name
                    self.age=age
                def echo(self):
                    print(self.name)
                    print(self.age)
                    
            obj2 = Foo('nana', 78 )
            obj2.echo()     
            Python默认会将obj2传给self参数,即:obj1.echo(obj2),
            此时方法内部的 self ＝ obj2,即:self.name 是 nana；self.age 是 78
            面向对象的封装,其实就是使用构造方法将内容封装到 对象 中,然后通过对象直接或者self间接获取被封装的内容.
                        
            任何以但下划线_开头的方法名字只属于内部实现.
            python本身并不会阻止他人访问内部名称.
            以双下划线开头的方法会导致实现名称重整.类的私有属性会被重命名为 _B__private 和 _B__method.意义在于属性不会因为继承而被覆盖.
            封装类属性的私有属性(类属性前面加__)
            class A:
                __num=10
                def __init__(self):
                    self.__num+=1
                    
            a=A()
            print(a.__dict__) -----> {'_A__num': 11}
            a._A__num           # 通过 对象._类名__属性名调用
            A._A__num           # 通过 类名._类名__属性名调用
            
            class B:
                def __init__(self):
                    self.__private=0
                def __method(self):
                    pass
                def pub(self):
                    self.__method(self)
                    pass
            
            class C(B):
                def __init__(self):
                    super().__init__()
                    self.__private=1
                def __method(self):
                    pass
            d=C()
            d._B__private -----> 0
            d._C__private -----> 1
            
            非公有名称使用但下划线开头.隐藏属性以双像下划线开头.
            
            *** property的方法详见 类的特殊方法
            '''

        继承 = '''
            1.继承是一种创建新类的方式
            2.新建的类可以继承一个或多个父类,父类有称为基类或者超类
            3.新建的类称为派生类或者子类
            在python中类的继承分为:单继承或多继承
            Python的类可以继承多个类
            Python的类如果继承了多个类,那么其寻找方法的方式有两种,分别是:深度优先和广度优先
            当类是经典类时,多继承情况下,会按照深度优先方式查找
            当类是新式类时,多继承情况下,会按照广度优先方式查找
            经典类和新式类,从写法上区分的话,如果 当前类或者父类继承了object类,那么该类便是新式类,否则便是经典类.
            
            class A:
                def __init__(self):
                    pass
                def echo(self):
                    print("This is from A")
            
            class B(A):
                def __init__(self):
                    pass
                    
            class C(A):
                def __init__(self):
                    pass
                def echo(self):
                    print("This is from C")
                    
            class D(B,C):
                def __init__(self):
                    pass
            
            obj=D()
            obj.echo()
            
            如果在经典类中,obj.echo() 显示 This is from A. 深度优先,查找顺序是 D -> B -> A
            如果在新式类中,obj.echo() 显示 This is from C. 广度优先,查找顺序是 D -> B -> C
            在查找echo方法的过程中,一旦找到,则寻找过程立即中断,便不会再继续找.
            
            查看继承(还是上面的例子)
            C.__bases__ -----> (__main__.A,)            # __bases__则是查看所有继承的父类,返回的是一个元组,即使只有一个父类.
            D.__bases__ -----> (__main__.B, __main__.C)
            D.__base__  -----> __main__.B               # __base__只查看从左到右继承的第一个父类,返回的是一个 类.
            
            如果没有指定基类,python的类会默认继承object类,object是所有python类的基类,它提供了一些常见方法(如__str__)的实现.
            A.__bases__ -----> (object,)
            
            派生:
        　　在父类的基础上产生子类,产生的子类就叫做派生类
        　　在子类中含有的父类中没有的方法,这样的方法就叫做派生方法.
        　　父类里有,子类也有的方法,就叫做方法的重写
            
            *** 关于super 子类可以使用父类的所有属性和方法,详见类的特殊方法.
            '''

        多态 = '''
            pass
            '''

    def 关于类的内置函数():

        def 内置函数super():

            super详解 = '''
            返回一个代理对象,委托调用父类或兄弟类的方法.用于访问在继承中被覆盖的继承方法.getattr()搜索顺序与使用的顺序相同 .
            该类__mro__属性列出了两者和使用的方法解析搜索顺序.该属性是动态的,只要继承层次更新就可以更改.getattr()super()
            如果省略第二个参数,则返回的超类是未绑定的.如果第二个参数是一个对象,则isinstance(obj, type) 必须为真.如果第二个参数是一个类型,则 issubclass(type2, type)必须为true(这对于类方法很有用).
            典型的超类调用如下所示:
            class C(B):
                def method(self, arg):
                    super().method(arg)     # super(C, self).method(arg)

            super() 函数是用于调用超类的方法.
            如果是单继承可是使用类名来调用父类的方法.
            super 是用来解决多重继承问题的,如果使用多继承,会涉及到查找顺序(MRO)、重复调用(钻石继承)等种种问题.
            MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表.通过 类名.mro() 或 类名.__mro__  来查看MRO列表.

            super 不一定指向父类, 他指向的是 mro 中的下一个类.
            在 mro 中, 父类一定出现在子类后面, 若有多个父类, 其相对順序保持不变
            super 对象不是其父类, 他的作用只是代理委托

            super 的原理,可以用下面的代码理解:

            def super(cls, obj):
                mro = obj.__class__.mro()
                return mro[mro.index(cls) + 1]

            super 会去找第二个参数(可以是类,也可以是对象) 的mro.
            返回 在mro 中第一个参数 cls 的下一個类.

            举例:
            class person:
                def __init__(self, name):
                    self.name = name

                @property
                def name(self):
                    return self._name

                @name.setter
                def name(self, value):
                    if not isinstance(value, str):
                        raise TypeError('Expected a string')
                    self._name = value

                @name.deleter
                def name(self):
                    raise AttributeError("Can't delete attribute")

            class subson(person):
                @property
                def name(self):
                    print('getting name')
                    return super().name

                @name.setter
                def name(self, value):
                    print('setting name to', value)
                    super(subson, subson).name.__set__(self, value)  # ??? 为什么要用 __set__  为什么不能用 super(subson,self)

                @name.deleter
                def name(self):
                    print('delete name')
                    super(subson, subson).name.__delete__(self)


            s=subson('lisi') -----> setting name to lisi
            s.__class__.mro()  -----> [<class '__main__.subson'>, <class '__main__.person'>, <class 'object'>]    # 对象s 的 类的mro
            super(subson, s) 指的是 person类                                # s的类是subson, 在subson的mro中,subson的下一個是person类
            super(subson, subson) 指的是 person                             # 在subson类的mro中 subson的下一个类是person类
            super(subson, person) 指的是 object                             # 在person类的mro中并没有subson,  super(type, obj): obj必须是一个实例对象,或者是type的子类.

            super 可以在类的外部使用,super 是一個內置函數, 不限制在 class 內部使用.
            在类的外部使用时, 不允许省略参数, 不然不知道是找谁的 mro, 也不知道找谁的下一个
            在类的內部使用时, 允许省略参数, 默认是super(类自己,self) 找的是自己的 mro, 找自己的下一个
            super 不一定指向父类, 他指向的是 mro 中的下一個类.多重继承情况下,mro的下一个类可能是父类,也可能是兄弟类.
            通常用 super 找单继承下的直接父类, 所以在类內部, 可以完全省略參数來调用 super()
            实际上 並不能通过 super得到他指向的那个类, 只能通过 super 对象的代理去委托指向的那个类 使用其方法.

            super在不同参数下可以代表unbound、bound到类型,Python3省略所有参数时候相当于super(class,self),是bound到对象.而super(class, class)自然是绑定到了父类.
            实际上代码中super(subson, subson)是一种完全错误的写法,它应该被写成super(subson, type(self)),如果存在多继承的话,后一种写法才能正确代理到多继承的其他类上面去,实现菱形继承.只是在单继承的时候这种写法也正好可以用而已.

            假如 A是一个类,而a是A的对象.
            我们通过实例去调用类的方法实际上是这样做的:
            A.__dict__['func'].__get__(a, A)=a.func -----> True  <bound method A.func of <__main__.A object at 0x0000025EB63AEC88>>
            A.__dict__['func'].__get__(A, A)=A.func -----> True   <function __main__.A.func>
            super(A,A).__init__是一个unbound,super(A,a).__init__是一个bound,
            bound和unbound的区别,就是__get__操作的第一个参数是不是传入了一个实例对象.

            关于绑定,类中的方法有staticmethod(无绑定)、method(绑定到对象)和classmethod(绑定到类)三种,第三种就是提供绑定到class的,它返回的类似于一个class对象.

            接下来需要理解的是property的原理,property是在类的__dict__当中创建了一个描述对象,这个对象可以通过Person.name来获得.
            对于@property创建的对象来说,property自己是个类,也是这个描述对象的类型,所以调用Person.name.__set__就相当于通过描述机制设置属性.
            之所以要这么做是因为super()的代理并不是万能的,它差不多是个只读的代理,而不能写入,所以必须手工去调用__set__.

            class Base:
                def __init__(self):
                    pass
                def func(self):
                    pass
            a=Base()

            '''

            子类可以使用父类的所有属性和方法 = '''
                super的官方文档
                super() -> 相当于super(__class__,<first argument>)
                            __class__就是对象的类,<first argument> 一般指定self.
                super(type,type2) 要求 type2 是type1的子类.
                子类可以使用父类的所有属性和方法
                如果子类有自己的方法,就执行自己的；如果子类没有自己的方法,就会找父类的.和命名空间一样.
                如果子类里面没有找到,父类里也没有找到,就会报错
                如果子类中实现了调用父类的方法
                在类内:super(子类,self).方法名()  supper().__init__(参数)
                super里第一个参数是一个子类.第二个参数
                在类外:super(子类名,对象名).方法名()
                实例:
                class A:
                    def __init__(self,name,age):
                        self.name=name
                        self.age=age
                    def add(self):
                        self.age+=1
                    def clear(self):
                        self.age=-1

                class B(A):
                    def __init__(self,name,age,money):
                        super().__init__(name,age)      # 调用父类的构造方法
                        self.money=money
                    def sub(self):
                        self.age-=1
                    def clear(self):
                        self.age=0

                b=B('lisi',22,100)
                b.age   -----> 22       # 继承了父类的属性
                b.add()                 # 使用父类的add方法
                b.age   -----> 23       
                b.sub()                 # 使用派生的sub方法
                b.age   -----> 22
                b.clear()               # 使用重写的clear方法
                b.age   -----> 0
                super(B,b).clear()      # 强至使用父类的clear方法
                b.age   -----> -1
                在继承中,如果子类有的方法就执行子类的,如果子类没有的方法就执行父类的.
                '''

            在子类中调用父类的某个已经被覆盖的方法 = ''' 
                class proxy:
                    def __init__(self,obj):
                        self._obj = obj
                    def __getattr__(self,name):
                        return getattr(self._obj,name)
                    def __setattr__(self,name,value):
                        if name.startswith('_'):
                            super().__setattr__name(name,value)
                        else:
                            setattr(self._obj,name,value)

                在上面代码中,__setattr__() 的实现包含一个名字检查.
                如果某个属性名以下划线(_)开头,就通过 super() 调用原始的 __setattr__() ,
                否则的话就委派给内部的代理对象 self._obj 去处理.
                python3中的类默认是新式类,隐式的继承了object,所以即使没有显示指名父类 super() 仍然可以使用.

                class Base:
                    def __init__(self):
                        print('Base.__init__')

                class A(Base):
                    def __init__(self):
                        super().__init__()
                        print('A.__init__')

                class B(Base):
                    def __init__(self):
                        super().__init__()
                        print('B.__init__')

                class C(A,B):
                    def __init__(self):
                        super().__init__()  # Only one call to super() here
                        print('C.__init__')

                c = C() ----->  Base.__init__
                                B.__init__
                                A.__init__
                                C.__init__

                Python是如何实现继承的.每一个定义的类,Python会计算出一个方法解析顺序(MRO)列表.
                MRO列表就是一个简单的所有基类的线性顺序表.super的继承属性并不是只继承父类,而是按照MRO列表来继承的.
                也就是说 可以继承并调用没有直接父类的类的方法(见:调用没有直接父类的类的方法).
                在上面的例子里,C 继承了A,B, A,B都继承了Base,当C里执行super时,去找A,A执行super 按照 MRO列表去找B,B执行super,去Base里找.
                例如:
                C.__mro__ -----> (__main__.C, __main__.A, __main__.B, __main__.Base, object)   # 通过 __mro__ 获取 Mro 列表.
                Python3只存在新式类,采用的MRO是C3算法.
                为了实现继承,Python会在MRO列表上从左到右开始查找基类,直到找到第一个匹配这个属性的类为止.
                MRO列表的构造是通过一个C3线性化算法来实现的.它实际上就是合并所有父类的MRO列表并遵循如下三条准则:
                子类会先于父类被检查
                多个父类会根据它们在列表中的顺序被检查
                如果对下一个类存在两个合法的选择,选择第一个父类
                类的继承是按照MRO列表中的类顺序来进行的.

                使用 super() 函数时,Python会在MRO列表上继续搜索下一个类.
                只要每个重定义的方法使用 super() 调用其父类的该方法,python就会遍历整个MRO列表,每个方法也只会被调用一次.
                这也是为什么不会调用两次 Base.__init__() 的原因.
                理解Python中MRO算法 详见 http://python.jobbole.com/85685/
                MRO列表               # ???
                '''

            调用没有直接父类的类的方法 = '''
                super() 并不一定去查找某个类在MRO中下一个直接父类,即使没有直接父类的类也可以调用.

                class A:
                    def spam(self):
                        print('A.spam')
                        super().spam()

                class B:
                    def spam(self):
                        print('B.spam')

                class C(A,B):
                    pass

                c=C()
                c.spam() -----> A.spam
                                B.spam

                C.__mro__ -----> (__main__.C, __main__.A, __main__.B, object)
                类A中使用 super().spam() 实际上调用的是跟类A毫无关系的类B中的 spam() 方法.查找顺序按照C的MRO列表.

                使用 super() 时,注意在继承体系中所有相同名字的方法要拥有可兼容的参数(比如相同的参数个数和参数名称).这样可以确保 super() 调用一个非直接父类方法时不会出错.
                最好确保最顶层的类提供了这个方法,在MRO上查找时,肯定可以找到你想要的方法.
                '''

        def 内置函数isinstance():
            '''isinstance(obj,cls)检查是否obj是否是类 cls 的对象'''

            例 = '''
                class A:
                    pass
                
                a = A()
                isinstance(a,A) -----> True
                '''

        def 内置函数issublclass():
            '''issubclass(sub, super)检查sub类是否是 super 类的子类 '''

            例 = '''
                class A:
                    pass

                class B(A):
                    pass
                
                issubclass(B,A) -----> True
                '''

        反射 = '''
            通过字符串的形式操作对象相关的属性.python中的一切事物都是对象(都可以使用反射),四个可以实现自省的函数.
            '''

        def 内置函数hasattr():
            '''
            返回对象是否具有给定名称的属性.
            hasattr(obj,属性名)
            '''
            例 = '''
                class A:
                    __a='b'
                    def __init__(self,name,age):
                        self.name,self.age = name,age
                    def func(self):
                        pass
                a =A('lisi',22)
                同时类也是一个对象
                hasattr(a,'name') -----> True
                hasattr(A,'func') -----> True
                hasattr(A,'__a') -----> False
                hasattr(A,'_A__a') -----> True
                hasattr(a,'_A__a') -----> True
                '''

        def 内置函数getattr():
            '''
            getattr(object, name[, default])
            从对象获取一个命名属性; getattr(a,'name')等同于a.name
            可以给定一个默认值,当对象没有指定的属性时,返回默认值,如在没有指定默认值的情况下,对象没有指定的属性,会触发 AttributeError.
            '''

            例 = '''
                getattr(a,'name') -----> 'lisi'
                getattr(a,'func') -----> <bound method A.func of <__main__.A object at 0x0000025EB656BF98>>
                getattr(A,'func') -----> <function __main__.A.func>
                getattr(a,'func')()     # 可以之间执行
                
                导入其他模块,利用反射查找该模块是否存在某个方法
                import 其他模块 as obj
                hasattr(obj,'属性或方法')
                getattr(obj,'属性或方法')()
                '''

        def 内置函数setattr():
            '''
            将给定对象上的指定的属性设置为指定的值.
            setattr(a,'name','nana') 相当于 a.name='nana'
            setattr(a,'job','it')   即使属性不存在也可以设置
            '''

        def 内置函数delattr():
            '''
            从给定的对象中删除指定的属性.
            delattr(a,'job')相当于 del a.job,对象没有指定的属性,会触发 AttributeError.
            '''

    def 类的装饰器():

        def property方法():
            '''
            属性的定义和调用:
            定义时,在普通方法的基础上添加 @property 装饰器；
            定义时,属性仅有一个self参数
            调用时,无需括号
            属性存在意义是:访问属性时可以制造出和访问字段完全相同的假象
            属性由方法变种而来,如果Python中没有属性,方法完全可以代替其功能.
            一个静态属性property本质就是实现了get,set,delete三种方法

            属性的定义有两种方式:分别是【装饰器】和【静态字段】
            装饰器 即:在方法上应用装饰器
            静态字段 即:在类中定义值为property对象的静态字段
            装饰器方式,新式类中的属性有三种访问方式,并分别对应了三个被@property、@方法名.setter、@方法名.deleter修饰的方法,三个方法定义为对同一个属性:获取、修改、删除
            静态字段方式,创建值为property对象的静态字段
            first_name = property(get_first_name, set_first_name, del_first_name,'description')
            属性名      = property(get方法,set方法,del方法,'描述')
            '''

            创建可管理的属性 = '''
                创建可管理的属性
                下述代码中有三个相关联的方法,这三个方法的名字都必须一样.
                第一个方法是一个 getter 函数,它使得 first_name 成为一个属性.
                其他两个方法给 first_name 属性添加了 setter 和 deleter 函数.
                只有在 first_name 属性被创建后,后面的两个装饰器 @first_name.setter 和 @first_name.deleter 才能被定义.
                property的一个关键特征是它看上去跟普通的attribute没有区别,但是访问它的时候会自动触发 getter 、setter 和 deleter 方法.

                class person:
                    def __init__(self,first_name):
                        self.first_name=first_name      # 实际就是执行 @first_name.setter

                    #getter function
                    @property
                    def first_name(self):
                        return self.fn

                    #setter function
                    @first_name.setter
                    def first_name(self,value):
                        if not isinstance(value,str):
                            raise TypeError('Expected a string')
                        self.fn = value

                    #deleter function
                    @first_name.deleter
                    def first_name(self):
                        raise AttributeError("Can't delete attrbute")

                在getter和setter方法中,对 _fn 属性的操作,这是实际数据保存的地方._fn 可以换成其他名字.
                 __init__() 方法中 self.first_name 而不是 self._first_name .
                本例创建一个property的目的就是在设置attribute的时候进行检查.
                要求在初始化的时候也进行这种类型检查.通过设置 self.first_name ,自动调用 setter 方法,这个方法里面会进行参数的检查.
                当创建实例的时候调用类的构造方法,__init__()  self.first_name=first_name 实际调用的是 first_name.setter方法,
                构造方法 __init__(self,first_name) 括号中的first_name 就是 first_name.setter方法中 value的实参.
                当使方式的使用调用的是 first_name.getter方法.返回self.fn.

                a=person('lisi')        # 调用first_name.setter
                a.first_name            # 调用first_name.getter
                del a.first_name        # 调用first_name.deleter
                '''

            在已存在的get和set方法基础上定义property = '''
                还能在已存在的get和set方法基础上定义property.
                例如:
                class person:
                    def __init__(self,first_name):
                        self.first_name=first_name

                    #getter function
                    def get_first_name(self):
                        return self._first_name

                    #setter function
                    def set_first_name(self, value):
                        if not isinstance(value, str):
                            raise TypeError('Expected a string')
                        self._first_name = value

                    #deleter function
                    def del_first_name(self):
                        raise AttributeError("Can't delete attribute")

                    #从现有的get / set方法中创建一个属性
                    first_name = property(get_first_name,set_first_name,del_first_name)

                property属性其实就是一系列相关绑定方法的集合.
                如果你去查看拥有property的类,就会发现property本身的fget、fset和fdel属性就是类里面的普通方法.
                在使用frist_name = property(get_first_name,set_first_name,del_first_name) 创建property属性时.
                括号里面的顺序不能变,分别对应的是 (fget,fset,fdel) 属性.通过指定property属性名字来调用.
                比如:
                person.first_name.fget -----> <function __main__.person.get_first_name>
                person.first_name.fset -----> <function __main__.person.set_first_name>
                person.first_name.fdel -----> <function __main__.person.del_first_name>
                调用方法
                a=person('lili')
                a.first_name           -----> 'lili'    # 相当于执行 a.get_first_name 
                a.first_name='nana'                     # 相当于执行 a.set_first_name('nana')
                del a.first_name                        # 相当于执行 a.del_first_name

                property还是一种定义动态计算attribute的方法.这种类型的attributes并不会被实际的存储,而是在需要的时候计算出来.
                比如:
                import math
                class Circle:
                    def __init__(self, radius):
                        self.radius = radius

                    @property
                    def area(self):
                        return math.pi * self.radius ** 2

                    @property
                    def diameter(self):
                        return self.radius ** 2

                    @property
                    def perimeter(self):
                        return 2 * math.pi * self.radius

                c = Circle(4.0)
                c.radius        -----> 4.0
                c.area          -----> 50.26548245743669
                c.perimeter     -----> 25.132741228718345
                通过使用property,将所有的访问接口形式统一起来,
                对半径、直径、周长和面积的访问都是通过属性访问,就跟访问简单的attribute是一样的.
                如果不这样做的话,那么就要在代码中混合使用简单属性访问和方法调用.
                '''

            在子类扩展父类property = '''
                在子类中,扩展定义在父类中的property的功能.
                class person:
                    def __init__(self,name):
                        self.name=name

                    # getter function
                    @property
                    def name(self):
                        return self._name

                    # setter function
                    @name.setter
                    def name(self,value):
                        if not isinstance(value,str):
                            raise TypeError('Expected a string')
                        self._name=value

                    # deleter function
                    @name.deleter
                    def name(self):
                        raise AttributeError("Can't delete attribute")

                class subson(person):
                    @property
                    def name(self):
                        print('getting name')
                        return super().name

                    @name.setter
                    def name(self,value):
                        print('setting name to',value)
                        super(subson,subson).name.__set__(self,value)       # ??? 为什么要用 __set__  为什么不能用     super(subson,self)

                    @name.deleter
                    def name(self):
                        print('delete name')
                        super(subson,subson).name.__delete__(self)

                s=subson('lisi') -----> 打印 setting name to lisi
                s.name           -----> 打印 getting name ,返回 lisi.
                s.name='nana'    -----> 打印 setting name to nana
                例子中,所有的property方法都被重新定义.在每一个方法中,使用了 super() 来调用父类的实现.
                在 setter 函数中使用 super(subson, subson).name.__set__(self, value) 的语句是为了委托给之前定义的setter方法,需要将控制权传递给之前定义的name属性的 __set__() 方法.
                获取这个方法的只能使用类变量而不是实例变量.这也是要使用 super(subson, subson) 的原因.

                只扩展property的一个方法.
                class subson(person):
                    @person.name.getter
                    def name(self):
                        print('getting name')
                        return super().name

                class subson(person):
                    @person.name.setter
                    def name(self,value):
                        print('setting name')
                        super(SubPerson, SubPerson).name.__set__(self, value)
                property其实是 getter、setter 和 deleter 方法的集合,而不是单个方法.扩展一个property时,先确定是否要重新定义所有的方法还是只修改其中某一个方法.
                只重定义其中一个方法,如果只使用 @property .比如,下面的代码就会出错:
                class subson(person):
                    @property
                    def name(self):
                        print('error')
                        return super().name
                如果不知道到底是哪个基类定义了property,那只能通过重新定义所有property并使用 super() 来将控制权传递给前面的实现.
            '''

            以描述器类的形式来定义的功能 = '''
                创建一个新的拥有一些额外功能的实例属性类型,比如类型检查.
                通过一个描述器类的形式来定义它的功能.下面是一个例子:
                class integer:
                    def __int__(self,name):
                        self.name=name
                    def __get__(self,instance,cls):
                        if instance is none:
                            return self
                        else:
                            return instance.__dict__[self.name]
                    def __set__(self,instance,value):
                        if not isinstance(value,int):
                            raise TypeError('Expected an int')
                        instance.__dict__[self.name] = value
                    def __delete__(self,instance):
                        del instance.__dict__[self.name]

                描述器就是一个实现了三个核心的属性访问操作(get, set, delete)的类,分别为 __get__() 、__set__() 和 __delete__() 这三个特殊的方法.
                这些方法接受一个实例作为输入,之后相应的操作实例底层的字典.
                使用一个描述器,需将这个描述器的实例作为类属性放到一个类的定义中.

                class Point:
                    x = Integer('x')
                    y = Integer('y')        # ??? 不懂原理

                    def __init__(self, x, y):
                        self.x = x
                        self.y = y

                所有对描述器属性(比如x或y)的访问会被__get__() 、__set__() 和 __delete__() 方法捕获到.
                p = Point(2, 3)
                p.x -----> 2        # 调用 Point.x.__get__(p,Point)
                p.y = 5             # 调用 Point.y.__set__(p, 5)
                p.x = 2.3           # 调用 Point.x.__set__(p, 2.3)
                作为输入,描述器的每一个方法会接受一个操作实例.
                为了实现请求操作,会相应的操作实例底层的字典(__dict__属性).描述器的 self.name 属性存储了在实例字典中被实际使用到的key.

                描述器可实现大部分Python类特性中的底层魔法,包括 @classmethod 、@staticmethod 、@property ,甚至是 __slots__ 特性.
                通过定义一个描述器,可以在底层捕获核心的实例操作(get, set, delete),并且自定义它们的行为.
                可以实现很多高级功能,并且它也是很多高级库和框架中的重要工具之一.
                描述器只能在类级别被定义,定义为类的属性,而不能为每个实例单独定义.

                # 错误示例
                class Point:
                    def __init__(self, x, y):
                        self.x = Integer('x') # No! Must be a class variable
                        self.y = Integer('y')
                        self.x = x
                        self.y = y

                __get__() 有点复杂的原因是实例变量和类变量的不同.如果一个描述器被当做一个类变量来访问,那么 instance 参数被设置成 None .
                这种情况下,标准做法就是简单的返回这个描述器本身即可(尽管你还可以添加其他的自定义操作).例如:

                class Integer:
                    def __get__(self, instance, cls):
                        if instance is None:
                            return self
                        else:
                            return instance.__dict__[self.name]

                p.x -----> 2        # 调用 Point.x.__get__(p,Point)
                Point.x -----> <__main__.Integer object at 0x100671890>    # 调用 Point.x.__get__(None, Point)

                描述器通常是那些使用到装饰器或元类的大型框架中的一个组件.
                同时它们的使用也被隐藏在后面.举个例子,下面是一些更高级的基于描述器的代码,并涉及到一个类装饰器:

                # Descriptor for a type-checked attribute
                class Typed:
                    def __init__(self, name, expected_type):
                        self.name = name
                        self.expected_type = expected_type
                    def __get__(self, instance, cls):
                        if instance is None:
                            return self
                        else:
                            return instance.__dict__[self.name]

                    def __set__(self, instance, value):
                        if not isinstance(value, self.expected_type):
                            raise TypeError('Expected ' + str(self.expected_type))
                        instance.__dict__[self.name] = value
                    def __delete__(self, instance):
                        del instance.__dict__[self.name]

                # Class decorator that applies it to selected attributes
                def typeassert(**kwargs):
                    def decorate(cls):
                        for name, expected_type in kwargs.items():
                            # Attach a Typed descriptor to the class
                            setattr(cls, name, Typed(name, expected_type))
                        return cls
                    return decorate

                # Example use
                @typeassert(name=str, shares=int, price=float)
                class Stock:
                    def __init__(self, name, shares, price):
                        self.name = name
                        self.shares = shares
                        self.price = price
                如果只是想简单的自定义某个类的单个属性访问的话就不用去写描述器了.这种情况下使用property会更加容易.
                当程序中有很多重复代码的时候描述器就很有用了(比如你想在你代码的很多地方使用描述器提供的功能或者将它作为一个函数库特性).
                '''

        def classmethod方法():
            '''classmethod是用来指定一个类的方法为类方法.被@classmethod装饰的函数的第一个参数必须是cls.
            当这个方法被调用时,传递类作为第一个参数,而不是那个类的实例.可以在该方法内使用该类及其属性.
            被@classmethod装饰的函数可以在没有实例化类的情况下被子类调用,通过继承,可以被子类重写.'''

            应用 = '''
                class Mydate:
                    def __init__(self,year=0,month=0,day=0):
                        self.year,self.month,self.day = year,month,day
                    def echo(self):
                        print(self.year,self.month,self.day)
                    @classmethod
                    def check(cls,tstr):
                        # 这里第一个参数是cls, 表示调用当前的类名
                        year,month,day =tstr.split('-')
                        # 返回的是一个初始化后的类
                        return cls(year,month,day)

                t=Mydate.check('2018-05-18')
                t.echo() -----> 2018 05 18
                '''

        def staticmethod方法():
            '''staticmethod函数不过是一个类中定义的函数.它不需要首先实例化类就可以调用.它的定义通过继承是不可变的.该方法不依赖于对象本身的状态;'''

            应用 = '''
                class B:
                    @staticmethod
                    def echo(s):
                        print(s)
                b = B()
                b.echo('lisi')
                B.echo('lisi')
                '''

        def overload方法():
            '''pass'''

    def 元类():

        元类 = '''
            详见 
            http://blog.jobbole.com/21351/
            http://python.jobbole.com/86566/
            python当中一切都是对象,而对象都是由类创建,类也是对象.
            元类就是用来创建类的类.
            继承type的类,称为元类(metaclass).类是由元类实例化创建来的(就是__metaclass__指定的类).
            元类和类 的关系类似于 实例和类 的关系.

            class A:
                pass
            类同样也是一种对象.
            这个对象(类)自身拥有创建对象(类实例)的能力,而这就是为什么它是一个类的原因.
            它的本质仍然是一个对象,于是可以对它做如下的操作:
            1)   可以将它赋值给一个变量
            2)   可以拷贝它
            3)   可以为它增加属性
            4)   可以将它作为函数参数进行传递
            type能动态的创建类. type可以接受一个类的描述作为参数,然后返回一个类.
            type(类名, 父类的元组(可以为空),包含属性的字典(名称和值))
            创建类就可以有两种方式
            普通方式:
            class A:
                def func1(self):
                    pass

            特殊方式(type类的构造函数):
            type 接受一个字典来为类定义属性.
            def func2(self):
                print('this is type')
            A = type('A',(), {'func': func2})    # 这里'func' 才是真正在A 中方法的名字.
            B = type('B',(A,),{})
            type第一个参数:类名
            type第二个参数:当前类的需要继承的类
            type第三个参数:类的成员
            b=B()
            b.func() -----> this is type
            
            __metaclass__属性
            你可以在写一个类的时候为其添加__metaclass__属性.
            class Foo(metaclass=something):
                __metaclass__ = something     # 这是python2 中的写法，在python3 中已经失效.
            Python会用元类来创建类Foo. 当执行到 class Foo: 时,类对象Foo还没有在内存中创建.
            Python会在类的定义中寻找 metaclass 属性,如果找到了,Python就会用它来创建类Foo.
            如果没有找到,就会用内建的type来创建这个类.
            
            class Foo(Bar):
                pass
            Python做了如下的操作:
            Foo中如果有 metaclass 这个属性,Python会在内存中通过 metaclass 创建一个名字为Foo的类对象(是类对象).
            如果Python没有找到 metaclas ,它会继续在Bar(父类)中寻找 metaclass 属性,并尝试做和前面同样的操作.
            如果Python在任何父类中都找不到 metaclas ,它就会在模块层次中去寻找 metaclass ,并尝试做同样的操作.
            如果还是找不到 metaclass ,Python就会用内置的type来创建这个类对象.
            metaclass 中放置可以创建一个类的东西.那就是type,或者任何使用到type或者子类化type的元类.
            
            自定义元类
            元类的主要目的就是为了当创建类时能够自动地改变类.
            通常,用在设计API时.
            metaclass 的主要任务是:拦截类,修改类,返回类
            自定义一个元类,让该元类产生的类对象的所有的属性都是大写形式.
            class UpperAttrMetaclass(type):
                def __new__(cls, name, bases, dct):
                    attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
                    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
                    return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)
            class A(metaclass=UpperAttrMetaclass):      # 在python3 中如果一个要指名他的元类使用 metaclass=UpperAttrMetaclass 与python2 不同.还需注意的是 父类要写在他的前面.
                b='hehe'
                
            hasattr(A,'B') -----> True
            元类的主要用途是创建API.一个典型的例子是Django ORM.
            class Person(models.Model):
                name = models.CharField(max_length=30)
                age = models.IntegerField()
            例:
            class SimpleMetaClass(type):
                def __init__(self,*args,**kwargs):
                    print("you have create a class instance by metaclass")
                    super(SimpleMetaClass,self).__init__(*args,**kwargs)
            class Eartch(metaclass=SimpleMetaClass):
                pass
            -----> you have create a class instance by metaclass
            只需这样写,无需运行.实际并没有使用过 Earth类,也没有使用过SimpleMetaClass这个元类.
            但实际的结果看来,SimpleMetaClass这个元类确实被使用过了,因为打印出了想要的结果.
            是因为python使用SimpleMetaClass元类来创建出了Earth这个类对象(不是Earth的一个实例).
            这个过程可以用一句话来描述:这个步骤相当于实例化了一个metaclass(SimpleMetaClass)对象,而这个对象正好是Earth类.
            如果你不写 metaclass=SimpleMetaClass,最终这个类的元类就是type. SimpleMetaClass是继承自type的.
            
            Earth类已经被metaclass所创建出来了,那么当实例化一个Earth类(也就是创建一个earth对象)的时候又发生了什么呢？
            有__call__,__new__这两个特殊方法,就能实现一个类的实例.对于一个实现了__call__的类,那么它的实例可以当做函数来调用.例子见 __call__ 的解释.
            __new__有拦截类实例化的功能,在创建一个对象的过程中,执行__init__方法时,解释器已经为对象分配了内存,实例已经存在了.
            __init__方法只是改变这个类当中的某些参数.而在执行__new__方法时,这个实例是不存在的,而__new__就是要创建这个实例,所以__new__必须要有返回值.

            为什么创建一个类的实例是这种写法:
            instance = SomeClass()
            instance = SomeClass(args1,args2,...)
            类是元类的一个对象,而元类的实例都有一个__call__方法.拥有__call__方法的对象可以把对象当做一个函数调用.
            我们在创建一个类的实例的时候,实际上是调用了这个类对象的元类的__call__(MetaClass:__call__)这个方法.

            例子: 
            class SimpleMetaClass(type):
                
                def __new__(cls,*args,**kwargs):
                    print ("creating class Earth...")
                    return  super(SimpleMetaClass,cls).__new__(cls,*args,**kwargs)
             
                def __init__(self,*args,**kwargs):
                    print ("you have create a class instance by metaclass")
                    super(SimpleMetaClass,self).__init__(*args,**kwargs)
             
                def __call__(self,*args,**kwargs):
                    print ("__call__ in metaclass has been invoked...","the args:",args,kwargs)
                    return super(SimpleMetaClass,self).__call__(*args,**kwargs)
             
            class Earth(metaclass=SimpleMetaClass):
                
                def __new__(cls,g,R=65535):
                    print ("creating instance using __new__")
                    cls.g = g
                    cls.R = R
                    return super(Earth,cls).__new__(cls);
             
                def __init__(self,g,R=65535):
                    print ("initializing instance in __init__")
                    print ("gravity on Earth is:%f" % self.g)
             
                def __call__(self):
                    print (self.g) 
             
                def sayHello(self):
                    print ("hello earth,your gravity is:%f" % self.g)
             
            earth = Earth(9.8,R=65535)
            earth()
            earth.sayHello()
            
            最终上面这段代码执行的结果是:
            ①creating class Earth...
            ②you have create a class instance by metaclass
            ③__call__ in metaclass has been invoked... the args: (9.8,) {'R': 65535}
            ④creating instance using __new__
            ⑤initializing instance in __init__
            ⑥gravity on Earth is:9.800000
            ⑦9.8
            ⑧hello earth,your gravity is:9.800000
             
            分析:
            首先python创建SimpleMetaClass类,这个SimpleMetaClass是元类,是由type创建的.
            当创建Earth这个类时,找到了它类中有__metaclass__属性,于是,采用SimpleClass来创建这个类
            创建Earh类时,解释器会把类名,父类元祖,类的属性三个参数传给SimpleMetaClass
            SimpleMetaClass 根据 className,(parent2,parent1,..),{‘attribute’:….,’method’:”},
            在自己__new__方法中创建出这个Earth实例 打印出①,然后调用自己的__init__方法初始化类的参数 打印出②.
            这时,这个Earth类作为metaclass的一个实例就被创建好了.
            接下来通过 earth = Earth(9.8,R=65535) 创建一个Earth对象实例earth.
            这一步实际上是调用 Earth这个类对象的元类(SimpleMetaClass)的__call__方法来创建一个Earth的实例. 
            打印出③,我们还能看到调用__call__的参数 .
            而创建earth实例的方法是调用 Earth这个类对象的 __new__(),和__init__(),
            先后执行 打印出④⑤⑥ 执行完成Earth实例earth对象被返回.
            ⑦⑧分别是调用earth实例的 __call__,sayHello方法的结果.
            '''

    def 类的特殊成员():
        '''更多内容详见官方文档 https://docs.python.org/3/reference/datamodel.html'''

        __slots__ = '''
            对于使用简单数据结构的类,通常在类的定义中增加__slots__属性,来大量减少内存的使用.
            class Date:
                __slots__ = ['year','month','day']
                def __init__(self,year,month,day):
                    self.year, self.month, self.day = year, month, day
            当定义了__slots__属性时,python会针对实例采用更加紧凑的内部表示.不在让每个实例都创建一个__dict__字典.实例时使用类似于列表元组的数组来构建的.
            缺点是,不能对实例添加任何新的属性.只允许使用__slots__中列出的属性名.python内很多部分基于传统的字典来实现.
            定义了__slots__的属性的类不支持某些特定的功能,如多重继承.__slots__可以阻止用户为实例添加新的属性.但__slots__更适合优化程序.
            '''

        __str__ = '''
            如果要把一个类的实例变成 str,就需要实现特殊方法__str__()
            如果一个类中定义了__str__方法,那么在打印 对象 时,或者 str(该对象)时,默认输出该方法的返回值.
            __str__方法必须有返回值.且返回的必须是一个字符串类型的数据.
            对象 = 类名()
            print(对象)   即调用该方法 
            
            例:
            class Person:
                def __init__(self,name,age):
                    self.name,self.age = name,age
                def __str__(self):
                    return 'this is str'
            p=Person('lisi',22)
            str(p) -----> 'this is str'
            print(p) -----> 'this is str'
            p -----> <__main__.Person at 0x25eb6584b38>
            直接 输入对象是不能调用 __str__ 方法的.
            '''

        __repr__ = '''
            由repr()函数调用,并通过字符串转换来计算对象的字符串表示形式.
            尝试让返回的字符串能够通过eval()来生成一个一样的对象.
            
            例:
            使用 __str__ 中的例子.
            repr(p) -----> '<__main__.Person object at 0x0000025EB6584B38>'     # 返回的是一个字符串
            class A:
                def __repr__(self):
                    return "this is repr"
            a=A()
            print(a) -----> this is repr
            str(a) -----> 'this is repr'
            repr(a) -----> 'this is repr'
            Python 定义了__str__()和__repr__()两种方法,__str__()用于显示给用户,而__repr__()用于显示给开发人员.
            如果__str__没有被定义,那么就会使用__repr__来代替输出
            __str__ 和 __repr__ 这俩方法的返回值必须是字符串,否则抛出异常

            可以这么写:
            class A:
                def __str__(self):
                    return 'your massage'
                __repr__ = __str__
                
            class Item:
                def __init__(self, name):
                    self._name = name;
                def __str__(self):
                    return "Item: %s" % self._name
                    
            print((Item("Car"),)) -----> (<__main__.Item object at 0x0000025EB65AD518>,)
            print(Item("Car")) -----> Item: Car
            
            会显示不同的原因是:
            当调用 print((Item("Car"),))时,实际是调用tuple类的__str__方法,这和__repr__方法相同. 
            该方法的工作原理是调用元组中每个元素的__repr__方法,并用逗号将它们连接在一起.
            
            格式化输出:
            %s => str()
            %r => repr()
            
            class A:
                def __str__(self):
                    return 'your massage'
            class B:
                def __str__(self):
                    return 'is str'
                    
                def __repr__(self):
                    return 'is repr'
            class C:
                pass
                    
            a=A()
            b=B()
            c=C()
            '%r' % a -----> '<__main__.A object at 0x0000025EB6574C18>'
            '%s' % a -----> 'your massage'
            '%r' % b -----> 'is repr'
            '%s' % b -----> 'is str'
            '%r' % c -----> '<__main__.C object at 0x0000025EB65AD908>'     # 如果没有定义__repr__ 会以字符串格式返回对象.
            '%s' % c -----> '<__main__.C object at 0x0000025EB65AD908>'     # 如果没有定义__str__  会使用__repr__来代替输出
            '''

        __format__ = '''
            自定制格式化字符串
            由format()内置函数调用，并通过扩展格式化字符串文本和str.format()方法，以生成对象的 格式化 字符串表示形式。
            format_spec参数是字符串类型的格式选项。
            format_spec参数的解释取决于类型实现__format__().
            返回值必须是一个字符串对象。
            class A:
                def __init__(self,name,age,job):
                    self.name = name
                    self.age  = age
                    self.job  = job
                    
                def __format__(self,format_spec):
                    print(format_spec)
                    msg = '{obj.name} age is {obj.age},job is {obj.job}.'
                    msg = msg.format(obj=self)
                    return msg
            
            a=A('lisi',22,'it')
            format(a) -----> 'lisi age is 22,job is it.'
            format函数 实际上是 调用值的 __format__ 方法,并传入一个参数 format_spec,默认传入的 format_spec 为空.所以在A 的__format__中,除self外需再接受一个形式参数.
            源码: Return value.__format__(format_spec)
            '''

        __init__ = '''
            初始化方法,通过类创建对象时,自动触发执行.
            '''

        __bool__ = '''
            真值测试和内置操作 bool(); 应该返回False或True
            '''

        __del__ = '''
            析构方法,当对象在内存中被释放时,自动触发执行.
            析构函数的调用是由解释器在进行垃圾回收时自动触发执行的.
            class A:
                def __del__(self):
                    print('del class')
                    
            a=A()
            del a -----> del class
            '''

        __getattr__ = '''
            __getattr__(self, item)
            在访问对象的item属性的时候，如果对象并没有这个相应的属性或方法。
            返回一个值或AttributeError异常。
            例:
            class A:
                name='lisi'
                def __getattr__(self,item):
                    print('getattr')
                    if item == 'name':return 'nana'
                    if item == 'age':return 22
            a=A()
            a.name -----> lisi      # 如果 对象有相应的属性就返回该属性的值,如果没有该属性，才会触发 __getattr__.
            a.age -----> getattr
                  -----> 22         
            '''

        __getattribute__ = '''
            无条件地调用以实现类的实例的属性访问。
            为了避免此方法中的无限递归，它的实现应始终调用具有相同名称的基类方法来访问它所需的任何属性，例如 object.__getattribute__(self, name)
            在 每次引用属性或方法名称时 Python 都调用它(特殊方法名称除外)
            只有在新式类中才有的，对于对象的所有特性的访问，都将会调用这个方法来处理
            可以理解为在__getattr__之前
            __getattribute__ 与 __getattr__ 的最大差异在于: 
                1. 无论调用对象的什么属性，包括不存在的属性，都会首先调用__getattribute__ 方法； 
                2. 只有找不到对象的属性时，才会调用__getattr__方法
            
            __getattribute__() 方法是绝对的、无条件的。

            class SuperDynamo(object):
                def __getattribute__(self, key):
                    if key == 'color':
                        return 'PapayaWhip'
                    else:
                        raise AttributeError

            dyn = SuperDynamo()
            dyn.color -----> PapayaWhip'
            dyn.color = 'LemonChiffon'
            dyn.color -----> PapayaWhip'
            在获取 dyn.color 的值时将调用 __getattribute__() 方法。
            即使显式地设置 dyn.color，在获取 dyn.color 的值时, 仍将调用 __getattribute__() 方法。
            如果存在 __getattribute__() 方法，将在每次查找属性和方法时 无条件地调用 它，哪怕在创建实例之后已经显式地设置了属性。
            如果定义了类的 __getattribute__() 方法，还想定义 __setattr__() 方法，会引起无限循环触发RecursionError。
            必须特别小心 __getattribute__() 方法，因为 Python 在查找类的方法名称时也将对其进行调用。
            
            class A:
                f = 'abc'
                def __getattribute__(self, *args, **kwargs):
                    print("__getattribute__() is called")
                    return object.__getattribute__(self, *args, **kwargs)

                def __getattr__(self, name):
                    print("__getattr__() is called ")
                    return name + " from getattr"
                
                def __get__(self, instance, owner):
                    print("__get__() is called", instance, owner)
                    return self
                
                def foo(self, x):
                    print(x)
            
            class B(object):
                ab = A()   # 一定要作为类属性，作为实例属性无效
            A = A()
            b = B()
            print(a.f) -----> __getattribute__() is called
                       -----> abc
            print(a.e) -----> __getattribute__() is called
                       -----> __getattr__() is called
                       -----> e from getattr
            b.ab -----> __get__() is called <__main__.B object at 0x00000175066D9C88> <class '__main__.B'>
            print(b.ab.f) -----> __get__() is called <__main__.B object at 0x00000175066D9C88> <class '__main__.B'>
                          -----> __getattribute__() is called
                         -----> abc

            每次通过实例访问属性，都会经过__getattribute__函数。而当属性不存在时，仍然需要访问__getattribute__，不过接着要访问__getattr__。
            每次访问descriptor(即实现了__get__的类)，都会先经过__get__函数。 
            '''

        __setattr__ = '''
            在进行属性设置时调用。name是属性名称，value是要分配给它的值。
            如果__setattr__()想给实例设置属性，它应该调用具有相同名称的基类方法，例如 object.__setattr__(self, name, value)
            '''

        __delattr__ = '''
            像__setattr__()但删除属性而不是赋值。只在对象有意义时才能实现。del obj.name
            '''

        __get__ = '''
            将对象作为数据描述符,这就是 __get__ 的作用，将整个对象都作为数据描述符.
            __get__ 作为数据描述符，那么此对象只能作为类属性，作为实例属性则无效.
            例:
            class Dept(object):
                  def __init__(self, name):
                      self.name = name
            
                  # target是拥有此属性的对象
                  def __get__(self, target, type=None):
                    # 默认返回self与obj都可以
                    return 'Dept'
            
            class Company(object):
                # 一定要作为类属性，作为实例属性无效
                dept = Dept('organ')
            
            x = Company()
            x.dept -----> 'Dept'
            '''

        __dir____= '''
            dir()在对象上调用时调用。必须返回一个序列。dir()将返回的序列转换为列表并对其进行排序。
            '''

        __getitem__ = '''
            例:
            class Foo():
                def __getitem__(self,key):
                    pass
                def __setitem__(self,key,value):
                    pass
                def __delitem__(self,key):
                    pass
            用于索引操作,如字典.以上分别表示获取数据
            obj=Foo()
            obj['k']            # 自动触发执行 __getitem__
            '''

        __setitem__ = '''
            用于索引操作,如字典.以上分别表示设置数据
            obj['k'] = values   # 自动触发执行 __setitem__
            '''

        __delitem__ = '''
            用于索引操作,如字典.以上分别表示获取删除数据
            del obj['k']        # 自动触发执行 __delitem__
            '''

        __call__ = '''
            __call__ 方法的执行是由对象后加括号触发的执行.
            __call__()是一个特殊方法,它可将一个类的实例变成一个可调用对象
            对象 = 类名() 
            对象() 或者 类()()
            '''

        __hash__ = '''
            由内置函数hash()调用,并用于对不可哈希序列(set、frozenset、dict)的操作. __hash __()应该返回一个整数.
            hash()会将从对象的自定义__hash __()方法返回的值 截断为Py_ssize_t的大小.在64位版本上是8个字节,在32位版本上是4个字节.
            详见官方文档 https://docs.python.org/3/reference/datamodel.html?highlight=__hash__#object.__hash__
            '''

        比较成员 = '''
            object.__lt__(self, other)  x<y     x.__lt__(y)
            object.__le__(self, other)  x<=y    x.__le__(y)
            object.__eq__(self, other)  x=y     x.__eq__(y)
            object.__ne__(self, other)  x!=y    x.__ne__(y)
            object.__gt__(self, other)  x>y     x.__gt__(y)
            object.__ge__(self, other)  x>=y    x.__ge__(y)
            默认情况下,__ne __()委托给__eq __(),并将结果反转
            '''

        __new__ = '''
            在类中,object是所有的类的父类
            object中的 __new__ 其实是一个类的静态方法,所以能通过类名直接调用.被调用来创建类cls的新实例。
            并且至少需要传递一个参数cls,cls表示需要实例化的类,此参数在实例化时由Python解释器自动提供.见object的源码.
            剩下的参数是传递给对象构造函数表达式(对类的调用)的参数.
            __new__是创建这个类实例的方法,在 __init__ 之前调用.
            __new__方法接受的参数虽然也是和__init__一样,但__init__是在类实例创建之后调用
            __new__()必须要有返回值,返回实例化出来的实例,需要注意的是,可以return父类__new__()出来的实例,也可以直接将object的__new__()出来的实例返回.
            典型的用法是,通过__new__()使用 适当的参数调用超类的该方法，然后在返回根据需求修改新创建的新实例。super().__new__(cls[, ...])
            如果__new__()返回一个cls实例，那么新实例的 __init__()方法将被调用，其中 self是新实例，其余参数与传递给它的相同。__init__(self[, ...])__new__()
            如果__new__()不返回cls的实例，那么新实例的 __init__()方法将不会被调用。

            例:
            class person:
                def __new__(cls,name,age):
                    return super(person,cls).__new__(cls,name,age)
                def __init__(self,name,age):
                    self.name = name
                    self.age  = age
            实例化一个类的时候,具体的执行逻辑是这样的:
            1,p = person('lisi',22)
            2,首先执行使用name和age参数来执行person类的__new__方法.
            这个__new__方法会 返回person类的一个实例(通常情况下是使用 super(Persion, cls).__new__(cls, … …) 这样的方式),
            3,然后利用这个实例来调用类的__init__方法,上一步里面__new__产生的实例也就是 __init__里面的的 self.

            __init__ 和 __new__ 最主要的区别在于:
            1.__init__ 通常用于初始化一个新实例,控制这个初始化的过程,比如添加一些属性, 做一些额外的操作,发生在类实例被创建完以后.它是实例级别的方法.
            2.__new__ 通常用于控制生成一个新实例的过程.它是类级别的方法.

            __new__最通常的用法:
            __new__方法主要是当你继承一些不可变的class时(比如int, str, tuple), 提供给你一个自定义这些类的实例化过程的途径.
            实现自定义的metaclass.见 __metaclass__
            实现单例.

            继承不可变的class类,对于int这种 不可变的对象,只有重载它的__new__方法才能起到自定义的作用.
            class PositiveInteger(int):
                def __new__(cls, value):
                    return super(PositiveInteger, cls).__new__(cls, abs(value))

            i = PositiveInteger(-3)
            print i

            用__new__来实现单例 单例适合只有一个对象的时候用.
            实现 设计模式中的 单例模式(singleton) .
            因为类每一次实例化后产生的过程都是通过__new__来控制的,所以通过重载__new__方法,我们 可以很简单的实现单例模式.

            class person:
                def __new__(cls):
                    if not hasattr(cls,'instance'):
                        # 关键在于这,每一次实例化的时候,我们都只会返回这同一个instance对象
                        cls.instance = super(person,cls).__new__(cls)
                        #cls.instance = super(person,person).__new__(cls)       # 注释掉的两种写法产生的结果与第一种写法的结果一样,推荐第一种.
                        #cls.instance = object.__new__(cls)
                    return cls.instance
            通过每次返回同一个 cls.instance 来实现单例.
            '''

        __metaclass__ = '''
            在python3 中已经没有这种写法了, class A(metaclass=something):pass
            这种形式来指定一个类的元类. 详见 元类的解释.
            '''

        __iter__ = '''
            用于迭代器
            class Foo:
                def __init__(self, sq):
                    self.sq = sq
            
                def __iter__(self):
                    return iter(self.sq)
            obj = Foo([11,22,33,44])
            for i in obj:
                print i
            '''

        __getslice__ = '''
            用于分片操作
            例:
            class Foo():
                def __getslice__(self, i, j):
                    pass
                def __setslice__(self, i, j, sequence):
                    pass
                def __delslice__(self, i, j):
                    pass
            obj = Foo()
            obj[-1:1]                   # 自动触发执行 __getslice__
            '''

        __setslice__ = '''
            用于分片操作
            obj[0:1] = [11,22,33,44]    # 自动触发执行 __setslice__
            '''

        __delslice__ = '''
            用于分片操作
            del obj[0:2]                # 自动触发执行 __delslice__
            '''

        __dict__ = '''
            类或对象中的所有成员
            类的普通字段属于对象,类中的静态字段和方法等属于lei.
            '''

        __module__ = '''
            表示当前操作的对象在那个模块
            '''

        __class__ = '''
            表示当前操作的对象的类是什么
            '''

        __doc__ = '''
            该方法或函数的文档字符串
            '''

        __len__ = '''
            详见官方文档 https://docs.python.org/3/reference/datamodel.html?highlight=__len__#object.__len__
            被内置函数len() 调用来触发本方法。 
            class A:
                def __init__(self):
                    self.a = 1
                    self.b = 2
            
                def __len__(self):
                    return len(self.__dict__)
            a = A()
            print(len(a))
            '''

        __delete__ = '''
            详见 类的描述符
            '''

        __set__ = '''
            详见 类的描述符
            '''

        __get__ = '''
            详见 类的描述符
            '''

    def 类的描述符():
        '''
        详见 https://blog.csdn.net/leafage_m/article/details/54960432
        描述符是具有 绑定行为 的对象属性,其属性访问被描述符协议中的方法重写.
        这些方法是__get__(),__set__()和__delete__().如果对象中定义了这些方法中的任何一种,则称它为描述符.
        属性访问的默认是从对象的字典中获取,设置或删除属性.
        例如,a.x有一个以a.__dict__['x']开始的查找链,接着是type(a).__dict__['x'],然后是除了元类之外的type(a)的基类.
        如果对象定义其中一个描述符方法,则Python可以调用描述符方法重写默认行为.
        描述符是一个强大的通用协议.它们是属性,方法,静态方法,类方法和super()的工作机制.

        descr.__get__(self, obj, type=None) --> value
        descr.__set__(self, obj, value) --> None
        descr.__delete__(self, obj) --> None
        这就是所有的描述符方法.定义这些方法中的任何一个,就将对象视为描述符,并且可以在查找属性时重写默认行为.
        如果一个对象同时定义了__get__()和__set__(),它就是一个数据描述符.
        只定义__get__()的描述符被称为非数据描述符.

        数据和非数据描述符不同在于它们在对象字典中的优先级.
        如果对象的字典中有一个与数据描述符同名的条目,则数据描述符优先.
        如果对象的字典中有一个与非数据描述符名称相同的条目,则字典条目优先.
        要创建一个只读数据描述符,同时定义__get __和__set__,并且定义__set__时引发AttributeError异常.

        调用描述符
        描述符可以通过其方法名直接调用.例如,d.__get__(obj).
        另外,更为常见的是描述符在属性访问时被自动调用.
        例如,obj.d在obj的字典中查找d.如果d定义了方法__get__(),则根据下面列出的优先规则d.__get__(obj)被调用.
        '''

    def type和object的关系():
        '''pass'''

    def 类的使用技巧():

        基类的公用__init__方法 = '''
        详见 https://www.kancloud.cn/kancloud/python3-cookbook/47264
        import math
        
        class PublicBase:
            _fields = []
            def __init__(self,*args,**kwargs):
                # 如果位置参数的个数不等于 字段列表的个数，就报类型错误.
                if len(args) != len(self._fields):
                    raise TypeError('Expected {} arguments'.format(len(self._fields)))
                
                # 先将位置参数设置完成
                for name,value in zip(self._fields,args):
                    setattr(self,name,value)
                
                # 得到的extra_args 是一个集合.里面是所有的关键字参数。
                extra_args = kwargs.keys() - self._fields
                for name in extra_args:
                    setattr(self,name,kwargs.pop(name))
                
                #如果关键字参数设置完成后，kwargs 里面还有值，就报类型错误.
                if kwargs:
                    raise TypeError('Duplicate values for {}'.format(','.join(kwargs)))
        if __name__ == '__main__':
            class Stock(PublicBase):
                _fields = ['name', 'shares', 'price']
        
            s1 = Stock('ACME', 50, 91.1)
            s2 = Stock('ACME', 50, 91.1, date='8/2/2012')
        '''

        用描述器实现类型检查 = '''
            class MustInt:
                def __init__(self, name):
                    self.name = name
            
                def __get__(self, instance, cls):
                    if instance is None:
                        return self
                    else:
                        # 这里不能用getattr的原因是 getattr 也是调用的__get__方法,会导致循环调用触发最大递归深度的错误。
                        return  instance.__dict__[self.name]  #getattr(instance, self.name)
            
                def __set__(self, instance, value):
                    if not isinstance(value, int):
                        raise TypeError('Expected an int')
                    # 这里不能用setattr的原因是 setattr 也是调用的__set__方法,会导致循环调用触发最大递归深度的错误。
                    #setattr(instance, self.name, value)
                    instance.__dict__[self.name]=value
            
                def __delete__(self, instance):
                    # 这里不能用delattr的原因是 delattr 也是调用的__delete__方法,会导致循环调用触发最大递归深度的错误。
                    #delattr(instance, self.name)
                    del instance.__dict__[self.name]
            
            
            class MayInt:
                # 这里必须有一个字符串格式的变量名作为MustInt的参数
                # 这个字符串作为存储在 MayInt实例对象字典中的key,可以取任何名但不能相同，因为他们用的是同一个Mayint 对象。
                x = MustInt('x')
                y = MustInt('y')
            
                def __init__(self, x, y):
                    # 在Mayint实例化后，self.x 就是 MustInt的实例对象。
                    # self.x = x 就是调用的 MustInt实例对象的__set__ 方法。
                    self.x = x
                    self.y = y
            
            m = MayInt(2, 3)
            # 执行 m.x 是MustInt的实例对象 执行它就是调用 __get__ 方法。
            # 必须通过不同 name值作为 Mayint 实例对象 字典中的key 来存取数据。
            print(m.x) -----> 2
            '''

        使用描述器类来装饰其他类的方法 = '''
            详见 https://www.kancloud.cn/kancloud/python3-cookbook/47263
            class myproperty:
                # 这里的func 是指 向Circle.area的内存地址
                def __init__(self, func):
                    self.func = func
            
                # 这里的self是指area,instance 是指 Circle的实例对象。cls 是指 Circle类。
                def __get__(self, instance,cls):
                    if instance is None:
                        return self
                    else:
                        value = self.func(instance)     #这里的 instance 就是Circle的实例对象中的self,返回值就是该方法的计算结果
                        setattr(instance, self.func.__name__, value)    # 为 Circle的实例对象 设置一个与self.func方法同名的静态属性。
                        return value        # 返回就算结果
            
            import math
            class Circle:
                def __init__(self, r):
                    self.r = r
            
                # area = myproperty(Circle.area)
                # 这个地方把area变成了 myproperty的一个实例把Circle.area当作参数传入到myproperty中
                # 同时把方法area变成了，Circle的一个属性。
                @myproperty
                def area(self):
                    return math.pi * self.r ** 2
            
                @myproperty
                def peri(self):
                    return 2 * math.pi * self.r
            
            c=Circle(3)
            print(c.area)  # 这里就相当于取 c的静态属性area
            print(c.peri)
            '''

def socket网络编程():

    方法 = '''相关方法及参数介绍
sk.bind(address)

　　#s.bind(address) 将套接字绑定到地址。address地址的格式取决于地址族。在AF_INET下，以元组（host,port）的形式表示地址。

sk.listen(backlog)

　　#开始监听传入连接。backlog指定在拒绝连接之前，可以挂起的最大连接数量。

      #backlog等于5，表示内核已经接到了连接请求，但服务器还没有调用accept进行处理的连接个数最大为5
      #这个值不能无限大，因为要在内核中维护连接队列

sk.setblocking(bool)

　　#是否阻塞（默认True），如果设置False，那么accept和recv时一旦无数据，则报错。

sk.accept()

　　#接受连接并返回（conn,address）,其中conn是新的套接字对象，可以用来接收和发送数据。address是连接客户端的地址。

　　#接收TCP 客户的连接（阻塞式）等待连接的到来

sk.connect(address)

　　#连接到address处的套接字。一般，address的格式为元组（hostname,port）,如果连接出错，返回socket.error错误。

sk.connect_ex(address)

　　#同上，只不过会有返回值，连接成功时返回 0 ，连接失败时候返回编码，例如：10061

sk.close()

　　#关闭套接字

sk.recv(bufsize[,flag])

　　#接受套接字的数据。数据以字符串形式返回，bufsize指定最多可以接收的数量。flag提供有关消息的其他信息，通常可以忽略。

sk.recvfrom(bufsize[.flag])

　　#与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。

sk.send(string[,flag])

　　#将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。即：可能未将指定内容全部发送。

sk.sendall(string[,flag])

　　#将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。

      #内部通过递归调用send，将所有内容发送出去。

sk.sendto(string[,flag],address)

　　#将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。该函数主要用于UDP协议。

sk.settimeout(timeout)

　　#设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如 client 连接最多等待5s ）

sk.getpeername()

　　#返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。

sk.getsockname()

　　#返回套接字自己的地址。通常是一个元组(ipaddr,port)

sk.fileno()

　　#套接字的文件描述符'''

def 常用模块():

    def collections模块():
        '''collections是Python内建的一个集合模块,提供了许多有用的集合类.'''

        deque方法 = '''
            from collections import deque  # 双端队列
            两端都可以操作的序列,在序列的前后你都可以执行添加或删除操作.
            q=deque()           # 可以通过maxlen=3限制长度,当超过指定长度时,会移除最老的元素.默认不指定无长度限制.
            q.append(1)         # 在右边追加一个元素
            q.appendleft(0)     # 在左边追加一个元素
            q.pop()             # 删除右边的最后一个元素,并返回其值.
            q.popleft()         # 删除左边的最后一个元素,并返回其值.
            q.extend([2,3])     # 在右边迭代追加一个列表中的元素.
            q.extend([1,2,3])   # 在左边迭代追加一个列表中的元素,追加进去的依次是1,2,3,在列表中的顺序是3,2,1.
            len(q)
            '''

        defaultdict方法 = '''
            存在默认值的字典,自动构造函数,将字典的键关联多个值,通常将多个值放到一个容器里面.一键多值字典,defaultdict 会自动初始化第一个值.
            from collections import defaultdict
            l = defaultdict(list)
            l[key].append(1)
            s = defaultdict(list)
            s[key].add(1)
            '''

        OrderedDict方法 = '''
            有序字典,当对字典做迭代时,会严格按照元素初始添加的顺序进行.有序字典要不普通字典所占的空间大.
            from collections import defaultdict as dict
            '''

        Counter方法 = '''
            找出序列中出现次数最多的n个值,序列中的元素必须是可迭代的,因为序列中的元素会作为字典的键,在Counter的实例化中.
            from collections import Counter
            word_a=['a','a','b','c','d','d','e','d','c']
            word_count = Counter(word_a)     word_count 是一个以words的元素为键,元素出现次数为值的Counter字典.
            word_count.most_common(3)       被实例化后的Counter对象,有一个most_common的方法,接收一个数字n,来返回指定n个的出现次数最多的值.
            可以直接 修改 Counter对象的值,word_count['a']=10,也可以使用字典的update方法跟新 Counter对象word_count.
            Counter对象 可以直接进行数学运算,适用于制表和数据统计
            word_b=['a','e','e','a','d','d','e','d','c']
            a=Counter(word_a)
            b=Counter(word_b)
            c=a+b
            d=a-b
            a ----> Counter({'a': 2, 'b': 1, 'c': 2, 'd': 3, 'e': 1})
            b ----> Counter({'a': 2, 'c': 1, 'd': 3, 'e': 3})
            c ----> Counter({'a': 4, 'b': 1, 'c': 3, 'd': 6, 'e': 4})
            d ----> Counter({'b': 1, 'c': 1})
            '''

        namedtuple方法 = '''
            命名元组,可以通过属性访问数据,同时具有普通元组的一些特性,可以通过索引取值.
            可以作为字典的替代.但命名元组是不可变的.
            from collections import namedtuple
            
            named_tp1=namedtuple('info',('name','age'))  创建一个命名元组实例 属性名也可以是列表的形式named_tp1=namedtuple('info',['name','age'])
            nt1=named_tp1('lisi',22)  -----> info(name='lisi', age=22)    实例化,插入一条数据
            nt1.name                  -----> 'lisi'     通过属性name取值
            nt1.age                   -----> 22         通过属性age 取值
            len(nt1)                  -----> 2          获取元素个数
            name,age=nt1              -----> name is 'lisi',age is 22   可以进行解包操作
            nt1[0]                    -----> 通过索引取值
            
            _replace()方法 
            nt1.age = 23 这种方法是错误的,但可以通过_replace方法来实现.该方法不会修改本身的元组,而是返回一个新的命名元组.
            nt1._replace(age=23)     nt1不会改变,返回info(name='lisi', age=23),可以这样实现更改 nt1=nt1._replace(age=23)
             _replace()方法 还可以接受通过解包一个字典作为参数去修改
            d1={'age': 33, 'name': 'nana'}
            nt1=nt1._replace(**d1)   -----> info(name='nana', age=33)  并且是有序的.
            '''

        ChainMap方法 = '''
            将多个字典或者关系映射,在逻辑上合并为一个字典或关系映射
            a={'x':1,'z':3}
            b={'y':2,'z':4}
            from collections import ChainMap
            c=ChainMap(a,b)
            c['x']    # 1
            c['y']    # 2
            c['z']    # 3  如果有重复的键,以第一个字典的键对应的值为主.
            a,b的值并不会变化
            如果要修改值,变化的只有第一个字典.
            c['z']=5
            del c['y'] 会报错,因为a字典中不存在y键.
            '''

        Iterable方法 = '''
            from collections import Iterable
            判断是不是可以迭代,用Iterable
            isinstance([1,],Iterable) -----> True
            '''

        Iterator方法 = '''
            from collections import Iterator
            判断是不是迭代器,用Iterator
            isinstance((i for i in range(11)), Iterator) -----> True
            '''

    def os模块():

        os方法 = '''
            os.getcwd()             获取当前工作目录,即当前python脚本工作的目录路径
            os.chdir("dirname")     改变当前脚本工作目录；相当于shell下cd
            os.curdir               返回当前目录: ('.')
            os.pardir               获取当前目录的父目录字符串名:('..')
            os.makedirs('dirname1/dirname2')    可生成多层递归目录
            os.removedirs('dirname1')   若目录为空,则删除,并递归到上一级目录,如若也为空,则删除,依此类推
            os.mkdir('dirname')         生成单级目录；相当于shell中mkdir dirname
            os.rmdir('dirname')         删除单级空目录,若目录不为空则无法删除,报错；相当于shell中rmdir dirname
            os.listdir('dirname')       列出指定目录下的所有文件和子目录,包括隐藏文件,并以列表方式打印
            os.remove()  删除一个文件
            os.rename("oldname","newname")  重命名文件/目录
            os.stat('path/filename')
                获取文件/目录信息
                st_mode: inode 保护模式
                st_ino: inode 节点号.
                st_dev: inode 驻留的设备.
                st_nlink: inode 的链接数.
                st_uid: 所有者的用户ID.
                st_gid: 所有者的组ID.
                st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据.
                st_atime: 上次访问的时间.
                st_mtime: 最后一次修改的时间.
                st_ctime: 由操作系统报告的"ctime".在某些系统上(如Unix)是最新的元数据更改的时间
            os.sep                  输出操作系统特定的路径分隔符,win下为"\\",Linux下为"/"
            os.linesep              输出当前平台使用的行终止符,win下为"\t\n",Linux下为"\n"
            os.pathsep              输出用于分割文件路径的字符串 win下为;,Linux下为:
            os.name                 输出字符串指示当前使用平台.win->'nt'; Linux->'posix'
            os.system("bash command")       运行shell命令,直接显示,得到返回状态 返回无法截取
            os.popen("bash command) 运行shell命令,获取执行结果,当需要得到外部程序的输出结果时,返回一个类文件对象,调用该对象的read()或readlines()方法可以读取输出内容.
            os.environ              获取系统环境变量
            os.access(path, mode)   检验权限模式
            os.chmod(path, mode)    更改权限
            os.chown(path, uid, gid)更改文件所有者
            os.chroot(path)         改变当前进程的根目录	
            os.close(fd)            关闭文件描述符 fd
            os.isatty(fd)           如果文件描述符fd是打开的,同时与tty(-like)设备相连,则返回true, 否则False
            os.link(src, dst)       创建硬链接,名为参数 dst,指向参数 src
            os.pipe()               创建一个管道. 返回一对文件描述符(r, w) 分别为读和写	
            os.readlink(path)                       返回软链接所指向的文件
            os.symlink(src, dst)                    创建一个软链接      
            os.getenv()             读取环境变量
            os.putenv()             设置环境变量
            os.walk('/root/')
                os.walk() 方法用于通过在目录树种游走输出在目录中的文件名,向上或者向下.
                walk()方法语法格式如下:
                os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
                参数
                top -- 根目录下的每一个文件夹(包含它自己), 产生3-元组 (dirpath, dirnames, filenames)【文件夹路径, 文件夹名字, 文件名】.
                topdown --可选,为True或者没有指定, 一个目录的的3-元组将比它的任何子文件夹的3-元组先产生 (目录自上而下).如果topdown为 False, 一个目录的3-元组将比它的任何子文件夹的3-元组后产生 (目录自下而上).
                onerror -- 可选,是一个函数; 它调用时有一个参数, 一个OSError实例.报告这错误后,继续walk,或者抛出exception终止walk.
                followlinks -- 设置为 true,则通过软链接访问目录.
            os.environ['HOME']      看系统环境变量
            os.statvfs("/")         获取磁盘信息
            '''

        os模块path方法 = '''
            os.path
            path="/usr/lib/systemd/system/diting.serivce"
            os.path.abspath(path)   返回path规范化的绝对路径
            os.path.split(path)     将path分割成目录和文件名二元组返回
            os.path.dirname(path)   返回path的目录.'/usr/lib/systemd/system',返回path的父目录,其实就是os.path.split(path)的第一个元素
            os.path.basename(path)  返回path最后的文件名.'diting.serivce', 如果path以／或\结尾,那么就会返回空值.即os.path.split(path)的第二个元素
            os.path.commonprefix(list) 返回list中,所有path共有的最长的路径.
            os.path.exists(path)    如果path存在,返回True；如果path不存在,返回False
            os.path.isabs(path)     如果path是绝对路径,返回True
            os.path.islink(path)    如果path是一个链接文件,返回True.否则返回False
            os.path.realpath(path)  返回链接文件的真实路径.
            os.path.isfile(path)    如果path是一个存在的文件,返回True.否则返回False
            os.path.isdir(path)     如果path是一个存在的目录,则返回True.否则返回False
            os.path.join(path1[, path2[, ...]])  将多个路径组合后返回,第一个绝对路径之前的参数将被忽略
            os.path.splitext(path)          分离文件名与扩展名；默认返回(fname,fextension)元组,可做分片操作
            os.path.ismount(path)           判断路径是否为挂载点()
            os.path.relpath(path[, start])  从start开始计算相对路径
            os.path.samefile(path1, path2)  判断目录或文件是否相同
            os.path.expanduser(path)        把path中包含的"~"和"~user"转换成用户目录
            os.path.getatime(path)          返回path所指向的文件或者目录的最后访问时间
            os.path.getmtime(path)          返回path所指向的文件或者目录的最后修改时间
            os.path.getsize(path)           返回path的大小 单位:bytes,本质上是 os.stat(path).st_size
            os.path.walk(path, visit, arg)  遍历path,进入每个目录都调用visit函数,visit函数必须有3个参数(arg, dirname, names),dirname表示当前目录的目录名,names代表当前目录下的所有文件名,args则为walk的第三个参数
            '''

    def sys模块():

        方法 = '''
        sys.argv        命令行参数List,第一个元素是程序本身路径
        sys.exit(n)     退出程序,正常退出时exit(0), 错误退出sys.exit(1)
        sys.version     获取Python解释程序的版本信息
        sys.path
            初始化时使用PYTHONPATH环境变量的值,获取指定模块搜索路径的字符串集合.
            可以将写好的模块放在得到的某个路径下,就可以在程序中import时正确找到.
            或 sys.path.append("自定义模块路径")
        sys.platform    返回操作系统平台名称
        sys.modules
            sys.modules是一个全局字典,该字典是python启动后就加载在内存中.
            每当导入新的模块,sys.modules将自动记录该模块.
            当第二次再导入该模块时,python会直接到字典中查找,从而加快了程序运行的速度.它拥有字典所拥有的一切方法.
        sys.getdefaultencoding()    获取系统当前编码,一般默认为ascii.
        sys.setdefaultencoding()    设置系统默认编码,执行dir(sys)时不会看到这个方法,在解释器中执行不通过,可以先执行reload(sys),在执行 setdefaultencoding('utf8'),此时将系统默认编码设置为utf8.(见设置系统默认编码 )
        sys.getfilesystemencoding() 获取文件系统使用编码方式,Windows下返回'mbcs',mac下返回'utf-8'.
        sys.stdin,sys.stdout,sys.stderr:
            stdin , stdout , 以及stderr 变量包含与标准I/O 流对应的流对象.
            如果需要更好地控制输出,而print 不能满足你的要求, 它们就是你所需要的.
            你也可以替换它们, 这时候你就可以重定向输出和输入到其它设备( device ), 或者以非标准的方式处理它们.
        '''

    def re模块():
        '''在线测试工具 http://tool.chinaz.com/regex/'''

        正则基础 = '''
            元字符       
                . 	        匹配除换行符以外的任意字符,匹配除 "\n" 之外的任何单个字符.要匹配包括 '\n' 在内的任何字符,请使用象 '[.\n]' 的模式.
                \w	        匹配字母或数字或下划线,匹配任何字母数字字符,相当与[a-zA-Z0-9_]
                \W          匹配非字母或数字或下划线,匹配任何非字母数字字符,相当与[^a-zA-Z0-9_]]
                \s	        匹配任意的空白符  匹配任何空白字符,相当与[ \t\n\r\f\v]  #注意前面有个空格
                \S          匹配非空白符,匹配任何非空白字符,相当与[^ \t\n\r\f\v]
                \d	        匹配数字,匹配任何是十进制数,相当与[0-9]
                \D          匹配非数字,匹配任何是非数字字符,相当与[^0-9]
                \n	        匹配一个换行符
                \t	        匹配一个制表符
                \b	        匹配一个单词的结尾,匹配一个单词边界,也就是指单词和任何特殊字符的边界.
                ^	        匹配字符串的开始 以某个字符开始.
                $	        匹配字符串的结尾
                a|b         匹配字符a或字符b,如 abc|abcd 这样写只会匹配abc,abcd是匹配不到的,abcd|abc 这样才能匹配到.如果有一短一长2个相似的的正则表达式,一定要把长的放在前面.
                ()          匹配括号内的表达式,表示分组,将括号里面的内容整体匹配.圆括号表示分组,里面的东西是一个整体.
                [...]       匹配字符组中的字符,元字符 [] 字符集 匹配里面的字符 或的关系,字符集取消元字符的特殊功能 (除了这三个\ ^ -)
                [^...]      匹配除了字符组中字符的所有字符,字符集取消元字符的特殊功能 (除了这三个\ ^ -)
                \           元字符 \ 转义 反斜杠后边跟元字符去除特殊功能.反斜杠后边跟普通字符实现特殊功能.
                \A	        匹配字符串开始
                \z	        匹配字符串结束
                \Z	        匹配字符串结束,如果是存在换行,只匹配到换行前的结束字符串.
                \G	        匹配最后匹配完成的位置.
                \B	        匹配非单词边界.'er\B' 能匹配 "verb" 中的 'er',但不能匹配 "never" 中的 'er'.
                \1...\9	    匹配第n个分组的内容.
                \10	        匹配第n个分组的内容,如果它经匹配.否则指的是八进制字符码的表达式.
                (?P<name>...)    分组,同时起一个别名
                (?P=name)        引用别名为name的分组匹配到的字符串
                \<number>        引用编号为number的分组匹配到的字符串
                \w\W        表示全集匹配所有的,另外还有\s\S、\d\D
                            
            贪婪匹配
                量词         用法说明
                *	        重复零次或更多次
                +	        重复一次或更多次
                ?	        重复零次或一次
                {n}	        重复n次
                {n,}	    重复n次或更多次
                {n,m}	    重复n到m次
            
            非贪婪匹配
                量词         用法说明
                *?          重复任意次,但尽可能少重复
                +?          重复1次或更多次,但尽可能少重复
                ??          重复0次或1次,但尽可能少重复
                {n,m}?      重复n到m次,但尽可能少重复
                {n,}?       重复n次以上,但尽可能少重复
            
            捕获组与非捕获组
                如果想用 () 对正则表达式进行分组,但想看到整体的匹配结果, 请用非捕获组  (?:正则表达式) 这里来取消组的优先级.   
                print(re.findall('www.(\w+).com','www.baidu.com'))    #['baidu'] 因为 () 的优先级比较高所以会优先显示组里面的内容.
                print(re.findall('www.(?:\w+).com','www.baidu.com'))  #['www.baidu.com'] 用 ?: 取消组的优先级.
                非捕获组意味着这个组只做匹配,但不捕获结果,也不会分配组号.
               
                ret=re.split("\d+","eva3egon4yuan")
                print(ret) -----> ['eva', 'egon', 'yuan']
                ret=re.split("(\d+)","eva3egon4yuan")
                print(ret) -----> ['eva', '3', 'egon', '4', 'yuan']
                ret=re.split("(?:\d+)","eva3egon4yuan")
                print(ret) -----> ['eva', 'egon', 'yuan']
                在匹配部分加上 () 之后所切出的结果是不同的,
                没有 () 的没有保留所匹配的项,但是有 () 的却能够保留了匹配的项.

            分组命名
                语法 (?P<name>) 注意先命名,后正则,可以在group中指定分组名,来获取匹配到的内容. 特别注意P是大写的.
                re_select=re.compile(r'select\s+(?P<limit>.*)\s+from\s+(?P<table_name>.*)\s+where\s+(?P<part>.*)')
                sql='select * from a.b where id<=1 '
                print(re_select.search(sql).group('limit','part'))

            转义符 \
                如匹配元字符,\d和\s等,如果要在正则中匹配"\d"字符,而不是"数字"就需要对"\"进行转义,变成'\\'.
                python中,无论是正则表达式,还是待匹配的内容,都是以字符串的形式出现的,在字符串中\也有特殊的含义,本身还需要转义.
                所以如果匹配一次"\d",字符串中要写成'\\d',那么正则里就要写成"\\\\d".
                用r'\d',表示是r'\\d' .在字符串之前加r,让整个字符串不转义
                详解:
                如果要匹配字符串\d 而不是正则中具有特殊意义的,代表数字的\d,匹配的正则表达式应该写成 \\d.
                但是如果要在python中表示 字符串 \\d ,本身的\\在python中只表示一个\,所有需要对每个\\,进行转义,即\\\\.
                
            .*?的用法
                . 是任意字符
                * 是取 0 至 无限长度
                ? 是非贪婪模式.
                何在一起就是 取尽量少的任意字符,一般不会这么单独写,他大多用在:
                .*?x
                就是取前面任意长度的字符,直到一个x出现
            
            group、groups、groupdict、start、end、span
                Match对象代表匹配的结果,包含匹配的相关信息.
                group() 返回一个或多个组匹配的子串,不填写参数默认为group(0),代表整个匹配的子串.
                ()里面的参数可以是编号,也可以是组的别名.没匹配到的组返回None,匹配到多个子串的组返回最后一个.
                groups()返所有组匹配的子串.当组没有匹配到子串时候返回None
                groupdict():    返回字典,键为组的别名,值为该组匹配到的子串.没有别名的组不返回.
                当一个匹配对象成功返回后,可以用start、end、span去查看他们的匹配位置,假如一个匹配对象是values.
                values.start() 指匹配的开始字符位置,返回指定组匹配的子串在string中的开始下标,没有匹配则返回-1 
                values.end()   指匹配的结束字符位置,返回指定组匹配的子串在string中的结束下标,没有匹配则返回-1 
                values.span()  指匹配的字符范围
                也可以在括号里通过指定分组的名字或编号的方式来指定第几个分组的的位置.
                values.start(1)
                values.span('part')
                详见 compile 方法.
            修饰符 - 可选标志    
                re.I	使匹配对大小写不敏感
                re.L	做本地化识别(locale-aware)匹配
                re.M	多行匹配,影响 ^ 和 $
                re.S	re.DOTALL   都可以使 . 匹配包括换行在内的所有字符
                re.U	根据Unicode字符集解析字符.这个标志影响 \w, \W, \b, \B.
                re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解.
            匹配多行
                text="/*  this is a 
                          multiline coment  */"
                comment = re.compile(r'/\*((?:.|\n)*?)\*/') 或 comment = re.compile(r'/\*(.*?)\*/',re.DOTALL)
                comment.findall(text) -----> ['  this is a\nmultiline coment ']
            '''

        split方法 = '''
            用一对[]指定多个分隔符,以字符串分组.
            如:
            line='asf sdf,sdf;  fdssdf,sf:dsfs,  sdfds fsasdf sdf'
            re.split(r'[,:;\s]\s*',line) -----> ['asf', 'sdf', 'sdf', 'fdssdf', 'sf', 'dsfs', 'sdfds', 'fsasdf', 'sdf']
            '''

        match方法 = '''
            函数语法
            re.match(pattern, string, flags=0)
            从字符串的起始位置匹配一个模式,如果不是起始位置匹配成功的话,match()就返回none.
            相当于search()加^,只匹配字符串开头,返回第一个匹配到的对象,否则返回None.对象可以调用group()得到返回结果.
            ret = re.match('a', 'abc').group()  # 同search,不过尽在字符串开始处进行匹配
            print(ret) -----> 'a'
            '''

        search方法 = '''
            函数语法:
            re.search(pattern, string, flags=0)
            扫描整个字符串并返回第一个成功的匹配.
            返回匹配到的第一个,是一个对象,对象可以调用group()得到返回结果.,如果字符串没有匹配,则返回None.
            ret = re.search('a', 'eva egon yuan').group()
            print(ret) -----> 'a'
            '''

        match与search的区别 = '''
            re.match只匹配字符串的开始,如果字符串开始不符合正则表达式,则匹配失败,函数返回None；而re.search匹配整个字符串,直到找到一个匹配.
            '''

        findall方法 = '''
            返回所有满足匹配条件的结果,放在列表里,在字符串中找到正则表达式所匹配的所有子串,并返回一个列表,如果没有找到匹配的,则返回空列表.
            语法格式
            findall(string[, pos[, endpos]]) 可以通过pos,endpos 来指定查找字符串的起始结束位置.
            '''

        compile方法 = '''
            用于编译正则表达式,生成一个正则表达式( Pattern )对象,供 match() 和 search() 这两个函数使用.
            语法格式
            re.compile(pattern[, flags])
            
            re_insert=re.compile(r'insert\s+into\s+(?P<table_name>.+)\s{0,}(?P<part>\(.+\))')
            sql="insert into test.t1(name,id,age)"
            values=re_insert.search(sql)
            print(values.group('table_name','part')) -----> ('test.t1', '(name,id,age)')
            print(values.start()) -----> 0 指匹配的开始字符位置
            print(values.end()) ----->  32 指匹配的结束字符位置
            print(values.span()) ----->  (0, 32) 指匹配的字符范围
            '''

        sub方法 = '''
            语法格式
            re.sub(pattern, repl, string, count=0)
            pattern : 正则中的模式字符串.
            repl : 替换的字符串,也可为一个函数.
            string : 要被查找替换的原始字符串.
            count : 模式匹配后替换的最大次数,默认 0 表示替换所有的匹配.
            字符串替换,用于替换字符串中的匹配项
            ret = re.sub('\d', 'H', 'eva3egon4yuan4', 1)   将数字替换成'H',参数1表示只替换1个
            print(ret) -----> evaHegon4yuan4
            
            如果 repl是一个函数
            def func1(matched):
                v=int(matched.group('values'))
                return str(v*2)
            strs="ab24cd67"
            print(re.sub(r'(?P<values>\d+)',func1,strs)) -----> ab48cd134
            '''

        subn方法 = '''
            ret = re.subn('\d', 'H', 'eva3egon4yuan4') 将数字替换成'H',返回元组(替换的结果,替换了多少次)
            '''

        finditer方法 = '''
            在字符串中找到正则表达式所匹配的所有子串,并把它们作为一个迭代器返回
            ret = re.finditer('\d', 'ds3sy4784a')   #finditer返回一个存放匹配结果的迭代器
            print(ret)  # <callable_iterator object at 0x10195f940>
            print(next(ret).group())  #查看第一个结果
            print(next(ret).group())  #查看第二个结果
            print([i.group() for i in ret])  #查看剩余的左右结果
            '''

        零宽断言 = '''
            str = 'aaa111aaa , bbb222&, 333ccc'
            re.compile('\d+(?=[a-z]+)').findall(str)          # 前向界定 (?=exp) 找出连续的数字并且最后一个数字跟着至少一个a-z ['111', '333']
            re.compile(r"\d+(?![a-z]+)").findall(str)         # 前向否定界定 (?!exp)  找出连续数字,且最后一个数字后不能跟a-z  ['11', '222', '33']
            re.compile(r"(?<=[a-z])\d+").findall(str)         # 反向界定 (?<=exp) 逆序环视 找出连续的数字,且第一个数字前面是a-z  ['111', '222']
            re.compile(r"(?<![a-z])\d+").findall(str)         # 反向否定界定 (?<!exp) 否定逆序环视  找出连续的数字,且第一个数字前不能是a-z  ['11', '22', '333']
            re.compile(r"(?:\d+)").findall(str)               # 无捕获的匹配 (?:exp)
            s= 'Tom:9527 , Sharry:0003 '
            re.match( r'(?P<name>\w+):(?P<num>\d+)' , s).group(0)   # 捕获组 <num>第二个标签变量[9527] 获取 group("num") 等同 group(2)[9527], group(0)全部[Tom:9527]
            '''

        例子 = '''
            re.findall(r'a[be]c','123abc456eaec789')         # 返回匹配对象列表 ['abc', 'aec']
            re.findall("(.)12[34](..)",a)                    # 取出匹配括号中内容   a='qedqwe123dsf'
            re.search("(.)123",a ).group(1)                  # 搜索匹配的取第1个标签
            re.match("^(1|2) *(.*) *abc$", str).group(2)     # 取第二个标签
            re.match("^(1|2) *(.*) *abc$", str).groups()     # 取所有标签
            re.sub('[abc]','A','alex')                       # 替换
            for i in re.finditer(r'\d+',s):                  # 迭代
                print i.group(),i.span()                     #
            '''

    def functools模块():

        partial方法 = '''
            生成一个固定参数的新函数,偏函数.接收一个函数,一些该函数的参数.
            partial 对特定的参数赋值,返回了一个新的可调用对象.新的可调用对象,仍然需要指定未被赋值的参数来调用.
            def spam(a,b,c,d):
                print(a,b,c,d)
                
            from functools import partial
            s1=partial(spam,1,2)
            s1(3,4) -----> 1 2 3 4
            s1(6,7) -----> 1 2 6 7
            s2=partial(spam,1,2,d=4)
            s2(3) -----> 1 2 3 4
            应用:
            列表的sort方法可以接受一个函数用来排序,但该函数只接受一个参数.如果根据另一个参数来排序.
            import math
            points=[(1,2),(3,4),(5,6),(7,8),(9,10)]
            def distance(p1,p2):
                x1,y1=p1
                x2,y2=p2
                return math.hypot(x2-x1,y2-y1)
            
            pt=(4,3)
            func=partial(distance,pt)
            points.sort(key=func)   # 也可以直接points.sort(key=partial(distanc,pt))
            print(points) -----> [(3, 4), (1, 2), (5, 6), (7, 8), (9, 10)]
            '''

        wraps='''
            pass
            '''

    def fnmatch模块():

        fnmatch方法 = '''
        '''

        fnamtchcase方法 = '''
        '''

    def heapq模块():
        '''
            堆是一种特殊的数据结构,它的通常的表示是它的根结点的值最大或者是最小.
            堆最重要的特性就是heap[0],总是最小的元素.
            可以接收一个可哈希的序列,以序列的第一元素作为关键字去比较,如果序列的第一个元素相同,就以第二个元素作为关键字去比较.以此类推
            '''

        list1 = [{'name':'a','price':2},{'name':'b','price':8},{'name':'a','price':1},{'name':'a','price':22},{'name':'a','price':32}]
        heap = [2, 4, 3, 5, 7, 8, 9, 6]

        nlargest方法 = '''
            从堆中找出最大的N个数,接收一个n值,表示想要获取值得个数,接收一个可迭代对象,接收一个函数key,用于筛选数据,用列表元素的某个属性和函数作为关键字.返回一个结果集 list
            heapq.nlargest(2,list1,key=lambda x:x['price'])
            '''

        nsmallest方法 = '''
            从堆中找出最小的N个数,接收一个n值,表示想要获取值得个数,接收一个可迭代对象,接收一个函数key,用于筛选数据,用列表元素的某个属性和函数作为关键字.返回一个结果集 list
            heapq.nsmallest(2,list1,key=lambda x:x['price'])
            '''

        heapify方法 = '''
            将列表转换为堆,接收的对象必须是列表.
            heapq.heapify(heap)  list里面的元素不能是不可哈希的,也就是说dict 不能作为列表的元素. 被heapify转化过的列表,不是有序的,但索引是0的位置的元素是最小的.
            '''

        heappop方法 = '''
            将堆的第一个元素(最小的)删除,并返回其值,第二小的元素取而代之.不支持key的方式指定函数.
            heapq.heappop(heap)
            '''

        heappush方法 = '''
            向list2里面添加一个值
            heapq.heappush(lheap, 66)
            '''

        heapreplace方法 = '''
            删除最小元素值,并返回最小的值,再添加新的元素值,相当于先heappop,再heappush.
            heapq.heapreplace(heap, 11) 返回2 ,而且添加的值并不是有序.------>heap = [3, 4, 8, 5, 7, 11, 9, 6]
            '''

        heappushpop方法 = '''
            如果添加元素值大于堆的第一个元素值(最小元素)对比,就删除第一个元素值(最小元素),然后添加新的元素值,如果添加元素值小于堆的第一个元素值,则不更改堆,只返回添加的元素.
            heapq.heappushpop(heap,10)    返回2,添加10
            heapq.heappushpop(heap,1)     只返回1
            '''

        merge方法 = '''
            将多个堆合或者列表合并
            heapq.merge(...)   返回的是一个生成器合并对象
            可以将多个有序的序列合并,返回新的有序的整个序列.要求输入的序列是有序的.
            a=[1,4,8]
            b=[2,7,9]
            c=[0,3,4,5,6]
            for i in heapq.merge(a,b,c):print(i)  返回有序的0-9.
            
            将俩个有序的文件合并成一个.
            with open('file1') as f1,\
                 open('file2') as f2,\
                 open('file2','w') as f3:
                 for line in heapq.merge(f1,f2):
                    f3.write(line)
            '''

        heapq应用 = '''
            from heapq import *
            h = list()
            heappush(h, (5, 'a'))
            heappush(h, (7, 'b'))
            heappush(h, (1, 'c'))  第一个值,可以根据1,排序,再根据字母排序
            heappush(h, (3, 'd'))
            heappush(h, (1, 'd'))
            
            def heapsort(iterable):
                heap = list()
                for value in iterable:
                    heappush(heap, value)
                return [heappop(heap) for i in range(len(heap))]
            '''

    def operator模块():

        itemgetter方法 = '''
            通过字典的公共键对字典列表进行排序,通过调用itemgetter,传入一个或多个键,返回相应的值.
            list1 = [{'name':'lisi','id':1,'age':22},{'name':'lili','id':2,'age':22},{'name':'lina','id':3,'age':24},{'name':'nan','id':5,'age':33},{'name':'mimi','id':4,'age':20}]
            sorted(list1,key=itemgetter('id'))
            sorted(list1,key=itemgetter('age'))
            sorted(list1,key=itemgetter('age','id'))   itemgetter比lambda要快一些
            sorted(list1,key=lambda d:(d['age'],d['id']))
            以上操作同样适用于min,max函数.
            '''

        attrgetter方法 = '''
            对不支持比较操作的对象排序
            基本与 itemgetter类似,attrgetter可以获取类的实例化对象的属性来进行排序.
            '''

    def itertools模块():

        groupby方法 = '''
            对字典列表,以字典中某个键来分组,分组的前提是,相对于这个键的字典,在列表中是有序的.
            list1 = [{'name':'lisi','id':1,'age':22},{'name':'lili','id':2,'age':22},{'name':'lina','id':1,'age':20},{'name':'nan','id':2,'age':33},{'name':'mimi','id':4,'age':20}]
            from operator import itemgetter
            from itertools import groupby
            list1.sort(key=itemgetter('age'))     也可以用  list1.sort(key=lambda d:d['age'])
            groupby(list1,key=itemgetter('age'))  也可以用  groupby(list1,key=lambda d:d['age'])
            groupby返回的是一个迭代器.每次迭代返回一个值和一个子迭代器.子迭代器里面包含该组的全部成员.返回的是一个itertools.groupby对象,该对象里面是一个个元组.
            元组的第一个值是每个分组指定的键的值,本例中的键是age,第二个值是一个itertools._grouper对象,该对象是一个元组,里面包含该组的全部成员.
            for group_name,groups in  groupby(list1,key=itemgetter('age')):
                print(group_name)
                print(*groups)
            '''

        compress方法 = '''
            接收一个可迭代对象,以及一个布尔选择器,返回所有为真的迭代对象的元素,返回的是一个迭代器.
            把一个序列的筛选结果作用于另一个相关序列
            a=(i if i > 0 else 0 for i in [1,-1,2,-2])
            b=['a', 'b', 'v', 'd']
            from itertools import compress
            list(compress(b,a))  -----> ['a', 'v']
            '''

        warps方法 = '''
        '''

        islice方法 = '''
            可以实现对生成器切片.islice本身是一个迭代器,通过接收一个生成器对象,一个起始值,默认为0,一个结束值,步长,默认为1,来实现对生成器切片.
            原理是通过丢弃不需要的值来实现的.这样会消耗生成器的数据,也就是说,之前的数据无法再次访问.
            也可用于跳过指定个数的元素.
            def test(n):
                while n:
                    yield n
                    n+=1
                    
            from itertools import islice
            t=test(1)
            for x in islice(t,2,10):
                print(x)
            '''

        dropwhile方法 = '''
            丢弃跳过可迭代对象的前几个元素,dropwhile 接收一个布尔选择器函数,一个可迭代对象.布尔选择器返回true,就会丢弃元素,直到遇到第一个false,停止丢弃.
            一旦停止丢弃,就不会再次丢弃,即使在接下来的迭代中遇到true条件.
            from itertools import dropwhile
            with open('/etc/passwd') as f:
                for line in dropwhile(lambda line: line.startswith('#'),f):
                    print(line,end='')
            只会丢弃文件前几行以#开头的行、
            with open('/etc/passwd') as f:
                lines=(for line in f if line not startswith('#'))
                for line in lines:
                    print(line)
            这种方法的缺点是,是会遍历所有的行.
            '''

        chain方法 = '''
            可以把一组迭代对象串联起来,形成一个更大的迭代器,可以传入不同类型的迭代对象.
            a=[1,2,3]
            b=[4,5,6]
            from itertools import chain
            for x in chain(a,b):
                print(x)
            '''

    def random模块():
        '''用于随机数,随机选择,import random'''
        v = [1,2,3,4,5,6,7]

        choice方法 = '''
            随机取列表一个参数,传入的序列可以是任意序列.
            random.choice(v) 
            '''

        sample方法 = '''
            不重复抽取n个,返回的是一个列表无论传入的哪种序列
            random.sample(v,3)
            '''

        random方法 = '''
            返回0-1间的随机浮点数
            random.random()
            '''

        shuffle方法 = '''
            将序列原地随机打乱顺序,传入的必须是列表.
            random.shuffle(v)  修改序列无返回值
            '''

        randint方法 = '''
            返回指定范围内的随机整数
            random.randint(0,99)
            '''

        randrange方法 = '''
            随机整数范围
            random.randrange(6)
            '''

        uniform方法 = '''
            计算均匀分布值
            '''

        gauss方法 = '''
            计算正态分布值
            '''

    def time模块():

        基础 = '''
            表示时间的三种方式:
        　　时间戳:数字(计算机能认识的)
        　　格式化时间:t='2012-12-12'
        　　结构化时间:time.struct_time(tm_year=2017, tm_mon=8, tm_mday=8, tm_hour=8, tm_min=4, tm_sec=32, tm_wday=1, tm_yday=220, tm_isdst=0)
            
            时间符号:
            %y 两位数的年份表示(00-99)
            %Y 四位数的年份表示(000-9999)
            %m 月份(01-12)
            %d 月内中的一天(0-31)
            %H 24小时制小时数(0-23)
            %I 12小时制小时数(01-12)
            %M 分钟数(00=59)
            %S 秒(00-59)
            %a 本地简化星期名称
            %A 本地完整星期名称
            %b 本地简化的月份名称
            %B 本地完整的月份名称
            %c 本地相应的日期表示和时间表示
            %j 年内的一天(001-366)
            %p 本地A.M.或P.M.的等价符
            %U 一年中的星期数(00-53)星期天为星期的开始
            %w 星期(0-6),星期天为星期的开始
            %W 一年中的星期数(00-53)星期一为星期的开始
            %x 本地相应的日期表示  05/06/18
            %X 本地相应的时间表示  00:04:45
            %Z 当前时区的名称
            %% %号本身
            
            struct_time元组共有9个元素共九个元素:
            tm_year(年)	    比如2011
            tm_mon(月)	    1 - 12
            tm_mday(日)	    1 - 31
            tm_hour(时)	    0 - 23
            tm_min(分)	    0 - 59
            tm_sec(秒)	    0 - 60
            tm_wday(weekday)	    0 - 6(0表示周一)
            tm_yday(一年中的第几天)	1 - 366
            tm_isdst(是否是夏令时)	默认为0
            '''

        方法应用 = '''
            字符串时间无法直接转成时间戳,需要格式化时间在中间转换.
            字符串时间转结构化时间需要指定字符串的格式.
            time.time() #时间戳
            time.strftime('%Y-%m-%d') -----> '2018-05-05'   返回字符类型的时间格式
            time.localtime() -----> time.struct_time(tm_year=2018, tm_mon=5, tm_mday=6, tm_hour=0, tm_min=0, tm_sec=54, tm_wday=6, tm_yday=126, tm_isdst=0)  时间元组:localtime将一个时间戳转换为当前时区的struct_time返回元组类型的时间格式
            
            时间戳-------------->结构化时间
            time.gmtime(时间戳)    #UTC时间,与英国伦敦当地时间一致
            time.localtime(时间戳)
            
            结构化时间-------------->时间戳
            time.mktime(结构化时间)
            time.mktime(time.localtime(1500000000))
            
            结构化时间-------------->字符串时间
            time.strftime("格式定义","结构化时间")  结构化时间参数若不传,则现实当前时间
            time.strftime("%Y-%m-%d %X") -----> '2018-05-06 00:09:38'
            time.strftime("%Y-%m-%d",time.localtime(1500000000))
            
            字符串时间-------------->结构化时间
            time.strptime(时间字符串,字符串对应格式)
            time.strptime("2017-03-16","%Y-%m-%d") -----> time.struct_time(tm_year=2017, tm_mon=3, tm_mday=16, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=75, tm_isdst=-1)
            time.strptime("07/24/2017","%m/%d/%Y") -----> time.struct_time(tm_year=2017, tm_mon=7, tm_mday=24, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=205, tm_isdst=-1)
            
            结构化时间--------------> %a %b %d %H:%M:%S %Y串
            time.asctime(结构化时间) 如果不传参数,直接返回当前时间的格式化串
            time.asctime(time.localtime(1500000000)) -----> 'Fri Jul 14 10:40:00 2017'
            time.asctime() -----> 'Sun May  6 00:12:49 2018'
            
            时间戳--------------> %a %d %d %H:%M:%S %Y串
            time.ctime(时间戳)  如果不传参数,直接返回当前时间的格式化串
            time.ctime() -----> 'Sun May  6 00:13:39 2018'
            time.ctime(1500000000) -----> 'Fri Jul 14 10:40:00 2017' 
            
            例:
            true_time=time.mktime(time.strptime('2017-09-11 08:30:00','%Y-%m-%d %H:%M:%S'))
            time_now=time.mktime(time.strptime('2017-09-12 11:00:00','%Y-%m-%d %H:%M:%S'))
            dif_time=time_now-true_time
            struct_time=time.gmtime(dif_time)
            print('过去了%d年%d月%d天%d小时%d分钟%d秒'%(struct_time.tm_year-1970,struct_time.tm_mon-1,struct_time.tm_mday-1,struct_time.tm_hour, struct_time.tm_min,struct_time.tm_sec))
            '''

    def datatime模块():

        timedelta方法 = '''
            表示时间间隔,即两个时间点的间隔
            from datetime import timedelta
            可以接收浮点数,负数
            (self, days: float = ..., seconds: float = ..., microseconds: float = ...,
            milliseconds: float = ..., minutes: float = ..., hours: float = ...,
            weeks: float = ...)
            a=timedelta(days=2,hours=9.1,seconds=1.2) -----> datetime.timedelta(2, 32761, 200000)
    
            两个实例可以相加减
            b=timedelta(days=1,hours=2)
            c=a+b
            可以通过属性来取值
            c.days 表示时间间隔的天数
            c.seconds 表示时间间隔的秒数 
            c.total_seconds 表示时间间隔的总秒数
            没有hours属性,可以通过c.seconds/3600 来取值.
            '''

        datatime方法 = '''
            表示特定的日期时间.可以使用标准的数学运算.
            from datetime import datetime
            a=datetime(2012,9,23)
            a+timedelta(days=10) -----> datetime.datetime(2012, 10, 3, 0, 0)
            b=datetime(2012,12,25)
            c=b-a  -----> datetime.timedelta(93)
            c.days  -----> 93
            now=datetime.today() ----->      datetime.datetime(2018, 5, 2, 17, 52, 7, 953916)
            now 可以通过属性获取值
            now.time() -----> datetime.time(17, 53, 38, 954168)
            now.date() -----> datetime.date(2018, 5, 2)
            now.today() -----> datetime.datetime(2018, 5, 2, 17, 55, 35, 344058)
            now.time() -----> datetime.time(17, 53, 38, 954168)
            now.weekday() -----> 2
            now.minute -----> 53
            now.hour -----> 17
            now.day -----> 2
            now.month -----> 5
            now.second -----> 38
            now+timedelta(minutes=10) -----> datetime.datetime(2018, 5, 2, 18, 3, 38, 954168)
            
            将字符串转化为datetime对象
            text = '2018-05-02'
            y=datetime.strptime(text,'%Y-%m-%d')
            datetime.now() - y  -----> datetime.timedelta(0, 65619, 976767)
            
            将datetime对象转化为字符串
            z=datetime.now()
            datetime.strftime(z,"%Y-%m-%d %H:%M:%S") -----> '2018-05-02 18:18:31'
            '''

    def subprocess模块():
        '''subprocess通过子进程来执行外部指令,并通过input/output/error管道,获取子进程的执行的返回信息.该模块旨在替换几个较旧的模块和功能:'''

        函数参数列表 = '''
            subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, shell=False, timeout=None,check=False, universal_newlines=False)
            subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)
            subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)
            subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False, timeout=None)
            subprocess.getstatusoutput(cmd)
            subprocess.getoutput(cmd)
            参数详解:
            args: 用于加载该进程的参数,这可能是一个列表或一个字符串
            shell: 如果shell为True,那么指定的命令将通过shell执行.如果我们需要访问某些shell的特性,如管道、文件名通配符、环境变量扩展功能,这将是非常有用的.
            check: 如果check参数的值是True,且执行命令的进程以非0状态码退出,则会抛出一个CalledProcessError的异常,且该异常对象会包含 参数、退出状态码、以及stdout和stder
            stdout, stderr
            input: 该参数是传递给Popen.communicate(),通常该参数的值必须是一个字节序列,如果universal_newlines=True,则其值应该是一个字符串
            universal_newlines:该参数影响的是输入与输出的数据格式,比如它的值默认为False,此时stdout和stderr的输出是字节序列,当该参数的值设置为True时,stdout和stderr的输出是字符串.
            
            subprocess.CompletedProcess类介绍
            subprocess.run()函数是Python3 .5中新增的一个高级函数,其返回值是一个subprocess.CompletedPorcess类的实例,
            subprocess.completedPorcess类也是Python3.5中才存在的.表示的是一个已结束进程的状态信息,
            所包含的属性如下:
            args: 用于加载该进程的参数,这可能是一个列表或一个字符串
            returncode: 子进程的退出状态码.通常情况下,退出状态码为0则表示进程成功运行；一个负值 - N表示这个子进程被信号N终止了
            stdout: 从子进程捕获的stdout.默认是一个字节序列,如果run()函数被调用时指定universal_newlines = True,则该属性值是一个字符串.如果run()函数被调用时指定stderr = subprocess.STDOUT,那么stdout和stderr将会被整合到这一个属性中,且stderr将会为None
            stderr: 从子进程捕获的stderr.它的值与stdout一样,是一个字节序列或一个字符串.如果stderr灭有被捕获的话,它的值就为None
            check_returncode(): 如果returncode是一个非0值,则该方法会抛出一个CalledProcessError异常
            '''

        run方法 = '''
            Python 3.5中新增的函数.执行指定的命令,等待命令执行完成后返回一个包含执行结果的CompletedProcess类的实例.
            官方文档中提倡通过subprocess.run()函数替代其他函数来使用subproccess模块的功能.
            run()函数默认不会捕获命令执行结果的正常输出和错误输出,如果我们向获取这些内容需要传递subprocess.PIPE,然后可以通过返回的CompletedProcess类实例的stdout和stderr属性或捕获相应的内容.
            obj=subprocess.run("ping 127.0.0.1",shell=True,stdout=subprocess.PIPE)  # 如果不指定 输出,默认直接显示.
            obj -----> CompletedProcess(args='ping 127.0.0.1', returncode=0)
            obj.stdout          # 获取执行的结果是bytes类型的.
            '''

        call方法 = '''
            call()和check_call()函数返回的是命令执行的状态码,而不是CompletedProcess类实例,所以对于它们而言,stdout和stderr不适合赋值为subprocess.PIPE.
            subprocess.call():执行命令,并返回执行状态,其中shell参数为False时,命令需要通过列表的方式传入,当shell为True时,支持命令以字符串的形式传入.
            subprocess.call('ls',shell=True)  执行命令,返回的是状态码.
            '''

        check_call方法 = '''
            执行命令,返回状态码.
            和 call 方法一样,两者唯一的区别在于返回值.执行成功,都返回 0；执行失败,check_call 将raise出来一个CalledProcessError
            '''

        getoutput方法 = '''
            check_output()函数默认就会返回命令执行结果,所以不用设置stdout的值,如果我们希望在结果中捕获错误信息,可以执行stderr=subprocess.STDOUT.
            以字符串的形式返回执行结果,错误或者正确都会返回,命令本身不会报错
            subprocess.getoutput('fdsfs') -----> '/bin/sh: fdsfs: command not found'
            '''

        getstatusoutput方法 = '''
            返回包含执行结果状态码和输出信息的元组.
            subprocess.getstatusoutput('dsfdsf') -----> (127, '/bin/sh: dsfdsf: command not found')
            '''

        Popen方法 = '''
            直接处理管道
            函数call(), check_call() 和 check_output() 都是Popen类的包装器.想要更个性化的需求,就要使用Popen类,该类生成的对象用来代表子进程.
            直接使用Popen会对如何运行命令以及如何处理其输入输出有更多控制.如通过为stdin, stdout和stderr传递不同的参数.
            要将一个进程的执行输出作为另一个进程的输入.
            如果要先进到输入环境,再执行一系列的指令.就需要用suprocess.Popen()方法.
            Popen对象创建后,主程序不会自动等待子进程完成.我们必须调用对象的wait()方法,父进程才会等待 (也就是阻塞block),
            该方法有以下参数:
            args:shell命令,可以是字符串,或者序列类型,如list,tuple.
            bufsize:指定缓存策略,0表示不缓冲,1表示行缓冲,其他大于1的数字表示缓冲区大小,负数 表示使用系统默认缓冲策略.
            preexec_fn: 用于指定一个将在子进程运行之前被调用的可执行对象,只在Unix平台下有效.
            stdin,stdout,stderr:分别表示程序的标准输入,标准输出及标准错误
            shell:当shell为True时,支持命令以字符串的形式传入.指定的命令将通过shell执行.
            cwd:用于设置子进程的当前目录
            env:用于指定子进程的环境变量.如果env=None,则默认从父进程继承环境变量
            例1:
            subprocess.Popen("ls -l",shell=True)    # 直接执行命令输出到屏幕
            obj=subprocess.Popen('echo "Stdout"',stdout=subprocess.PIPE,shell=True)    # 不输出到屏幕,输出到变量
            stdout = obj.communicate() -----> (b'Stdout\n', None)    # communicate()提交命令,返回标准输出和标准错误输出,如果stdout不是默认值,需要使用communicate提交
            
            obj=subprocess.Popen('ls',stdout=subprocess.PIPE,shell=True,cwd='/home')
            obj.stdout.read()
            
            f = open("/home/t.log",'w+')
            subprocess.Popen("ls -l",shell=True,stdout=f)   # 将结果输出到文件
            
            在communicat之前可以进行交互输入
            obj=subprocess.Popen('read n',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            obj.stdin.write('abc'.encode('utf-8'))  # 输入的内容要求是bytes类型的,返回输入内容的长度.
            obj.communicate()   # 提交命令
            
            obj=subprocess.Popen("ping 127.0.0.1 -t ",shell=True)
            print('wait')   # 父进程在开启子进程之后并没有等待obj的完成,而是直接运行print
            obj.wait()      # 父进程在开启子进程之后并等待obj的完成后,再运行print.
            
            例2:将一个子进程的输出,作为另一个子进程的输入
            child1 = subprocess.Popen(["cat","/etc/passwd"], stdout=subprocess.PIPE,universal_newlines=True)
            child2 = subprocess.Popen(["grep","root"],stdin=child1.stdout, stdout=subprocess.PIPE,universal_newlines=True)
            out = child2.communicate()
            
            可以在父进程中对子进程进行其它操作
            obj.poll()      # 用于检查子进程(命令)是否已经执行结束,没结束返回None,结束后返回状态码.
            obj.wait(timeout=None)  # 等待子进程结束,并返回状态码；如果在timeout指定的秒数之后进程还没有结束,将会抛出一个TimeoutExpired异常.
            obj.kill()      # 杀死该子进程
            obj.send_signal() # 向子进程发送信号
            obj.terminate() # 终止子进程
            obj.pid         # 子进程的PID
            obj.returncode  # 获取子进程状态码,0表示子进程结束,None未结束
            
            communicate()方法的说明:
            可选参数 input 是发送给子进程的数据,如没有数据发送给子进程,该参数是None.input参数的数据类型必须是字节串,如果universal_newlines参数值为True,则input参数的数据类型必须是字符串.
            该方法返回一个元组(stdout_data, stderr_data),这些数据将会是字节穿或字符串(如果universal_newlines的值为True).
            '''

        check_output方法 = '''
            如果当返回值为0时,直接返回输出结果,如果返回值不为0,直接抛出异常.
            '''

    def commands模块():

        方法 = '''
        commands模块在python3.x被subprocess取代,但是许多Linux 系统内置的python版本还是2.x,所以收入到本手册中.
        commands.getstatusoutput(cmd)         返回(status, output) status代表的shell命令的返回状态,如果成功的话是0；output是shell的返回的结果
        commands.getoutput(cmd)               仅仅返回输出结果
        commands.getstatus(file)              返回文件或目录的状态,返回ls -ld file的运行结果字符串,调用了getoutput.不建议使用此方法
        '''

    def json模块():
        '''
        序列化: 数据类型 -----> 字符串的过程
        使用序列化的场景: 数据从内存到文件 数据在网络上传输
        python中的序列化模块:
        json   通用的 支持的数据类型 list tuple dict
        pickle python中通用的 支持几乎所有python中的数据类型
        shelve python中使用的便捷的序列化工具
        '''

        '''Json模块提供了四个功能:dumps、dump、loads、load'''

        loads和dumps = '''
            import json
            dic = {'k1':'v1','k2':'v2','k3':'v3'}
            str_dic = json.dumps(dic)                                                               # 序列化:将一个字典转换成一个字符串
            print(type(str_dic),str_dic) -----> <class 'str'>   {"k3": "v3", "k1": "v1", "k2": "v2"}  # 注意，json转换完的字符串类型的字典中的字符串是由""表示的
            
            dic2 = json.loads(str_dic)                                                              # 反序列化:将一个字符串格式的字典转换成一个字典
            注意，要用json的loads功能处理的字符串类型的字典中的字符串必须由""表示
            print(type(dic2),dic2) -----> <class 'dict'>    {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
            
            list_dic = [1,['a','b','c'],3,{'k1':'v1','k2':'v2'}]
            str_dic = json.dumps(list_dic)                                                          # 也可以处理嵌套的数据类型
            print(type(str_dic),str_dic) -----> <class 'str'>   [1, ["a", "b", "c"], 3, {"k1": "v1", "k2": "v2"}]
            list_dic2 = json.loads(str_dic)
            print(type(list_dic2),list_dic2) -----> <class 'list'>  [1, ['a', 'b', 'c'], 3, {'k1': 'v1', 'k2': 'v2'}]
            '''

        load和dump = '''
            f = open('json_file','w')
            dic = {'k1':'v1','k2':'v2','k3':'v3'}
            json.dump(dic,f)        # dump方法接收一个文件句柄，直接将字典转换成json字符串写入文件
            f.close()
            
            f = open('json_file')
            dic2 = json.load(f)     # load方法接收一个文件句柄，直接将文件中的json字符串转换成数据结构返回
            f.close()
            print(type(dic2),dic2) -----> <class 'dict'>    {'k1':'v1','k2':'v2','k3':'v3'}
            '''

        ensure_ascii关键字参数 = '''
            在使用json.dumps时要注意,json.dumps或dump 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False:
            f = open('file','w')
            json.dump({'国籍':'中国'},f)            # 输出的会是中文的ascii 字符码，而不是真正的中文。
            json.dumps({'国籍':'中国'})             # 输出的会是中文的ascii 字符码，而不是真正的中文。
            json.dump({'国籍':'美国'},f,ensure_ascii=False)         # 想输出真正的中文需要指定ensure_ascii=False
            json.dumps({'国籍':'美国'},ensure_ascii=False)          # 想输出真正的中文需要指定ensure_ascii=False
            f.close()
            '''

        其他参数说明 = '''
            字符串表示的json对象
            Skipkeys:
                默认值是False，如果dict的keys内的数据不是python的基本类型(str,unicode,int,long,float,bool,None)，设置为False时，就会报TypeError的错误。
                此时设置成True，则会跳过这类key.
            ensure_ascii:
                当它为True的时候，所有非ASCII码字符显示为\uXXXX序列，只需在dump时将ensure_ascii设置为False即可，此时存入json的中文即可正常显示。
            indent:
                应该是一个非负的整型，如果是0就是顶格分行显示，如果为空就是一行最紧凑显示，否则会换行且按照indent的数值显示前面的空白分行显示，这样打印出来的json数据也叫pretty-printed json
            separators:
                分隔符，实际上是(item_separator, dict_separator)的一个元组，默认的就是(‘,’,’:’)；这表示dictionary内keys之间用“,”隔开，而KEY和value之间用“:”隔开。
            sort_keys:
                将数据根据keys的值进行排序。
            '''

        json的格式化输出 = '''
            import json
            data = {'username':['李华','二愣子'],'sex':'male','age':16}
            json_dic2 = json.dumps(data,sort_keys=True,indent=2,separators=(',',':'),ensure_ascii=False)
            print(json_dic2)
            -----> 
            {
              "age":16,
              "sex":"male",
              "username":[
                "李华",
                "二愣子"
              ]
            }
            按照字母排序，并美化输入格式。
            '''

    def pickle模块():
        '''
        pickle，用于python特有的类型 和 python的数据类型间进行转换
        pickle模块提供了四个功能:dumps、dump(序列化，存)、loads(反序列化，读)、load  (不仅可以序列化字典，列表...可以把python中任意的数据类型序列化)不能序列化迭代器。

        import pickle
        dic = {'k1':'v1','k2':'v2','k3':'v3'}
        str_dic = pickle.dumps(dic)
        print(str_dic) -----> 一串二进制内容

        dic2 = pickle.loads(str_dic)
        print(dic2) -----> {'k1':'v1','k2':'v2','k3':'v3'}

        import time
        struct_time  = time.localtime(1000000000)
        f = open('pickle_file','wb')
        pickle.dump(struct_time,f)
        f.close()

        f = open('pickle_file','rb')
        struct_time2 = pickle.load(f)
        print(struct_time2.tm_year)
        json是一种所有的语言都可以识别的数据结构。
        序列化其他的数据类型，并对这个数据进行反序列化，使用pickle。
        '''

    def shelve模块():
        '''详见网站 http://www.cnblogs.com/Eva-J/articles/7228075.html#_label9'''

    def hashlib模块():
        '''
        算法介绍
        Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
        摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
        hashlib模块  摘要算法  --->  单向不可逆

        import hashlib
        md5 = hashlib.md5()     # 实例化一个md5摘要算法的对象
        md5.update('how to use md5 in python hashlib?'.encode('utf-8'))     # 使用md5算法的对象来操作字符串
        md5.hexdigest() -----> 'd26a53750bc40b38b65a520292f69306'

        如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：

        md5 = hashlib.md5()
        md5.update('how to use md5 in '.encode('utf-8'))
        md5.update('python hashlib?'.encode('utf-8'))
        md5.hexdigest()
        MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：

        import hashlib

        sha1 = hashlib.sha1()
        sha1.update('how to use sha1 in ')
        sha1.update('python hashlib?')
        sha1.hexdigest() -----> 'd26a53750bc40b38b65a520292f69306'
        SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法越慢，而且摘要长度更长。

        要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：
        在创建对象的时候进行加盐。
        hashlib.md5("salt".encode("utf8"))
        经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。
        但是如果有两个用户都使用了相同的简单口令比如123456，在数据库中，将存储两条相同的MD5值，这说明这两个用户的口令是一样的。有没有办法让使用相同口令的用户存储不同的MD5呢？
        如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。
        摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。
        '''

    def configparse模块():
        '''详见: http://www.cnblogs.com/Eva-J/articles/7228075.html#_label14'''

    def logging模块():
        '''
        日志等级:使用范围
        FATAL:致命错误
        CRITICAL:特别糟糕的事情，如内存耗尽、磁盘空间为空，一般很少使用
        ERROR:发生错误时，如IO操作失败或者连接问题
        WARNING:发生很重要的事件，但是并不是错误时，如用户登录密码错误
        INFO:处理请求或者状态变化等日常事务
        DEBUG:调试过程中使用DEBUG等级，如算法中每个循环的中间状态
        '''

        函数式简单配置 = '''
            import logging
            logging.debug('debug message')
            logging.info('info message')
            logging.warning('warning message')
            logging.error('error message')
            logging.critical('critical message')
            默认logging模块将日志打印到了标准输出中，且只显示大于等于WARNING级别的日志.
            默认的日志级别设置为WARNING(日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG)，默认的日志格式为日志级别:Logger名称:用户输出消息。
    
            灵活配置日志级别，日志格式，输出位置:
            
            import logging
            logging.basicConfig(level=logging.DEBUG,
                                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                                datefmt='%a, %d %b %Y %H:%M:%S',
                                filename='/tmp/test.log',
                                filemode='w')
            logging.debug('debug message')
            logging.info('info message')
            logging.warning('warning message')
            logging.error('error message')
            logging.critical('critical message')
    
            配置参数:
            logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有:
            filename:用指定的文件名创建FiledHandler，这样日志会被存储在指定的文件中。
            filemode:文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
            format:指定handler使用的日志显示格式。
            datefmt:指定日期时间格式。
            level:设置rootlogger(后边会讲解具体概念)的日志级别
            stream:用指定的stream创建StreamHandler。
                可以指定输出到sys.stderr,sys.stdout或者文件(f=open(‘test.log’,’w’))，默认为sys.stderr。
                若同时列出了filename和stream两个参数，则stream参数会被忽略。
                
            format参数中可能用到的格式化串:
            %(name)s Logger的名字
            %(levelno)s 数字形式的日志级别
            %(levelname)s 文本形式的日志级别
            %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
            %(filename)s 调用日志输出函数的模块的文件名
            %(module)s 调用日志输出函数的模块名
            %(funcName)s 调用日志输出函数的函数名
            %(lineno)d 调用日志输出函数的语句所在的代码行
            %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
            %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
            %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
            %(thread)d 线程ID。可能没有
            %(threadName)s 线程名。可能没有
            %(process)d 进程ID。可能没有
            %(message)s用户输出的消息
            '''

        logger对象配置='''
            logging中包含的handler主要有如下几种:
            StreamHandler:      logging.StreamHandler；                  日志输出到流，可以是sys.stderr，sys.stdout或者文件
            FileHandler:        logging.FileHandler；                    日志输出到文件
            BaseRotatingHandler:logging.handlers.BaseRotatingHandler；   基本的日志回滚方式
            RotatingHandler:    logging.handlers.RotatingHandler；       日志回滚方式，支持日志文件最大数量和日志文件回滚
            TimeRotatingHandler:logging.handlers.TimeRotatingHandler；   日志回滚方式，在一定时间区域内回滚日志文件
            SocketHandler:      logging.handlers.SocketHandler；         远程输出日志到TCP/IP sockets
            DatagramHandler:    logging.handlers.DatagramHandler；       远程输出日志到UDP sockets
            SMTPHandler:        logging.handlers.SMTPHandler；           远程输出日志到邮件地址
            SysLogHandler:      logging.handlers.SysLogHandler；         日志输出到syslog
            NTEventLogHandler:  logging.handlers.NTEventLogHandler；     远程输出日志到Windows NT/2000/XP的事件日志
            MemoryHandler:      logging.handlers.MemoryHandler；         日志输出到内存中的指定buffer
            HTTPHandler:        logging.handlers.HTTPHandler；           通过"GET"或者"POST"远程输出到HTTP服务器
            
            SetLevel 日志级别
            Logging有如下级别: DEBUG，INFO，WARNING，ERROR，CRITICAL
            默认级别是WARNING，logging模块只会输出指定level以上的log。
            这样的好处, 就是在项目开发时debug用的log，在产品release阶段不用一一注释，只需要调整logger的级别就可以了。
            
            import logging
            logger = logging.getLogger(name=None)                       # 获取logger实例，如果参数为空则返回root logger
            logger.setLevel(logging.DEBUG)                              # 指定日志的最低输出级别，默认为WARN级别
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')       # 指定logger输出格式
            
            fh = logging.FileHandler('test.log',encoding='utf-8')       # 创建一个handler，用于写入日志文件
            fh.setLevel(logging.DEBUG)                                  # 单对文件流设置某个级别。
            fh.setFormatter(formatter)                                  # 可以通过setFormatter指定输出格式
            
            
            ch = logging.StreamHandler()                                # 再创建一个handler，用于输出到控制台
            ch.setLevel(logging.DEBUG)                                  
            ch.setFormatter(formatter)
            ch.formatter = formatter                                    # 也可以直接给formatter赋值
            
            logger.addHandler(fh)                                       # logger对象可以添加多个fh和ch 日志处理器对象
            logger.addHandler(ch)
            
            logger.debug('logger debug message')
            logger.info('logger info message')
            logger.warning('logger warning message')
            logger.error('logger error message')
            logger.critical('logger critical message')
            
            logger.removeHandler(fh)                                    # 移除一些日志处理器
            
            logging库提供了多个组件:Logger、Handler、Filter、Formatter。
            Logger对象提供应用程序可直接使用的接口，Handler发送日志到适当的目的地，Filter提供了过滤日志信息的方法，Formatter指定日志显示格式。
            另外，可以通过:logger.setLevel(logging.Debug)设置级别,当然，也可以通过
            
            除了这些基本用法，还有一些常见的技巧
            格式化输出日志
            service_name = "Booking"
            logger.error('%s service is down!' % service_name)              # 使用python自带的字符串格式化，不推荐
            logger.error('%s service is down!', service_name)               # 使用logger的格式化，推荐
            logger.error('%s service is %s!', service_name, 'down')         # 多参数格式化
            logger.error('{} service is {}'.format(service_name, 'down'))   # 使用format函数，推荐
 
            记录异常信息

            使用logging模块记录异常信息时，不需要传入该异常对象，直接调用logger.error() 或者 logger.exception()就可以将当前异常记录下来。
            记录异常信息
 
            try:
                1 / 0
            except:
                logger.exception('this is an exception message')            # 等同于error级别，但是会额外记录当前抛出的异常堆栈信息
            
            '''

        logging的配置文件 = '''
            通过文件配置logging
            参考官方文档。https://docs.python.org/3.6/library/logging.config.html
            # logging.conf
            假设配置文件放在和模块相同的目录，代码中的调用如下。
            
            import os
            filepath = os.path.join(os.path.dirname(__file__), 'logging.conf')
            logging.config.fileConfig(filepath)
            return logging.getLogger()
            '''

        多模块使用logging = '''
            GetLogger()方法,这是最基本的入口，该方法参数可以为空，默认的logger名称是root，
            如果在同一个程序中一直都使用同名的logger，其实会拿到同一个实例，使用这个技巧就可以跨模块调用同样的logger来记录日志。
            可以通过日志名称来区分同一程序的不同模块，比如这个例子。
            logger = logging.getLogger("App.UI")
            logger = logging.getLogger("App.Service")
            更多例子详见:
            https://www.jianshu.com/p/feb86c06c4f4
            http://python.jobbole.com/86887/
            https://www.cnblogs.com/liujiacai/p/7804848.html
            https://blog.csdn.net/orangleliu/article/details/53896441
            https://blog.csdn.net/chosen0ne/article/details/7319306
            '''

    def copy模块():
        '''pass'''

    def tempfile模块():
        pass

    def virtualenv模块():
        pass

    def inspect模块():
        '''https://blog.csdn.net/freeking101/article/details/52458647'''

    def 模块和包():
        '''
        模块就是一个py文件
        所谓的模块导入 就是执行了这个文件而已
        import加载的模块分为四个通用类别：　
        　　1 使用python编写的代码（.py文件）
        　　2 已被编译为共享库或DLL的C或C++扩展
        　　3 包好一组模块的包
        　　4 使用C编写并链接到python解释器的内置模块

        import
        模块可以包含可执行的语句和函数的定义.
        它们只在模块名第一次遇到导入import语句时才执行.
        import语句是可以在程序中的任意位置使用的,且针对同一个模块可以import多次.
        第一次导入后就将模块名加载到内存了，后续的import语句仅是对已经加载大内存中的模块对象增加了一次引用，不会重新执行模块内的语句

        我们可以从sys.modules中找到当前已经加载的模块。
        sys.modules是一个字典，内部包含模块名与模块对象的映射，该字典决定了导入模块时是否需要重新导入。

        每个模块都是一个独立的名称空间
        把这个模块的名称空间当做全局名称空间，这样我们在编写自己的模块时，就不用担心我们定义在自己模块中全局变量会在被导入时，与使用者的全局变量冲突

        首次导入模块my_module时会做三件事：
        1.为源文件(my_module模块)创建新的名称空间，在my_module中定义的函数和方法若是使用到了global时访问的就是这个名称空间。
        2.在新创建的命名空间中执行模块中包含的代码事实上函数定义也是“被执行”的语句，模块级别函数定义的执行将函数名放入模块全局名称空间表，用globals()可以查看
        3.创建名字my_module来引用该命名空间

        为模块名起别名
        import my_module as sm

        例:
        def sqlparse():
            print('from mysql sqlparse')

        def sqlparse():
            print('from oracle sqlparse')

        db_type=input('>>: ')
        if db_type == 'mysql':
            import mysql as db
        elif db_type == 'oracle':
            import oracle as db

        例:
        为已经导入的模块起别名的方式编写可扩展的代码.
        假设有两个模块xmlreader.py和csvreader.py，它们都定义了函数read_data(filename):用来从文件中读取一些数据，但采用不同的输入格式。
        可以编写代码来选择性地挑选读取模块，例如
        if file_format == 'xml':
             import xmlreader as reader
        elif file_format == 'csv':
             import csvreader as reader
        data=reader.read_date(filename)

        在一行导入多个模块
        import sys,os,re
        from ... import...

        对比import my_module，会将源文件的名称空间'my_module'带到当前名称空间中，使用时必须是my_module.名字的方式
        而from 语句相当于import，也会创建新的名称空间，但是将my_module中的名字直接导入到当前的名称空间中，在当前名称空间中，直接使用名字就可以了、
        from my_module import read1,read2
        这样在当前位置直接使用read1和read2就好了，执行时，仍然以my_module.py文件全局名称空间

        如果当前有重名read1或者read2，那么会有覆盖效果。
        python中的变量赋值不是一种存储操作，而只是一种绑定关系

        from my_module import read1 as read
        from my_module import (read1,
                             read2,
                             money)

        from my_module import *     # 把my_module中所有的不是以下划线(_)开头的名字都导入到当前位置
        from my_module import *     # 将模块my_module中所有的名字都导入到当前名称空间

        在my_module.py中新增一行
        __all__=['money','read1']   # 这样在另外一个文件中用from my_module import *就这能导入列表中规定的两个名字
        如果my_module.py中的名字前加_,即_money，则from my_module import *,则_money不能被导入
        每个模块只被导入一次,放入字典sys.modules中，如果你改变了模块的内容，你必须重启程序，python不支持重新加载或卸载之前导入的模块，

        我们可以通过模块的全局变量__name__来查看模块名：
        当做脚本运行：
        __name__ 等于'__main__'

        当做模块导入：
        __name__= 模块名

        模块搜索路径
        python解释器在启动时会自动加载一些模块，可以使用sys.modules查看
        在第一次导入某个模块时（比如my_module），会先检查该模块是否已经被加载到内存中（当前执行文件的名称空间对应的内存），如果有则直接引用
        如果没有，解释器则会查找同名的内建模块，如果还没有找到就从sys.path给出的目录列表中依次寻找my_module.py文件。
        模块的查找顺序是：内存中已经加载的模块->内置模块->sys.path路径中包含的模块

        sys.path的初始化的值来自于：
        需要特别注意的是：我们自定义的模块名不应该与系统内置模块重名。
        在初始化后，python程序可以修改sys.path,路径放到前面的优先于标准库被加载。
        import sys
        sys.path.append('/a/b/c/d')
        sys.path.insert(0,'/x/y/z') #排在前的目录，优先被搜索
        注意：搜索时按照sys.path中从左到右的顺序查找，位于前的优先被查找。
        sys.path中还可能包含.zip归档文件和.egg文件，python会把.zip归档文件当成一个目录去处理。

        import sys
        sys.path.append('module.zip')
        import foo,bar

        #也可以使用zip中目录结构的具体位置
        sys.path.append('module.zip/lib/python')

        #windows下的路径不加r开头，会语法错误
        sys.path.insert(0,r'C:\Users\Administrator\PycharmProjects\a')
        至于.egg文件是由setuptools创建的包，这是按照第三方python库和扩展时使用的一种常见格式，.egg文件实际上只是添加了额外元数据(如版本号，依赖项等)的.zip文件。
        只能从.zip文件中导入.py，.pyc等文件。使用C编写的共享库和扩展块无法直接从.zip文件中加载（此时setuptools等打包系统有时能提供一种规避方法），且从.zip中加载文件不会创建.pyc或者.pyo文件，因此一定要事先创建他们，来避免加载模块是性能下降。
        官网链接：https://docs.python.org/3/tutorial/modules.html#the-module-search-path
        搜索路径：
        当一个命名为my_module的模块被导入时
            解释器首先会从内建模块中寻找该名字
            找不到，则去sys.path中找该名字

        sys.path从以下位置初始化
        执行文件所在的当前目录
        在支持软连接的文件系统中，执行脚本所在的目录是在软连接之后被计算的。
        包含软连接的目录不会被添加到模块的搜索路径中
        在初始化后，我们也可以在python程序中修改sys.path,执行文件所在的路径默认是sys.path的第一个目录。在所有标准库路径的前面。
        当前目录是优先于标准库目录的
        https://docs.python.org/3/library/compileall.html#module-compileall
        '''

def 生产工具():

    批量修改目录下的文件 = '''
        import os
        BASE_PATH = '/usr/share/zabbix'
        sec = 'zabbix.php'
        des = 'zk.php'

        def replace(path):
            path = os.path.abspath(path)
            file_list = os.listdir(path)
            for file_dir in file_list:
                file_path = os.path.join(path, file_dir)
                if os.path.isfile(file_path):
                    if file_path.endswith('.php') or \
                            file_path.endswith('.js') or \
                            file_path.endswith('.html') or \
                            file_path.endswith('.css'):
                        cmd = "sed -i 's/{s}/{d}/g' {file}".format(s=sec, d=des, file=file_path)
                        os.popen(cmd)
                elif os.path.isdir(file_path):
                    replace(file_path)

        replace(BASE_PATH)
        '''

    调用zabbix_api = '''
        pip3 install pyzabbix
        from pyzabbix import ZabbixAPI
        zapi = ZabbixAPI("http://10.10.10.254:80/zabbix")   ##完整的url路径如下"http://10.10.10.254:80/zabbix/api_jsonrpc.php"
        zapi.login("admin", "zabbix")
        print("Connected to Zabbix API Version %s" % zapi.api_version())
        zapi.history.get(output="extend", history=0, itemids=item_id, sortfield="itemid", sortorder="DESC",limit=10080):  #获取历史数据
        zapi.item.get(output="extend",hostids='hostid'):   #通过主机id获取监控项
        zapi.host.get(output="extend"):   #获取主机,循环得到主机的监控项
        '''

    写入execl = '''
        style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')  # 格式1
        style1 = xlwt.easyxf()  # 格式2
        wb = xlwt.Workbook()    # 一个新文件
        ws = wb.add_sheet('ASR引擎服务器监控信息周统计表') # 表的标题
        ws.write(x,y,'items',style)     # 根据坐标写入表格 从0开始,x表示行,y表示列.最后表示写入的格式
        ws.write(0,0,'项目名',style0)
        ws.write(0,1,'平均值',style0)
        excel_name='file_name.xls'      # 指定文件名
        wb.save(excel_name)             # 报存文件
        '''

def 题目详解():

    def 字符串格式化精讲():
        '''官方文档地址 https://docs.python.org/3/library/string.html 以下是官方文档的内容.'''
        '''格式字符串包含由花括号包裹的 {替换字段}.任何不包含在花括号中的内容都将被视为普通字符串,并将其原样输出.
        如果输出中要包含花括号,则可以通过使用两对花括号来表示,{{str}}.
        格式化之前,转换字段会导致类型的强制转换.
        通常,格式化操作是通过对象本身的__format__()方法完成的.
        但是,在某些情况下,希望强制将某个类型格式化为字符串.在填充前先用对应的函数来处理参数.通过在调用之前将该值转换为字符串__format__().
        目前支持三种转换符:'!s'使用str()强转,'!r'使用repr(),'!a'使用ascii().
        例子:
        "Harold's a clever {0!s}"        # 在第一个参数上调用 str()
        "Bring out the holy {name!r}"    # 在第一个参数上调用 repr()
        "More {!a}"                      # 在第一个参数上调用 ascii()
        
        以下在字符串中花括号的写法.
        替换字段格式(replacement_field)      {[field_name] [!conversion] [:format_spec]}
        字段对象(field_name)                arg_name('.' attribute_name | '[' element_index ']')*
        位置名称(arg_name)                  [identifier | digit+]
        属性名(attribute_name)              identifier
        元素索引(element_index)             digit+ | index_string
        字符串索引(index_string)            <any source character except "]"> +
        转换符(conversion)                 "r" | "s" | "a"
        格式(format_spec)                  <described in the next section>
        field_name该字段指定要格式化其值的对象,是一个带属性的对象.并将其插入到输出中而不是替换字段中.
        field_name后面可以选择跟转换符!s或!r或!a,用对应的函数来处理.可以用:指定值得输出格式.
        字段对象(field_name)可以使用.来指定属性名.field_name.attribute_name 也可以用元素索引来指定  field_name[element_index]
        在field_name 本身是位置参数,可以是位置参数或关键字参数.类似于{1},{name} 这种.
        如果field_name是一个对象,attribute_name是field_name的一个属性,属于关键字参数.如果field_name是一个序列,使用索引值或字典的键来指定.
        arg_name不能在格式字符串中以字典的方式指定键(key:values),arg_name可以跟多个索引或属性表达式.field_name.name使用getattr()获取指定的属性,field_name[index] 使用__getitem__()查找索引.
        :format_spec,冒号format_spec表示输出的格式.
        举例:
        "First, thou shalt count to {0}"  # 引用第一个位置参数
        "Bring me a {}"                   # 隐式引用第一个位置参数
        "From {} to {}"                   # 从0到1,按顺序引用
        "My quest is {name}"              # 引用关键字参数'name'
        "Weight in tons {0.weight}"       # 引用第一个位置参数的'weight'属性
        "Units destroyed: {players[0]}"   # 引用关键字参数'players'的第一个元素.
        def func():pass
        func.x=1
        func.y=2
        '{a.x},{a.y}'.format(a=func)            -----> '1,2'
        {0.x},{0.y}'.format(func)               -----> '1,2'
        b={'x':1,'y':2}
        '{0[x]},{0[y]}'.format(b)               -----> '1,2'
        '{d[x]},{d[y]}'.format(d=b)             -----> '1,2'
        
        按位置访问参数:
        '{0}, {1}, {2}'.format('a', 'b', 'c')   -----> 'a, b, c'
        '{}, {}, {}'.format('a', 'b', 'c')      -----> 'a, b, c'
        '{2}, {1}, {0}'.format('a', 'b', 'c')   -----> 'c, b, a'
        '{2}, {1}, {0}'.format(*'abc')          -----> 'c, b, a'      # 解包参数序列
        '{0}{1}{0}'.format('abra', 'cad')       -----> 'abracadabra'   # 参数可以重复

        按名称访问参数:
        'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')  -----> 'Coordinates: 37.24N, -115.81W'
        coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
        'Coordinates: {latitude}, {longitude}'.format(**coord)                                  -----> 'Coordinates: 37.24N, -115.81W'

        访问参数的属性:
        c = 3-5j
        ('The complex number {0} is formed from the real part {0.real} and the imaginary part {0.imag}.').format(c)  -----> 'The complex number (3-5j) is formed from the real part 3.0 and the imaginary part -5.0.'
        
        class Point:
            def __init__(self, x, y):
                self.x, self.y = x, y
            def __str__(self):
                return 'Point({self.x}, {self.y})'.format(self=self)
        
        str(Point(4, 2)) -----> 'Point(4, 2)'

        访问参数的项目:
        coord = (3, 5)
        'X: {0[0]};  Y: {0[1]}'.format(coord)
        'X: 3;  Y: 5'
        
        替换%s和%r:
        "repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2') -----> "repr() shows quotes: 'test1'; str() doesn't: test2"
        
        对齐文本并指定宽度:
        '{:<30}'.format('left aligned')     -----> 'left aligned                  '
        '{:>30}'.format('right aligned')    -----> '                 right aligned'
        '{:^30}'.format('centered')         -----> '           centered           '
        '{:*^30}'.format('centered')        -----> '***********centered***********'  # 使用'*'作为填充字符
        
        更换%+f,%-f以及与指定的标志:% f
        '{:+f}; {:+f}'.format(3.14, -3.14)          -----> '+3.140000; -3.140000'  # 始终显示
        '{: f}; {: f}'.format(3.14, -3.14)          -----> ' 3.140000; -3.140000'  # 显示正数的空间
        '{:-f}; {:-f}'.format(3.14, -3.14)          -----> '3.140000; -3.140000'   # 只显示减号

        替换%x并将%o值转换为不同的基础:
        "int: {0:d}; hex: {0:x}; oct: {0:o}; bin: {0:b}".format(42)     -----> 'int: 42;  hex: 2a;  oct: 52;  bin: 101010'          # 格式也支持二进制数字
        "int: {0:d}; hex: {0:#x}; oct: {0:#o}; bin: {0:#b}".format(42)  -----> 'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'    # 以0x,0o或0b作为前缀

        使用逗号作为千位分隔符:
         '{:,}'.format(1234567890)          -----> '1,234,567,890'
        
        表示一个百分比:
        points = 19
        total = 22
        'Correct answers: {:.2%}'.format(points/total)      -----> 'Correct answers: 86.36%'

        使用特定于类型的格式:
        import datetime
        d = datetime.datetime(2010, 7, 4, 12, 15, 58)
        '{:%Y-%m-%d %H:%M:%S}'.format(d)                    -----> '2010-07-04 12:15:58'

        嵌套论据和更复杂的例子:
        for align, text in zip('<^>', ['left', 'center', 'right']):
            '{0:{fill}{align}16}'.format(text, fill=align, align=align)
            
        'left<<<<<<<<<<<<'
        '^^^^^center^^^^^'
        '>>>>>>>>>>>right'
        
        octets = [192, 168, 0, 1]
        '{:02X}{:02X}{:02X}{:02X}'.format(*octets)-----> 'C0A80001'
        int(_, 16)3232235521

        width = 5
        for num in range(5,12): 
            for base in 'dXob':
                print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
            print()

        5     5     5   101
        6     6     6   110
        7     7     7   111
        8     8    10  1000
        9     9    11  1001
       10     A    12  1010
       11     B    13  1011
        '''

    def 生成器相关():

        题一 = '''
            def demo():
                for i in range(4):
                    yield i

            g=demo()

            g1=(i for i in g)
            g2=(i for i in g1)

            print(list(g1))
            print(list(g2))
            
            返回[0,1,2,3]
            []
            解:
            g,g1,g2都是生成器,在不调用的时候都不执行,用list去强转g1的时候,就相当于执行了g1,当list再去强转g2的时候,g1已经执行完毕,g2取不到值,遂返回空.
            '''

        题二 = '''
            def add(n,i):
                return n+i

            def test():
                for i in range(4):
                    yield i

            g=test()
            for n in [1,3,10]:
                g=(add(n,i) for i in g)

            print(list(g))
            返回[30, 31, 32, 33]
            解:
            首先g=test(),g是一个生成器,for循环取反复的调用g,并重新赋值给g.
            第一次 for 循环结束后,g=(add(1,i) for i in test())  n指向了内存中值为1的地址
            第二次 for 循环结束后,g=(add(3,i) for i in (add(3,i) for i in test()))  n指向了内存中值为3的地址  
            第三次 for 循环结束后,g=(add(10,i) for i in (add(10,i) for i in (add(10,i) for i in test())))  n指向了内存中值为10的地址
            在用list强转时,执行了最后的g,  list((add(10,i) for i in (add(10,i) for i in (add(10,i) for i in test()))))
            从左到右,第一个add,第二个add,第三个add test() 依次是:
            i=0         10+20      10+10    10+0     0
            i=1         10+21      10+11    10+1     1
            i=2         10+22      10+12    10+2     2
            i=3         10+23      10+13    10+3     3
            所以返回  [30, 31, 32, 33]                      
            '''

    def 匿名函数相关():

        题一 = '''
            def mul():
                return [lambda x:x*i  for i in range(4)]
            print([m(2) for m in mul()])
            返回结果[6,6,6]
            解:
            lambda表达式中的变量,不是定义的时候去绑定,而是运行的时候去绑定.
            mul() 返回了一个列表,列表里面是4个lambda表达式,最后一个i 的值是3,当匿名函数被调用时i的值时3,所以返回结果[6,6,6]
            如何修改才能返回想要的结果呢？[0, 2, 4, 6]
            法一:
            return [lambda x,i=i:x*i  for i in range(4)]  通过给lambda传参的方式.
            法二:
            return (lambda x:x*i  for i in range(4))      通过返回一个生成器表达式.生成器只有调用__next__的时候才执行一次.
            '''

    def sorted相关():

        题一 = '''
        list1 = [7, -8, 5, 4, 0, -2, -5]
        要求1.正数在前负数在后 2.整数从小到大 3.负数从大到小
        sorted(list1,key=lambda x:(x<0,abs(x)))
        解:
        先明确两个知识点
        1、sorted 可以接收序列的元素为元组进行比较,以元组的第一个元素为比较依据,如果第一个元素相等,以第二个元素为依据.以此类推
        2、在数学运算中 int(True) = 1,int(False) = 0 ,在比较运算中  True > False
        lambda x:(x<0,abs(x)) 此匿名函数返回的是一个元组,第一个元素是False 或 True,第二个元素是绝对值.False在前面,以绝对值排序,True在后面,以绝对值排序.
        '''

    def globals_locals_dir_vars区别():

        globals函数 = '''
            函数会以字典类型返回当前位置的全部全局变量.globals不会有局部变量的值,如果你在def或class中定义了某个变量,在全局中式没有的,即使你执行了函数,除非使用global 参数声明.
            '''
        locals函数 = '''
            会以字典类型返回当前位置的全部局部变量. 获取执行本方法所在命名空间内的局部变量的字典
            '''
        vars函数 = '''
            返回对象object的属性和属性值的字典对象.
            '''
        dir函数 = '''
            不带参数时,默认查看全局空间内的属性,返回当前范围内的变量、方法和定义的类型列表;带参数时,返回参数的属性、方法列表.如果参数包含方法__dir__(),该方法将被调用.如果参数不包含__dir__(),该方法将最大限度地收集参数信息.
            '''
        区别 = '''
            在全局执行这三个函数时没有区别,print(globals() is locals() is vars()) ----> True
            在局部空间里执行vars()和local(),返回的结果是一样的,在任何地方执行globals() 返回的结果都和全局一样.
            一个类实例化与未实例化的var(对象) 是不一样的,此处待完善.
            dir 与其他三者的区别,dir 返回的是 一个列表,并且实例化之后的属性列表包含未实例化的所有属性.'''

    def Iterator和Iterable的区别():
        '''
        from collections import Iterable,Iterator
        判断是不是可以迭代,用Iterable
        isinstance([1,],Iterable) -----> True
        判断是不是迭代器,用Iterator
        isinstance((i for i in range(11)), Iterator) -----> True
        凡是可以for循环的,都是Iterable,都有 __iter__ 属性.
        凡是可以next()的,都是Iterator,都有  __iter__ __next__ 属性.
        '''

    def __repr__和__str__区别():
        pass

    def 类的题目():
        '''
        class Person:
            def __init__(self,name,age,sex):
                self.name = name
                self.age = age
                self.sex = sex

            def __hash__(self):
                return hash(self.name+self.sex)

            def __eq__(self, other):
                if self.name == other.name and self.sex == other.sex:return True


        p_lst = []
        for i in range(84):
            p_lst.append(Person('egon',i,'male'))

        print(p_lst)
        print(set(p_lst))
        '''

def 使用参考():

    def 去除序列中的重复元素保持元素顺序不变():

        法一 = '''   #序列中的元素必须是可哈希的,不变的. 
            def dedupe(items):
                seen = set()
                for item in items:
                    if item not in seen:
                        yield item
                        seen.add(item)
            '''

        法二 = '''
            sorted(set(ls), key=ls.index)
            '''

        法三 = '''
            以上两种方法均不能对不可哈希的元素排序,如字典列表
            def dedupe(items,key=None):
                seen = set()
                for item in items:
                    val = item if key is None else key(item)
                    if val not in seen:
                        yield item
                        seen.add(val)
            a=[{'x':1,'y':2},{'x':1,'y':3},{'x':1,'y':2},{'x':2,'y':4}]
            dedupe(a,key=lambda d:(d['x'],d['y']))  # 字典是不可哈希的,通过用字典的键来去重.       
            '''

    def 实现switch_case():

        def func1(*args,**kwargs):
            pass

        def func2(*args,**kwargs):
            pass

        def switch(func,*args,**kwargs):
            case = globals().get(func.__name__,None)
            return case(*args,**kwargs)

        switch(func1,1,2)

    def format_map与vars():
        n='lisi'
        num=2
        s='{name} has {num} egg.'
        s.format_map(vars())      #vars() 返回对象object的属性和属性值的字典对象.

    def 处理多层嵌套的可迭代序列():
        from collections import Iterable
        def flatten(items,igonre_type=(str,bytes)):
            for item in items:
                if isinstance(item,Iterable) and not isinstance(item,igonre_type):
                    yield from flatten(item)
                else:
                    yield item
        items=[1,2,[3,4,[5,6],7],8,9]
        for i in flatten(items):print(i)

    def python中执行shell命令():
        '''
        os.system: 只能显示在屏幕上,返回的是命令的执行状态.
        os.popen: 内部其实是调用的subprocess.pope方法.
        subprocess.pope: 详见subprocess模块
        commands.getstatusoutput: python3 中已经废弃,详见 commands模块
        sh: 第三方模块,用于替代subprocess 模块.详见,https://github.com/amoffat/sh
        '''

    def 秒起一个下载服务器():
        '''
        python 内置了一个下载服务器,进入到某个目录执行
        python -m http.server 80
        如果当前目录下存在一个 index.html 的文件,则显示该文件的内容.如果不存在,就显示文件列表.
        '''

def 例子():
    pass