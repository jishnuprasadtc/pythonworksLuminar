# def add(n1,n2):
#     res=(n1+n2)
#     return(res)
# print(add(10,20))


# def maxtwo(num1,num2):
#     if num1>num2:
#         return "num1 is greater "
#     else:
#         return "num2 is greater"
# print(maxtwo(10,2))   

# def sub (n1,n2):
#     return n1-n2
# print(sub(20,10))


# def smartsum(n1,n2):
#     sum=0
#     if n1>n2:
#         return n1-n2
#     else:
#         return n2-n1
# print(smartsum(5,10)) 
# print(smartsum(15,10))   



# def odd_even(n1,n2):
#     if n1%2==0:
#         return "even"
#     else:
#         return "odd"
# print(odd_even(1,2))


# def get_dicount_price(actualprice,discount):
#     sell_price=actualprice-(actualprice*discount)/100
#     return sell_price
# print(get_dicount_price(50,10))




# def hcf(num1,num2):
#     res=1
#     sm=num1 if num1<num2 else num2
#     for i in range(sm+1,1):

def least_coomon_multiple(n1,n2):
    max=n1 if n1>n2 else n2
    flag=True
    while(flag):
        if max%n1==0 and max%n2==0:
            print(f"lcm of{n1},{n2} is {max}")
            break
        else:
            max=max+1
least_coomon_multiple(30,25)            

