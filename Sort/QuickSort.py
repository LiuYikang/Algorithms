#��������
#1.������������һ��Ԫ����Ϊ��׼����
#2.�������̣����Ȼ�׼����ķŵ��ұߣ�С�ڻ�������������ŵ���ߡ�
#3.�ٶ���������ݹ�ִ�еڶ�����ֱ��������ֻ��һ������

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
    #������ɺ�ѻ�׼���ŵ�ָ��λ�ã���������ÿ���̶ܹ�һ����׼����λ��
    ary[left], ary[lp] = ary[lp], ary[left]
    QuickSort(ary[left: lp])
    QuickSort(ary[lp+1: right])
    return ary
    