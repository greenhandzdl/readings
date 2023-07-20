#!/bin/bash

# 获取当前年份
year=$(date +%Y)
# 获取当前目录
dir=$(pwd)
# 生成的uuid
uuid=$(date +%Y%m%d%H%M%S)

# 定义一个函数，接受两个参数，第一个为父目录，第二个为子目录
check_folder() {
    # 判断父目录下是否存在子目录
    if [ -d "$1/$2" ]; then
        # 如果存在，打印提示信息
        echo "The folder $2 already exists in $1"
    else
        # 如果不存在，创建文件夹并打印提示信息
        mkdir "$1/$2"
        echo "The folder $2 has been created in $1"
    fi
}

# 调用函数，传入当前目录和年份作为参数
check_folder $dir $year
# 定义一个数组，存储要检查的文件夹名
folders=(book card essay 0_index 999_others)
# 遍历数组中的每个元素
for folder in ${folders[@]}; do
    # 调用函数，传入年份目录和元素作为参数
    check_folder "$dir/$year" $folder
done


# 问下用户选择是什么类型的卡片，并打印选项
echo "Please choose which type of card you want to create:"
echo "1. 事件卡"
echo "2. 人物卡"
echo "3. 图示卡"
echo "4. 基础卡"
echo "5. 新知卡"
echo "6. 新词卡"
echo "7. 术语卡"
echo "8. 行动卡"
echo "9. 金句卡"
read type


# 判断用户是否输入了有效的类型，如果没有就打印错误信息并退出程序，用if语句和test命令进行判断。
if ! test "$type" -ge 1 -a "$type" -le 9; then
    echo "Invalid type. Please enter a number between 1 and 9."
    exit 1
fi

types=(事件卡 人物卡 图示卡 基础卡 新知卡 新词卡 术语卡 行动卡 金句卡)

# 问下用户选择是在哪个子目录下创建文件，并打印选项
echo "Please choose which subfolder you want to create a file in:"
echo "1. book"
echo "2. card"
echo "3. essay"
read choice

# 判断用户是否输入了有效的子目录，如果没有就打印错误信息并退出程序，用if语句和test命令进行判断。
if ! test "$choice" -ge 1 -a "$choice" -le 3; then
    echo "Invalid choice. Please enter a number between 1 and 3."
    exit 1
fi

# 询问第一行的插入语，并读取用户的输入，并在文件中插入插入语，用read命令读取输入，用sed命令在文件中插入文本。
echo "Please enter the first line of the file:"
read firstline

# 根据用户的选择执行不同的操作
case $choice in
# 如果用户选择book
1)
    # 判断book目录下是否存在该书的目录，后续由用户选择（暂时不需要管这个分支）
    echo "You chose book. This feature is not implemented yet."
;;
# 如果用户选择card
2)
    # 在年份同级的文件里面copy相应的文件出来，并重命名为%Y%m%d%H%M%S这种格式的markdown文件，并根据用户选择的类型进行复制和重命名，并打印提示信息，用cp命令复制文件，用date命令获取当前时间。
    filename=$(date +%Y%m%d%H%M%S).md

    cp "$dir/sample_card/${types[$((type - 1))]}.md" "$dir/$year/card/$filename"

    sed -i "1i #$firstline" "$dir/$year/card/$filename"
    echo "uuid:$(date +%Y%m%d%H%M%S)" >> "$dir/$year/card/$filename"
    echo "A markdown file named $filename has been created in $dir/$year/card from sample_card/${types[$((type - 1))]}.md with the first line: #$firstline"
;;
# 如果用户选择essay
3)
    #判断该目录下是否有文件，如果没有就直接复制一个名为1.md的文件，如果有就读取最后一个文件名，再加一进行重命名，并打印提示信息，用ls命令列出文件，用wc命令计数，用if语句进行判断，用sort命令排序，用tail命令取最后一个，用cut命令分割文件名和扩展名，用算术运算符加一。
    count=$(ls "$dir/$year/essay" | wc -l)
    if test "$count" -eq 0; then
        #在年份同级的文件里面移动相应的文件出来，并根据用户选择的类型进行重命名，并打印提示信息，用mv命令移动文件。
        cp "$dir/sample_card/${types[$((type - 1))]}.md" "$dir/$year/essay/1.md"
        filename=1.md
    else
        last=$(ls "$dir/$year/essay" | sort -n | tail -n 1 | cut -d "." -f 1)
        next=$((last + 1))
        filename=$next.md
        cp "$dir/sample_card/${types[$((type - 1))]}.md" "$dir/$year/essay/$filename"
    fi

    sed -i "1i #$firstline" "$dir/$year/essay/$filename"
    echo "uuid:$(date +%Y%m%d%H%M%S)" >> "$dir/$year/essay/$filename"

    echo "A markdown file named $filename has been moved from sample_card/${types[$((type - 1))]}.md to $dir/$year/essay with the first line: #$firstline"
;;
# 如果用户选择其他无效的选项
*)
    # 打印错误信息并退出程序
    echo "Invalid choice. Please enter 1, 2 or 3."
    exit 1
esac
