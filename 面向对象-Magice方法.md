# Magice方法
+ Magice方法是类里的一些特殊的方法
+ 特点： 
  - 不需要手动调用，会在合适的时机自动调用
  - 这些方法，都是使用 __ 开始， 使用 __ 结束
  - 方法名都是系统规定好的，在合适的时机自己调用

```
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __del__(self):
        print("__del__ 方法被调用了")
        
    def __str__(self):
        return "good"
        
    def __repr__(self):
        return "hello"
        
p = Person('zhangsan',18)
print(p) # 如果不做任何的修改，直接打印一个对象，是显示对象的类型以及内存地址
print(p.__repr__()) # Magice 方法一般不手动调用，但可以进行手动调用
print(repr(p)) # 调用内置函数repr会触发对象的__repr__方法
 
          
```
  
# \_\_init\_\_ 方法
+ 在创建对象时，会自动调用这个方法 
  
# \_\_del\_\_ 方法
+ 当对象被销毁时，会自动调用这个方法
+ 程序结束时，会自动销毁对象

# \_\_str\_\_ 方法
+ 当打印一个对象的时候，会调用这个对象的 __str__ 或者 __repr__ 方法
+ 如果两个方法都写了，则选择 __str__ 的内容输出
+ Magice 方法一般不手动调用，但可以进行手动调用
+ 调用内置函数repr会触发对象的__repr__方法






# 运算符相关的方法
+ 怎样比较两个对象是否是同一个对象呢？ 比较内存地址即可，内存地址一致表名是同一个对象，否则为不同的对象

## ***is*** 身份运算符
+ 用来判断两个对象是否是同一个对象

## ==
+ 会调用对象的 __eq__方法，获取这个方法的比较结果
+ A == B 的本质是调用 A.\_\_eq\_\_(B)
+ \_\_eq\_\_ 如果不重写，默认比较的依然是内存地址
+ list（列表）中已重写了\_\_eq\_\_方法，不再是比较内存地址，而是比较值。

```
class Person(object):
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
        
p1 = Person('zhangsan',18)
p2 = Person('zhangsan',18)
# 注意，此处p1和p2不是同一个人，因为，两者具有不同的内存地址
# 怎样比较两个对象是否是同一个对象呢？ 比较内存地址即可

print('0x%X' % id(p1))
print('0x%X' % id(p2))

print（p1 is p2） # False

num1 = [1,2,3]
num2 = [1,2,3]
print(num1 is num2) # False     is 是比较两个对象的内存地址
print(num1 == num2) # True      == 是比较值的，会调用对象的__eq__方法，获取这个方法的比较结果




```
 







