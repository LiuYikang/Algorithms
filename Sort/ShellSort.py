#ϣ������
#����������һ�����в����зֱ���в��������ظ�����̣�����ÿ���ø������У����������ˣ����������ˣ������С�
#����������ֻ��һ���ˡ�������ת��������Ϊ�˸��õ�������㷨���㷨������ʹ�������������

def ShellSort(ary):
    aryLength = len(ary)
    gap = aryLength / 2    #��ʼ����
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
        gap /= 2         #�������ò���
    return ary
