#BubbleSort


#Basic algorithm
def BubbleSort1(array):
    n = len(array)
    for i in range(n):
        for j in range(1, n-i):
            if array[j-1] > array[j]:
                #exchange
                array[j-1], array[j] = array[j], array[j-1]
    return array


#Optimization 1
#Use a mark to record the state if there is no exchange
def BubbleSort2(array):
    n = len(array)
    for i in range(n):
        #record the state
        flag = 1
        for j in range(1, i-1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                #if exchange happen, change the state
                flag = 0
        if flag:
            break
    return array


#Optimization 2
#Record the last data exchange position of each iteration
#Use the position to determine the scope of the next iteration
def BubbleSort3(array):
    n = len(array)
    p = n
    for i in range(n):
        flag = 1
        for j in range(1, p):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
                flag = 0
                #record the position
                p = j
        if flag:
            break
    return array
