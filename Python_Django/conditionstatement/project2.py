height_cm=int(input("enter your height="))
weight_kg=int(input("enter your weight="))
height_m=height_cm/100
print(height_m)           
bmi=weight_kg//height_m**2
print("bmi is =",bmi)
if(bmi<20):
    print("your in light weight")
elif(bmi<25):
    print("your in normal weight")
elif(bmi<30):
    print("your in pre obesity")
else:
    print("your in obesity")


# <20 lightweight
# 20-25 normal
# 25-30 pre obesity
# >30 is obesity
