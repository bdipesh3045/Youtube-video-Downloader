a=[{'144p': [17, 'p']}, {'360p': [18, 'p']}, {'360p': [18, 'm']}, {'480p': [135, 'm']}, {'360p': [134, 'm']}, {'240p': [133, 'm']}, {'144p': [160, 'm']}, {'160': ['251', 'a']}]
unique=[]

    # if a[0].keys()
index=0

keys=[]
for d in a:
    for z in d:
        
        if (d[z][1]=="p") :
            keys.append(z)
            unique.append(d)
    for key in d.keys():
        if key not in keys:
            keys.append(key)
            unique.append(d)
print(unique)

# for i in a:
#     # print(str(a[index].keys()))
#     index+=1
#     # print(i)
#     for z in i:
#         if (i[z][1]=="p") :
#             unique.append(i)
# print(a)
# print("-----------------")
# for i in unique:
#     a.remove(i)
# print(a)

# for p in unique:
#     if (p.keys())!=(a[index].keys()):
#         unique.append(i)

# for i in unique:
#     print(str(i.keys()))