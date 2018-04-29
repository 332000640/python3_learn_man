#!/usr/local/python3/bin/python3  
# -*- encoding:utf-8 -*-
# Filename: python3实例手册.py
# Author  : litao
# Python  : 3.6
# Time    : 2018/4/22 21:14
# Version : 1

def 更新日志():
    #数据的分解操作
    log_2018_04_29 = '''
            基本完成函数部分。
            '''
    log_2018_04_28 = '''
            完成内置函数。
            '''
    log_2018_04_27 = '''
        完成数据类型，进行文件操作，和函数。
        '''
    log_2018_04_26 = '''
        逐个测试所有方法。
        '''
    log_2018_04_22 = '''
        第一次编写，将博客的内容迁移到这里。
        '''

def 更新备忘录():
    '''
    更新print到文件
    python书籍补充。
    python2实例手册补充。
    '''

def 说明():
    '''
    作者：涛
    仅用于自学python3，其中借鉴python2版的实例手册中的一些内容。
    python2版的实例手册地址: https://github.com/liquanzhou/ops_doc
    请使用"pycharm"打开此文档, "Ctrl+Shift+NumPad+/-"将函数展开或折叠后方便查阅
    错误在所难免, 还望指正！
    '''

def 基础():
    '''
    python3的基础知识
    '''

    def 查看帮助():
        模块方法 = '''
            help('modules')   # 查看python所有模块  命令行下：python -c "help('modules')"
            for i in dir(os):print(i)   # 模块的方法
            help(os.path)               # 方法的帮助
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
        '''数字，字符串，列表，元组，字典，集合'''

        共性 = '''
            除数字类型不能使用for循环遍历外，其他的均可遍历
            for i in obj:print(i)
            除字典，数字不能使用 + * 号拼接外，其他的均可拼接
            'abc'+'def'         'abc'*3
            [1,2,3]+[4,5,6]     [1,2,3]*3
            (1,2,3)+(4,5,6)     (1,2,3)*3
            '''

        数据的分解操作 = '''
            只要对象是可迭代的，就可以就行分解操作。
            a,_,b,_='1234'   丢弃操作
            a,*_,b='1234'    分解操作
            
            
        '''

        def 数字():

            特性 = '''
                只能存放一个值
                一经定义，不可更改直接访问
                分类：整型，布尔，浮点，复数
                整型(Int)
                通常被称为是整型或整数，是正或负整数，不带小数点。Python3整型是没有限制大小的，可以当作 Long类型使用，所以Python3没有 Python2的Long类型。
                浮点型(float)
                浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示
                复数(complex)
                复数由实数部分和虚数部分构成，可以用a + bj, 或者complex(a, b)表示， 复数的实部a和虚部b都是浮点型。
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
                <   小于      - 返回x是否小于y。返回1表示真，返回0表示假。
                >=  大于等于   - 返回x是否大于等于y。
                <=  小于等于  - 返回x是否小于等于y。
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
                在没有()的情况下,not优先级高于 and，and优先级高于or，即优先级关系为() >not > and > or ，同一优先级从左往右计算。
                x or y      x为真，值就是x，x为假，值是y。其中一个为真，就返回为真的值，如果两个都为真，就返回第一个。
                x and y     x为真，值是y, x为假，值是x。在第一个值为真的时候，就看第二个值，第二值为真，就为真，第二个值为假，就为假。第一个值为假，直接返回第一个值，即，为假。
                x and y     布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。
                x or y      布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。
                not x       布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。
                '''

            成员运算符 = '''
                in 如果在指定的序列中找到值返回True，否则返回False。x在y序列中, 如果x在y序列中返回True。
                not in 如果在指定的序列中没有找到值返回True，否则返回False。
                '''

            身份运算符 = '''
                is 是判断两个标识符是不是引用自一个对象x is y, 类似id(x) == id(y), 如果引用的是同一个对象则返回True，否则返回False
                is not 是判断两个标识符是不是引用自不同对象，x is not y，类似id(a) != id(b)。如果引用的不是同一个对象则返回结果True，否则返回False。
                数据类型是不允许改变的, 这就意味着如果改变数字数据类型的值，将重新分配内存空间
                '''

            删除 = '''
                del  变量名  # 删除一些数字对象的引用
                '''

            类型转换 = '''
                int()       # 将数字组成的字符重转换为数字类型
                float()     # 将整数和字符串转换成浮点数。
                data = 10.bit_length()  # 当十进制用二进制表示时，最少使用的位数
                conjugate()     # 复数
                from_bytes()
                res = int.from_bytes(x)  # 把bytes类型的变量x，转化为十进制整数，并存入res中。其中bytes类型是python3特有的类型
                to_bytts()      # 是int.from_bytes的逆过程，把十进制整数，转换为bytes类型的格式
                complex(x)      # 将x转换到一个复数，实数部分为x，虚数部分为0。
                complex(x, y)   # 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式在整数除法中，除法（/）总是返回一个浮点数，如果只想得到整数的结果，丢弃可能的分数部分，可以使用运算符 //
                abs(x)          # 返回数字的绝对值，如abs(-10) 返回 10
                ceil(x)         # 返回数字的上入整数，如math.ceil(4.1) 返回 5
                floor(x)        # 返回数字的下舍整数，如math.floor(4.9)返回4
                max(x1, x2, ...)# 返回给定参数的最大值，参数可以为序列。
                min(x1, x2, ...)# 返回给定参数的最小值，参数可以为序列。
                modf(x)         # 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
                pow(x, y)       # x ** y运算后的值。
                round(x,[,n])      # 返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
                sqrt(x)         # 返回数字x的平方根。
                choice(seq)     # 从序列的元素中随机返回一个元素，比如import random; random.choice(range(10))，从0到9中随机挑选一个整数。
                randrange([start, ]stop[, step]) # 从指定范围内，按指定基数递增的集合中返回一个随机数，基数缺省值为1
                random()        # 随机返回下一个实数，它在[0, 1)范围内。import random;random.random()
                seed([x])       # 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
                shuffle(lst)    # 将序列的所有元素随机排序
                uniform(x, y)   # 随机生成下一个实数，它在[x, y] 范围内。
                '''

        def 字符串():

            字符串表达 = '''
                引号包含的都是字符串类型,单引双引没有区别
                三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。
                在Python3中，所有的字符串都是Unicode字符串
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
                %s后面可以是数字类型。但 %d后面必须是数字类型的。
                print('abdc %s sdfsdf' % 'aaa')  # %2s表示占用两个字符的位置
                %d 格式化整数。
                %f 格式化浮点数字，可指定小数点后的精度。如 %0.2f 表示保留小数点后两位。

                msg = 'my name is %(name)s, age is %(age)s' % {"name": "lisi", "age": "18"} # 使用字典的方式
                msg = 'name:{},age:{},sex:{}'.format('haiyan', 18, 'girl')                  # 按顺序
                msg = 'name:{0},age:{1},sex:{0}'.format('aaaaaa', 'bbbbbb')                 # 按索引
                msg = 'name:{x},age:{y},sex:{z}'.format(x='haiyan', y='18', z='women')      # 赋值的方式
                '''

            字符编码 = '''
                sys.getdefaultencoding()        # 获取系统编码
                python3默认编码为unicode，在unicode中，一个字符就是两个字节。python3,有两种数据类型，bytes和unicode. 字符串是unicode类型，bytes是bytes类型。
                bytes.decode(encoding="utf-8", errors="strict")  # Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。
                'test'.encode(encoding='UTF-8', errors='strict')  # 以 encoding 指定的编码格式编码字符串，errors 默认为 'strict'，触发UnicodeError 也可指定'ignore'，忽略，或者'replace' 将未知编码替换成？。
                例：            
                str='i an 特斯拉'
                unicode--->gbk
                uni_to_gbk=str.encode('gbk')  # 编码为gbk  encode是编码方法，括号中为目的编码.
                uni_to_gbk                    # 此时uni_to_gbk 是 b 字节类型。encode在编码的同时会把中文转成字节bytes类型。gbk用俩个字节表示一个中文字符。utf-8用三个字节表示一个中文字符。
                gbk--->unicode
                uni_to_gbk.decode('gbk')      # 解码为unicode   decode是解码方法，在括号中指定原来的编码。    
                ss='李四'
                b1=ss.encode()                # 默认解码为utf8，将unicode 解码为bytes类型，解码格式为utf8。encode 就是将unicode转换成bytes，utf8格式。
                #b1.decode('utf8')            # 括号里指定b1的格式。将b1 格式转成utf8.
                d1=b1.decode('utf8')          # 将bytes类型的utf8格式编码为Unicode，decode编码，并指定b1的是什么格式。
                g1=ss.encode('gbk')
                by=bytes(ss,'utf8')           # 另一种类型转换的方法，用bytes函数，将unicode转成utf8编码的bytes类型。
                st=str(by,'utf8')             # 用str函数将utf8编码的bytes类型转成unicode。后面指定，by的当前格式。   
                '''

            字符串方法 = '''
                'test'.count('t',beg,end)        # 返回 str 在 string 里面出现的次数,可以指定查找开始和结束的位置。
                'test'.startswith(str, beg,end)  # 检查字符串是否是以 str 开头，可以指定查找开始和结束的位置,返回bool值。
                'test'.endswith('t', beg, end)   # 检查字符串是否以指定的字符串结束，可以指定查找开始和结束的位置，返回bool值。
                'te\tst'.expandtabs(tabsize=8)                   # 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 ,也可以指定其他空格数。
                'test'.find(str,beg,end)                         # 检测 str 是否包含在字符串中，可以指定查找开始和结束的位置，正常返回开始的索引值，未找到返回-1。
                'test'.index(str, beg,end)                       # 跟find()方法一样，只不过如果str不在字符串中会报一个异常。
                'test'.upper()      # 转换字符串中的小写字母为大写。
                'test'.isalnum()    # 如果字符串至少有一个字符并且所有字符都是字母或数字则返回True, 否则返回False。
                'test'.isdigit()    # 如果字符串只包含数字则返回 True 否则返回 False。
                'test'.islower()    # 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False。
                'test'.isnumeric()  # 如果字符串中只包含数字字符，则返回 True，否则返回 False。
                'test'.isspace()    # 如果字符串中只包含空白，则返回 True，否则返回 False。
                'test'.istitle()    # 如果字符串是标题化的(见 title())则返回 True，否则返回 False。
                'test'.isupper()    # 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False。
                'test'.split(str="t", num)    # 以 str 为分隔符截取字符串，可以指定分割次数。默认以空格分割。也可以以其他的字符分割，分割完成后，如果没有指定分割符，或者分隔符为None,任何以空格为分隔符的结果中的空字符串，将从结果中删除。
                ' sdf '.split()     # 返回 ['sdf']
                ' sdf '.split(' ')  # 返回['', 'sdf', '']
                'test'.strip()      # 在字符串上执行 lstrip()和 rstrip(),默认去掉两边的空格，可以指定多个字符，如: 'abcdef'.strip('abef'),返回：cd 。尽可能的匹配。
                 len('test')         # 返回字符串长度。
                'test'.ljust(6,'*') # 返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。
                'test'.lower()      # 转换字符串中所有大写字符为小写。
                'test'.lstrip()     # 截掉字符串左边的空格或指定字符。
                'test'.replace('t', 'T',2)  # 把 将字符串中的 str1 替换成 str2,也可以指定替换次数。有返回值,返回替换后的字符串。
                'test'.maketrans()          # 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
                 max('test')     # 返回字符串 str 中最大的字母。
                 min('test')     # 返回字符串 str 中最小的字母。
                'test'.capitalize()     # 将字符串的第一个字符转换为大写。
                'test'.isalpha()        # 如果字符串至少有一个字符并且所有字符都是字母则返回True, 否则返回False。
                'test'.rfind(str, beg, end)   # 类似于 find()函数，不过是从右边开始查找。
                'test'.rindex(str, beg, end)  # 类似于 index()，不过是从右边开始。
                'test'.rjust(7,'*')     # 返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串。
                'test'.rstrip()         # 删除字符串字符串末尾的空格.
                'test'.swapcase()       # 将字符串中大写转换为小写，小写转换为大写
                'test'.title()          # 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
                'test'.translate('test', deletechars="")    # 根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
                'test'.zfill(9)         # 返回长度为 width 的字符串，原字符串右对齐，前面填充0
                'test'.isdecimal()      # 检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。
                'test'.splitlines(True) # 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
                '+'.join([1,2,3])       # join,以指定的字符并将一个容器类型的数据。接受一个可迭代对象，返回拼接后的字符串。
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
                创建一个列表，用逗号分隔的不同的数据项，使用方括号括起来，
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
                list.extend(seq)        # 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表） 无返回值
                list.index(obj)         # 从列表中返回某个值第一个匹配项的索引位置
                list.insert(index, obj) # 将对象插入列表，指定插入位置 
                list.pop(obj=list[-1])  # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
                list.remove(obj)        # 移除列表中某个值的第一个匹配项 无返回值
                list.reverse()          # 反向列表中元素,无返回值,改变列表本身,但reversed()不改变列表本身，返回反向的列表,列表中不能出现不同类型的数据.
                list.sort([func])       # 对原列表进行排序,无返回值 ,改变列表本身,但sorted()不改变列表本身，返回反向的列表,列表中不能出现不同类型的数据.
                list.clear()            # 清空列表 无返回值 
                list.copy()             # 复制列表 无返回值,属于浅拷贝
                del                     # 语句可以删除列表中的元素，也可以在内存空间删除整个列表。
                '''

        def 元组():
            '''
                元组的元素不能修改。元组使用小括号。即使元组中有一个元素，也需要使用逗号分割。可以使用tuple()函数创建
                '''

            元组的方法 = '''
                即使没有圆括号，python也能识别除元组，如  a=1,2,3,4
                del             # 语句来删除整个元组，不能删单个元素 
                len(tuple)      # 计算元组元素个数。     
                max(tuple)      # 返回元组中元素最大值。     
                min(tuple)      # 返回元组中元素最小值。     
                tuple(list)     # 将列表转换为元组。
                sorted(tuple)   # 如果使用sorted对元组进行排序，返回的是一个列表
                '''

        def 字典():
            '''
                可变容器模型，且可存储任意类型对象。 键必须是唯一的，但值则不必。 值可以取任何数据类型，但键必须是可哈希的,不可变的，如字符串，数字或元组。
                字典虽然是无序的，但字典的顺序是固定的。
                字典的keys(),items()支持常见的集合操作，求并集，交集，差集，不必转成集合。它们都是唯一的，而values()不支持集合操作。
                '''

            字典的方法 = '''
                len(dict1)          # 计算字典元素个数，即键的总数。     
                str(dict1)          # 输出字典，以可打印的字符串表示。
                eval(str1)          # 将字符串类型的字典转换成字典，返回字典         
                dict1.clear()       # 删除字典内所有元素 
                dict1.copy()        # 返回一个字典的浅复制 
                dict1.fromkeys(seq,[val])       # 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值  如：dic1=dict().fromkeys([1,2,3,4,5],'test') 
                dict1.get(key, default=None)    # 返回指定键的值，如果值不在字典中返回default值 
                key in dict1                    # 如果键在字典dict里返回true，否则返回false 
                dict1.items()                   # 以列表返回可遍历的(键, 值) 元组数组 
                dict1.keys()                    # 以列表返回一个字典所有的键 
                dict1.setdefault(key, default=None)     # 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default 
                dict1.update(dict2)                     # 把字典dict2的键/值对更新到dict里 
                dict1.values()                  # 以列表返回字典中的所有值 
                dict1.pop(key,[default])        # 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。是有返回值的。 
                dict1.popitem()                 # 随机返回并删除字典中的一对键和值(一般删除末尾对)。 是有返回值的。
                del                             # 能删单一的元素也能清空字典。 
                '''

            有序字典 = '''
                from collections import OrdreDict
                当对字典做迭代时，会严格安装字典的初始添加顺序进行
                '''

            字典的应用 = '''
                a={'a':1,'b':2,'c':3}
                b={'b':2,'c':3}
                a.keys() & b.keys()  求a,b 键的交集
                a.keys() - b.keys()  求a,b 键的差集
                a.keys() | b.keys()  求a,b 键的并集
                a.items() & b.items()  求a,b 项的交集
                a.items() - b.items()  求a,b 项的差集
                a.items() | b.items()  求a,b 项的并集
                '''

        def 集合():
            '''
                集合是一个无序的，不重复的数据组合，基本功能是成员关系测试和删除重复元素。关系测试，测试两组数据之前的交集、差集、并集等关系，创建一个空集合必须用set()。
                set([obj]) 可变集合:ojb必须是支持迭代的,由obj中的元素创建集合,否则创建一个空集合
                frozenset([obj]) 不可变集:执行方式与set()方法相同,但它返回的是不可变集合
                '''

            集合的使用 = '''
                s | t
                s.union(t)          # 求并集
                s & t
                s.intersection(t)   # 求交集
                s - t
                s.difference(t)     # 求差集
                s ^ t
                s.symmetric_difference(t)   # 对称差集，a和b中不同时存在的元素
                s <= t
                s.issubset(t)               # 测试是否 s 中的每一个元素都在 t 中
                s >= t
                s.issuperset(t)             # 测试是否 t 中的每一个元素都在 s 中
                len(s)          # 集合s中元素个数
                obj in s        # 成员测试
                obj not in s    # 非成员测试
                s == t          # 等价测试
                s != t          # 不等价测试
                s.copy()        # 赋值操作：返回s的（浅复制）副本
                s.update(t)     # 将t中的成员添加s,t 必须是一个可迭代对象，类似于列表的extend()方法。
                s.add(obj)      # 将obj添加到s
                s.remove(obj)   # 删除操作
                s.discard(obj)  # 丢弃操作：remove() 的友好版本，如果s中存在ojb，从s中删除它
                s.pop()         # 移除并返回s中的任意一个值
                s.clear()       # 移除s中的所有元素a'v'a'a
                '''

    def 流程结构():

        if判断='''
        布尔值操作符 and or not 实现多重判断
        if elif elif ... else
        '''

        for循环='''
        
        '''
    
    def 文件操作():

        参数说明 = '''
            open(name,mode,encoding)
            with open(name,'r') as f,open(name1,'w') as f1:
            参数说明：
            name : 文件名称的字符串。
            mode : 打开文件的模式，默认文件访问模式为只读(r)。
            encoding : 默认的打开方式r ，默认的打开编码是操作系统的默认编码
            不同模式打开文件的完全列表：
            模式	描述
            r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
            rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
            r+	打开一个文件用于读写。文件指针将会放在文件的开头。
            rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
            w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
            wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
            w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
            wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
            a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
            ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
            a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
            ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
            '''

        属性与方法 = '''
            f.read(3) 文件打开方式为文本模式时,代表读取3个字符.文件打开方式为b模式时,代表读取3个字节.
            f.readline() 一行一行读  每次只读一行，不会自动停止
            f.readlines([size]) 返回包含size字符的列表,size 未指定则返回全部行,只有字符个数超过本行的范围,返回下一行.
            for line in f: print line #通过迭代器访问,一行一行读  从第一行开始 每次读一行 读到没有之后就停止
            f.write("hello\n") #如果要写入字符串以外的数据,先将他转换为字符串.
            f.tell() 返回一个整数,表示当前文件指针的位置(就是到文件头的比特数).
            f.seek(偏移量,[起始位置]) 用来移动文件指针. 偏移量:单位:比特,可正可负。起始位置:0-文件头,默认值;1-当前位置;2-文件尾,1和2必须在b模式下进行，但无论哪种模式，都是以bytes为单位移动的
            f.truncate()  截断必须是写模式，但是不能用w或w+等方式打开，因为那样直接清空文件了，所以truncate要在r+或a或a+等模式下测试效果,截取文件到最大size字节,默认为当前文件位置
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
            fe.newlines        # 读取行分隔符,未读取到行分隔符时为None,只有一种行分隔符时为一个字符串,当文件有多种类型的行结束符时,则为一个包含所有当前所遇到的行结束符的列表
            f.softspace       # 为0表示在输出一数据后,要加上一个空格符,1表示不加
            '''

    def 函数():
        '''python3 函数详解'''

        def 内置函数():

            作用域相关 = '''
                globals() # 函数会以字典类型返回当前位置的全部全局变量。可以这样用 globals().get(func)()  就可以调用函数。
                locals()  # 会以字典类型返回当前位置的全部局部变量。 获取执行本方法所在命名空间内的局部变量的字典
                '''

            字符串执行 = '''
                eval()      
                    用来执行一个字符串表达式，并返回表达式的值。eval(def_name) 里面可以直接跟函数名。返回的是函数对象（内存地址） 用eval(def_name)() 执行。用于将字典格式的字符串转换为字典。 
                exec()      
                    执行储存在字符串或文件中的 Python 语句，相比于 eval，exec可以执行更复杂的 Python 代码。 
                compile()   
                    函数将一个字符串编译为字节代码。 
                '''

            输入输出 = '''
                print(*objects, sep=' ', end='\n', file=sys.stdout,flush=False) 
                    打印输出 可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
                    sep -- 用来间隔多个对象，默认值是一个空格。
                    end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。
                    file -- 要写入的文件对象。file是一个文件描述符，with open('test.txt','a+') as file:
                input()
                    函数接受一个标准输入数据，返回为 string 类型。
                '''

            内存相关 = '''
                hash()
                    用于获取取一个对象（字符串或者数值等）的哈希值。
                id()
                    用于获取对象的内存地址。
                '''

            文件操作 = '''
                open()
                    用于打开一个文件，创建一个 file 对象，相关的方法才可以调用它进行读写。详见文件操作。 
                '''

            模块相关 = '''
                __import__
                    用于动态加载类和函数。 如果一个模块经常变化就可以使用 __import__() 来动态载入。 
                '''

            帮助 = '''
                help()
                    用于查看函数或模块用途的详细说明。 输入q退出
                '''

            调试相关 = '''
                callable()
                    用于检查一个对象是否是可调用的。如果返回True，object仍然可能调用失败；但如果返回False，调用对象ojbect绝对不会成功。 
                    对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True 
                '''

            查看内置属性 = '''
                dir()
                    不带参数时，默认查看全局空间内的属性,返回当前范围内的变量、方法和定义的类型列表;带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
                '''

            数字类型 = '''
                int() ***** 
                    用于将一个字符串或数字转换为整型。 
                loat()
                    将整数和字符串转换成浮点数。 
                complex()
                    用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数
                '''

            进制转换 = '''
                hex()
                    用于将10进制整数转换成16进制，以字符串形式表示。返回的是一个字符串。 
                oct()
                    将一个整数转换成8进制字符串。
                bin()
                    一个整数 int 或者长整数 long int 的二进制表示。 
                '''

            数学运算 = '''
                abs()
                    函数返回数字的绝对值。 
                min()
                    返回给定参数的最小值，参数可以为序列。也可以不是序列。
                    min也可以接受多个元素为元组进行比较，已元组的第一个元素为比较依据，如果第一个元素相等，以第二个元素为依据。
                    例: min((3,'a'),(1,'b'),(1,'a')) 返回 (1, 'a')
                max()
                    返回给定参数的最大值，参数可以为序列。也可以不是序列。
                    max也可以接受多个元素为元组进行比较，已元组的第一个元素为比较依据，如果第一个元素相等，以第二个元素为依据。
                    例: max((3,'a'),(1,'b'),(1,'a')) 返回 (3, 'a')
                round()
                    返回浮点数x的四舍五入值。
                sum(iterable,start)
                    对系列进行求和计算。参数必须是可迭代的数字集,可以指定开始位置。
                pow(x,y)
                    方法返回 xy（x的y次方） 的值。
                divmod(x,y)
                    返回x除y的商和余数的元组。
                '''

            序列相关 = '''
                list()
                    用于将元组转换为列表。
                tuple()
                    函数将列表转换为元组。
                sorted(reverse=True)
                    对所有可迭代的对象进行排序操作,通过reverse参数可以反向排序。这里的方向排序是返回一个列表,而reversed()函数返回的是一个迭代器。
                    sort 与 sorted 区别： 
                    sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。 
                    list 的 sort 方法返回的是对已经存在的列表进行操作，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
                reversed()
                    返回一个反转的迭代器。 接受一个序列
                slice()
                    实现切片对象，主要用在切片操作函数里的参数传递。
                str()
                    将对象转化为适于人阅读的形式。 
                format()
                    字符串格式化的功能。详见字符串格式化。
                bytes()
                    返回一个新的 bytes 对象，该对象是一个 0 <= x < 256 区间内的整数不可变序列。它是 bytearray 的不可变版本。 
                bytearray()
                    法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。
                memoryview()
                    返回给定参数的内存查看对象(Momory view)。 所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，在不需要复制对象基础上允许Python代码访问
                ord()
                    是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。 
                chr()
                    用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。
                ascii()
                    类似 repr() 函数, 返回一个表示对象的字符串, 但是对于字符串中的非 ASCII 字符则返回通过 repr() 函数使用 \x, \u 或 \U 编码的字符。  
                repr()
                    将对象转化为供解释器读取的形式。
                dict()
                    用于创建一个字典。
                set()
                    创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
                frozenset()
                    返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。
                len()
                    返回对象（字符、列表、元组等）长度或项目个数。 
                enumerate()
                    用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
                all()
                    用于判断给定的可迭代参数 iterable 中的所有元素是否不为 0、''、False 或者 iterable 为空，如果是返回 True，否则返回 False 
                any()
                    用于判断给定的可迭代参数 iterable 是否全部为空对象，如果都为空、0、false，则返回 False，如果不都为空、0、false，则返回 True。 
                zip()
                    函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解包为列表。 
                filter()
                    用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表中。 
                map()
                    会根据提供的函数对指定序列做映射。第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。 
                '''

            反射相关 = '''
                delattr()
                    函数用于删除属性。 
                setattr()
                    对应函数 getatt()，用于设置属性值，该属性必须存在。
                getattr()
                    函数用于返回一个对象属性值。 
                hasattr()
                    用于判断对象是否包含对应的属性。 
                '''

            迭代与生成器 = '''
                range()
                    返回的是一个可迭代对象（类型是对象），而不是列表类型， 所以打印的时候不会打印列表。
                next()
                    迭代器的下一个项目。
                iter()
                    用来生成迭代器。
                '''

            定义类方法 = '''
                classmethod()
                    修饰符对应的函数不需要实例化，不需要 self 参数，但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
                staticmethod()
                    返回函数的静态方法。
                property()
                    作用是在新式类中返回属性值。如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象。
                '''

            判断类关系 = '''
                isinstance()
                    来判断一个对象是否是一个已知的类型，类似 type()。
                    isinstance() 与 type() 区别： 
                    type() 不会认为子类是一种父类类型，不考虑继承关系。 
                    isinstance() 会认为子类是一种父类类型，考虑继承关系。 
                    如果要判断两个类型是否相同推荐使用 isinstance()。 
                issubclass()
                    用于判断参数 class 是否是类型参数 classinfo 的子类。
                '''

            其他方法 = '''
                vars()
                    返回对象object的属性和属性值的字典对象。
                object()
                    所有类的基类。
                super()
                    函数是用于调用父类(超类)的一个方法。 super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。    
                type()
                    判断一个数据的类型。
                bool()
                    用于将给定参数转换为布尔类型，如果没有参数，返回 False。bool 是 int 的子类。
                '''

        def 自定义函数():

            函数定义 = '''
                def 关键字 函数名（设定与变量相同）:
                    函数的第一行语句建议使用三引号字符串—用于存放函数说明。可以使用  函数名.__doc__  调用。
                    函数体
                    return 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。 返回多个值，将多个值放在元组中返回。
                    return 后面可以跟逻辑判断和短路逻辑 
                    如: return a > 0 and a   
                    return b > 0 or 0
                    return a if a > 0 else 4
                    return a or b
                    return a and b
                    '''

            函数的参数 = '''
                函数创建时：
                默认参数。 必须在位置参数后面。
                动态参数 *args，**kwargs 
                位置参数，*args,默认参数,**kwargs
                函数使用时
                位置参数。形参与实参必须一一对应，按顺序传入。
                关键字参数。必须一一对应，不分顺序。
                混合参数。一一对应 且 关键字参数必须在位置参数后面。
                顺序：位置参数,*args,关键字参数,**args
                
                a=[1,2,3]
                b='test'
                [1,2,3] 是 List 类型，"test" 是 String 类型，而变量 a 是没有类型，a仅仅是一个对象的引用），可以是指向任何类型对象。 
                在 python 中，strings, tuples, 和 numbers 是不可变类型，而 list,dict 等则是可变类型。 
                不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，而是a指向了10。 
                可变类型：变量赋值 l=[1,2,3,4] 后再赋值 l[2]=5 则是将 list l 的第三个元素值更改，本身l没有动，只是其内部的一部分值被修改了。 
                python 函数的参数传递： 
                不可变类型：如 整数、字符串、元组。如fun（a），传递的只是a的copy，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。 
                可变类型：如 列表，字典。如 fun（l），则是将 l 的引用传过去，修改后fun外部的la也会受影响。
                传入函数的和函数返回的都是同一个对象的引用。
                函数的默认参数应该是不可变类型的。如果一定要使用可变类型的，在函数外部声明 _no_value=object()  将_no_value作为默认参数的值传入函数。在函数里判断 if 默认参数 is _no_value:默认参数=？
                object()是一个内存地址，独特的私有实例，可以用这个特殊值判断用户是否提供了参数。
                '''

            函数作用域 = '''
                全局作用域：全局名称空间，内置名称空间。 
                局部作用域：局部名称空间 
                变量与值的加载顺序：内置命名空间(程序运行前加载)->全局命名空间(程序运行中：从上到下加载)->局部命名空间(程序运行中：调用时才加载) 
                变量与值的取值顺序：局部名称空间 ---> 全局名称空间 ----> 内置名称空间 
                global 关键字用来在函数或其他局部作用域中使用全局变量。但是如果不修改全局变量也可以不使用global关键字。如果更改一个全局变量，要先声明，后更改。
                nonlocal 关键字用来在函数或其他作用域中使用外层(非全局)变量。外部必须有这个变量,在内部函数声明nonlocal变量之前不能再出现同名变量.
                '''

            函数的特性 = '''
                函数名本质上就是函数的内存地址的引用
                可以互相赋值。 
                函数名可以当成函数的参数 
                可以当成容器类数据类型的参数 
                函数名可以当成函数的返回值 
                函数是第一类对象
                第一类对象:可在运行期创建,可用作函数参数或返回值,可存入变量的实体。
                '''

        def 装饰器():
            '''为已存在的功能添加额外的功能,只在初始化脚本的时候执行一次.本质是函数, 用于装饰其他函数'''

            闭包 = '''
                闭包： 内层函数对外层函数非全局变量的引用，叫做闭包 
                闭包的好处：如果python 检测到闭包,函数的局部作用域不会随着函数的结束而结束 
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
                
                @para(3)    通过执行para,把装饰器返回。
                def test(num):
                    print(num)
            
                装饰器返回被装饰函数的属性
                import functools
                functools.warps 通过对装饰器内层函数的装饰，被装饰函数的属性传递给外层函数。
                
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

        def 迭代器生成器():

            迭代器 = '''
                凡是可以使用for循环取值的都是可迭代的
                可迭代协议 ：内部含有__iter__方法的都是可迭代的
                迭代器协议 ：内部含有__iter__方法和__next__方法的都是迭代器
                iter()函数将一个可迭代的对象，转化为迭代器。
                迭代器的三个方法:
                __length_hint__()   # 获取迭代器中元素的个数
                __setstate__()      # 根据索引值指定从哪里开始迭代
                __next()__()        # 一个一个取值，在for循环中，就是在内部调用了__next__方法
                迭代器的优势:
                    节省内存
                    取一个值就能进行接下来的计算 ，而不需要等到所有的值都计算出来才开始接下来的运算 —— 快
                迭代器的特性:
                    惰性运算
            '''

            生成器 = '''
                一个包含yield关键字的函数就是一个生成器函数。yield可以为我们从函数中返回值，但是yield又不同于return。
                return的执行意味着程序的结束，调用生成器函数不会得到返回的具体的值，而是得到一个可迭代的对象。
                每一次获取这个可迭代对象的值，就能推动函数的执行，获取新的返回值。直到函数执行结束。
                生成器函数的调用不会触发代码的执行，而是会返回一个生成器(迭代器).generator object。
                需要使用next()函数或生成器函数的__next__()方法，才会执行一次生成器。
                
                生成器.send()方法，相当于，先发送给生成器一个值，然后再执行next()方法，所以在使用send()之前，要先执行一次next().如果不先执行一次next(),send()发送的值将无变量接受。
                会报错。
                生成器用来解决 内存问题 和程序功能之间的解耦,是实现迭代器的一种手段
                '''

            生成器实例 = '''
                实例：
                def test(num=0):
                    while True:
                        print(num)
                        num = yield num
    
                t=test()
                n=next(t)       # 打印0，返回0
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
                如果本身就是循环一个可迭代的，且要把可迭代数据中的每一个元素都返回 可以用yield from
                def test():
                    yield from range(10) 
                for n in test():print(i)

                从生成器中取值，next send、循环、数据类型的强制转化
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
                推导式里面可以跟三元运算，可以有多个 for 循环，每个for循环里面可以跟三元运算
                生成器表达式:  庞大数据量的时候 使用生成器表达式
                (i**2 for i in range(10))
                (i**2 for i in range(10) if i%2==0 )
                列表推导式:
                [i**2 for i in range(10)]
                [i**2 for i in range(10) if i%2==0]
                [(x,y,z) for x in range(10) if x%2==0 for y in range(10,20) if y%2==0 for z in range(20,30) if z%2==0] 
                字典推导式:
                {k:v for item in [('a':1,'b':2)]}
                集合推导式:  自带去重功能
                {i**2 for i in range(10)}
                '''

        def 递归函数():

            递归的定义 = '''
                在一个函数里调用这个函数本身，这种使用函数的方式就叫做递归。
                递归的最大深度:997
                修改递归最大深度
                import sys; sys.setrecursionlimit(100000)
                递归必须有一个明确的结束条件
                每进入更深层次的递归时，问题的规模应由所减小
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
                函数名 = lambda 参数 ：返回值
                lambda表达式中的变量，不是定义的时候去绑定，而是运行的时候去绑定。
                lambda可以定义默认参数，如果要给lambd传入外部的变量，lambda x,y=n:x+y  这样就把n穿进去了。
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
                
                4，过滤除偶数
                a=[1, 4, 6, 7, 9, 12, 17]
                b=filter(lambda x:x if x%2==0 else False,a)
                '''

def 常用模块():
    pass

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
        zapi.host.get(output="extend"):   #获取主机，循环得到主机的监控项
        '''

    写入execl = '''
        style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on', num_format_str='#,##0.00')  # 格式1
        style1 = xlwt.easyxf()  # 格式2
        wb = xlwt.Workbook()    # 一个新文件
        ws = wb.add_sheet('ASR引擎服务器监控信息周统计表') # 表的标题
        ws.write(x,y,'items',style)     # 根据坐标写入表格 从0开始，x表示行，y表示列。最后表示写入的格式
        ws.write(0,0,'项目名',style0)
        ws.write(0,1,'平均值',style0)
        excel_name='file_name.xls'      # 指定文件名
        wb.save(excel_name)             # 报存文件
        '''

def 题目详解():

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
            g,g1,g2都是生成器，在不调用的时候都不执行，用list去强转g1的时候，就相当于执行了g1，当list再去强转g2的时候，g1已经执行完毕，g2取不到值，遂返回空。
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
            首先g=test()，g是一个生成器，for循环取反复的调用g,并重新赋值给g.
            第一次 for 循环结束后,g=(add(1,i) for i in test())  n指向了内存中值为1的地址
            第二次 for 循环结束后,g=(add(3,i) for i in (add(3,i) for i in test()))  n指向了内存中值为3的地址  
            第三次 for 循环结束后,g=(add(10,i) for i in (add(10,i) for i in (add(10,i) for i in test())))  n指向了内存中值为10的地址
            在用list强转时，执行了最后的g,  list((add(10,i) for i in (add(10,i) for i in (add(10,i) for i in test()))))
            从左到右，第一个add,第二个add,第三个add test() 依次是:
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
            lambda表达式中的变量，不是定义的时候去绑定，而是运行的时候去绑定。
            mul() 返回了一个列表，列表里面是4个lambda表达式，最后一个i 的值是3，当匿名函数被调用时i的值时3，所以返回结果[6,6,6]
            如何修改才能返回想要的结果呢？[0, 2, 4, 6]
            法一:
            return [lambda x,i=i:x*i  for i in range(4)]  通过给lambda传参的方式。
            法二:
            return (lambda x:x*i  for i in range(4))      通过返回一个生成器表达式。生成器只有调用__next__的时候才执行一次。
            '''

def 使用技巧():

    def 去除序列中的重复元素保持元素顺序不变():

        法一 = '''   #序列中的元素必须是可哈希的，不变的。 
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
            以上两种方法均不能对不可哈希的元素排序，如字典列表
            def dedupe(items,key=None):
                seen = set()
                for item in items:
                    val = item if key is None else key(item)
                    if val not in seen:
                        yield item
                        seen.add(val)
            a=[{'x':1,'y':2},{'x':1,'y':3},{'x':1,'y':2},{'x':2,'y':4}]
            dedupe(a,key=lambda d:(d['x'],d['y']))   # 字典是不可哈希的，通过用字典的键来去重。       
            '''

def 例子():
    pass