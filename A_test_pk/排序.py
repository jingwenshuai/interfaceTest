#coding=utf-8
#__author__= 'jws'

def sortnumb(l,number):
    li = sorted(l)
    for i in range(len(li)):
        if number < li[i]:
            li.insert(i,number)
            break
        elif number == li[i]:
            li.insert(i,number)
            break
        elif number > li[i]:
            continue
        else:
            li.insert(i,number)
            break
    return li

l = [40,34,5,7,9,14,17,20]
nu = int(input("请输入要插入的数："))
a = sortnumb(l,nu)
print(a)