def errorHanler(func):
    def innerfunc(*args,**kwargs):
        print(kwargs)
        for i in range(kwargs['num']):
            func(*args,*kwargs)
    return innerfunc

@errorHanler
def Print(num=12):
    print(num)

Print(num = 13)
