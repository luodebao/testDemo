"""wraps修饰器"""
from functools import wraps
def decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        """doc of  wrapper"""
        print("123")
        return func(*args,**kwargs)

    return wrapper
@decorator
def say_hello():
    """
    doc of say hello
    """
    print("你好")
if __name__ =='__main__':
    print(say_hello.__name__)
    print(say_hello.__doc__)