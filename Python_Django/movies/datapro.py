from json import load
path="C:\\Users\\DELL\\OneDrive\\Desktop\\Python_Django\\movies\\mdb.json"
with open(path,encoding="utf-8")as f:
    filims=load(f)
# #number of filims
# print(len(filims))


# # print all movies relesed in 2015
# movie_filter=[f.get("title") for f in filims if f.get("year")=="2015"]
# print(movie_filter)

# # print comedy genure
# fun_movies=[f.get("title") for f in filims if "Comedy" in f.get("genres")]
# print(fun_movies)

# # id in range(20,30) and run time >110

# m_filter=[f.get("title") for f in filims  if f.get("id") in range(20,31) and  f.get("runtime")>="110"]
# print(m_filter)

# # print the single name in the title movies

# title_filter=[f.get("title") for f in filims if len(f.get("title").split(" "))==1]
# print(title_filter)


# # print minum runtm
# r_time=min(filims,key=lambda d: d.get("runtime"))
# print(r_time)


# # print run time max in dram in genur
# # d_ram=[f for f in filims if "Drama" in f.get("genres")]   #f used for take the entire
# # longest_mv=max(d_ram,key=lambda f:int(f.get("runtime")))
# # print(longest_mv)

# # print all geners
wc={}
for m in filims:
    years=m.get("year")
    if years in wc:
        wc[years]+=1
    else:
        wc[years]=1
print(max((v,k)for k,v in wc.items()))  #k=key & v=value



# # print largest number movies in which year

# num_mv={}
# for f in filims:
#     if f.get("year") in num_mv:
#         num_mv[(f.get("year"))]+=1
#     else:
#         num_mv[(f.get("year"))]=1
# most=max(num_mv,key=lambda d:num_mv[d])
# print(most)

