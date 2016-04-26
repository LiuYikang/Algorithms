#Longest Increasing Subsequence
#O(n) space and O(nlogn) time
#B[N],for every B[i] in B[N], record the minimum element of the length i LIS.

#Find the exchange location
def BinarySearch(array, value, length):
    low, high = 0, length - 1
    while low < high:
        mid = (low + high) / 2
        if array[mid] == value:
            return mid
        elif array[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return low

def LIS(array, length):
    B = [0 for i in range(length)]
    B[0] = array[0]
    LISlen = 1

    for i in range(1, nlength):
        if array[i] > B[LISlen - 1]:
            B[LISlen] = array[i]
            LISlen += 1
        else:
            loc = BinarySearch(B, array[i], LISlen)
            B[loc] = array[i]

    return LISlen
