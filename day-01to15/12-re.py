"""
Day 12
正则表达式
"""

import re

def case_one():
    m1 = False
    m2 = False
    while not m1 or not m2:
        username = input('请输入用户名：')
        qq_number = input('请输入QQ号码：')
        m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
        if not m1:
            print('请输入有效的用户名。')
        m2 = re.match(r'[1-9]\d{4,11}$', qq_number)
        if not m2:
            print('请输入有效的qq号码。')
        if m1 and m2:
            print('您的用户名和qq号码为：%s，%s' % (username, qq_number))
            break

def case_two():
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('--------分割线--------')
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('----------------------')
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())

def case_three():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。,.]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)

if __name__ == '__main__':
    #case_one()
    case_two()
    case_three()