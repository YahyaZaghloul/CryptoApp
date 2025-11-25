import hashlib
import binascii
import Crypto
from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from user_manager import UserManager
password = ""
######################################################################
#SHA-256 Hashing
hashed = hashlib.sha256(password.encode()).hexdigest()
print("SHA-256 Hash:", hashed)
#DES Encryption
DESkey = get_random_bytes(8)
DES_object = DES.new(DESkey, DES.MODE_ECB)
SHA_value= hashed.encode()
DES_cipher = DES_object.encrypt(SHA_value)
decrypted_text = DES_object.decrypt(DES_cipher)
#AES Encryption
AESkey = get_random_bytes(16)
AEScipher = AES.new(AESkey, AES.MODE_ECB)
padded_data = pad(DES_cipher, AES.block_size)
AES_cipher = AEScipher.encrypt(padded_data)
#RSA Encryption
RSAkey = RSA.generate(2048)
private_key = RSAkey.export_key()
public_key = RSAkey.publickey().export_key()
private_cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
public_cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
RSA_encrypted = public_cipher.encrypt(AES_cipher)
######################################################################
user_manager = UserManager()
print("=== User Registration System ===")
print("Enter user details (type 'quit' to exit)")
    
while True:
        print("\n" + "="*40)
        username = input("Enter username: ").strip()
        
        # Exit condition
        if username.lower() == 'quit':
            break
        
        if not username:
            print("Username cannot be empty!")
            continue
        
        password = input("Enter password: ").strip()
        if not password:
            print("Password cannot be empty!")
            continue
        
        # Create user
        user_manager.create_user(username, RSA_encrypted)
        
        # Ask if user wants to continue
        continue_input = input("\nAdd another user? (y/n): ").lower()
        if continue_input != 'y':
            break
    
    # Display all registered users
user_manager.display_users()
print("\nThank you for using the User Registration System!")
######################################################################