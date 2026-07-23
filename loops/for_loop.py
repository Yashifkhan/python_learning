# prectice queston 


# accept the integer number and print hello world n time 
# num=int(input("Enter the number"))
# print("User num is : ", num)

# for i in range(num):
#     print("Hello world")


# print the natural number 
# num=int(input("Enter the number"))
# for i in range(1,num+1):
#     print(i)

# revers the loop from n to 1 
# num=int(input("Enter the number"))

# for i in range(num,0,-1):
#     print(i)

# take a number amnd print the table 
# num=int(input("Enter the number"))

# for i in range(num,num*10+1,num):
# for i in range(1,11):
#     print(i*num)


# sum up to n term 
# num=int(input("Enter the number"))

# sum=0
# for i in range(1,num+1):
#     sum+=i

# print(f" 1 to {num} numbers sum is : ",sum)


# print the factorial of number 
# num=int(input("Enter the number"))

# fect=1
# for i in range(1,num+1):
#     fect*=i
# print(fect)

# print the sum of all odd and even number in a range 
# num=int(input("Enter the number"))
# even_sum=0
# odd_sum=0

# for i in range(1,num+1):
#     if i%2 ==0:
#         even_sum += i
#     else:
#         odd_sum +=i
        
# print("sum of even values lie in range",even_sum)
# print("sum of odd values lie in range",odd_sum)


# print the feactor of number 
# num=int(input("Enter the number"))

# for i in range(1,num+1):
#     if num % i == 0:
#         if(i==1):
#             print(f"this are all feactor of {num}")
#         print(i)
    

# accept the number and check it is perfect number or not 
# num=int(input("Enter the number"))

# sum=0
# for i in range(1,num):
#     if num % i == 0:
#         sum+=i
    
# if(sum == num):
#     print("Yes it is perfect number : ",num)


# check the number is prime or not 
# num=int(input("Enter the number"))


# way 1
# count=0
# for i in range(1,num+1):
#     if num % i == 0:
#         count += 1
# print(count)
# if(count == 2):
#     print("number is prime",num)
# else:
#     print("number is not prime",num)


# way 2 
# if num <= 1:
#     print("number is not prime")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not prime")
#             break
#     else:
#         print("Prime")

# revers the string 
# string="yashif"
# for i in range(len(string)-1,-1,-1):
#     print(string[i])

# print(string[::-1])


# check the string is palindrom or not 

string ="racar"
revstr=""
for i in range(len(string)-1,-1,-1):
    revstr+=string[i]
    
if string == revstr:
    print("str is palindrom",revstr)
else:
    print("Stringis not palindrom")
