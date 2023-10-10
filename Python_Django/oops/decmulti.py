def dec1(f):
    def inner():
        x=f()
        return x*x
    
    return inner

def dec2(f):
    def inner():
        x=f()
        return 2*x
    return inner



@dec2
@dec1
def num():


    return 10



print(num())

    