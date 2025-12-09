import hashlib
from typing import List, Optional, Tuple

from Encryption import encrypt_password, verify_password
from models import User
from user_manager import UserManager


class CryptoEngine:
    """Facade that bridges the GUI with encryption and user management."""

    def __init__(self, excel_file: str = 'users.xlsx') -> None:
        self._user_manager = UserManager(excel_file)
        self._current_user: Optional[User] = None

    @property
    def current_user(self) -> Optional[User]:
        return self._current_user

    def register_user(self, username: str, password: str, confirm_password: str) -> Tuple[bool, str]:
        username = username.strip()
        if not username:
            return False, 'Username is required.'
        if len(username) < 3:
            return False, 'Username must be at least 3 characters long.'
        if not password or len(password) < 8:
            return False, 'Password must be at least 8 characters long.'
        if password != confirm_password:
            return False, 'Passwords do not match.'
        if any(user.username == username for user in self._user_manager.users):
            return False, 'That username is already in use.'

        # Encrypt password and get keys
        encrypted_hex, keys_dict = encrypt_password(password)

        # Create user with encrypted password and save keys
        if self._user_manager.create_user(username, encrypted_hex, keys_dict):
            return True, 'Account created successfully. You can log in now.'
        return False, 'Unable to create user. Please try again.'

    def authenticate_user(self, username: str, password: str) -> Tuple[bool, str]:
        username = username.strip()
        if not username or not password:
            return False, 'Username and password are required.'

        user = self._find_user(username)
        if not user:
            return False, 'Invalid username or password.'

        # Get encryption keys for this user
        keys_dict = self._user_manager.get_encryption_keys(username)
        if not keys_dict:
            return False, 'Authentication failed. Unable to retrieve encryption keys.'

        # Verify password using decryption
        encrypted_password = user.password
        if not verify_password(password, encrypted_password, keys_dict):
            return False, 'Invalid username or password.'

        # Login successful
        self._current_user = user
        self._current_user.is_logged_in = True
        return True, f'Welcome back, {user.username}!'

    def logout(self) -> Tuple[bool, str]:
        if self._current_user:
            self._current_user.is_logged_in = False
        self._current_user = None
        return True, 'You have been logged out.'

    def get_all_users(self) -> List[User]:
        return list(self._user_manager.users)

    def refresh_from_storage(self) -> List[User]:
        excel_file = self._user_manager.excel_file
        self._user_manager = UserManager(excel_file)
        if self._current_user:
            refreshed_user = self._find_user(self._current_user.username)
            if refreshed_user:
                refreshed_user.is_logged_in = True
                self._current_user = refreshed_user
            else:
                self._current_user = None
        return self.get_all_users()

    def encrypt_value(self, value: str) -> Tuple[bool, str]:
        value = value.strip()
        if not value:
            return False, 'Enter a value to encrypt.'
        try:
            encrypted, keys_dict = encrypt_password(value)
            # Return both encrypted value and a formatted version of keys
            result = f"Encrypted: {encrypted}\n\n"
            result += "Keys (save these to decrypt):\n"
            result += f"DES Key: {keys_dict['DES_key'][:32]}...\n"
            result += f"AES Key: {keys_dict['AES_key'][:32]}...\n"
            result += "RSA Private Key: [stored securely]\n"
        except Exception as exc:
            return False, f'Encryption failed: {exc}'
        return True, result

    def _find_user(self, username: str) -> Optional[User]:
        for user in self._user_manager.users:
            if user.username == username:
                return user
        return None