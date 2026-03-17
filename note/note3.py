from pathlib import Path  
import os

print("当前工作目录：", os.getcwd())  # 输出类似：/Users/username/Documents

path1 = Path('note/pi_digits.txt')  #此为相对文件路径，相对于当前工作目录
path2 = Path('note/programming.txt')
try:
    # 显式指定编码，避免乱码
    contents = path1.read_text(encoding='utf-8')   #读取文件
    #写入文件
    path2.write_text('I love programming!')
    #写入多行
    sentences = "I love me!\n"
    sentences += "I love you!\n"
    sentences += "You love me!"
    path2.write_text(sentences)   #第二次调用会覆盖第一次写入的内容
except FileNotFoundError:   #可直接在后面直接跟pass
    print(f"错误：文件不存在，请检查路径是否正确。")
except UnicodeDecodeError:
    print(f"错误：文件编码不是 UTF-8，请确认编码格式。")
else:   #try成功后才会执行
    # 如需删除首尾空白，使用 strip()；仅删除末尾用 rstrip()
    print(contents.strip())  
    lines = contents.splitlines()   #splitlines()方法会返回一个列表，内部元素为字符串的各行内容
    pi_string = ''
    for line in lines:
        pi_string += line.strip()   #字符串拼接
    print(pi_string)
    #判断生日在不在pi内部
    birthday = input('请输入你的生日日期：')
    if birthday in pi_string:   #字符串也可类似列表写出类似语句
        print('yes')
    else:
        print('no')



