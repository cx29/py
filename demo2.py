#!/usr/bin/python3

# 函数
def computeTwo():
    # 区间小
    low=1
    # 区间大
    high=2
    # 区间中
    mid=0
    # 循环停止条件,因为需要保留8位小数所以需要计算到第九位
    while high-low>float("0.000000001"):
        # 二分查找法,取中间
        mid=(high+low)/2
        # **为指数运算符等同于mid*mid,如果mid的平方大于2则代表需要将区间的上限缩小到mid
        if mid ** 2>2:
            high=mid
        else: # 如果mid的平方小于2则需要将区间的下限缩小到mid
            low=mid
        # [low===>[[[[mid]]]]<===high] 向中间靠的过程
    return float('%.8f'%mid) # "%.8f"%mid则是保留mid的8位小数,float()为数据类型的强制转换(可要可不要)

# 二分查找而来
print("computeTwo=>",computeTwo())
# 使用内置函数而来
print("pow()=>",pow(2,0.5))
