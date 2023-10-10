def product(*args):   #single astric is used for taking any number
    multi=1
    for n in args:
        multi*=n
    print(multi)


product(1,2,3,4,5)
product(10,20)    