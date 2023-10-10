# def greetings(**kwargs):
#     print(f"(hello {kwargs.get('msg')} app user {kwargs.get('user_name')})")



# greetings(msg="good mrng",user_name="jishnu")






def dispatch_order(**kwargs):
    print(f"hello user {kwargs.get('name')} your order {kwargs.get('item')} {kwargs.get('code')} is {kwargs.get('status')}")
    


dispatch_order(item="shirt",code="c346",status="delivered",name="jishnu")





