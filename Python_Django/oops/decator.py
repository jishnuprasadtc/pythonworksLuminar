# @ dector

# syntax 

# def dector_name(just a variable):
#     def anotherfun(number_of parameters):
# def inner_fun(n1,n2):
#         # condition should perform
#         if(n1<n2):
#             (n1,n2)=(n2,n1)
#         return vn(n1,n2)
    # return inner_fun






def swap_num(vn):
    def inner_fun(n1,n2):
        # condition should perform
        if(n1<n2):
            (n1,n2)=(n2,n1)
        return vn(n1,n2)
    return inner_fun






def smart_div(fn):
    def wrapper(n1,n2):
        if n2==0:
            print(" sorry not possible !!!")
            return 
        return fn(n1,n2)
    return wrapper

# call the dector here
# @swap_num

# def sub(n1,n2):
    # return n1-n2
@swap_num
@smart_div
def div(n1,n2):

    return n1/n2
# print(sub(10,20))
print(div(10,0))