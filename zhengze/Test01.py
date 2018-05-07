#coding=utf-8
import re
#2. re模块示例(匹配以wang开头的语句)

# result = re.match("wang","wanglei")
# print result.group()


#表示字符
#示例1: .
# ret = re.match(".","ab")
# print ret.group()
# ret = re.match(".","bc")
# print ret.group()
# ret = re.match(".","Mc")
# print ret.group()

# ret = re.match("[12346]","8366")
# print ret

#示例二:[]
# #⼤⼩写h都可以的情况
# ret = re.match("[hH]","hello Python")
# print ret.group()
# ret = re.match("[hH]","Hello Python")
# print ret.group()
# # 匹配0到9第⼀种写法
# ret = re.match("[0123456789]","7Hello Python")

#示例3：\d
# ret = re.match("张三\d号","张三s号")
# print  ret.group()

#原始字符串
#一\ 在正则中匹配 需要  \\\\个
# mm = "c:\\a\\b\\c"
# print  mm
#
# ret = re.match("c:\\\\",mm)
# print ret.group()
#
# # r 表示原⽣字符串
# ret = re.match("c:\\b",mm)
#
# ret = re.match(r"c:\b",mm)
# print ret


#表示数量
#示例1：*
#需求：匹配出，⼀个字符串第⼀个字⺟为⼤⼩字符，后⾯都是⼩写字⺟并且 这些⼩写字⺟可有可⽆
# ret = re.match("[A-Z][a-z]*","M")
# print ret.group()
# ret = re.match("[A-Z][a-z]*","Aabcdef")
# print ret.group()

#示例2：+    前一个字符必须出现一次或无数次,至少一次
#需求：匹配出，变量名是否有效
# ret = re.match("[a-zA-Z_]+[\w_]*","1ame1")
# print ret.group()
# ret = re.match("[a-zA-Z_]+[\w_]*","_name")
# print ret.group()
# ret = re.match("[a-zA-Z_]+[\w_]*","2_name")
# print ret.group()

#示例3：?
# 需求：匹配出，0到99之间的数字
# ret = re.match("[1-9]?[0-9]","7")
# print ret.group()
# ret = re.match("[1-9]?[0-9]","33")
# print ret.group()
# ret = re.match("[1-9]?[0-9]","09")
# print ret.group()

#示例4：{m}
#需求：匹配出，8到20位的密码，可以是⼤⼩写英⽂字⺟、数字、下划线
# ret = re.match("[a-zA-Z0-9_]{6}","1ad1")
# print ret.group()
# ret = re.match("[a-zA-Z0-9_]{8,20}","1ad12f23s34455ff66abcdefg")
# print ret.group()
# ret = re.match("[a-zA-Z0-9_]{8,}","1ad12f23s34455ff66abcdefg")
# print ret.group()

# ret = re.match("^123","987456")
# print ret
#表示边界
#示例1：$
#需求：匹配163.com的邮箱地址
# 正确的地址
# ret = re.match("[\w]{4,20}@163\.com", "xiaoWang@163.com")
# print ret.group()
# 不正确的地址
# ret = re.match("[\w]{4,20}@163\.com", "xiaoWang@163.comheihei"  )
# print ret.group()
# 通过$来确定末尾
# ret = re.match("[\w]{4,20}@163\.com$", "xiaoWang@163.com")
# print ret.group()

#示例2：^
##以abc开头
# ret = re.match('^abc','abc')
# print ret

#示例3: \b
#正确
# ret = re.match(r".*\bver\b", "ho ver abc").group()
# print ret
# 错误
# ret = re.match(r".*\bver\b", "ho verabc").group()
# print ret

#示例3：\B


#匹配分组
#示例1：|
#需求：匹配出0-100之间的数字
# ret = re.match("[1-9]?\d","8")
# print ret.group()
#
# ret = re.match("[1-9]?\d","78")
# print ret.group()
# # 不正确的情况
# ret = re.match("[1-9]?\d","08")
# print ret.group()
# # 修正之后的
# ret = re.match("[1-9]?\d$","08")
# print ret.group()

#匹配分组
# ret = re.match("[1-9]?\d$|100","120")
# print ret.group()
# ret = re.match("[1-9]?\d$|100","78")
# print ret.group()
# # 不正确的情况
# ret = re.match("[1-9]?\d$|100","08")
# print ret.group()
# ret = re.match("[1-9]?\d$|100","100")
# print ret.group()


#示例2：( )
#需求：匹配出163、126、qq邮箱之间的数字
# ret = re.match("\w{4,20}@163\.com", "test@163.com")
# print ret.group()
# ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@126.com")
# print ret.group()
# ret = re.match("\w{4,20}@(163|126|qq)\.com", "test@qq.com")
# print ret.group()

#示例3：\
# 能够完成对正确的字符串的匹配
# ret = re.match("<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</htmls> ")
# print ret.group()

# 通过引⽤分组中匹配到的数据即可，但是要注意是元字符串，即类似 r""这种格式
# ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</html>")
# print ret.group()

# 因为2对<>中的数据不⼀致，所以没有匹配出来
# ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</htmlbalab ala>")
# print  ret.group()

#示例4：\number
#需求：匹配出 <html><h1>www.itcast.cn</h1></html>
# ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", "<html><h1>www. itcast.cn</h1></html>")
# print ret.group()
# ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", "<html><h1>www. itcast.cn</h2></html>")
# print ret.group()

#示例5： (?P<name>)   (?P=name)
# ret = re.match(r"<(?P<s>\w*)><(?P<b>\w*)>.*</?P=s></?P=b>", "<html><h1>www. itcast.cn</h1></html>")
# print ret.group()
# ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", "<html><h1>www. itcast.cn</h2></html>")
# print ret.group()

# ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name 2)></(?P=name1)>", "<html><h1>www.itcast.cn</h1></html>")
# print ret.group()
# ret = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name 2)></(?P=name1)>", "<html><h1>www.itcast.cn</h2></html>")
# print ret.group()

#search:
#需求：匹配出⽂章阅读的次数
# ret = re.search(r"\d+", "阅读次数为 9999")
# print ret.group()


#findall
#需求：findall查找全部r标识代表后面是正则的语句
# regular_v1 = re.findall("docs",r"https://docs.python.org/3/whatsnew/3.6.html,docs")
# print (regular_v1)


#sub
# 将匹配到的数据进⾏替换
#数字的全部替换位333
# inputStr = "hello 123 world 456 se 41241"
# rep = re.sub("\d+","333",inputStr)
# print rep
# #数字的前2位替换为333
# rep = re.sub("\d+","333",inputStr,2)
# print rep


#split 根据匹配进⾏切割字符串，并返回⼀个列表
#根据空格进行分割成列表
# ret = re.split(" ","info:xiao Zhang 33 shandong")
# print ret


#贪婪与非贪婪示例
s = "This is a number 234-235-22-423"
r = re.match(".+(\d+-\d+-\d+-\d+)", s)
d=r.group(1)
print d
#
#
# r=re.match(".+?(\d+-\d+-\d+-\d+)",s)
# d= r.group(1)
# print d
#
# d= re.match(r"aa(\d+?)ddd","aa2343ddd").group(1)
# print d


# r=re.match(r"aa(\d+)","aa2343ddd").group(1)
# print r
# r=re.match(r"aa(\d+?)","aa2343ddd").group(1)
# print r
# r=re.match(r"aa(\d+)ddd","aa2343ddd").group(1)
# print r
# r=re.match(r"aa(\d+?)ddd","aa2343ddd").group(1)
# print r


