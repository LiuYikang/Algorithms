#������
#���ö������ʵ�֣��󶥶Ѻ�С����

#���ѵ��������ѵ�ĩ���ӽڵ���������ʹ���ӽڵ���ԶС�ڸ��ڵ�
#startΪ��ǰ��Ҫ�������ѵ�λ�ã�endΪ�����߽�
#�洢��ʽΪ˳��洢
def MaxHeapify(ary, start, end):
    root = start
    while True:
        child = 2 * root
        if child > end:
            break
        #�ҵ������ӽڵ��еĴ���ӽڵ�
        if child + 1 <= end and ary[child] < ary[child + 1]:
            child = child + 1
        #������ڵ�С�ڽϴ���ӽڵ㣬�򽻻����ڵ�ͽϴ��ӽڵ�
        if ary[root] < ary[child]:
            ary[root], ary[child] = ary[child], ary[root]
            #����ָ��ϴ��ӽڵ㣬�жϸ��ӽڵ����ڵ������Ǵ󶥶�
            root = child
        else:
            break


def HeapSort(ary):
    aryLength = len(ary)
    first = aryLength / 2 - 1    #���һ����Ҷ�ӽڵ�
    for start in range(first, -1, -1):
        MaxHeapify(ary, start, aryLength - 1)
    #HeapSort
    for end in range(aryLength - 1, -1, -1):
        ary[end], ary[0] = ary[0], ary[end]
        MaxHeapify(ary, 0, end - 1)
    return ary
