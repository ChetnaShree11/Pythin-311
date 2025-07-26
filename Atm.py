from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.metrics import dp
from datetime import datetime, timedelta
import random
import time

Window.clearcolor = (1, 1, 1, 1)  # Set background color

class User:
    def __init__(self, user_id, password, balance):
        self.user_id = user_id
        self.password = password
        self.balance = balance
        self.failed_login_attempts = 0
        self.locked = False
        self.transaction_history = []

    def deduct_maintenance_fee(self):
        current_date = datetime.now().date()
        maintenance_day = 1  # Specify the day of the month for maintenance fee deduction
        if current_date.day == maintenance_day:
            maintenance_fee = 23
            self.balance -= maintenance_fee
            self.record_transaction(f'Maintenance Fee Deducted: -Rs. {maintenance_fee}')

    def record_transaction(self, description, amount=0):
        timestamp = datetime.now()
        transaction = {'timestamp': timestamp, 'description': description, 'amount': amount}
        self.transaction_history.append(transaction)
        if len(self.transaction_history) > 5:
            self.transaction_history.pop(0)

class Admin:
    def __init__(self, admin_id, password, total_balance):
        self.admin_id = admin_id
        self.password = password
        self.total_balance = total_balance
        self.failed_login_attempts = 0
        self.locked = False

class ATM(App):
    def __init__(self):
        super().__init__()
        self.users = {
            "user1": User(user_id="user1", password="pass1", balance=5000),
            # Add more users here
        }
        self.admin = Admin(admin_id="admin", password="admin123", total_balance=500000)
        self.current_user = None
        self.init_ui()

    def build(self):
        return self.login_layout

    def init_ui(self):
        self.login_layout = BoxLayout(orientation='vertical', padding=dp(20))
        self.services_layout = BoxLayout(orientation='vertical', padding=dp(20))
        self.mobile_verification_layout = BoxLayout(orientation='vertical', padding=dp(20))

        label = Label(text='Welcome to the ATM', font_size=dp(24), color=(0, 0, 0, 1))
        login_button = Button(text='Login', size_hint=(None, None), size=(dp(150), dp(50)),
                              background_color=(0.2, 0.6, 1, 1))
        login_button.bind(on_press=self.mobile_verification)

        self.login_layout.add_widget(label)
        self.login_layout.add_widget(login_button)

    def mobile_verification(self, instance):
        self.login_layout.clear_widgets()
        self.mobile_verification_layout.clear_widgets()

        label = Label(text="Enter your phone number:")
        self.phone_number_input = TextInput(hint_text="Phone Number")
        verify_button = Button(text="Send Code")
        verify_button.bind(on_press=self.send_verification_code)

        self.mobile_verification_layout.add_widget(label)
        self.mobile_verification_layout.add_widget(self.phone_number_input)
        self.mobile_verification_layout.add_widget(verify_button)

        self.root.add_widget(self.mobile_verification_layout)

    def send_verification_code(self, instance):
        self.phone_number = self.phone_number_input.text
        self.verification_code = str(random.randint(1000, 9999))

        print(f"Verification code sent to {self.phone_number}: {self.verification_code}")

        time.sleep(2)

        code_label = Label(text="Enter the verification code sent to your phone:")
        self.code_input = TextInput(hint_text="Verification Code")
        verify_code_button = Button(text="Verify Code")
        verify_code_button.bind(on_press=self.verify_code)

        self.mobile_verification_layout.clear_widgets()
        self.mobile_verification_layout.add_widget(code_label)
        self.mobile_verification_layout.add_widget(self.code_input)
        self.mobile_verification_layout.add_widget(verify_code_button)

    def verify_code(self, instance):
        entered_code = self.code_input.text
        if entered_code == self.verification_code:
            self.mobile_verification_layout.clear_widgets()
            self.show_verification_success_message()
            self.login_user()
        else:
            self.show_error_popup("Error", "Invalid verification code")

    def show_verification_success_message(self):
        verified_label = Label(text="Verified!", font_size=dp(20), color=(0, 0.7, 0, 1))
        self.mobile_verification_layout.add_widget(verified_label)

    def login_user(self):
        user_id = self.phone_number
        if user_id in self.users:
            self.current_user = self.users[user_id]
            if not self.current_user.locked:
                self.show_user_menu()
            else:
                self.show_error_popup("Error", "Account is locked. Contact admin.")
        else:
            self.show_error_popup("Error", "User not found")

    def show_user_menu(self):
        self.services_layout.clear_widgets()

        balance_button = Button(text='Check Balance', size_hint=(None, None), size=(dp(150), dp(50)),
                                background_color=(0.2, 0.6, 1, 1))
        balance_button.bind(on_press=self.check_balance)

        withdraw_button = Button(text='Withdraw', size_hint=(None, None), size=(dp(150), dp(50)),
                                 background_color=(0.2, 0.6, 1, 1))
        withdraw_button.bind(on_press=self.withdraw)

        deposit_button = Button(text='Deposit', size_hint=(None, None), size=(dp(150), dp(50)),
                                background_color=(0.2, 0.6, 1, 1))
        deposit_button.bind(on_press=self.deposit)

        currency_button = Button(text='Currency Exchange', size_hint=(None, None), size=(dp(150), dp(50)),
                                 background_color=(0.2, 0.6, 1, 1))
        currency_button.bind(on_press=self.currency_option)

        change_password_button = Button(text='Change Password', size_hint=(None, None), size=(dp(150), dp(50)),
                                        background_color=(0.2, 0.6, 1, 1))
        change_password_button.bind(on_press=self.show_change_password_popup)

        logout_button = Button(text='Logout', size_hint=(None, None), size=(dp(150), dp(50)),
                               background_color=(0.2, 0.6, 1, 1))
        logout_button.bind(on_press=self.logout)

        self.services_layout.add_widget(balance_button)
        self.services_layout.add_widget(withdraw_button)
        self.services_layout.add_widget(deposit_button)
        self.services_layout.add_widget(currency_button)
        self.services_layout.add_widget(change_password_button)
        self.services_layout.add_widget(logout_button)

        self.root.add_widget(self.services_layout)

    def logout(self, instance):
        self.current_user = None
        self.root.clear_widgets()
        self.init_ui()

    def check_balance(self, instance):
        if self.current_user:
            self.current_user.deduct_maintenance_fee()
            self.show_transaction_history()
            self.show_popup('Balance', f'Your balance is Rs. {self.current_user.balance}')
        else:
            self.show_error_popup('Error', 'Login to check balance')

    def withdraw(self, instance):
        if self.current_user:
            if not self.current_user.locked:
                self.current_user.deduct_maintenance_fee()
                self.show_transaction_history()
                self.show_withdraw_deposit_popup("Withdraw", self.withdraw_action)
            else:
                self.show_error_popup("Error", "Account is locked. Contact admin.")
        else:
            self.show_error_popup('Error', 'Login to withdraw')

    def deposit(self, instance):
        if self.current_user:
            if not self.current_user.locked:
                self.current_user.deduct_maintenance_fee()
                self.show_transaction_history()
                self.show_withdraw_deposit_popup("Deposit", self.deposit_action)
            else:
                self.show_error_popup("Error", "Account is locked. Contact admin.")
        else:
            self.show_error_popup('Error', 'Login to deposit')

    def currency_option(self, instance):
        self.services_layout.clear_widgets()

        currencies = {
            "USD": "$ (Dollar) - 1.0",
            "INR": "₹ (Rupee) - 74.5",
            "GBP": "£ (Pound) - 0.72",
            "JPY": "¥ (Yen) - 113.05",
            # Add more currencies here
        }
        for code, details in currencies.items():
            currency_button = Button(text=details, size_hint=(None, None), size=(dp(200), dp(50)),
                                     background_color=(0.2, 0.6, 1, 1))
            currency_button.bind(on_press=lambda instance, code=code: self.convert_currency(code))
            self.services_layout.add_widget(currency_button)

        back_button = Button(text="Back", size_hint=(None, None), size=(dp(150), dp(50)),
                             background_color=(0.2, 0.6, 1, 1))
        back_button.bind(on_press=self.show_user_menu)
        self.services_layout.add_widget(back_button)

    def convert_currency(self, target_currency):
        conversion_rates = {
            "USD": 1.0,
            "INR": 74.5,
            "GBP": 0.72,
            "JPY": 113.05,
            # Add more conversion rates here
        }
        target_symbol = {
            "USD": "$",
            "INR": "₹",
            "GBP": "£",
            "JPY": "¥",
            # Add more symbols here
        }
        target_rate = conversion_rates.get(target_currency, 1.0)
        converted_balance = self.current_user.balance / target_rate
        symbol = target_symbol.get(target_currency, "")
        self.show_popup('Converted Balance', f'Your balance is {symbol}{converted_balance:.2f} in {target_currency}')

    def show_change_password_popup(self, instance):
        content = BoxLayout(orientation='vertical', padding=dp(20))
        current_password_input = TextInput(hint_text="Current Password", password=True)
        new_password_input = TextInput(hint_text="New Password", password=True)
        confirm_password_input = TextInput(hint_text="Confirm New Password", password=True)
        change_password_button = Button(text="Change Password")
        change_password_button.bind(
            on_press=lambda instance: self.change_password(current_password_input.text,
                                                           new_password_input.text,
                                                           confirm_password_input.text))

        content.add_widget(current_password_input)
        content.add_widget(new_password_input)
        content.add_widget(confirm_password_input)
        content.add_widget(change_password_button)

        popup = Popup(title='Change Password', content=content, size_hint=(None, None), size=(300, 300))
        popup.open()

    def change_password(self, current_password, new_password, confirm_password):
        if self.current_user and current_password == self.current_user.password:
            if new_password == confirm_password:
                self.current_user.password = new_password
                self.show_popup('Password Changed', 'Password has been changed successfully.')
            else:
                self.show_error_popup('Error', 'New passwords do not match.')
        else:
            self.show_error_popup('Error', 'Invalid current password.')

    def show_withdraw_deposit_popup(self, action, action_function):
        content = BoxLayout(orientation='vertical', padding=dp(20))
        amount_input = TextInput(hint_text=f"Enter {action} amount", input_filter='float')
        denomination_input = TextInput(hint_text="Enter denominations (comma-separated)", input_filter='int')
        action_button = Button(text=action)
        action_button.bind(on_press=lambda instance: action_function(float(amount_input.text), denomination_input.text))

        content.add_widget(amount_input)
        content.add_widget(denomination_input)
        content.add_widget(action_button)

        popup = Popup(title=action, content=content, size_hint=(None, None), size=(300, 300))
        popup.open()

    def withdraw_action(self, amount, denominations):
        denominations_list = [int(d) for d in denominations.split(',')]
        total_withdraw = sum(denominations_list)
        if total_withdraw == amount <= 50000:
            if amount <= self.current_user.balance:
                self.current_user.balance -= amount
                self.current_user.record_transaction(f'Withdrawal: -Rs. {amount}')
                self.show_popup('Withdrawal Successful', f'Amount withdrawn: Rs. {amount}')
            else:
                self.show_error_popup('Error', 'Insufficient balance.')
        else:
            self.show_error_popup('Error', 'Invalid withdrawal amount or denominations.')

    def deposit_action(self, amount, denominations):
        denominations_list = [int(d) for d in denominations.split(',')]
        total_deposit = sum(denominations_list)
        if total_deposit == amount <= 100000:
            self.current_user.balance += amount
            self.current_user.record_transaction(f'Deposit: +Rs. {amount}')
            self.show_popup('Deposit Successful', f'Amount deposited: Rs. {amount}')
        else:
            self.show_error_popup('Error', 'Invalid deposit amount or denominations.')

    def show_popup(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(300, 200))
        popup.open()

    def show_error_popup(self, title, content):
        popup = Popup(title=title, content=Label(text=f"Error: {content}"), size_hint=(None, None), size=(300, 200))
        popup.open()

    # Existing methods

    def show_transaction_history(self):
        if self.current_user:
            print("Transaction History:")
            for transaction in reversed(self.current_user.transaction_history):
                timestamp = transaction['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
                description = transaction['description']
                amount = transaction['amount']
                print(f'{timestamp}: {description} {"-" if amount < 0 else "+"}Rs. {abs(amount)}')

    def withdraw_action(self, amount, denominations):
        if self.current_user:
            if not self.current_user.locked:
                self.current_user.deduct_maintenance_fee()  # Deduct maintenance fee before withdrawal
                self.current_user.withdraw_action(amount, denominations)
                self.show_transaction_history()
            else:
                self.show_error_popup("Error", "Account is locked. Contact admin.")
        else:
            self.show_error_popup('Error', 'Login to withdraw')

    def deposit_action(self, amount, denominations):
        if self.current_user:
            if not self.current_user.locked:
                self.current_user.deduct_maintenance_fee()  # Deduct maintenance fee before deposit
                self.current_user.deposit_action(amount, denominations)
                self.show_transaction_history()
            else:
                self.show_error_popup("Error", "Account is locked. Contact admin.")
        else:
            self.show_error_popup('Error', 'Login to deposit')

    def show_popup(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(300, 200))
        popup.open()

    def show_error_popup(self, title, content):
        popup = Popup(title=title, content=Label(text=f"Error: {content}"), size_hint=(None, None), size=(300, 200))
        popup.open()

if __name__ == "__main__":
    ATM().run()





    
