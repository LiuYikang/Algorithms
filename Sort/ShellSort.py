#希尔排序
#将数组列在一个表中并对列分别进行插入排序，重复这过程，不过每次用更长的列（步长更长了，列数更少了）来进行。
#最后整个表就只有一列了。将数组转换至表是为了更好地理解这算法，算法本身还是使用数组进行排序。

def ShellSort(ary):
    aryLength = len(ary)
    gap = aryLength / 2    #初始步长
    while gap > 0:
        for i in range(gap, aryLength):
            tmp = ary[i]
            j = i
            for j in range(i, gap-1, -gap):   #InsertionSort
                if ary[j] > tmp:
                    ary[i] = ary[j-gap]
                else:
                    break
            ary[j] = tmp
        gap /= 2         #重新设置步长
    return ary
