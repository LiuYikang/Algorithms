#ֱ�Ӳ�������
#1.�ӵ�һ��Ԫ�ؿ�ʼ����Ԫ�ؿ�����Ϊ�Ѿ�������
#2.ȡ����һ��Ԫ�أ����Ѿ������Ԫ�������дӺ���ǰɨ��
#3.�����ɨ���Ԫ�أ������򣩴�����Ԫ�أ�����Ԫ�غ���һλ
#4.�ظ�����3��ֱ���ҵ��������Ԫ��С�ڻ��ߵ�����Ԫ�ص�λ��
#5.����Ԫ�ز��뵽��λ�ú�
#6.�ظ�����2~5

def InsertionSort(ary):
    aryLength = len(ary)
    for i in range(1, aryLength):
        if ary[i] < ary[i-1]:
            tmp = ary[i]
            index = i       #�������ֵ���±�
            for j in range(i-1, -1, -1):    #��i-1ѭ����0
                if ary[j] > tmp:
                    ary[j+1] = ary[j]
                    index = j
                else:
                    break
            ary[index] = tmp
    return ary
