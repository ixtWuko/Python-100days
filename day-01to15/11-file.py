"""
Day 11
读取文件
"""

def reading_file():
    try:
        with open('./res/ball.png', 'rb') as file_in:
            data = file_in.read()
            print(type(data))
        with open('./res/ball-copy.png', 'wb') as file_out:
            file_out.write(data)
    except FileNotFoundError as e:
        print('无法打开指定文件！')
    except IOError as e:
        print('无法读写指定文件！')
    print('执行成功')

if __name__ == '__main__':
    reading_file()