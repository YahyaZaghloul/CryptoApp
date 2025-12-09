import pandas as pd
import json
from models import User

class UserManager:
    def __init__(self, excel_file='users.xlsx', keys_file='encryption_keys.xlsx'):
        self.excel_file = excel_file
        self.keys_file = keys_file
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
    
    def create_user(self, username, password, keys_dict=None):
        """Create a new user and add to Excel with encryption keys"""
        # Check if username already exists
        if any(user.username == username for user in self.users):
            print(f"Username '{username}' already exists!")
            return False
        
        # Create new user
        new_user = User(username, password)
        self.users.append(new_user)
        
        # Save user to main Excel
        self.save_to_excel()
        
        # Save encryption keys if provided
        if keys_dict:
            self.save_encryption_keys(username, keys_dict)
        
        print(f"User '{username}' created successfully!")
        return True
    
    def save_encryption_keys(self, username, keys_dict):
        """Save encryption keys to separate Excel file"""
        try:
            # Try to load existing keys file
            try:
                df = pd.read_excel(self.keys_file)
                keys_data = df.to_dict('records')
            except FileNotFoundError:
                keys_data = []
            
            # Add new user's keys
            key_entry = {
                'Username': username,
                'DES_Key': keys_dict['DES_key'],
                'AES_Key': keys_dict['AES_key'],
                'RSA_Private_Key': keys_dict['RSA_private_key'],
                'Encrypted_Password': keys_dict['encrypted_password']
            }
            keys_data.append(key_entry)
            
            # Save to Excel
            df = pd.DataFrame(keys_data)
            df.to_excel(self.keys_file, index=False)
            print(f"Encryption keys saved for '{username}' to {self.keys_file}")
            
        except Exception as e:
            print(f"Error saving encryption keys: {e}")
    
    def get_encryption_keys(self, username):
        """Retrieve encryption keys for a specific user"""
        try:
            df = pd.read_excel(self.keys_file)
            user_row = df[df['Username'] == username]
            
            if user_row.empty:
                return None
            
            keys_dict = {
                'DES_key': user_row.iloc[0]['DES_Key'],
                'AES_key': user_row.iloc[0]['AES_Key'],
                'RSA_private_key': user_row.iloc[0]['RSA_Private_Key'],
                'encrypted_password': user_row.iloc[0]['Encrypted_Password']
            }
            return keys_dict
            
        except FileNotFoundError:
            print(f"Keys file not found: {self.keys_file}")
            return None
        except Exception as e:
            print(f"Error retrieving encryption keys: {e}")
            return None
    
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