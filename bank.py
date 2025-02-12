class User():
    def __init__(self, name, age, gender, password):
        self.name = name
        self.age = age
        self.gender = gender
        self.password = password

    def show_details(self):
        print("Personal Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)


class Bank(User):
    def __init__(self, name, age, gender, password):
        super().__init__(name, age, gender, password)
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
        else:
            self.balance += amount
            print(f"€{amount} has been deposited. Updated balance: €{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print(f"Insufficient balance. Available balance: €{self.balance}")
        else:
            self.balance -= amount
            print(f"€{amount} has been withdrawn. Updated balance: €{self.balance}")

    def view_balance(self):
        print(f"Account balance: €{self.balance}")


class BankSystem():
    def __init__(self):
        self.users = []
        self.logged_in_user = None

    def add_user(self, user):
        self.users.append(user)

    def login(self, name, password):
        for user in self.users:
            if user.name == name and user.password == password:
                self.logged_in_user = user
                print(f"Login successful! Welcome {user.name}.")
                return True
        print("Invalid username or password.")
        return False

    def create_account(self):
        print("Create your new bank account")
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        gender = input("Enter your gender: ")
        password = input("Create a password: ")

        new_user = Bank(name, age, gender, password)
        self.add_user(new_user)
        print(f"Account created successfully for {name}!\n")

    def deposit(self, amount):
        if self.logged_in_user:
            self.logged_in_user.deposit(amount)
        else:
            print("You need to log in first.")

    def check_balance(self):
        if self.logged_in_user:
            self.logged_in_user.view_balance()
        else:
            print("You need to log in first.")


# Example Usage

bank_system = BankSystem()

# Account Creation or Login Prompt
while True:
    action = input("Do you want to (1) Create a new account, (2) Login to your account, or (3) Exit: ")

    if action == '1':
        bank_system.create_account()
    elif action == '2':
        print("Please log in to access your bank account.")
        username = input("Enter your name: ")
        password = input("Enter your password: ")

        if bank_system.login(username, password):
            # After successful login, allow deposit and balance check
            while True:
                action = input("Do you want to (1) Deposit, (2) Check balance, or (3) Logout: ")
                if action == '1':
                    amount_to_deposit = float(input("Enter deposit amount: "))
                    bank_system.deposit(amount_to_deposit)
                elif action == '2':
                    bank_system.check_balance()
                elif action == '3':
                    print("Logged out successfully.")
                    break
                else:
                    print("Invalid option.")
        else:
            print("Login failed. Please try again.")
    elif action == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please select again.")
