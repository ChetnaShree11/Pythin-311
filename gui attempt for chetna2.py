from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

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

    
            
class AdminScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text='Admin Login')
        self.layout.add_widget(self.label)

        self.user_id_input = TextInput(hint_text='Admin ID')
        self.layout.add_widget(self.user_id_input)

        self.password_input = TextInput(hint_text='Password', password=True)
        self.layout.add_widget(self.password_input)

        self.login_button = Button(text='Login', on_press=self.login)
        self.layout.add_widget(self.login_button)

        self.add_widget(self.layout)

    def login(self, instance):
        if self.user_id_input.text == 'admin' and self.password_input.text == 'admin':
            self.manager.current = 'admin_operations'
        elif self.user_id_input.text == 'user' and self.password_input.text == 'user':
            self.manager.current = 'user_operations'
        else:
            self.label.text = 'Invalid credentials'



class AdminOperationsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text='Admin Options')
        self.layout.add_widget(self.label)

        self.create_user_button = Button(text='Create User')
        self.create_user_button.bind(on_press=self.create_user)
        self.layout.add_widget(self.create_user_button)

        self.change_password_button = Button(text='Change User Password')
        self.change_password_button.bind(on_press=self.change_password)
        self.layout.add_widget(self.change_password_button)

        self.block_user_button = Button(text='Block User')
        self.block_user_button.bind(on_press=self.block_user)
        self.layout.add_widget(self.block_user_button)

        self.user_operations_button = Button(text='User Operations')
        self.user_operations_button.bind(on_press=self.user_operations)
        self.layout.add_widget(self.user_operations_button)

        self.logout_button = Button(text='Logout')
        self.logout_button.bind(on_press=self.logout)
        self.layout.add_widget(self.logout_button)

        self.add_widget(self.layout)

    def create_user(self, instance):
        user_id_input = TextInput(hint_text='User ID')
        password_input = TextInput(hint_text='Password', password=True)
        create_button = Button(text='Create')

        def create_user_action(instance):
            admin.create_user(user_id_input.text, password_input.text)
            self.layout.remove_widget(user_id_input)
            self.layout.remove_widget(password_input)
            self.layout.remove_widget(create_button)

        create_button.bind(on_press=create_user_action)
        self.layout.add_widget(user_id_input)
        self.layout.add_widget(password_input)
        self.layout.add_widget(create_button)

    def change_password(self, instance):
        user_id_input = TextInput(hint_text='User ID')
        new_password_input = TextInput(hint_text='New Password', password=True)
        change_button = Button(text='Change')

        def change_password_action(instance):
            admin.change_user_password(user_id_input.text, new_password_input.text)
            self.layout.remove_widget(user_id_input)
            self.layout.remove_widget(new_password_input)
            self.layout.remove_widget(change_button)

        change_button.bind(on_press=change_password_action)
        self.layout.add_widget(user_id_input)
        self.layout.add_widget(new_password_input)
        self.layout.add_widget(change_button)

    def block_user(self, instance):
        user_id_input = TextInput(hint_text='User ID')
        block_button = Button(text='Block')

        def block_user_action(instance):
            admin.block_user(user_id_input.text)
            self.layout.remove_widget(user_id_input)
            self.layout.remove_widget(block_button)

        block_button.bind(on_press=block_user_action)
        self.layout.add_widget(user_id_input)
        self.layout.add_widget(block_button)

    def user_operations(self, instance, user_id, password):
        self.manager.current = 'user_operations'
        user = User(user_id, password)
        if user in users:
            print(f"Logged in as {user_id}")
            while True:
                print("1. Deposit\n2. Withdraw\n3. Balance Enquiry\n4. Change Password\n5. Logout")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    amount = int(input("Enter amount to deposit: "))
                    user.deposit(amount)
                elif choice == 2:
                    amount = int(input("Enter amount to withdraw: "))
                    user.withdraw(amount)
                elif choice == 3:
                    user.balance_enquiry()
                elif choice == 4:
                    new_password = input("Enter new password: ")
                    user.change_password(new_password)
                elif choice == 5:
                    print("Logged out successfully!")
                    break
                else:
                    print("Invalid choice!")
        

    def logout(self, instance):
        self.manager.current = 'admin_login'

class UserScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')

        self.label = Label(text='User Operations')
        self.layout.add_widget(self.label)

        self.logout_button = Button(text='Logout')
        self.logout_button.bind(on_press=self.logout)
        self.layout.add_widget(self.logout_button)

        self.add_widget(self.layout)

    def user_login(self, instance):
        user_id_input = TextInput(hint_text='User ID')
        password_input = TextInput(hint_text='Password', password=True)
        login_button = Button(text='Login')

        def login_action(instance):
            global current_user
            for user in users:
                if user.user_id == user_id_input.text and user.password == password_input.text:
                    current_user = user
                    self.layout.clear_widgets()
                    self.label.text = f'Logged in as {current_user.user_id}'
                    return
            self.layout.clear_widgets()
            self.label.text = 'Invalid credentials'

        login_button.bind(on_press=login_action)
        self.layout.add_widget(user_id_input)
        self.layout.add_widget(password_input)
        self.layout.add_widget(login_button)

    def logout(self, instance):
        global current_user
        current_user = None
        self.manager.current = 'admin_operations'



class ATMSimulationApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.admin_screen = AdminScreen(name='admin_login')
        self.admin_operations_screen = AdminOperationsScreen(name='admin_operations')
        self.user_screen = UserScreen(name='user_operations')

        self.screen_manager.add_widget(self.admin_screen)
        self.screen_manager.add_widget(self.admin_operations_screen)
        self.screen_manager.add_widget(self.user_screen)

        return self.screen_manager

if __name__ == '__main__':
    users = []
    admin = Admin('admin', 'admin')
    current_user = None

    ATMSimulationApp().run()
