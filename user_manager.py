import pandas as pd
from models import User  # Fixed import

class UserManager:
    def __init__(self, excel_file='users.xlsx'):
        self.excel_file = excel_file
        self.users = []
        self.load_existing_users()
    
    def load_existing_users(self):
        """Load existing users from Excel file"""
        try:
            df = pd.read_excel(self.excel_file)
            for _, row in df.iterrows():
                user = User(row['Username'], row['Password'])
                self.users.append(user)
            print(f"Loaded {len(self.users)} existing users from {self.excel_file}")
        except FileNotFoundError:
            print("No existing user file found. Starting fresh.")
    
    def create_user(self, username, password):
        """Create a new user and add to Excel"""
        # Check if username already exists
        if any(user.username == username for user in self.users):
            print(f"Username '{username}' already exists!")
            return False
        
        # Create new user
        new_user = User(username, password)
        self.users.append(new_user)
        
        # Save to Excel
        self.save_to_excel()
        print(f"User '{username}' created successfully!")
        return True
    
    def save_to_excel(self):
        """Save all users to Excel file"""
        user_data = [user.to_dict() for user in self.users]
        df = pd.DataFrame(user_data)
        df.to_excel(self.excel_file, index=False)
        print(f"Users saved to {self.excel_file}")
    
    def display_users(self):
        """Display all registered users"""
        print("\n--- Registered Users ---")
        for user in self.users:
            print(f"Username: {user.username}")
        print(f"Total users: {len(self.users)}")