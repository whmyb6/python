# encoding: utf-8
# 搜索最大公共子串===
#思路：
#根据源数列，标出目标数列在源数列中的位置列表，保存的目标数列的位置列表
#对目标数列的位置列表，按逆向从列表长度 数值最大位置到 1 ，计算每个的顺序的数值的长度，保存到长度字典
# 计算长度列表的MAX，即结果
# #
#   date：  2019-7-21
#
#

list1 =[2,3,4,0,1,3]
list2 =[0,1,2,3,3,4]
#list2=list1 =[1,1]
#list1=list2 =[8,9,6,9,8,9,9,9,9,9,9,9,9]
#list1=[5,5,4,0,5,3,2,1,9,9,8,1,4,1,8,8,7,5,2,0,7,4,6,5,2,1,7,3,8,2]
#list2=[1,7,9,7,2,0,6,1,9,6,2,2,5,4,3,7,4,9,7,0,5,3,2,3,6,0,4,0,9,7]
#list1=list2=[999,999,1000,10001]

#list1=[5,5,4,0,5,3,2,1,9,9,8,1,4,1,8,8,7,5,2,0,7,4,6,5,2,1,7,3,8,2]
#list2=[1,7,9,7,2,0,6,1,9,6,2,2,5,4,3,7,4,9,7,0,5,3,2,3,6,0,4,0,9,7]

list1=[7,0,9,8,3,6,2,4,8,1,2,0,2,0,5,3,5,6,9,0,7,8,3,2,3,2,3,5,9,6]
list2=[8,2,1,6,1,0,3,3,9,7,1,6,4,6,2,3,8,6,8,9,6,3,8,3,8,1,7,2,2,5]
# === 13

list1=[3,2,0,8,3,8,3,5,3,9,4,6,8,2,9,1,0,7,1,3,4,1,0,3,0,6,9,2,5,0]
list2=[1,7,3,3,6,2,0,5,0,3,2,2,9,6,0,6,9,3,3,5,8,8,1,9,2,7,7,9,6,2]
#=== 12======

#list1=[0,0,1,8,0,9,6,8,5,4,4,1,0,5,8,8,5,2,6,2,9,6,0,9,2,4,4,5,1,5]
#list2=[5,7,5,3,7,1,3,3,9,0,7,4,5,0,1,4,0,6,9,2,2,4,8,2,1,9,9,0,3,3]
#====10

#计算目标数列在源数列中的位置，并输出目标数列的位置列表
def findIndex(source_list,deset_list):
    destIndex =[]
    length = len(source_list)
    for i in deset_list:
        start = 0
        dtemp= []
        while start < length:
            #print(start)
            try:
                start = source_list.index(i,start)
                start +=1
                dtemp.append(start)
            except:
                break
        destIndex.append(dtemp)
    return destIndex

# 找出数值在二维数列中出现的所有位置
def findNumInLists(destIndexList,num):
    rindex =[]
    index =-1

    for i in destIndexList:
        index +=1
        if num in i:
            rindex.append(index)
    return rindex

# 计算 多维数列中的最大值
def maxMutlArray(destIndexList):
    l=[]
    for m in destIndexList:
        for a in m:
            l.append(a)
    return max(l)


# 逆向计算，从后往前计算===
# 思路：最后一位的长度为1，它的前一位为后一位的长度值加+1，以此类推，直到第一位
# 当前子串的字符，出现的长度 = max（它位置后的字符的长度）+1
# 便于计算
def clauSubLengthReserv(destIndexList):
    lengthDict ={} # 保存每一个位置后的子串长度（含自身），如：最后一位的  [第一公共子串位置,当前公共子串位置]=1
    length_destIndex = len(destIndexList)
    # 从最大 的位置 开始 到1 位置  ，进行遍历，计算每个位置到最后的长度
    for num_index in range(maxMutlArray(destIndexList),0,-1):
        #找到 当前位置标识 出现在 位置标识列表中的位置
        tempis = findNumInLists(destIndexList,num_index)
        print("num_index=", num_index)
        if len(tempis)>0:
            #循环查找 出现的每个数列
            for tempi in tempis:
                cLen = 1
                tempLength=[0]  # 后一位数字的子串长度 缓冲列表
                #print("tempi=", tempi)
                # 从当前位置的下一个位置开始，向后查找
                for stempi in range(tempi + 1, length_destIndex):
                    cList = destIndexList[stempi]
                    for numt in cList:
                        if numt > num_index:
                            #print("found stempi=", stempi)
                            #保存每一位的最大值保存到缓冲
                            tempLength.append(lengthDict.get((numt,stempi),0))
                # 选择 最大的长度，做为当前字典的长度值
                lengthDict[(num_index,tempi)]=max(tempLength)+cLen
                print("lengthDict=",num_index,tempi, lengthDict[(num_index,tempi)])
    #return max(lengthDict,key=lengthDict.get)
    return lengthDict.values()

#  此算法复杂度高，有错误，选择放弃 #########@@@@@！！！！！！！！！！！！！！！！！
# 从1号位置开始循环到最大号的位置数列长度，  计算每个数字的序列长度，并保存
def caluSubLength(destIndexList):
    maxLen=[]
    counti = 0  # 测试用

    #for numi in range(len(destIndexList)):
    # 从 1 位置 开始 到 最大 的位置，进行遍历，计算每个位置到最后的长度
    for num_index in range(maxMutlArray(destIndexList)):
        cLen = 0
        curr_num_index = num_index + 1  #位置标识
        #找到 当前位置标识 出现在 位置标识列表中的位置
        tempis = findNumInLists(destIndexList,curr_num_index)
        print('tempis',tempis)
        #找到后，从当前位置的下一个位置开始，向后查找
        if len(tempis)>0:
            length_destIndex = len(destIndexList)

            for tempi in tempis:
                # print('curr_num=',curr_num)
                # print('tempi=',tempi)
                cLen = 1
                #从当前位置的下一个位置开始，向后查找

                for stempi in range(tempi+1,length_destIndex):
                    # 如果当前的最大子串长度值 大于等于 剩余位置标识列表的长度，就退出循环，节省运算时间
                    counti+=1
                    if len(maxLen) >0:
                        if max(maxLen) >= length_destIndex - stempi:
                            #print("max()",max(maxLen),'length=',length_destIndex - stempi,'counti=',counti  )
                            break
                            #pass

                    #取出位置标识列表中的数据列表，如果取得的数据大于当前数据，意味序列满足顺序要求，子串长度加一
                    cList = destIndexList[stempi]
                    for numt in cList:
                        if numt > curr_num_index:
                            cLen+=1
                            curr_num_index = numt
                            break
                #print('cLen=',cLen)
                #子串长度保存到buffer
                maxLen.append(cLen)
    return maxLen

#交换数列的顺序，进行计算，得到最大值
def allArrayLists(list1,list2):
    source_list = list2
    deset_list = list1
    dl = findIndex(source_list, deset_list)
    print("dest_index_1=",dl)
    cL1 = caluSubLength(dl)
    c1 = max(cL1)

    source_list = list1
    deset_list = list2
    dl = findIndex(source_list, deset_list)
    print("dest_index_2=",dl)
    cL2 = caluSubLength(dl)
    c2 = max(cL2)
    print('num1=',c1,'num2 =',c2)
    return  c1 if c1>c2 else c2

#交换数列的顺序，进行计算，得到最大值
def allArrayListsResrv(list1,list2):
    source_list = list1
    deset_list = list2
    dl = findIndex(source_list, deset_list)
    print("dest_index_1=",dl)
    cL1 = clauSubLengthReserv(dl)
    print("dict=",cL1)
    print( max(cL1))
    return max(cL1)

## =====   mian =========
print ('max length=',allArrayListsResrv(list1,list2))
#index = findNumInLists(dl,6)
#print('num=',2,'index =',index)