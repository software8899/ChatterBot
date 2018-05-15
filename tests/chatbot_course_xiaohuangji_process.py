#coding:utf-8
import os
import time

def row_process(file_name, row_max_num):
    """
        时间：20180514
        功能说明：
            处理文本，对每行超过最大限制长度的内容替换为三个省略号
        使用限制：
            脚本和需要处理的文件需要在同一目录，由于是频繁文件IO操作，受限于电脑性能，大文件运行时间会变慢。
        参数：
            1.完整的文件名字   例如：xiaohuangji.yml
            2.每行最大长度限制 例如：253
        运行：
             python chatbot_course_xiaohuangji_process.py
    """

    star_time = time.time()
    pwd = os.getcwd()
    row_total = 0
    process_count = 0
    file_path = os.path.join(pwd, file_name)
    name_tuple = os.path.splitext(file_name)
    row_max_num = int(row_max_num) // 3
    format_file_name = name_tuple[0]+'_format'+name_tuple[1]
    format_file_path = os.path.join(pwd, format_file_name)
    print("您输入的文件路径为【 %s 】 \n" % file_path)

    try:
        print('程序正在运行，请等待...')
        with open(file_path, 'rb') as file:
            if os.path.exists(format_file_path):
                os.remove(format_file_path)
                print('发现旧的格式化文件，已删除')

            prefix_first ="- - "
            prefix_second="  - "


            while True:
                has_line = file.readline()
                if not has_line:
                    break
                line = has_line.decode('utf-8').strip("\n")
                if line is '':
                    continue
                pairs = line.split("|", 2)
                if(len(pairs) != 2):
                    continue
                with open(format_file_name, 'ab+') as wfile:
                    str1 = ""
                    for oneWord in pairs[0]:
                        if is_chinese(oneWord):
                            str1 += oneWord
                    if len(str1) < 2:
                        continue
                    line_first = prefix_first + str1 + "\n"
                    if len(line_first) > row_max_num:
                        print("发现长度为 【 %s 】 的行，开始进行长度限制 >>>\n" % len(line_first))
                        line_first = line_first[0:row_max_num-3] + '...'
                        process_count += 1
                        print("处理后的内容 >>> \n%s\n处理后的长度 >>> 【 %s 】 \n" % (line_first, len(line_first)))


                    str2 = ""
                    for oneWord in pairs[1]:
                        if is_chinese(oneWord):
                            str2 += oneWord
                    if len(str2) < 2:
                        continue
                    line_second = prefix_second + str2 + "\n"
                    if len(line_second) > row_max_num:
                        print("发现长度为 【 %s 】 的行，开始进行长度限制 >>>\n" % len(line_second))
                        line_second = line_second[0:row_max_num-3] + '...'
                        process_count += 1
                        print("处理后的内容 >>> \n%s\n处理后的长度 >>> 【 %s 】 \n" % (line_second, len(line_second)))

                    wfile.write(line_first.encode('utf-8'))
                    wfile.write(line_second.encode('utf-8'))
                row_total += 1


        end_time = time.time()
        run_time = int(end_time - star_time)
        print("程序运行结束：\n  运行时间： %s 秒 \n  文件总行数： %s 行\n  处理的行数： %s 行\n  新的文件已写入： %s \n  感谢使用！" % (run_time, row_total, process_count, format_file_path))
    except IOError:
        print("Error: 没有找到文件或读取文件失败")

def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

def is_number(uchar):
    """判断一个unicode是否是数字"""
    if uchar >= u'\u0030' and uchar <= u'\u0039':
        return True
    else:
        return False

def is_alphabet(uchar):
    """判断一个unicode是否是英文字母"""
    if (uchar >= u'\u0041' and uchar <= u'\u005a') or (uchar >= u'\u0061' and uchar <= u'\u007a'):
        return True
    else:
        return False

def is_legal(uchar):
    """判断是否非汉字，数字和英文字符"""
    if not (is_chinese(uchar) or is_number(uchar) or is_alphabet(uchar)):
        return False
    else:
        return True


if __name__ == '__main__':
    file_name = input("请输入完整文件名：")
    row_max_num = input("请输入每行最大长度限制：")

    row_process(file_name, row_max_num)
