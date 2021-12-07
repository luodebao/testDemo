"""
property 装饰器
property 装饰器用于类中的函数，使得我们可以像访问属性一样来获取一个函数的返回值
"""
class XiaoMing():
    first_name = '明'
    last_name = '小'
    @property
    def full_name(self):
        return self.last_name+self.first_name
if __name__ == '__main__':
    xiaoming =XiaoMing()
    print(xiaoming.full_name)