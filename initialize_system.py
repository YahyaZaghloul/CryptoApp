"""
Initialization script to create the Excel files with proper structure
Run this before starting the application for the first time
"""

import pandas as pd
import os

def initialize_excel_files():
    """Create initial Excel files with proper structure"""
    
    # Create users.xlsx
    users_file = 'users.xlsx'
    if not os.path.exists(users_file):
        users_df = pd.DataFrame(columns=['Username', 'Password', 'Status'])
        users_df.to_excel(users_file, index=False)
        print(f"✓ Created {users_file}")
    else:
        print(f"ℹ {users_file} already exists")
    
    # Create encryption_keys.xlsx
    keys_file = 'encryption_keys.xlsx'
    if not os.path.exists(keys_file):
        keys_df = pd.DataFrame(columns=[
            'Username', 
            'DES_Key', 
            'AES_Key', 
            'RSA_Private_Key',
            'Encrypted_Password'
        ])
        keys_df.to_excel(keys_file, index=False)
        print(f"✓ Created {keys_file}")
    else:
        print(f"ℹ {keys_file} already exists")
    
    print("\n✓ System initialized successfully!")
    print("\nFile Structure:")
    print(f"  • {users_file} - Stores usernames and encrypted passwords")
    print(f"  • {keys_file} - Stores decryption keys for each user")
    print("\n⚠ IMPORTANT: Keep encryption_keys.xlsx secure!")
    print("  This file contains the keys needed to decrypt passwords.")

if __name__ == "__main__":
    print("="*50)
    print("CryptoApp Initialization")
    print("="*50)
    print()
    initialize_excel_files()
    print()
    print("="*50)
