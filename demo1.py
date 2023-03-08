#!/usr/bin/python3

L=[1]
# def定义函数
def is_primeNum(num,tag): # 判断是否是质数
    for item in range(2,tag): # 从2开始遍历,用需要判断的数来取余
        if num % item == 0: # 如果取余为0则代表可以被除了1和本身以外的其他数整除,返回0代表不是质数
            return 0
    return 1 # 遍历完了则代表这个数只能被1和本身整除,所以返回1代表是质数

for i in range(2,101): # 从2开始遍历到100,range左边取得到,右边取不到
    tag=0 # 用来标记需要遍历几次
    if i<10: #如果10以内的数则直接从2遍历到本身即可,避免本身太小导致运算出错
        tag=i
    else: # 大于9的数则只需要遍历到中间即可,当判断的遍历到本身的一半时就可以判断出是否是质数,避免多余的循环浪费时间
        tag=i//2 # //代表除法取整,偏向小的部分例如 3/2=1
    if is_primeNum(i,tag): # 传入需要判断的数,循环的次数
        L.append(i)

print(L)
