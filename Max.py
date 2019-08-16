# encoding: utf-8

#
# 从两个数列中，按数字出现顺序，组成一个最大的数列
# 数列由 K 个数字 组成
#
#
# 制作：whm
# 日期：2019-7-11
#

# 设置最小的值，方便比较
MIN_VALUE = -9999999

# 数列1
num1 = [3, 4, 6, 5]
# 数列2
num2 = [9, 1, 2, 5, 8, 3]
# 取数的长度
k = 7

# num1=[3,9]
# num2=[8,9]
# k = 3

# num1 =[6,7]
# num2 =[6,0,4]
# k=5

# num1=[1,5,6,8]
# num2=[1,5,7,7]
# k=6

# num1=[5,7,8,88,8,9]
# num2=[5,7,8,88,8,9]
# k=11

# print(num1)
# print(num2)

# 全局变量，计算的结果==
curr_l = []


# 全排列=======
def allarray(num1, num2):
    l = []  # 存储计算结果
    while True:
        # 按从左至右，按位搜索===
        if len(num1) > 0:
            t1 = num1[0]
        else:
            t1 = MIN_VALUE
        if len(num2) > 0:
            t2 = num2[0]
        else:
            t2 = MIN_VALUE
        if t1 == MIN_VALUE and t2 == MIN_VALUE:
            break
        # 处理大小不同的情况
        if t1 > t2:
            l.append(t1)
            if len(num1) > 1:
                num1 = num1[1:]
            else:
                num1 = []
        #
        else:
            if t1 < t2:
                l.append(t2)
                if len(num2) > 1:
                    num2 = num2[1:]
                else:
                    num2 = []
            else:  # 处理大小相同的情况
                l.append(t1)

                flag = find_next_max(num1, num2, t1)
                print('flag=', flag)

                if (flag == 1):
                    if len(num1) > 1:
                        num1 = num1[1:]
                    else:
                        num1 = []
                else:
                    if len(num2) > 1:
                        num2 = num2[1:]
                    else:
                        num2 = []
    return l


# 查找相同数字后的最大值所在的数据列表的组号：flag
# 返回 组号====
def find_next_max(num1, num2, val):
    nextnum1 = MIN_VALUE
    nextnum2 = MIN_VALUE
    if len(num1) > 1:
        num1 = num1[1:]
    else:
        return 2
    if len(num2) > 1:
        num2 = num2[1:]
    else:
        return 1

    print('num1=', num1)
    print('num2=', num2)

    # 循环查询下一个数字，找到最大的数列的标识
    while True:
        if (len(num1) > 0):
            nextnum1 = num1[0]
        if (len(num2) > 0):
            nextnum2 = num2[0]

        print('nextnum1=', nextnum1, 'nextnum2=', nextnum2)
        if nextnum1 > nextnum2:
            return 1
        else:
            if nextnum1 < nextnum2:
                return 2
            else:
                if val > nextnum1:
                    return 1
                else:
                    if len(num1) > 1:
                        num1 = num1[1:]
                    else:
                        return 2
                    if len(num2) > 1:
                        num2 = num2[1:]
                    else:
                        return 1


# 回溯算法====
# 原理：按flag组号，进行回溯=====
def priv_array(num1, num2, start, k, flag, num_index):
    old_num1 = num1
    old_num2 = num2
    print("priv_array : p_num1=", num1, "p_num2=", num2)

    # 按flag标识的数列，进行回溯
    if (flag == 1):
        num1 = num1[0:num_index]
    else:
        num2 = num2[0:num_index]
    print("tttt  p_num1=", num1, "p_num2=", num2)

    length_num1 = len(num1)
    length_num2 = len(num2)

    max1 = MIN_VALUE
    max2 = MIN_VALUE

    maxc = 0
    #    flag =1

    if length_num1 > 0 or length_num2 > 0:
        if len(num1) > 0: max1 = max(num1)
        if len(num2) > 0: max2 = max(num2)

    print("priv_array  max1=", max1, "max2=", max2)

    num1 = old_num1
    num2 = old_num2
    # 计算最大值及调整后的数列
    if flag == 1:
        maxc = max1
        num_index = num1.index(maxc)
        num1 = num1[num_index + 1:]
    else:
        maxc = max2
        num_index = num2.index(maxc)
        num2 = num2[num_index + 1:]

    print('pppp max=', maxc, "num1=", num1, "num2=", num2, 'start=', start, 'k=', k, "flag=", flag)
    # 如果 剩余的数列长度 小于 需要 的数字长度，继续 回溯
    if len(num1) + len(num2) < k - start - 1:
        print('priv-->>', k, start)
        # 递归，沿着flag 方向，向前回溯，查找最大值========
        return priv_array(old_num1, old_num2, start, k, flag, num_index)
    else:
        print(" priv return maxc=", maxc, 'num1=', num1, 'num2=', num2)
        # 返回 回溯后的最大值，和满足正向递归的数列
        return maxc, num1, num2


# 正向搜索 ===========
def selectMax(num1, num2, start, k):
    max1 = MIN_VALUE
    max2 = MIN_VALUE

    length_num1 = len(num1)
    length_num2 = len(num2)

    # 如果 数列的长度 等于 需要的数据长度 ，执行全排列并返回
    if length_num1 + length_num2 == k - start:
        last_array = allarray(num1, num2)
        curr_l.append(last_array)
        print(' MAIN last_array=', last_array)
        return curr_l
    # 如果 数列长度 小于 需要 的数据长度，返回空
    if length_num1 + length_num2 < k - start:
        return []

    if length_num1 > 0 or length_num2 > 0:
        if len(num1) > 0: max1 = max(num1)
        if len(num2) > 0: max2 = max(num2)
    # 最大值
    maxc = 0

    old_num1 = num1
    old_num2 = num2

    # 数列组的标识
    flag = 1
    # 最大值的位置指针
    num_index = -1

    # 正向计算 数列的最大值，和剩余的数据列表
    if max1 > max2:
        maxc = max1
        num_index = num1.index(maxc)
        num1 = num1[num_index + 1:]
    if max2 > max1:
        flag = 2
        maxc = max2
        num_index = num2.index(maxc)
        num2 = num2[num_index + 1:]
    if max2 == max1:
        maxc = max1
        index_max_1 = num1.index(maxc)
        index_max_2 = num2.index(maxc)
        if index_max_1 <= index_max_1:
            num1 = num1[index_max_1 + 1:]
            num_index = index_max_1
        else:
            flag = 2
            num2 = num2[index_max_2 + 1:]
            num_index = index_max_2
    # 如果 剩余的数据列表 的长度 小于 所需的数据个数，数据进行回溯，一直找到满足长度条件的 大数值 和数据列表
    if len(num1) + len(num2) < k - start - 1:
        maxc, num1, num2 = priv_array(old_num1, old_num2, start, k, flag, num_index)
        # print("a=",a)

    #    print( 'max=',maxc ,"num1=",num1,"num2=",num2,'start=',start,'k=',k)
    # 把结果保存到全局变量，并把计数指针 加1
    start += 1
    curr_l.append(maxc)
    print('  MAIN max =', maxc, "num1=", num1, "num2=", num2, 'start=', start, 'k=', k)

    # 如果计数个数 小于 所需要的总数 ，继续递归，按正向查询方向递归
    if start < k:
        return selectMax(num1, num2, start, k)
    else:
        # 计数个数 到达 需要的总数，返回结果！
        return curr_l


# main ------------
print('result=', selectMax(num1, num2, 0, k))
