# -----------------------------控制台输入---------------------------
def study1():
    salary = input('please enter a string:')
    print(len(salary))


# ------------------------------字符串的方法-------------------------
def study2():
    str1 = '我们今天去踢足球，我们好开心啊'
    # ----------------------count 有多少个这样的字符串----------------
    count = str1.count('我们')
    print(count)
    # --------------------find 找到这个字符串返回索引，找不到返回-1--------
    index = str1.find('我们', 5, 17)
    print(index)
    # ---------------------split分割、join连接------------------------
    str2 = '小张：79 | 小李：88 | 小赵：83'
    post2 = str2.split('小张')
    print(post2)
    print('--------------------')
    str3 = '''
小王  10000元
小李  20000元
小徐  15000元
'''
    post3 = str3.splitlines()  # 按换行符切割
    print(post3)
    str4 = '|'.join(post2)
    print(str4)

    # -------------------去空格strip\lstrip\rstrip---------------
    str5 = '        haoa a     '
    str5 = str5.strip()
    print(str5)

    # --replace--
    str5 = str5.replace(' ', '')
    print(str5)

    # ------------------startswith\endswith是否以。。开头或者结尾---------------
    if str1.startswith('我们'):
        print('是以我们开头')

    # --------------------isdigit 是否都是数字---------------------
    if not str1.isdigit():
        print('不是都是数字')


# ---------------------------------列表的方法-----------------------------
def study3():
    # ----------------append在最后添加---------------
    strList = ['i', 'am', 'happy']
    strList.append('!')
    print(strList)
    # ----------------insert指定位置添加--------------
    strList.insert(2, 'always')
    print(strList)
    # -----------------pop根据索引删除---------------
    str1 = strList.pop(4)
    print(str1, end='')
    print(strList)
    # -----------------remove根据值删除---------------
    strList.remove('always')
    print(strList)
    # -----------------reverse列表翻转-----------------
    strList.reverse()
    print(strList)


if __name__ == '__main__':
    # test4("名字是:hs", '年龄是:18')
    # test1()
    study2()
