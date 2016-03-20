#归并排序
#分治思想

def MergeSort(ary):
    if len(ary) <= 1:
        return ary
    mid = len(ary) / 2     #二分分解
    left = MergeSort(ary[:mid])
    right = MergeSort(ary[mid:])
    return Merge(left, right)

#Merge Function: Merge two array to a sorted one array
def Merge(leftAry, rightAry):
    l, r = 0, 0
    ret = []
    leftLength, rightLength = len(leftAry), len(rightAry)
    while l < leftLength and r < rightLength:
        if leftAry[l] < rightAry[r]:
            ret.append(leftAry[l])
            l += 1
        else:
            ret.append(rightAry[r])
            r += 1
    ret += leftAry[l:]
    ret += rightAry[r:]
    return ret
