#coding=utf-8
#__author__= 'jws'

li = [23,65,12,45,96,234,34,24,56,345]

def find_second(li):
    #1,直接排序，输出倒数第二个数
    tmp_list = sorted(li)
    print("第二个最大的数是：",tmp_list[-2])

    #2,设置两个标志位，一个存最大，一个存第二大

    one = li[0]
    two = li[0]
    for i in range(1,len(li)):
        if li[i]>one:
            two = one
            one = li[i]
        elif li[i]>two:
            two = li[i]
        else:
            pass
    print("第二大数是：",two)

a = find_second(li)
print(a)