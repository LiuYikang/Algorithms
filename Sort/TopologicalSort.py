#拓扑排序
#拓扑排序（Topological Sorting）是一个有向无环图（DAG, Directed Acyclic Graph）的所有顶点的线性序列。且该序列必须满足下面两个条件：
#1.每个顶点出现且只出现一次。
#2.若存在一条从顶点 A 到顶点 B 的路径，那么在序列中顶点 A 出现在顶点 B 的前面。

#拓扑排序的关键是维护一个入度为0的顶点的集合
#用邻接表存储图可以很好的实现拓扑排序

#输入   v：表示顶点集   e：表示边集
#v = ['a', 'b', 'c', 'd', 'e'], e=[('a','b'),('a','d'),('b','c'),('d','c'),('d','e'),('e','c')]

#入度为0的顶点的集合
def inDegreeZero(v, e):
    if not v:
        return None
    tmp = v[:]

    #删去有入度的顶点
    for item in e:
        if item[1] in tmp:
            tmp.remove(item[1])

    if not tmp:
        return -1

    #删除包含已删除顶点的边
    eTmp = []
    for item in tmp:
        for i in range(len(e)):
            if item in e[i]:
                e[i] = "todel"
    if e:  
        eset=set(e)  
        eset.remove('todel')  
        e[:]=list(eset)

    if v:
        for item in tmp:
            v.remove(item)
    return tmp

def topoSort(v, e):
    result = []
    while True:
        nodes = inDegreeZero(v, e)
        if not nodes:
            break
        if nodes == -1:
            return None
        result.extend(nodes)
    return result

v=['a','b','c','d','e']  
e=[('a','b'),('a','d'),('b','c'),('d','c'),('d','e'),('e','c')]  
print v,e
res=topoSort(v,e)  
print(res)