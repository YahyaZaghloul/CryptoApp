# CryptoApp - Secure User Registration System 🔐

A Python-based secure user registration system with a modern PyQt5 GUI that implements multi-layer encryption for password protection.

## ✨ Features

### Security
- **Multi-layer Encryption**: SHA-256 → DES → AES → RSA encryption chain
- **Secure Storage**: Encrypted user data stored in Excel files
- **Session Management**: Secure login/logout functionality
- **Input Validation**: Real-time validation of user credentials

### User Interface
- **Modern Design**: Professional dark theme with gradient backgrounds
- **Responsive Layout**: Clean, intuitive interface with glassmorphic cards
- **Interactive Elements**: Smooth hover effects and focus states
- **Accessibility**: WCAG AA compliant color contrast ratios
- **Real-time Feedback**: Visual success/error messages

### Functionality
- **User Management**: Complete CRUD operations for user accounts
- **Live Encryption**: Encrypt any value on-demand through the GUI
- **User Table**: View all registered users with status indicators
- **Data Persistence**: Automatic loading of existing users on startup

## 🎨 UI Design

The application features a modern, professional color scheme:
- **Deep indigo gradient backgrounds** for visual depth
- **Vibrant cyan primary actions** (#06b6d4) for clear CTAs
- **Semi-transparent glassmorphic cards** for a contemporary look
- **High contrast text** for optimal readability
- **Smooth transitions** and hover effects for polish

See [STYLE_GUIDE.md](STYLE_GUIDE.md) and [COLOR_REFERENCE.md](COLOR_REFERENCE.md) for detailed design documentation.

## 🚀 Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Required Packages
```bash
pip install PyQt5 pandas openpyxl pycryptodome
```

## 💻 Usage

### Running the Application
```bash
cd CryptoApp
python main.py
```

### Application Flow
1. **Login/Register**: Start at the login screen or create a new account
2. **Registration**: Username (min 3 chars) + Password (min 8 chars)
3. **Home Dashboard**: After login, access:
   - Encryption tool (encrypt any text value)
   - User table (view all registered accounts)
   - Session controls (logout, refresh)

### File Structure
```
CryptoApp/
├── main.py              # Application entry point
├── crypto_engine.py     # Backend logic & encryption
├── ui_login.py          # Login page UI
├── ui_register.py       # Registration page UI
├── ui_home.py           # Home dashboard UI
├── models.py            # User data model
├── user_manager.py      # User CRUD operations
├── Encryption.py        # Multi-layer encryption
├── users.xlsx           # Encrypted user database
├── README.md            # This file
├── STYLE_GUIDE.md       # Complete design system
├── COLOR_REFERENCE.md   # Quick color palette reference
└── COLOR_IMPROVEMENTS.md # Design change documentation
```

## 🎨 Design Documentation

- **[STYLE_GUIDE.md](STYLE_GUIDE.md)**: Complete design system with all colors, spacing, typography
- **[COLOR_REFERENCE.md](COLOR_REFERENCE.md)**: Quick reference card for developers
- **[COLOR_IMPROVEMENTS.md](COLOR_IMPROVEMENTS.md)**: Detailed before/after comparison

## 🛠️ Technical Stack

- **Frontend**: PyQt5 (QtWidgets)
- **Backend**: Python 3.x
- **Database**: Excel (pandas + openpyxl)
- **Encryption**: pycryptodome (AES, DES, RSA)
- **Hashing**: hashlib (SHA-256)

## 🔒 Security Implementation

1. **Password Input** → SHA-256 Hash
2. **SHA-256 Hash** → DES Encryption
3. **DES Cipher** → AES Encryption
4. **AES Cipher** → RSA Encryption
5. **Final RSA Output** → Stored in Excel

## 📱 Screenshots

### Login Page
- Modern gradient background
- Clean card-based layout
- Real-time error validation

### Register Page
- Password confirmation
- Minimum length validation
- Success/error feedback

### Home Dashboard
- Welcome header with user info
- Live encryption tool
- User management table
- Action buttons (Logout, Refresh)

## 🎯 Key Improvements (v2.0)

### Color Scheme
✅ Professional indigo/cyan palette  
✅ WCAG AA accessibility compliance  
✅ Consistent across all pages  
✅ Modern glassmorphic effects  

### User Experience
✅ Smooth hover/focus transitions  
✅ Clear visual feedback  
✅ Intuitive navigation  
✅ Error handling with styled messages  

## 📄 License

This project is part of a secure authentication system demonstration.

## 🤝 Contributing

When contributing to the UI:
1. Follow the color palette in [COLOR_REFERENCE.md](COLOR_REFERENCE.md)
2. Maintain consistent spacing and border radius values
3. Ensure all text meets WCAG AA contrast standards
4. Test hover/focus states on all interactive elements

---

**Version**: 2.0  
**Last Updated**: November 26, 2025  
**Status**: ✅ Production Ready with Modern UI
