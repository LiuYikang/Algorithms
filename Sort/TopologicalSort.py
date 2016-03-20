#��������
#��������Topological Sorting����һ�������޻�ͼ��DAG, Directed Acyclic Graph�������ж�����������С��Ҹ����б���������������������
#1.ÿ�����������ֻ����һ�Ρ�
#2.������һ���Ӷ��� A ������ B ��·������ô�������ж��� A �����ڶ��� B ��ǰ�档

#��������Ĺؼ���ά��һ�����Ϊ0�Ķ���ļ���
#���ڽӱ�洢ͼ���Ժܺõ�ʵ����������

#����   v����ʾ���㼯   e����ʾ�߼�
#v = ['a', 'b', 'c', 'd', 'e'], e=[('a','b'),('a','d'),('b','c'),('d','c'),('d','e'),('e','c')]

#���Ϊ0�Ķ���ļ���
def inDegreeZero(v, e):
    if not v:
        return None
    tmp = v[:]

    #ɾȥ����ȵĶ���
    for item in e:
        if item[1] in tmp:
            tmp.remove(item[1])

    if not tmp:
        return -1

    #ɾ��������ɾ������ı�
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