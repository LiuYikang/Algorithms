#堆排序
#利用二叉堆来实现，大顶堆和小顶堆

#最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
#start为当前需要调整最大堆的位置，end为调整边界
#存储方式为顺序存储
def MaxHeapify(ary, start, end):
    root = start
    while True:
        child = 2 * root
        if child > end:
            break
        #找到根的子节点中的大的子节点
        if child + 1 <= end and ary[child] < ary[child + 1]:
            child = child + 1
        #如果根节点小于较大的子节点，则交换根节点和较大子节点
        if ary[root] < ary[child]:
            ary[root], ary[child] = ary[child], ary[root]
            #将根指向较大子节点，判断该子节点所在的子树是大顶堆
            root = child
        else:
            break


def HeapSort(ary):
    aryLength = len(ary)
    first = aryLength / 2 - 1    #最后一个非叶子节点
    for start in range(first, -1, -1):
        MaxHeapify(ary, start, aryLength - 1)
    #HeapSort
    for end in range(aryLength - 1, -1, -1):
        ary[end], ary[0] = ary[0], ary[end]
        MaxHeapify(ary, 0, end - 1)
    return ary
