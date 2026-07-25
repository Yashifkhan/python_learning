# list are mutable we can change the value after creation 
# list allow the duplicat value store 
# list are hetorgenous means we store the int str flot accept the multy data typ value
# list are order and we can access the element help of index and position 

# l=[1,2,3,4]

# print the first all positive number and then negitive number in luist 
# l=[1,2,3,4,-8,6,-7]


# for i in l:
#     if i >=  0:
#         print("Positive num : ", i)
#     else :
#         print("neg num :" ,i)

# mean of list 
# l=[1,2,3,4,5]


# sum=0
# for i in l:
#     sum+=i
# print(sum/len(l))


# prin the gratest element in array and print index 

# l=[1,2,38,6,9]

# max=l[0]
# index=0
# for i in range(len(l)):
#     if l[i] > max:
#         max=l[i]
#         index=i
# print(max)
# print(index)



# find the second largest number 
# arr=[1,4,2,5,6,3,9]

# max1=arr[0]
# max2=arr[0]

# for i in arr:
#     if i > max1:
#         max2=max1
#         max1=i
#     elif max2 >max1:
#         max2=i
        
# print("first larget number",max1)
# print("second larget number",max2)


# check the list is short or not  

l=[1,2,6]
for i in range(len(l)-1):
    if l[i] < l[i+1]:
        continue
    else:
        print("Your list is not sort")
        break
else:
    print("Your list is sort")    

        
