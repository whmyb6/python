# encoding: utf-8

# 判断岛屿的个数
# 0代表海水 1代表陆地
# 如果陆地，上下左右为水，就定义为一个岛屿
#计算岛屿的个数

#=====
#算法原理：遍历每为数是否为1，为1代表为新大陆，发现一个新大陆，就采用递归法，按上、右、下、左 四个方面，遍历，把发现的新大陆标记为 >=2 的数，以此标记发现整个岛屿
# 遍历完成所有的表格，得到岛屿数====

import copy

map_source=[[0,0,0,1,1,0,0,1,1,1]
           ,[0,1,1,0,1,0,0,0,0,1]
           ,[1,0,0,0,1,0,0,1,1,1]
           ,[1,0,1,1,1,1,1,1,0,0]
           ,[0,0,0,0,1,1,0,1,0,1]
           ,[0,1,1,0,1,1,1,0,0,1]
            ]

# 新大陆标记
landList=[]

# 表示表格 列数
H=0

# 表示表格 行数
W=0


# 采用递归算法 ，遍历发现的新大陆
#标记所有的一个新的岛屿====
def find_newLand(X,Y,FlagValue):
    #print ("FlagValue",X,Y,FlagValue)
    #print("landList[X][Y]",landList[X][Y])
    #将标记写入当前发现的新大陆位置
    landList[X][Y]=FlagValue
    #  LEFT 向左遍历====
    dy = Y-1
    if dy >=0 :
        # 发现新大陆，开始递归
        if landList[X][dy] ==1:
            find_newLand(X,dy,FlagValue)
    #  DOWN 向下遍历 =====
    dx =X+1
    if dx < W :
        if landList[dx][Y]==1:
            find_newLand(dx,Y,FlagValue)
    # RIGHT  向右遍历====
    dy=Y+1
    if dy<H:
        if landList[X][dy]==1:
            find_newLand(X,dy,FlagValue)
    # UP 向上遍历 ====
    dx = X-1
    if dx >=0:
        if landList[dx][Y]==1:
            find_newLand(dx,Y,FlagValue)
    return 0

# 计算岛屿个数 ======
# 从头到尾，对每个节点进行遍历
def search_allPoin():
    flagValue=1
    for x in range(W):  #按行遍历
        for y in range(H):  #按列遍历
            # 1 表示发现一个新大陆===
            if landList[x][y] ==1 :
                flagValue += 1
                find_newLand(x,y,flagValue)
                #print("landList[X][Y]",x,y, landList[x][y])

    return flagValue -1

#==================  MAIN ==========================
if __name__ == '__main__':
    #flagValue =2
    landList=copy.deepcopy(map_source)
    H =len(landList[0]) # 获取列号
    W =len(landList)   # 获取行号

    for x in landList:
        print(x)
    #print(landList,H,W)
    num = search_allPoin()
    #find_newLand(0,3,2)
    print("")
    for x in landList:
        print(x)
    print("Result:" ,num )