allusers=["sachin", "rahul","rohit","dhawan","kohli","gill","laxman"]
sachinfollowing=["rohit","kohli","rahul"]
# change to set
sachinsuggetion=set(allusers).difference (set(sachinfollowing))
sachinsuggetion.remove("sachin")
print(sachinsuggetion)