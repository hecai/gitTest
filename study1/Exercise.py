def test1(str1, str2):
    str3 = str1.split(':', -1)
    str4 = str2.split(':', -1)
    print(str3[1] + ':' + str4[1])


def test2():
    highStr = input('请输入你的身高(单位米):')
    weightStr = input("请输入你的体重(单位公斤):")
    ageStr = input("请输入你的年龄:")
    high = float(highStr)
    weight = float(weightStr)
    age = int(ageStr)
    if age < 10:
        print('10岁以下儿童不参与健康评估')
    elif 10 <= age < 60:
        if weight / (high ** 2) > 24:
            print('用户体重超重')
        elif weight / (high ** 2) < 18:
            print('用户体重超轻')
        else:
            print('用户体重正常')
    else:
        print('60岁以上老人不参与健康评估')


def test3(str):
    if str.count(' '):
        print('有空格')
        return False
    elif str.count('@') != 1:
        print('没有@或者多个@')
        return False
    else:
        strList = str.split('@')
        if strList[0] == '':
            print('@前面无字符')
            return False
        else:
            if strList[1].count('.') != 1:
                print('@后面没有或者多个.')
                return False
            else:
                strList2 = strList[1].split('.')
                if strList2[0] == '' or strList2[1] == '':
                    print('.前或后无字符')
                    return False
                else:
                    print('email格式正确')
                    return True


def test4():
    # str1 = '大家好，我的名字叫：'
    # str2 = '黑羽白月'
    # print('%s%s' % (str1, str2))

    # str1 = input('输入你的名字:')
    # str2 = input('输入你的年龄:')
    # print(f'你的名字:{str1} 你的年龄:{str2}')

    info = [
        ['user1', 345.6, 12, '黄金'],
        ['user2', 2345.6, 8, '白银'],
        ['user3555', 55345.6, 22, '钻石'],
    ]

    for infoX in info:
        print(f'用户：{infoX[0]:>7}，积分：{infoX[1]:4f}，等级：{infoX[2]}，头衔：{infoX[3]}')


def getStrList(str1):
    str1List = str1.splitlines()
    # print(str1List)
    names = []
    for str1 in str1List:
        str1 = str1.strip()
        if str1 == '':
            continue
        names.append(str1)
    print(names)
    return names


def test5():
    str1 = '''
        熊宁
        杰益

        王伟伟

        青芳

        玉琴
        焦候涛
        莫福
        杨高旺
        唐欢欢
        韩旭
        '''

    str2 = '''
        焦候涛 
        熊宁 
        玉琴 

        骆龙 

        韩旭 
        杨高旺

        杰益  

        莫福  

        伟伟

        李福  
        '''
    names1 = getStrList(str1)
    names2 = getStrList(str2)
    for name in names2:
        if name not in names1:
            print(name)


def test6():
    ageTable = '''
        诸葛亮, 28
        刘备, 48
        刘琦, 25
        赵云, 32
        张飞, 43
        关羽, 45
    '''
    ageTableList = ageTable.splitlines()
    ages = []
    for age in ageTableList:
        age = age.strip()
        if age != '':
            ages.append(age)
    print(ages)
    largeList = []
    smallList = []
    for age in ages:
        name, age = age.split(',')
        if int(age) >= 30:
            largeList.append(name)
        else:
            smallList.append(name)
    print('大于等于30的人有：')
    print(largeList)
    print('小于30的人有：')
    print(smallList)


def calculate_score(matches):
    gywin = 0
    zfwin = 0
    for match in matches:
        gy = match[0]
        zf = match[1]
        if if_win(gy, zf) == 1:
            gywin += 1
        elif if_win(gy, zf) == -1:
            zfwin +=1
    matchNum = len(matches)
    if gywin > zfwin:
        print(f'关羽 {matchNum}局赢了{gywin}局，关羽胜出')
    elif zfwin > gywin:
        print(f'张飞 {matchNum}局赢了{zfwin}局，张飞胜出')
    else:
        print('平局')


def if_win(str1, str2):
    if str1 == '剪刀':
        if str2 == '石头':
            return -1
        elif str2 == '布':
            return 1
        else:
            return 0
    elif str1 == '石头':
        if str2 == '石头':
            return 0
        elif str2 == '布':
            return -1
        else:
            return 1
    else:
        if str2 == '石头':
            return 1
        elif str2 == '布':
            return 0
        else:
            return -1


if __name__ == '__main__':
    # test1("名字是:hs", '年龄是:18')
    # test3('gmail@163.com')
    # test6()
    calculate_score([["剪刀", "石头"], ["布", "剪刀"], ["剪刀", "剪刀"]])