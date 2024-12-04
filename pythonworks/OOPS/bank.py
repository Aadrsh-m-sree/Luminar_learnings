class Bank:
    cus_name:str
    acc_no:int
    acc_type:str
    balance:int

    def __init__(self,acc_no,cus_name,acc_type,balance):
        self.acc_no, self.cus_name, self.acc_type, self.balance=acc_no, cus_name, acc_type, balance
    
    def deposit(self,amount):
        self.balance+=amount
        print(f"Acc credited with RS {amount}.Available balance is RS {self.balance}")
    
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"RS {amount} is debited from your Acc {self.acc_no}. Available balance is RS {self.balance}")
        else:
            print("Balance is less than entered amount")

    def get_balance(self):
        print(f"Balance:{self.balance}")
        


cust1=Bank(2345678910,"Ajay","Savings",45000)
cust1.get_balance()
cust1.deposit(100)
cust1.withdraw(45100)

