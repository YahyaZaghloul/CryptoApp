# CryptoApp - Secure Authentication System 🔐

A professional-grade user authentication system featuring multi-layer cryptographic protection and a modern PyQt5 interface. Built with enterprise security practices and contemporary UI/UX design principles.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [System Requirements](#system-requirements)
- [Security Implementation](#security-implementation)
- [User Interface](#user-interface)
- [Project Structure](#project-structure)
- [Documentation](#documentation)
- [Technology Stack](#technology-stack)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

CryptoApp is a secure user registration and authentication system that implements a sophisticated multi-layer encryption pipeline. The application combines robust cryptographic security with an accessible, professionally designed user interface built on PyQt5.

**Version:** 2.0  
**Status:** Production Ready  
**License:** MIT

---

## Key Features

### 🔒 Enterprise Security
- **Multi-Layer Encryption Pipeline**: SHA-256 → DES → AES → RSA
- **Secure Key Management**: Isolated storage with per-user encryption keys
- **Session Security**: Stateful authentication with automatic logout
- **Password Validation**: Configurable strength requirements
- **Secure Storage**: Encrypted persistence using Excel-based data store

### 🎨 Modern User Interface
- **Professional Design**: WCAG AA compliant color scheme
- **Responsive Layout**: Adaptive interface with smooth transitions
- **Glassmorphic Design**: Contemporary card-based UI with depth
- **Real-Time Feedback**: Immediate validation and error messaging
- **Accessible**: High-contrast text, keyboard navigation support

### ⚙️ Core Functionality
- **User Management**: Registration, authentication, and session handling
- **Live Encryption**: On-demand encryption tool for arbitrary values
- **Data Persistence**: Automatic user data loading and synchronization
- **Administrative View**: Comprehensive user table with status tracking

---

## Architecture

### System Design

```
┌─────────────────────────────────────────┐
│           PyQt5 GUI Layer               │
│  (Login, Register, Home, Welcome)       │
└───────────────┬─────────────────────────┘
                │
┌───────────────▼─────────────────────────┐
│        CryptoEngine (Facade)            │
│   (Business Logic & Orchestration)      │
└───────────┬─────────────┬───────────────┘
            │             │
┌───────────▼────────┐  ┌─▼───────────────┐
│  UserManager       │  │  Encryption      │
│  (Data Access)     │  │  (Crypto Layer)  │
└───────────┬────────┘  └──────────────────┘
            │
┌───────────▼────────────────────────────┐
│   Excel Storage (users.xlsx,          │
│   encryption_keys.xlsx)                │
└────────────────────────────────────────┘
```

### Encryption Flow

```
User Password
    │
    ├─→ SHA-256 Hashing
    │
    ├─→ DES Encryption (64-bit key)
    │
    ├─→ AES Encryption (128-bit key)
    │
    ├─→ RSA Encryption (2048-bit key)
    │
    └─→ Hexadecimal Storage
```

---

## Installation

### Prerequisites

- **Python**: 3.7 or higher
- **pip**: Latest version recommended
- **Operating System**: Windows, macOS, or Linux

### Dependencies

Install required packages using pip:

```bash
pip install -r requirements.txt
```

**Core Dependencies:**
```
PyQt5>=5.15.0
pandas>=1.3.0
openpyxl>=3.0.0
pycryptodome>=3.15.0
```

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd CryptoApp
   ```

2. **Install dependencies:**
   ```bash
   pip install PyQt5 pandas openpyxl pycryptodome
   ```

3. **Initialize the system:**
   ```bash
   python initialize_system.py
   ```

4. **Launch the application:**
   ```bash
   python main.py
   ```

---

## Quick Start

### First-Time Setup

1. Run the initialization script to create required Excel files:
   ```bash
   python initialize_system.py
   ```

2. Launch the application:
   ```bash
   python main.py
   ```

3. Create your first account:
   - Click **"Create Account"** from the welcome screen
   - Enter a username (minimum 3 characters)
   - Create a password (minimum 8 characters)
   - Confirm your password

4. Access the dashboard:
   - Log in with your credentials
   - Use the encryption tool to secure additional data
   - View all registered users in the table

---

## System Requirements

### Minimum Requirements
- **CPU**: 1 GHz processor
- **RAM**: 2 GB
- **Storage**: 50 MB free space
- **Display**: 1024×768 resolution

### Recommended Requirements
- **CPU**: Multi-core processor
- **RAM**: 4 GB or higher
- **Storage**: 100 MB free space
- **Display**: 1920×1080 resolution or higher

---

## Security Implementation

### Cryptographic Layers

1. **SHA-256 Hashing**
   - Initial password transformation
   - One-way cryptographic hash function
   - 256-bit output

2. **DES Encryption**
   - Data Encryption Standard
   - 64-bit block cipher
   - Unique 8-byte key per user

3. **AES Encryption**
   - Advanced Encryption Standard
   - 128-bit block cipher
   - Unique 16-byte key per user

4. **RSA Encryption**
   - Public-key cryptography
   - 2048-bit key pair
   - PKCS#1 OAEP padding scheme

### Key Management

- Each user has **unique encryption keys**
- Keys are stored separately from encrypted data
- Private keys never exposed through the interface
- Automatic key generation during registration

### Best Practices

- Passwords are never stored in plaintext
- Keys are isolated per-user for compartmentalization
- All encryption uses industry-standard libraries (PyCryptodome)
- Session management prevents unauthorized access

---

## User Interface

### Design Philosophy

The interface follows modern design principles:
- **Minimalist**: Clean layouts without visual clutter
- **Intuitive**: Clear navigation and self-explanatory controls
- **Responsive**: Immediate feedback for all interactions
- **Accessible**: WCAG AA compliant for inclusivity

### Color Scheme

| Element | Color | Purpose |
|---------|-------|---------|
| Background | `#0a0e27` | Deep indigo base |
| Primary Action | `#06b6d4` | Vibrant cyan for CTAs |
| Card Surface | `rgba(30, 41, 59, 0.75)` | Semi-transparent slate |
| Success | `#10b981` | Emerald for positive feedback |
| Error | `#fb7185` | Rose for error states |

### Screenshots

#### Welcome Screen
Modern landing page with navigation options.

#### Login Interface
Streamlined authentication with real-time validation.

#### Registration Form
Comprehensive account creation with password confirmation.

#### Home Dashboard
Central hub featuring encryption tools and user management.

---

## Project Structure

```
CryptoApp/
├── main.py                    # Application entry point
├── crypto_engine.py           # Business logic facade
├── models.py                  # Data models
├── user_manager.py            # Database operations
├── Encryption.py              # Cryptographic functions
│
├── ui_welcome.py              # Welcome screen UI
├── ui_login.py                # Login screen UI
├── ui_register.py             # Registration screen UI
├── ui_home.py                 # Dashboard UI
│
├── initialize_system.py       # System setup utility
├── test_encryption.py         # Encryption tests
├── view_keys.py               # Key management utility
├── excel_column_fix.py        # Excel formatting tool
│
├── users.xlsx                 # User database
├── encryption_keys.xlsx       # Key storage
│
├── README.md                  # This file
├── STYLE_GUIDE.md             # Complete design system
├── COLOR_REFERENCE.md         # Quick color reference
├── COLOR_IMPROVEMENTS.md      # Design changelog
└── requirements.txt           # Python dependencies
```

---

## Documentation

Comprehensive documentation is available:

- **[STYLE_GUIDE.md](STYLE_GUIDE.md)**: Complete UI design system with colors, typography, and spacing
- **[COLOR_REFERENCE.md](COLOR_REFERENCE.md)**: Quick reference for developers implementing new features
- **[COLOR_IMPROVEMENTS.md](COLOR_IMPROVEMENTS.md)**: Detailed changelog of design evolution

---

## Technology Stack

### Frontend
- **Framework**: PyQt5 5.15+
- **UI Components**: QtWidgets
- **Styling**: QSS (Qt Style Sheets)

### Backend
- **Language**: Python 3.7+
- **Cryptography**: PyCryptodome 3.15+
- **Data Storage**: Pandas + OpenPyXL

### Libraries
| Library | Purpose | Version |
|---------|---------|---------|
| PyQt5 | GUI framework | 5.15+ |
| pandas | Data manipulation | 1.3+ |
| openpyxl | Excel operations | 3.0+ |
| pycryptodome | Cryptographic functions | 3.15+ |
| hashlib | SHA-256 hashing | Built-in |

---

## Contributing

We welcome contributions! Please follow these guidelines:

### Code Style
- Follow PEP 8 conventions
- Use type hints where applicable
- Document all public functions with docstrings

### UI Contributions
- Reference [COLOR_REFERENCE.md](COLOR_REFERENCE.md) for color values
- Maintain consistent spacing (14px button padding, etc.)
- Ensure WCAG AA contrast compliance (4.5:1 minimum)
- Test hover and focus states on all interactive elements

### Pull Request Process
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License. See `LICENSE` file for details.

---

## Support

For issues, questions, or feature requests:
- Open an issue on GitHub
- Contact the development team
- Refer to the documentation files

---

## Acknowledgments

- Built with [PyQt5](https://www.riverbankcomputing.com/software/pyqt/)
- Cryptography powered by [PyCryptodome](https://www.pycryptodome.org/)
- Design inspired by modern web frameworks (Tailwind CSS, Material Design)

---

**CryptoApp** - Secure by Design, Modern by Nature

*Last Updated: December 9, 2024*