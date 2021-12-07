"""
classmethod修饰器
classmethod 装饰器classmethod 依旧是用于类中的方法，这表示这个方法将会是一个类方法，意味着该方法可以直接被调用无需实例化，但同样意味着它没有 self 参数，也无法访问实例化后的对象。相对于 staticmethod 的区别在于它会接收一个指向类本身的 cls 参数。

"""
class XiaoMing():
    name = '小明'
    @classmethod
    def say_hello(cls):
        print("同学你好，我是"+cls.name)
if __name__ == '__main__':
    XiaoMing.say_hello()
