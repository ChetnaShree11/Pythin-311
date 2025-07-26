class User:
    def __init__(self, user_id, password, balance=100000, blocked=False):
        self.user_id = user_id
        self.password = password
        self.balance = balance
        self.blocked = blocked
        self.wrong_password_count = 0

    def deposit(self, amount):
        if amount > 0 and amount <= 100000:
            self.balance += amount
            print(f"Deposited: {amount} | Current Balance: {self.balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= 50000 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount} | Current Balance: {self.balance}")
            if self.balance < 75000:
                print("Warning: Your balance is less than 75000.")
        else:
            print("Invalid withdrawal amount or insufficient balance!")

    def balance_enquiry(self):
        print(f"Current Balance: {self.balance}")

    def change_password(self, new_password):
        self.password = new_password
        print("Password changed successfully!")

class Admin(User):
    def __init__(self, user_id, password):
        super().__init__(user_id, password)

    def create_user(self, user_id, password):
        new_user = User(user_id, password)
        users.append(new_user)
        print(f"User '{user_id}' created successfully!")

    def change_user_password(self, user_id, new_password):
        for user in users:
            if user.user_id == user_id:
                user.change_password(new_password)
                return
        print("User not found!")

    def block_user(self, user_id):
        for user in users:
            if user.user_id == user_id:
                user.blocked = True
                print(f"User '{user_id}' blocked successfully!")
                return
        print("User not found or already blocked!")

# Functions to handle ATM operations

def login(user_id, password):
    for user in users:
        if user.user_id == user_id:
            if user.blocked:
                print("Account blocked! Contact admin.")
                return None
            if user.password == password:
                user.wrong_password_count = 0
                return user
            else:
                user.wrong_password_count += 1
                if user.wrong_password_count >= 3:
                    user.blocked = True
                    print("Too many wrong attempts! Account blocked.")
                    return None
                print("Incorrect password!")
            break
    else:
        print("User not found!")
    return None

# Main program
admin = Admin("admin", "admin_password")  # Create admin account
users = []  # List to store user objects

# Create some user accounts
admin.create_user("user1", "password1")
admin.create_user("user2", "password2")
admin.create_user("user3", "password3")
admin.create_user("user4", "password4")
admin.create_user("user5", "password5")

# ATM operations simulation
while True:
    print("\nWelcome to the ATM!")
    user_id = input("Enter User ID: ")
    password = input("Enter Password: ")

    if user_id == "admin" and password == "admin_password":
        while True:
            print("\nAdmin Options:")
            print("1. Create User")
            print("2. Change User Password")
            print("3. Block User")
            print("4. Logout as Admin")

            admin_choice = input("Enter choice (1-4): ")
            if admin_choice == '1':
                new_user_id = input("Enter new user ID: ")
                new_password = input("Enter password for new user: ")
                admin.create_user(new_user_id, new_password)
            elif admin_choice == '2':
                user_to_change = input("Enter user ID to change password: ")
                new_password = input("Enter new password: ")
                admin.change_user_password(user_to_change, new_password)
            elif admin_choice == '3':
                user_to_block = input("Enter user ID to block: ")
                admin.block_user(user_to_block)
            elif admin_choice == '4':
                print("Logged out as Admin.")
                break
            else:
                print("Invalid choice!")

    else:
        user = login(user_id, password)
        if user:
            while True:
                print("\n1. Deposit")
                print("2. Withdraw")
                print("3. Balance Enquiry")
                print("4. Change Password")
                print("5. Logout")

                choice = input("Enter choice (1-5): ")
                if choice == '1':
                    amount = int(input("Enter deposit amount: "))
                    user.deposit(amount)
                elif choice == '2':
                    amount = int(input("Enter withdrawal amount: "))
                    user.withdraw(amount)
                elif choice == '3':
                    user.balance_enquiry()
                elif choice == '4':
                    new_password = input("Enter new password: ")
                    user.change_password(new_password)
                elif choice == '5':
                    print("Logged out. Have a nice day!")
                    break
                else:
                    print("Invalid choice!")

        else:
            print("Login failed. Please try again.")
