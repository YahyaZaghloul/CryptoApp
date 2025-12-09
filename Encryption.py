import hashlib
import binascii
from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_password(password):
    """
    Encrypt password using SHA256 -> DES -> AES -> RSA chain
    Returns: (encrypted_hex, keys_dict)
    """
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
    private_key = RSAkey.export_key()
    public_cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    RSA_encrypted = public_cipher.encrypt(AES_cipher)
    
    # Convert to hex string for storage
    encrypted_hex = binascii.hexlify(RSA_encrypted).decode()
    
    # Store all keys needed for decryption
    keys_dict = {
        'DES_key': binascii.hexlify(DESkey).decode(),
        'AES_key': binascii.hexlify(AESkey).decode(),
        'RSA_private_key': private_key.decode(),
        'encrypted_password': encrypted_hex
    }
    
    return encrypted_hex, keys_dict

def decrypt_password(encrypted_hex, keys_dict):
    """
    Decrypt password using the stored keys
    Returns: original password hash (SHA-256)
    """
    try:
        # Extract keys
        DESkey = binascii.unhexlify(keys_dict['DES_key'])
        AESkey = binascii.unhexlify(keys_dict['AES_key'])
        private_key = keys_dict['RSA_private_key'].encode()
        
        # Convert encrypted hex back to bytes
        RSA_encrypted = binascii.unhexlify(encrypted_hex)
        
        # RSA Decryption
        rsa_key = RSA.import_key(private_key)
        private_cipher = PKCS1_OAEP.new(rsa_key)
        AES_cipher = private_cipher.decrypt(RSA_encrypted)
        
        # AES Decryption
        AEScipher = AES.new(AESkey, AES.MODE_ECB)
        DES_cipher = unpad(AEScipher.decrypt(AES_cipher), AES.block_size)
        
        # DES Decryption
        DES_object = DES.new(DESkey, DES.MODE_ECB)
        SHA_value = unpad(DES_object.decrypt(DES_cipher), DES.block_size)
        
        # Return the SHA-256 hash (this is what we'll compare for login)
        return SHA_value.decode()
        
    except Exception as e:
        raise Exception(f"Decryption failed: {str(e)}")

def verify_password(input_password, encrypted_hex, keys_dict):
    """
    Verify if input password matches the encrypted one
    Returns: True if match, False otherwise
    """
    try:
        # Hash the input password
        input_hash = hashlib.sha256(input_password.encode()).hexdigest()
        
        # Decrypt stored password to get its hash
        stored_hash = decrypt_password(encrypted_hex, keys_dict)
        
        # Compare hashes
        return input_hash == stored_hash
    except Exception as e:
        print(f"Verification error: {e}")
        return False

# Keep the old main() function for backward compatibility if needed
def main():
    from user_manager import UserManager
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
        
        # Encrypt the password and get keys
        encrypted_password, keys_dict = encrypt_password(password)
        
        # Create user with encrypted password and keys
        user_manager.create_user(username, encrypted_password, keys_dict)
        
        # Ask if user wants to continue
        continue_input = input("\nAdd another user? (y/n): ").lower()
        if continue_input != 'y':
            break
        
    user_manager.display_users()
    print("\nThank you for using the Secure User Registration System!")

if __name__ == "__main__":
    main()