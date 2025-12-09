"""
Script to properly view encryption keys from Excel
Handles long RSA private keys that don't display well in Excel
"""

import pandas as pd
import os

def view_encryption_keys():
    """Display encryption keys in a readable format"""
    
    keys_file = 'encryption_keys.xlsx'
    
    if not os.path.exists(keys_file):
        print(f"❌ File not found: {keys_file}")
        print("Run initialize_system.py first or register a user.")
        return
    
    try:
        df = pd.read_excel(keys_file)
        
        if df.empty:
            print("📋 No encryption keys found yet.")
            print("Register a user first to see their keys.")
            return
        
        print("="*80)
        print("ENCRYPTION KEYS DATABASE")
        print("="*80)
        print(f"\nTotal users: {len(df)}\n")
        
        for idx, row in df.iterrows():
            print(f"{'='*80}")
            print(f"USER #{idx + 1}: {row['Username']}")
            print(f"{'='*80}")
            
            print(f"\n📌 DES Key:")
            print(f"   {row['DES_Key']}")
            
            print(f"\n📌 AES Key:")
            print(f"   {row['AES_Key']}")
            
            print(f"\n📌 RSA Private Key (length: {len(str(row['RSA_Private_Key']))} chars):")
            rsa_key = str(row['RSA_Private_Key'])
            # Display first 100 and last 100 characters
            print(f"   {rsa_key[:100]}...")
            print(f"   ...{rsa_key[-100:]}")
            
            print(f"\n📌 Encrypted Password:")
            encrypted = str(row['Encrypted_Password'])
            print(f"   {encrypted[:80]}...")
            print(f"   (Total length: {len(encrypted)} chars)")
            
            print(f"\n{'-'*80}\n")
        
        # Show statistics
        print(f"{'='*80}")
        print("STATISTICS")
        print(f"{'='*80}")
        print(f"Total Users: {len(df)}")
        print(f"Average RSA Key Length: {df['RSA_Private_Key'].apply(lambda x: len(str(x))).mean():.0f} chars")
        print(f"Average Encrypted Password Length: {df['Encrypted_Password'].apply(lambda x: len(str(x))).mean():.0f} chars")
        print(f"{'='*80}")
        
    except Exception as e:
        print(f"❌ Error reading keys: {e}")

def export_user_keys(username):
    """Export specific user's keys to a text file"""
    
    keys_file = 'encryption_keys.xlsx'
    
    try:
        df = pd.read_excel(keys_file)
        user_row = df[df['Username'] == username]
        
        if user_row.empty:
            print(f"❌ User '{username}' not found.")
            return
        
        output_file = f"{username}_keys.txt"
        
        with open(output_file, 'w') as f:
            f.write(f"ENCRYPTION KEYS FOR USER: {username}\n")
            f.write("="*80 + "\n\n")
            
            f.write("DES Key:\n")
            f.write(f"{user_row.iloc[0]['DES_Key']}\n\n")
            
            f.write("AES Key:\n")
            f.write(f"{user_row.iloc[0]['AES_Key']}\n\n")
            
            f.write("RSA Private Key:\n")
            f.write(f"{user_row.iloc[0]['RSA_Private_Key']}\n\n")
            
            f.write("Encrypted Password:\n")
            f.write(f"{user_row.iloc[0]['Encrypted_Password']}\n\n")
            
            f.write("="*80 + "\n")
            f.write("⚠️  KEEP THIS FILE SECURE - Contains decryption keys!\n")
        
        print(f"✅ Keys exported to: {output_file}")
        
    except Exception as e:
        print(f"❌ Error exporting keys: {e}")

def main():
    print("\n" + "="*80)
    print("ENCRYPTION KEYS VIEWER")
    print("="*80)
    
    while True:
        print("\nOptions:")
        print("1. View all keys")
        print("2. Export specific user's keys to text file")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ").strip()
        
        if choice == '1':
            print()
            view_encryption_keys()
        elif choice == '2':
            username = input("Enter username: ").strip()
            export_user_keys(username)
        elif choice == '3':
            print("\nGoodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
