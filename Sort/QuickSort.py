#快速排序
#1.从数列中挑出一个元素作为基准数。
#2.分区过程，将比基准数大的放到右边，小于或等于它的数都放到左边。
#3.再对左右区间递归执行第二步，直至各区间只有一个数。

def QuickSort(ary):
    left, right = 0, len(ary)-1
    lp, rp = left, right
    base = ary[lp]
    while lp < rp:
        while ary[lp] <= base and lp < rp:
            lp += 1
        while ary[rp] >= base and lp < rp:
            rp += 1
        ary[lp], ary[rp] = ary[rp], ary[lp]
    #分区完成后把基准数放到指定位置，快速排序每次能固定一个基准数的位置
    ary[left], ary[lp] = ary[lp], ary[left]
    QuickSort(ary[left: lp])
    QuickSort(ary[lp+1: right])
    return ary
    