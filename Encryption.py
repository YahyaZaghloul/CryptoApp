import hashlib
import binascii
import Crypto
from Crypto.Cipher import AES
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
#SHA-256 Hashing
password = input("Enter password: ")
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

print('DES Encrypted: ', hex(binascii.hexlify(DES_cipher)).decode())
print('AES Encrypted: ', hex(binascii.hexlify(AES_cipher)).decode())
print('RSA Encrypted: ', hex(binascii.hexlify(RSA_encrypted)).decode())