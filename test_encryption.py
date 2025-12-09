"""
Test script to verify encryption and decryption functionality
"""

from Encryption import encrypt_password, decrypt_password, verify_password

def test_encryption_decryption():
    print("="*60)
    print("Testing Encryption/Decryption System")
    print("="*60)
    
    # Test password
    original_password = "MySecurePass123!"
    print(f"\n1. Original Password: {original_password}")
    
    # Encrypt
    print("\n2. Encrypting password...")
    encrypted_hex, keys_dict = encrypt_password(original_password)
    print(f"   ✓ Encrypted (hex): {encrypted_hex[:50]}...")
    print(f"   ✓ DES Key: {keys_dict['DES_key']}")
    print(f"   ✓ AES Key: {keys_dict['AES_key']}")
    print(f"   ✓ RSA Private Key: [length={len(keys_dict['RSA_private_key'])} chars]")
    
    # Decrypt
    print("\n3. Decrypting password...")
    decrypted_hash = decrypt_password(encrypted_hex, keys_dict)
    print(f"   ✓ Decrypted hash: {decrypted_hash[:50]}...")
    
    # Verify with correct password
    print("\n4. Verifying with correct password...")
    is_valid = verify_password(original_password, encrypted_hex, keys_dict)
    print(f"   ✓ Verification result: {is_valid}")
    
    # Verify with wrong password
    print("\n5. Verifying with wrong password...")
    is_valid_wrong = verify_password("WrongPassword123", encrypted_hex, keys_dict)
    print(f"   ✓ Verification result: {is_valid_wrong}")
    
    print("\n" + "="*60)
    if is_valid and not is_valid_wrong:
        print("✓ All tests passed!")
    else:
        print("✗ Tests failed!")
    print("="*60)

if __name__ == "__main__":
    test_encryption_decryption()
