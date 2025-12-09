import sys
from typing import List

from PyQt5 import QtWidgets

from crypto_engine import CryptoEngine
from models import User
from ui_home import HomeWidget
from ui_login import LoginWidget
from ui_register import RegisterWidget
from ui_welcome import WelcomeWidget


class MainWindow(QtWidgets.QMainWindow):
    """Primary window hosting stacked authentication and home views."""

    def __init__(self, engine: CryptoEngine, parent=None) -> None:
        super().__init__(parent)
        self.engine = engine
        self.setWindowTitle("CryptoApp - Secure Vault")
        self.resize(900, 600)

        self.stack = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stack)

        self.login_view = LoginWidget()
        self.register_view = RegisterWidget()
        self.home_view = HomeWidget()
        self.welcome_view = WelcomeWidget()

        self.stack.addWidget(self.welcome_view)
        self.stack.addWidget(self.login_view)
        self.stack.addWidget(self.register_view)
        self.stack.addWidget(self.home_view)

        # Welcome navigation
        self.welcome_view.loginNavigate.connect(self.show_login)
        self.welcome_view.registerNavigate.connect(self.show_register)

        self.login_view.loginRequested.connect(self.handle_login)
        self.login_view.registerNavigate.connect(self.show_register)

        self.register_view.registerRequested.connect(self.handle_register)
        self.register_view.backToLogin.connect(self.show_login)

        self.home_view.logoutRequested.connect(self.handle_logout)
        self.home_view.refreshRequested.connect(self.refresh_users)
        self.home_view.encryptRequested.connect(self.encrypt_value)

        self.show_welcome()

    def show_welcome(self) -> None:
        self.stack.setCurrentWidget(self.welcome_view)

    def show_login(self) -> None:
        self.login_view.reset_fields()
        self.stack.setCurrentWidget(self.login_view)

    def show_register(self) -> None:
        self.register_view.reset_fields()
        self.stack.setCurrentWidget(self.register_view)

    def show_home(self) -> None:
        current = self.engine.current_user
        if not current:
            self.show_login()
            return
        users = [
            (
                user.username,
                str(user.password),
                'Logged In' if user.is_logged_in else 'Active'
            )
            for user in self.engine.get_all_users()
        ]
        self.home_view.populate(current.username, users)
        self.home_view.clear_feedback()
        self.stack.setCurrentWidget(self.home_view)

    def handle_login(self, username: str, password: str) -> None:
        success, message = self.engine.authenticate_user(username, password)
        if success:
            self.login_view.set_error("")
            self.show_home()
            self.statusBar().showMessage(message, 5000)
        else:
            self.login_view.set_error(message)

    def handle_register(self, username: str, password: str, confirm_password: str) -> None:
        self.register_view.reset_styles()
        success, message = self.engine.register_user(username, password, confirm_password)
        if success:
            self.register_view.show_success(message)
        else:
            self.register_view.set_error(message)

    def handle_logout(self) -> None:
        self.engine.logout()
        self.home_view.show_feedback("Session ended.")
        self.show_welcome()

    def refresh_users(self) -> None:
        users = self.engine.refresh_from_storage()
        user_rows = [
            (
                user.username,
                str(user.password),
                'Logged In' if user.is_logged_in else 'Active'
            )
            for user in users
        ]
        current = self.engine.current_user
        if current:
            self.home_view.populate(current.username, user_rows)
            self.home_view.show_feedback("User list refreshed.")

    def encrypt_value(self, value: str) -> None:
        success, message = self.engine.encrypt_value(value)
        if success:
            self.home_view.show_encrypted_value(message)
            self.home_view.show_feedback("Value encrypted successfully.")
        else:
            self.home_view.show_feedback(message)
            self.home_view.show_encrypted_value("")


def gather_users(users: List[User]) -> List[tuple[str, str]]:
    return [(user.username, 'Logged In' if user.is_logged_in else 'Active') for user in users]


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    # Load global stylesheet
    try:
        with open('styles/modern.qss', 'r', encoding='utf-8') as f:
            app.setStyleSheet(f.read())
    except Exception:
        pass
    engine = CryptoEngine()
    window = MainWindow(engine)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
