import hashlib
import binascii
from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from user_manager import UserManager

def encrypt_password(password):
    """Encrypt password using SHA256 -> DES -> AES -> RSA chain"""
    # SHA-256 Hashing
    hashed = hashlib.sha256(password.encode()).hexdigest()
    
    # DES Encryption
    DESkey = get_random_bytes(8)
    DES_object = DES.new(DESkey, DES.MODE_ECB)
    SHA_value = hashed.encode()
    DES_cipher = DES_object.encrypt(pad(SHA_value, DES.block_size))
    
    # AES Encryption
    AESkey = get_random_bytes(16)
    AEScipher = AES.new(AESkey, AES.MODE_ECB)
    padded_data = pad(DES_cipher, AES.block_size)
    AES_cipher = AEScipher.encrypt(padded_data)
    
    # RSA Encryption
    RSAkey = RSA.generate(2048)
    public_key = RSAkey.publickey().export_key()
    public_cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    RSA_encrypted = public_cipher.encrypt(AES_cipher)
    
    # Convert to hex string for storage
    encrypted_hex = binascii.hexlify(RSA_encrypted).decode()
    
    return encrypted_hex

def main():
    user_manager = UserManager()
    
    print("=== Secure User Registration System ===")
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
        
        # Encrypt the password
        encrypted_password = encrypt_password(password)
        
        # Create user with encrypted password
        user_manager.create_user(username, encrypted_password)
        
        # Ask if user wants to continue
        continue_input = input("\nAdd another user? (y/n): ").lower()
        if continue_input != 'y':
            break
        
    user_manager.display_users()
    print("\nThank you for using the Secure User Registration System!")

if __name__ == "__main__":
    main()