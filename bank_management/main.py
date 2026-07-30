print("Press 1 for create account")
print("Press 2 for deposit money")
print("Press 3 for withdrawing money")
print("Press 4 for profile view")
print("Press 5 for update info")
print("Press 6 for delete the acount")

import json
from pathlib import Path
import random 
import string

class Bank:
    database='data.json'
    data=[]
    
    try:
        if Path(database.exists()):
           with open(database) as fs:
               data=json.load(fs.read())
        else :
            print("no such file exist in db")
            
    except Exception as err:
        print(f"have some error",err)
        
        
    @staticmethod
    def update():
        with open(Bank.database,'w') as fs:
            fs.write(json.dumps(Bank.data))
             
    @classmethod
    def __accoundGenrate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        sp=random.choices("!@#$%^&*",k=1)
        id=alpha+num+sp
        random.shuffle(id)
        return "".join(id)
        
    
    def createAccount(self):
        data ={
                "name":input("enter your name"),
                "age":int(input("enter your age")),
                "email":input("enter your email"),  
                "pin":int(input("enter your pin")),
                "accountNo.":Bank.__accoundGenrate(),
                "balance":0         
        }
        if data["age"] < 18 or len(str(data['pin'])) != 4:
            print("sorry you can not creat account")
        else:
            print("account created succfully")
            for i in data:
                print(f"{i} : {data[i]}")
                
            print("pleace not down your bacnk account")
            Bank.data.append(data)
            Bank.update()
            
        
user=Bank()
check=int(input("tell me your number"))
if check == 1:
    user.createAccount()
        


