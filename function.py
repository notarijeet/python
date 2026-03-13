def hello_fun():
    return 'hello function'
    
def arijeet():
    return 'namastesir'



name = hello_fun()
print(name)
print(hello_fun)
print(len(name))



#args and kwargs
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
    
student_info('math','Art',name = 'john',age = 22)
