items=[
    {"id":1,"name":"sugar","price":40,"avl_qty":10},
    {"id":2,"name":"milk","price":28,"avl_qty":40},
    {"id":3,"name":"teapowder","price":230,"avl_qty":100},
    {"id":4,"name":"tomatto","price":120,"avl_qty":5},
    {"id":5,"name":"potatto","price":45,"avl_qty":70},
    {"id":6,"name":"carrot","price":80,"avl_qty":0},
    {"id":7,"name":"oreo","price":45,"avl_qty":0},
    {"id":8,"name":"hideandseek","price":50,"avl_qty":50},
]

# pc={}
# # print all product names
# print("1.---------------------------") 
# for p in items:
#     print(p.get("name"))
product_name=[p.get("name") for p in items]  #using comperhensiona method
print(product_name)
   

# # print total number of products
# print("2.---------------------------") 
product_c=len(items) #find the len  of list for finding the number in list 
print(product_c)
  

# # print all in stock product names  
# print("3.---------------------------") 
# for p in items:
#     if p.get("avl_qty")>0: #or !=0
# #         print(p.get("name"))
product_stock=[p.get("name") for p in items if p.get("avl_qty")>0]
print(product_stock)

# # # print product names avaialble under rs 50
# # print("4.---------------------------") 
# # for p  in items:
# #     if p.get("price")<50:
#      print(p.get("name"))

price_filter=[p.get("name") for p in items if p.get("price")<50]
print(price_filter)
       

# # # print all product names avilable in ranage of 20 to 50
# # print("5.---------------------------") 
# # for p in items:
# #      if p.get("price") in range(20,50):
# #     #  if p.get("price")>20 and p.get("price")<50:
# #           print(p.get("name"))

range_filter=[p.get("name") for p in items if p.get("price") in range(20,50)]
print(range_filter)
          
oreoprice=[p.get("price") for p in items if p.get("name")=="oreo"]
print(oreoprice)

#update the  price of oreo
oreo_data=[p for p in items if p.get("name")=="oreo"][0]
oreo_data["price"]=90
print(oreo_data)


# take max and min from the list

largestcount=max(items,key=lambda p:p.get("price"))
print(largestcount)
cheapestcount=min(items,key=lambda p:p.get("price"))
print(cheapestcount)

