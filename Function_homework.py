# 1. 编写函数，求1+2+3+...+N 的和
## Method 1
def get_sum(n):
    sum = 0
    for i in range(0,n+1):
        sum += i
    return sum

## Method 2
def get_sum(n):
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1
    return sum


# 2. 编写一个函数，求多个数中的最大值
## Method 1
def get_max(*args):
#     max = 0
#     for i in range(0,len(args)):
#         if args[i] > args[i+1]:
#             max = args[i]
#             args[i],args[i+1] = args[i+1],args[i]
#         else:
#             max = args[i+1]
#     return max
     
    max = args[0]
    for arg in args:
        if arg > max:
            max = arg
    return max

## Method 2
def get_max(*args):
    return sorted(args)[-1]  # 此处使用soreted而不适用sort是因为args为元组形式，不能进行编辑。sort函数直接对原有数据进行修改，不适合该处情况，sorted方法并不改变原有数据
                

# 3. 编写一个函数，实现摇骰子的功能，打印N个骰子的点数和
## Method 1
def dice(n):
    import random
    i = 1
    sum = 0
    while i <= n:
        num = random.randint(1,6)
        sum += num
        i += 1
    return sum
        
