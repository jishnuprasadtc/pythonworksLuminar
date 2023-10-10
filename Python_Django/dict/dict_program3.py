enquires=["django","testing","django","bigdata","django","bigdata","aws","aws","bigdata"]
courses={}
for course in enquires:
    if course in courses:
        courses[course]+=1
    else:
        courses[course]=1
print(courses)