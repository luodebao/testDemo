#encoding=utf-8
"""

"""
def decorator(fnc):
    def wrapper(*args,**kwargs):
        print("123")
        return fnc(*args,**kwargs)
    return wrapper
@decorator
def say_hello():
    print("你好")
if __name__ == '__main__':
    say_hello()
