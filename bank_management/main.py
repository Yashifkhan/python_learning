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
        if Path(database).exists():   # ✅ correct
            with open(database, "r") as fs:
                data = json.load(fs)  # ✅ correct
        else:
            print("no such file exist in db")
    except Exception as err:
        print("have some error", err)
            
            
            
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
        info ={
                "name":input("enter your name"),
                "age":int(input("enter your age")),
                "email":input("enter your email"),  
                "pin":int(input("enter your pin")),
                "accountNo":Bank.__accoundGenrate(),
                "balance":0         
        }
        if info["age"] < 18 or len(str(info['pin'])) != 4:
            print("sorry you can not creat account")
        else:
            print("account created succfully")
            for i in info:
                print(f"{i} : {info[i]}")
                
            print("pleace not down your bacnk account")
            Bank.data.append(info)
            Bank.update()
            
    def depositmoney(self):
        accuntNumber = input("Enter your number: ")
        pin = int(input("Enter your pin: "))
        print("bank data ->>",Bank.data)

        userdata = [i for i in Bank.data if i['accountNo'] == accuntNumber and i["pin"] == pin]

        if not userdata:
            print("Sorry data not found")
        else:
            amount = int(input("How much you want to deposit: "))
            if amount <= 0 or amount > 100000:
                print("Invalid amount")
            else:
                print("userdata",userdata)
                userdata[0]["balance"] += amount
                Bank.update()
                print("Amount deposited successfully")
                
                
user=Bank()
check=int(input("tell me your number"))
if check == 1:
    user.createAccount()
    
if check ==2:
    user.depositmoney() 
        


