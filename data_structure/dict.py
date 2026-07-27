# merge the two dictd1

# d1={1:10,2:20}
# d2={3:30,4:40}


# for i in d2:
#     d1[i]=d2[i]
# print(d1)

# sum of all dict 
# d={1:1,2:2,3:3,4:4,5:5}
# sum=0
# for i in d:
#     sum+=d[i]
# print(sum)



# count the frequnce of all value in dict 
# d=[1,2,3,45,2,4,5,6,3,2,7]
# dict={}
# for i in d:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
        
# print(dict)

# merge the two dict if key are same then add id 


d1={1:10,3:20}
d2={3:30,4:40}

for i in d2:
    if i in d1:
        d1[i]+=d2[i]
    else:
        d1[i]=d2[i]
        
print(d1)