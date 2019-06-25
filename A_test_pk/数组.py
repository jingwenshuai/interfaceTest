#coding=utf-8
#__author__= 'jws'


def sz(nums,target):
    #如果列表长度小于2，直接结束
    if len(nums) < 2:
        return ("只有一个数")
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            print('test')
            if nums[i] + nums[j] == target:
                return [i,j]

num = [3,5,8,12,5,7,9]
a = sz(num,10)
print(a)
