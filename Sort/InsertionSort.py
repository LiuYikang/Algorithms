#直接插入排序
#1.从第一个元素开始，该元素可以认为已经被排序
#2.取出下一个元素，在已经排序的元素序列中从后向前扫描
#3.如果被扫描的元素（已排序）大于新元素，将该元素后移一位
#4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
#5.将新元素插入到该位置后
#6.重复步骤2~5

def InsertionSort(ary):
    aryLength = len(ary)
    for i in range(1, aryLength):
        if ary[i] < ary[i-1]:
            tmp = ary[i]
            index = i       #待插入的值得下标
            for j in range(i-1, -1, -1):    #从i-1循环到0
                if ary[j] > tmp:
                    ary[j+1] = ary[j]
                    index = j
                else:
                    break
            ary[index] = tmp
    return ary
