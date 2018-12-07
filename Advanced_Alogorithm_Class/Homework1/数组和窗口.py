def answer():
    strArray = input().split()
    array = []

    for i in range(len(strArray)):
        array.append(int(strArray[i]))
    window_size = int(input())
    sum = 0
    max_value = -1000000
    start_index = 0
    end_index = 0
    if window_size == 0 :
        # sum = 0
        # for i in range(len(array)):
        #     sum += array[i]
        # print(sum)
        sum = 0
    # max_value = -int('inf')

    if  window_size <  len(array) :
        end_index = window_size-1
        while (end_index <= len(array) - 1):
            max_value = array[start_index]
            for i in range(start_index + 1, end_index + 1):
                if (array[i] > max_value):
                    max_value = array[i]
            end_index += 1
            start_index += 1
            sum += max_value
        #好坑比啊，老师的例子是错的。。。例子的答案应该是32（也就是把第一个初始窗口位置的最大值也要计算）
        # max0 = array[0]
        # for k in range(window_size):
        #     if (max0 < array[k]):
        #         max0 = array[k]
        # sum += max0
    else:
        # print(0)
        max0  = array[0]
        for k in range(len(array)):
            if( max0 < array[k]):
                max0 = array[k]
        sum += max0

    print(sum)

if __name__=='__main__':
    answer()

    # print(array)
    # print(window_size)