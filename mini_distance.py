# encoding: utf-8
#
#    计算有一个字符串变化为目标字符串的最小长度，并显示每一步的变化过程！
# author ： whm
# date   :  2019-7-28   开始编程
# update :  2019-7-31   修改 bug 。。。。。
# update :  2019-8-07   增加 变化详细情况 显示
# ========= python 2.7   =========
#
#  !!!!   注意：适用 PYTHON 2.7 !!!!  =========
#
#  ********************************************************************************************
#  整体思路：暴力搜索：以目标字符串的每一个字符，作为关键节点，对源字符串进行双向遍历：
#            向从前往后遍历，计算关键节点后，每一个字符到最后字符需要变化的长度，记录下来，
#            由于每个字符到最后位置，需要变化的长度数，有多个，而且保存在buffer中。
#            选择最小的长度数，做为该字符节点后需要变化的长度。以此类推，把目标节点的每个字符往后的
#            长度计算出来。
#            接着，再把每个字符，向从往前遍历，计算出最小长度。
#            最后，把每个字符节点的前向长度 和 后向长度 相加，取最小值，即为结果！！！
#***********************************************************************************************
#
#
#

import copy
source_str= 'horse' ; dest_str =  'ros'

#source_str = "intention" ; dest_str = "execution"

#source_str = "wonderful"  ; dest_str = "wrong"

source_str = "industry" ; dest_str   = "interest"

#source_str = "AdustrA" ; dest_str   = "AteresA"

#dest_str = 'ffff'
#source_str=dest_str = 'kkrthgetrytyrytyreyretyrtyretyrtuytriuytiuyoiuoiupopiuooiuod'

MAX_DISTANCE = 999999 #设置默认最大距离长度
PATH_END_FLAG = -999999 #设置路径的结束标记
#计算目标数列在源数列中的位置，并输出目标数列的位置列表
def findIndex(source_list,deset_list):
    destIndex =[]
    length = len(source_list)
    for i in deset_list:
        start = 0
        dtemp= []
        while start < length:
            try:
                start = source_list.index(i,start)
                dtemp.append(start)
                start +=1
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
    if len(l) > 0 :
        return max(l)
    else:
        return -1

# 逆向计算，从后往前计算===
# 思路：最后一位的长度为1，它的前一位为后一位的长度值加+1，以此类推，直到第一位
# 当前子串的字符，出现的长度 = min（它位置后的字符的长度）+1
# 便于计算
def clauSubLengthReserv(destIndexList,source_str):
    lengthDict ={} # 保存每一个位置后的子串长度（含自身），如：最后一位的  [第一公共子串位置,当前公共子串位置]=1
    postIndexDict = {}  # 保存每一个位置后的子串的字典
    length_source_str = len(source_str)
    length_destIndex= len(destIndexList)
    # 从最大 的位置 开始 到0 位置  ，进行遍历，计算每个位置到最后的长度
    for num_index in range(maxMutlArray(destIndexList),-1,-1):
        #找到 当前位置标识 出现在 位置标识列表中的位置
        tempis = findNumInLists(destIndexList,num_index)
        #print("num_index=", num_index,'tempis=',tempis)
        if len(tempis)>0:
            #循环查找 出现的每个数列
            for tempi in tempis:
                findNode = False
                tempLength=[MAX_DISTANCE ]  # 后一位数字的子串长度 缓冲列表
                #print('tempLength',tempLength,length_source_str,num_index)
                cLen = 0 # 字符处理的距离长度变量， 初始化距离 ======
                indexCount =0  #记录连续个数
                # 从当前位置的下一个位置开始，向后查找
                #print("****** num_index=%d,tempi=%d **** " %(num_index,tempi))
                tempLengthDict ={}

                for stempi in range(tempi +1 , length_destIndex):
                    cList = destIndexList[stempi]
                    #print("FOR num_index = %d tempi=%d,stempi=%d,cLen=%d,indexCount=%d" % (num_index,tempi,stempi, cLen,indexCount),'cList=',cList)
                    #findCurrIndex = -10 # 设置满足条件的序列位置
                    indexCount +=1
                    for numt in cList:
                        if numt > num_index: # 找到所有满足条件的的字符序列，放到缓冲区====
                            #findCurrIndex = numt
                            findNode = True
                            #保存每一位的最大值保存到缓冲
                            destTempLen = numt - num_index-  1 # indexCount  #计算两个位置之间的距离差
                            currLen = cLen if cLen > destTempLen else destTempLen  # 取两个位置之间的差最大值 作为距离
                            #print("found num_index =",num_index, " numt=", numt,'num_index',num_index,'indexCount=',indexCount,'cLen=',cLen,'destTempLen=',destTempLen,'result=',lengthDict.get((numt,stempi) )  )
                            tempLength.append(lengthDict.get((numt,stempi)) +currLen ) # 取缺省长度，保存到缓冲区
                            tempLengthDict[(numt,stempi)]= lengthDict.get((numt,stempi)) +currLen
                            #print("Add BUFFER num_index =%d" %num_index ,'tempLength=',tempLength)
                    # 如果两个字符位置之间非连续，且当前字符距离的长度小于 源字符串的长度或 目标字符串的长度，则距离计数累加
                    #if num_index != findCurrIndex-1 and ( stempi< length_source_str-1 or stempi < length_destIndex) :
                    if (stempi < length_source_str - 1 or stempi < length_destIndex):
                            cLen +=1 #两个数之间非连续，距离计数累加
                        #print('两个数之间非连续，计数累加Clen=%d num_index=%d '%(cLen,num_index))

                if num_index  == tempi : # 判断当前字符位置相同的情况
                    tempLength.append(MAX_DISTANCE -num_index - 1)

                if findNode : #对于满足顺序条件的字符序列，计算最短距离，作为当前位置字符 向后处理的距离
                    # 选择 最小的长度，做为当前字典的长度值
                    lengthDict[(num_index,tempi)]= min(tempLength)
                    #print("findNode num_index =%d" % num_index, 'tempLength=', lengthDict[(num_index, tempi)])
                    # 保存 记录 =====
                    multDict =[]
                    #buffer ={}
                    for k,v in tempLengthDict.items():
                        if v == min(tempLength):
                            multDict.append(k)
                    postIndexDict[(num_index,tempi)]=multDict
                else:     #没有满足顺序条件的字符序列=====
                    if indexCount > 0: #处理中间位置的字符的距离长度
                        destTempLen = length_source_str - num_index - 1
                        currLen = cLen if cLen > destTempLen else destTempLen
                        lengthDict[(num_index, tempi)] = currLen

                    else:# 处理最后一个位置的字符的距离长度
                        lengthDict[(num_index, tempi)] = cLen + length_source_str - num_index-1
                        #print("NOT findNode num_index =%d" % num_index, 'tempLength=', lengthDict[(num_index, tempi)])
                    postIndexDict[(num_index, tempi)] = []

                #print("lengthDict=",num_index,tempi, lengthDict[(num_index,tempi)])
    lengthDict[-1,-1]=0  # 防止找不到匹配字符的情况
    return lengthDict,postIndexDict

# 正向向计算，从前往后计算===
# 思路：最后一位的长度为0，它的前一位为后一位的长度值加+1，以此类推，直到第一位
# 当前子串的字符，出现的长度 = min（它位置后的字符的长度）+1
# 便于计算
def clauSubLengthForward(destIndexList,source_str):
    lengthDictForward ={} # 保存每一个位置后的子串长度（含自身），如：最后一位的  [第一公共子串位置,当前公共子串位置]=1
    postIndexDict = {}  # 保存每一个位置前的子串的字典

     # 从 0 位置到最大 的位置 ，进行遍历，计算每个位置到最后的距离
    for num_index in range(maxMutlArray(destIndexList)+1):
        #找到 当前位置标识 出现在 位置标识列表中的位置
        tempis = findNumInLists(destIndexList,num_index)
        #print("num_index=", num_index,'tempis=',tempis)
        #tempLength = [0]  # 前一位数字的子串长度 缓冲列表
        if len(tempis)>0:
            #循环查找 出现的每个数列
            for tempi in tempis:
                findNode = False
                cLen = 0 # 初始化距离 ======
                tempLength=[MAX_DISTANCE ]  # 前一位数字的子串长度 缓冲列表
                tempLengthDict ={}

                #print('START tempLength',tempLength,num_index,'tempi=',tempi)

                # 从当前位置的前一个位置开始，向前查找
                indexCount = 0  #记录连续个数
                for stempi in range(tempi-1,-1,-1 ):
                    indexCount +=1 #连续个数累加
                    cList = destIndexList[stempi]
                    #findCurrIndex = -10 # 设置满足条件的序列位置
                    #print("stempi=%d,cLen=%d" % (stempi, cLen),'cList:',cList)
                    for numt in cList:
                        #print("found numt=", numt, 'num_index=', num_index)
                        if numt < num_index:
                            findNode = True
                            #findCurrIndex = numt
                            #print("found numt=",numt,'num_index=',num_index )
                            destTempLen = num_index - numt- 1   #indexCount  #计算两个位置之间的距离差
                            currLen = cLen if cLen > destTempLen else destTempLen  # 取两个位置之间的差最大值 作为距离
                            #保存每一位的最大值长度保存到缓冲
                            tempLength.append(lengthDictForward.get((numt,stempi)) + currLen)
                            tempLengthDict[(numt, stempi)] = lengthDictForward.get((numt, stempi)) + currLen

                    #如果两个字符位置之间非连续
                    #if findCurrIndex != num_index-1:
                    cLen +=1  # 两个之间需要插入的个数累加
                if num_index  == tempi : # 判断当前字符位置相同的情况
                    if num_index > 0 :
                        tempLength.append( num_index )

                if findNode:  # 对于满足顺序条件的字符序列，计算最短距离，作为当前位置字符 向后处理的距离
                    lengthDictForward[(num_index, tempi)] = min(tempLength)
                    #print("findNode num_index =%d" % num_index, 'tempLength=', lengthDictForward[(num_index, tempi)])
                    # 保存 记录 =====
                    multDict =[]
                    for k,v in tempLengthDict.items():
                        if v == min(tempLength):
                            multDict.append(k)
                    postIndexDict[(num_index,tempi)]=multDict
                else:  # 没有满足顺序条件的字符序列=====
                    if indexCount > 0 :
                        currLen = cLen if cLen > num_index else num_index
                        lengthDictForward[(num_index, tempi)] = currLen
                    else:
                        lengthDictForward[(num_index, tempi)] =  num_index
                    postIndexDict[(num_index, tempi)] = []
                    #print("NOT findNode num_index =%d" % num_index, 'tempLength=', lengthDictForward[(num_index, tempi)])

    lengthDictForward[-1,1]=0 # 防止找不到匹配字符的情况
    return lengthDictForward,postIndexDict

#字典相加  ==========
def merge_Dict(x,y):
    buffer ={}
    for k,v in x.items():
        if k in y.keys():
            buffer[k] = y[k]+ v
            y.pop(k)
        else:
            buffer[k] = v + MAX_DISTANCE
    #print('dict Y=',y)
    for k,v in y.items():
        if k in x.keys():
            buffer[k] =x[k]+v
        else:
            buffer[k]=v +MAX_DISTANCE
    return buffer

# 计算最短距离 =========
def getDistance(source_str,dest_str):
    destIndex = findIndex(source_str,dest_str)
    print('destIdex=',destIndex)

   # 取得向后的距离字典
    back_Dict,post_back_Dict = clauSubLengthReserv(destIndex,source_str)
    print('   back_Dict:',back_Dict)
    print('   post_back_Dict:',post_back_Dict)

    # 取得向前的距离字典
    forward_Dict,post_forward_Dict = clauSubLengthForward(destIndex,source_str)
    print('   forward_Dict:',forward_Dict)
    print('   post_forward_Dict:',post_forward_Dict)

    # 合并相加字典并返回距离最小值
    allDict = merge_Dict(back_Dict,forward_Dict)

    for k,v in allDict.items():
        if v == min(allDict.values()):
            print('******<<  key Point:[{0[0]},{0[1]}]={1}  >>*******'.format(k,v))
            # 显示详细变化步骤 =====
            showAll_path(k,v,source_str,dest_str,post_back_Dict,post_forward_Dict)
            #print ('getAll_path=',getAll_path(k,source_str,dest_str,post_back_Dict,post_forward_Dict))
    # 返回最短变化数
    return min(allDict.values())

#显示所有路径变化的详细过程
def showAll_path(mini_key,value,source_str,dest_str,post_back_Dict,post_forward_Dict):
    pathjs = 0
    back_paths,forward_paths = getAll_path(mini_key,source_str,dest_str,post_back_Dict,post_forward_Dict)
    for k,back_path in back_paths.items():
        for k2,forward_path in forward_paths.items():
            pathjs +=1
            count = 0
            if len(back_path) + len(forward_path) == value or True:
                print('  ------- source : {} --( path:{} )------'.format(source_str,pathjs))
                for path in back_path:
                    count += 1
                    print('    %d %s' % (count,path))
                for path in forward_path:
                    count += 1
                    print('    %d %s' % (count,path))
                print('  ------- dest   : {} -------'.format(dest_str))

#计算所有路径变化记录======
def getAll_path(mini_key,source_str,dest_str,post_back_Dict,post_forward_Dict):
    #all_path ={}
    #计算后向路径
    next_post_key_lists = getBack_post_path(mini_key, post_back_Dict)
    #print("back:", next_post_key_lists)
    back_paths = showDetailStep(source_str, dest_str, next_post_key_lists)
    #计算前向路径
    next_post_key_lists = getBack_post_path(mini_key, post_forward_Dict)
    #print("forward:" ,next_post_key_lists )

    #修改字符串
    source_str = source_str[:mini_key[0]] + dest_str[mini_key[1]:]

    forward_paths = showDetailStep(source_str, dest_str, next_post_key_lists,False)
    #print('back_path',back_path)
    return back_paths,forward_paths

#计算前后的多条路径节点列表
def getBack_post_path(mini_key,post_back_Dict):
    curr_key = mini_key
    #计算向后的详细步骤
    back_post_paths =[]  #保存全部路由表 ==
    total_paths = 1

    # 从第0条路由开始记录点位置信息
    back_path = {0: [curr_key]}
    TaskEnd  = False
    while True:
        last_total_paths =0
        if TaskEnd:
            for i in range(total_paths):
                back_post_paths.append(back_path[i])
            break
        # 设置退出条件
        for v in back_path.values():
#            print(v)
            if v[-1] ==(PATH_END_FLAG,PATH_END_FLAG):
                TaskEnd =True
            else:
                TaskEnd =False
                break

        new_back_path = copy.deepcopy(back_path) # 新增一个变量，深度copy，防止Python中遍历字典过程中更改元素导致异常的解决方法

        for k,back_path_one in back_path.items():
            curr_key = back_path_one[-1]
            if(curr_key==(PATH_END_FLAG,PATH_END_FLAG) ):continue
            try:
                next_post_key_list = post_back_Dict[curr_key]
            except:
                next_post_key_list=[]

            if next_post_key_list==[]: #找到最后一个节点，退出
                new_back_path[k].append((PATH_END_FLAG,PATH_END_FLAG))
                #break
            else: #重复排列节点序列表   1*2*3
                TaskEnd = False
                paths_count = 0 # 路由标识 =====
                curr_total_paths = len(next_post_key_list)  # 当前节点到下一节点的有效路径数量==
                last_total_paths = total_paths
                total_paths *= curr_total_paths #总路由数量
                start_i = len(new_back_path)

                if start_i < total_paths:#复制多份节点记录
                    for i in range(0,total_paths -last_total_paths):
                        new_back_path[start_i+i] = copy.deepcopy(new_back_path[i])

            back_path = new_back_path  # 还原变量==

            for _ in range(last_total_paths):
                for next_post_key in next_post_key_list:
                    if back_path[paths_count][-1] != (PATH_END_FLAG,PATH_END_FLAG):
                        if back_path[paths_count][-1] == curr_key:
                            back_path[paths_count].append(next_post_key)
                    paths_count +=1
    return back_post_paths

# 显示后向每一步详细的字符变化过程
def showDetailStep( source_str,dest_str,next_post_key_lists,Back=True):
    save_source_str = source_str
    pointPathDict={}
    Path_js = 0
    for next_post_key_list in next_post_key_lists:
        Path_js +=1
        stepStr = []
        source_str = save_source_str
        # 计算后向记录变化情况
        if Back:
            for i  in range( len(next_post_key_list)-1,0,-1):
                res,source_str = TowCharPath(next_post_key_list,i,source_str,dest_str)
                stepStr.extend(res)
        else:
            # 计算前向记录变化情况
            #post_key_list_reverse = next_post_key_list[::-1]
            for i  in range( 1,len(next_post_key_list)):
                res,source_str = TowCharPath(next_post_key_list, i, source_str, dest_str,Back)
                stepStr.extend(res)

        pointPathDict[Path_js] =stepStr
    return pointPathDict

# 计算两个字符需要变化的节点详细情况
def TowCharPath(next_post_key_list,i,source_str,dest_str,Back = True):
    stepStr = []
    if Back:  # 后向计算,计算两点位置
        next_post_key = next_post_key_list[i]
        curr_key = next_post_key_list[i - 1]
        if next_post_key == (PATH_END_FLAG, PATH_END_FLAG):
            next_post_key = (len(source_str), len(dest_str))
        if  curr_key == (PATH_END_FLAG, PATH_END_FLAG):
            curr_key = (len(source_str), len(dest_str))

    else:      #前向计算
        next_post_key = next_post_key_list[i-1]
        curr_key = next_post_key_list[i]
        if next_post_key == (PATH_END_FLAG, PATH_END_FLAG):
            next_post_key =(-1,-1)
        if  curr_key == (PATH_END_FLAG, PATH_END_FLAG):
            curr_key =(-1,-1)


    # 处理找不到字符的情况
    if(curr_key[0] == -1 or curr_key[1]== -1): curr_key =(-1,-1)

    #print('curr_key,next_post_key', curr_key, next_post_key)
    charCount = 0
    source_distance = next_post_key[0] - curr_key[0] - 1  # 计算源字符串的距离长度
    dest_distance = next_post_key[1] - curr_key[1] - 1  # 计算目的字符串的距离长度
    # 特殊情况，退出
    if source_distance < 0 or dest_distance < 0:
        return stepStr,source_str

    add_distance = source_distance - dest_distance
    if source_distance - dest_distance >= 0:
        # 更新字符
        for i in range(dest_distance):
            charCount += 1
            s = "Update %s(%s)%s = %s(%s)%s" % (
                source_str[0:curr_key[0] + i + 1], source_str[curr_key[0] + 1 + i], source_str[curr_key[0] + i + 2:],
                source_str[0:curr_key[0] + i + 1], dest_str[curr_key[1] + 1 + i], source_str[curr_key[0] + i + 2:])
            # new_source_str[curr_key[0] + 1] = dest_str[curr_key[1] + 1]
            source_str = source_str[0:curr_key[0] + i + 1] + dest_str[curr_key[1] + 1 + i] + source_str[
                                                                                             curr_key[0] + i + 2:]
            #print(s)
            stepStr.append(s)
        # 删除字符
        if add_distance > 0:
            for i in range(add_distance):
                charCount += 1
                # 删除字符
                i=0
                s = "Delete %s(%s)%s = %s" % (
                    source_str[0:curr_key[0] + i + 1 + dest_distance], source_str[curr_key[0] + 1 + i + dest_distance],
                    source_str[curr_key[0] + i + 2 + dest_distance:]
                    , source_str[0:curr_key[0] + i + 1 + dest_distance] + source_str[
                                                                          curr_key[0] + i + 2 + dest_distance:])
                # new_source_str[curr_key[0] + 1] = dest_str[curr_key[1] + 1]
                source_str = source_str[0:curr_key[0] + i + 1 + dest_distance] + source_str[
                                                                                 curr_key[0] + i + 2 + dest_distance:]
                stepStr.append(s)
                #print(s)
    else:
        # 更新字符
        for i in range(source_distance):
            charCount += 1
            s = "Update %s(%s)%s = %s(%s)%s" % (
                source_str[0:curr_key[0] + i + 1], source_str[curr_key[0] + 1 + i], source_str[curr_key[0] + i + 2:],
                source_str[0:curr_key[0] + i + 1], dest_str[curr_key[1] + 1 + i], source_str[curr_key[0] + i + 2:])
            # new_source_str[curr_key[0] + 1] = dest_str[curr_key[1] + 1]
            source_str = source_str[0:curr_key[0] + i + 1] + dest_str[curr_key[1] + 1 + i] + source_str[
                                                                                             curr_key[0] + i + 2:]
            #print(s)
            stepStr.append(s)
        # 增加字符
        if add_distance < 0:
            for i in range(-add_distance):
                charCount += 1
                # 增加字符
                s = "Insert %s = %s(%s)%s" % (
                    source_str,
                    source_str[0:curr_key[0] + i + 1 + source_distance],
                    dest_str[curr_key[1] + 1 + i + source_distance], source_str[curr_key[0] + i + 1 + source_distance:])
                # new_source_str[curr_key[0] + 1] = dest_str[curr_key[1] + 1]
                source_str = source_str[0:curr_key[0] + i + 1 + source_distance] + dest_str[
                    curr_key[1] + 1 + i + source_distance] + source_str[curr_key[0] + i + 1 + source_distance:]
                stepStr.append(s)
                #print(s)
    #stepStr.append(source_str)
    return stepStr,source_str

#==================  MAIN ==========================
if __name__ == '__main__':
    d1 = len(source_str)
    d2 = len(dest_str)

    MAX_DISTANCE = d1 if d1>d2 else d2
    print('\n   OK Result = %d   !'%getDistance(source_str,dest_str))

# ==================   END ==========================-