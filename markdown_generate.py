#!/usr/bin/env python3

import os
import datetime

# 获取当前年份
year = datetime.datetime.now().strftime("%Y")

# 获取当前目录
dir = os.getcwd()

# 生成的uuid
uuid = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# 定义一个函数，接受两个参数，第一个为父目录，第二个为子目录
def check_folder(parent, child):

    # 判断父目录下是否存在子目录
    if os.path.isdir(os.path.join(parent, child)):

        # 如果存在，打印提示信息
        print(f"The folder {child} already exists in {parent}")
    else:
        # 如果不存在，创建文件夹并打印提示信息
        os.mkdir(os.path.join(parent, child))
        print(f"The folder {child} has been created in {parent}")

# 调用函数，传入当前目录和年份作为参数
check_folder(dir, year)

# 定义一个列表，存储要检查的文件夹名
folders = ["book", "card", "essay", "0_index", "999_others"]

# 遍历列表中的每个元素
for folder in folders:
    # 调用函数，传入年份目录和元素作为参数
    check_folder(os.path.join(dir, year), folder)

# 问下用户选择是什么类型的卡片，并打印选项
print("Please choose which type of card you want to create:")
print("1. 事件卡")
print("2. 人物卡")
print("3. 图示卡")
print("4. 基础卡")
print("5. 新知卡")
print("6. 新词卡")
print("7. 术语卡")
print("8. 行动卡")
print("9. 金句卡")
type = int(input())

# 判断用户是否输入了有效的类型，如果没有就打印错误信息并退出程序，用if语句进行判断。
if not 1 <= type <= 9:
    print("Invalid type. Please enter a number between 1 and 9.")
    exit(1)

types = ["事件卡", "人物卡", "图示卡", "基础卡", "新知卡", "新词卡", "术语卡", "行动卡", "金句卡"]

# 问下用户选择是在哪个子目录下创建文件，并打印选项
print("Please choose which subfolder you want to create a file in:")
print("1. book")
print("2. card")
print("3. essay")
choice = int(input())

# 判断用户是否输入了有效的子目录，如果没有就打印错误信息并退出程序，用if语句进行判断。
if not 1 <= choice <= 3:
    print("Invalid choice. Please enter a number between 1 and 3.")
    exit(1)

# 询问第一行的插入语，并读取用户的输入，并在文件中插入插入语，用input函数读取输入，用open函数和write方法在文件中插入文本。
firstline = input("Please enter the first line of the file:")

# 根据用户的选择执行不同的操作
if choice == 1: # 如果用户选择book
    os.system(f"tree &quot;{os.path.join(dir, year, 'book')}&quot;") # 打印book目录下的文件树结构
    print("文件目录如上")
    bookname = input("因为这个选言支暂时不支持自动化命名，所以请手动输入书名: ") # 询问书名
    check_folder(os.path.join(dir, year, "book"), bookname) # 检查并创建书名目录
    filename = input("因为这个选言支暂时不支持自动化命名，所以请手动输入名字（格式：章节_abcd.md）: ") # 询问文件名
    os.system(f"cp '{os.path.join(dir, 'sample_card', types[type - 1] + '.md')}' '{os.path.join(dir, year, 'book', bookname, filename)}'") # 复制模板文件到目标目录
    with open(os.path.join(dir, year, "book", bookname, filename), "r+") as f: # 以读写模式打开文件
        content = f.read() # 读取文件内容
        f.seek(0) # 将文件指针移动到开头
        f.write(f"#{firstline}\n{content}") # 写入第一行和原内容
        f.write(f"\nuuid:{uuid}") # 写入最后一行
    print(f"A markdown file named {filename} has been created in {os.path.join(dir, year, 'book', bookname)} from sample_card/{types[type - 1]}.md with the first line: #{firstline}")
elif choice == 2: # 如果用户选择card
    #在年份同级的文件里面copy相应的文件出来，并重命名为%Y%m%d%H%M%S这种格式的markdown文件，并根据用户选择的类型进行复制和重命名，并打印提示信息，用os.system函数执行cp命令，用datetime模块获取当前时间。
    filename = f"{uuid}.md"
    os.system(f"cp '{os.path.join(dir, 'sample_card', types[type - 1] + '.md')}' '{os.path.join(dir, year, 'card', filename)}'")
    with open(os.path.join(dir, year, "card", filename), "r+") as f: # 以读写模式打开文件
        content = f.read() # 读取文件内容
        f.seek(0) # 将文件指针移动到开头
        f.write(f'#{firstline}\n{content}') # 写入第一行和原内容
        f.write(f"\nuuid:{uuid}") # 写入最后一行
    print(f"A markdown file named {filename} has been created in {os.path.join(dir, year, 'card')} from sample_card/{types[type - 1]}.md with the first line: #{firstline}")
elif choice == 3: # 如果用户选择essay
    #判断该目录下是否有文件，如果没有就直接复制一个名为1.md的文件，如果有就读取最后一个文件名，再加一进行重命名，并打印提示信息，用os.listdir函数列出文件，用len函数计数，用if语句进行判断，用sorted函数排序，用split方法分割文件名和扩展名，用算术运算符加一。
    files = os.listdir(os.path.join(dir, year, "essay")) # 获取essay目录下的所有文件
    if len(files) == 0: # 如果没有文件
        #在年份同级的文件里面移动相应的文件出来，并根据用户选择的类型进行重命名，并打印提示信息，用os.system函数执行cp命令。
        filename = "1.md"
        os.system(f"cp '{os.path.join(dir, 'sample_card', types[type - 1] + '.md')}' '{os.path.join(dir, year, 'essay', filename)}'")
    else: # 如果有文件
        last = sorted(files)[-1] # 获取最后一个文件名
        num = int(last.split(".")[0]) + 1 # 获取最后一个文件名的数字部分并加一
        filename = f"{num}.md"
        os.system(f"cp '{os.path.join(dir, 'sample_card', types[type - 1] + '.md')}' '{os.path.join(dir, year, 'essay', filename)}'")
    with open(os.path.join(dir, year, "essay", filename), "r+") as f: # 以读写模式打开文件
        content = f.read() # 读取文件内容
        f.seek(0) # 将文件指针移动到开头
        f.write(f"#{firstline}\n{content}") # 写入第一行和原内容
        f.write(f"\nuuid:{uuid}") # 写入最后一行
    print(f"A markdown file named {filename} has been moved from sample_card/{types[type - 1]}.md to {os.path.join(dir, year, 'essay')} with the first line: #{firstline}")
else: # 如果用户选择其他无效的选项
    # 打印错误信息并退出程序
    print("Invalid choice. Please enter 1, 2 or 3.")
    exit(1)
