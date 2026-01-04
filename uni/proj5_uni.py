import secrets


class Accounts:
    _accounts = []

    def inputer(self):
        account_number = secrets.randbits(16)
        account_passwd = input(
            "Enter your password carefully, It can obtain any numbers, characters and symbols\n"
        )
        account_type = int(input("Account type: (1.Normal), (2.Student): "))
        return account_number, account_passwd, account_type

    def amounter(self):
        try:
            return int(input("Enter the amount you want to deposit: "))
        except:
            print("Enter a valid amount.")
            return self.amounter()

    def make_account(self, account_passwd, account_type):
        account = {
            "account_number": secrets.randbits(16),
            "account_passwd": account_passwd,
            "account_type": account_type,
            "credit": 0,
        }
        Accounts._accounts.append(account)
        print(f"Done, {account['account_number']}, password: {account_passwd}")

    def make_account_auto(self):
        account_number, account_passwd, account_type = self.inputer()
        account = {
            "account_number": account_number,
            "account_passwd": account_passwd,
            "account_type": account_type,
            "credit": 0,
        }
        Accounts._accounts.append(account)
        print(
            f"Done, Account : {account['account_number']} | with password: {account['account_passwd']} is created"
        )

    def deposit(self):
        acc_num = int(input("Enter your account number: "))
        for account in Accounts._accounts:
            if account["account_number"] == acc_num:
                amount = self.amounter()
                account["credit"] += amount
                print(f"Done, {amount} has added to your account.")
                return
        print("Account not found.")

    def withdraw(self):
        acc_num = int(input("Enter your account number: "))
        for account in Accounts._accounts:
            if account["account_number"] == acc_num:
                if account["account_type"] == 1:
                    amount = self.amounter()
                    if account["credit"] >= amount:
                        account["credit"] -= amount
                        print("Withdraw successful.")
                    else:
                        print("Not enough credit.")
                else:
                    Checking_Account().withdraw()
                return
        print("Account not found.")


class Checking_Account(Accounts):
    def withdraw(self):
        acc_num = int(input("Enter your account number: "))
        for account in Accounts._accounts:
            if account["account_number"] == acc_num:
                print(
                    f"You have {account['credit']} and you can borrow up to 1000 more (total {account['credit'] + 1000})"
                )
                amount = self.amounter()
                if account["credit"] - amount < -1000:
                    print("Borrow limit exceeded.")
                else:
                    account["credit"] -= amount
                    print(
                        f"Done, {amount} withdrawn. Current credit: {account['credit']}"
                    )
                return
        print("Account not found.")


class Saving_Account(Accounts):
    def interest(self):
        admin_pass = "00000000"
        if input("Enter the manager password: ") != admin_pass:
            print("Incorrect password.")
            return

        acc_num = int(input("Enter your account number: "))
        for account in Accounts._accounts:
            if account["account_number"] == acc_num:
                ratio = int(input("Enter the interest ratio: "))
                interest = account["credit"] * (ratio / 100)
                account["credit"] += interest
                print(f"Interest added: {interest}")
                return
        print("Account not found.")


account = Accounts()
account.make_account(1234, 1)

flag = 85
while flag:
    print(
        "\nCreate new account: 1\nDeposit money: 2\nWithdraw money: 3\nvariz sood(Admins only): 4\nExit: 0"
    )
    flag = int(input("What to do: "))
    if flag == 1:
        account.make_account_auto()
    elif flag == 2:
        account.deposit()
    elif flag == 3:
        account.withdraw()
    elif flag == 4:
        Saving_Account().interest()
