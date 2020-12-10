# 可以输出数字
print(520)

# 可以输出字符串
print('HelloWorld')

# 含有运算符的表达式
print(2*5)

# 将数据输出到文件中

# 注意点：1.使用 file=
sh = open('C:/Users/Administrator/Desktop/text1.txt', 'a+')  # a+：file不存在就build,exist就继续添加
print('helloWorld', file=sh)
sh.close()

# 不进行换行输出，用，
print('hello', 'world', 'python')
