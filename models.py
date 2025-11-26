class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_logged_in = False
    
    def login(self, entered_password, entered_username):
        if entered_password == self.password and entered_username == self.username:
            self.is_logged_in = True
            return f"Welcome {self.username}!"
        else:
            return "Invalid credentials!"
    
    def logout(self):
        self.is_logged_in = False
        return f"{self.username} logged out."
    
    def get_info(self):
        status = "logged in" if self.is_logged_in else "logged out"
        return f"User: {self.username} - Status: {status}"
    
    def to_dict(self):
        """Convert user data to dictionary for Excel export"""
        return {
            'Username': self.username,
            'Password': self.password,
            'Status': 'Active'
        }