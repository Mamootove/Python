class Bankaccount:
    def __init__(self):
        self.__account: str
        self.__balance: float

    def account_caller(self):
        account = input("Enter you account number: ")
        return account
    
    def new_account(self):
        account = self.account_caller()
        balance = float(input("Enter initial balance: "))
        self.__account = account
        self.__balance = balance
        print(f'Account {self.__account} created successfully.')
        
    
    def del_account(self):
        account = self.account_caller()
        if account == self.__account:
            self.__account = None
            self.__balance = None
            print("Account deleted successfully.")
            
        
    def get_balance(self):
        account = self.account_caller()
        if account == self.__account:
            print(self.__balance)
        else:
            print("Account not found.")
            
    def deposite(self):
        account = self.account_caller()
        if account == self.__account:
            amount = float(input("Enter amount to deposit: "))
            self.__balance += amount
            print("Deposited successfully.")
        else:
            print("Account not found.")
            flag = input("Do you want to create a new account? (y/n)")
            if flag.lower() == 'y':
                self.new_account()
            else:
                print("Operation cancelled.")
                
                

account = Bankaccount()

def bank():
    continue_Bank = True
    while continue_Bank:
        what_to_do = input("What do you want to do? (create(0)/delete(1)/check_balance(2)/deposit(3)): ")
        if what_to_do == '0':
            account.new_account()
        elif what_to_do == '1':
            account.del_account()
        elif what_to_do == '2':
            print(account.get_balance())
        elif what_to_do == '3':
            account.deposite()
    ...



bank()