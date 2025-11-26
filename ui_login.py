from PyQt5 import QtCore, QtGui, QtWidgets


class LoginWidget(QtWidgets.QWidget):
    """Login form with validation hints and navigation to registration."""

    loginRequested = QtCore.pyqtSignal(str, str)
    registerNavigate = QtCore.pyqtSignal()

    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("AppRoot")
        self._build_ui()
        self._apply_styles()

    def _build_ui(self) -> None:
        wrapper_layout = QtWidgets.QVBoxLayout(self)
        wrapper_layout.setContentsMargins(0, 0, 0, 0)
        wrapper_layout.setSpacing(0)

        backdrop = QtWidgets.QFrame(self)
        backdrop_layout = QtWidgets.QVBoxLayout(backdrop)
        backdrop_layout.setContentsMargins(40, 40, 40, 40)
        backdrop_layout.addStretch()

        card = QtWidgets.QFrame(backdrop)
        card.setObjectName("Card")
        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(50)
        shadow.setOffset(0, 20)
        shadow.setColor(QtGui.QColor(10, 14, 39, 200))
        card.setGraphicsEffect(shadow)
        card_layout = QtWidgets.QVBoxLayout(card)
        card_layout.setContentsMargins(32, 32, 32, 32)
        card_layout.setSpacing(18)

        title = QtWidgets.QLabel("CryptoApp Login", card)
        title.setObjectName("Title")
        title.setAlignment(QtCore.Qt.AlignHCenter)
        card_layout.addWidget(title)

        subtitle = QtWidgets.QLabel("Sign in to manage your secure vault.", card)
        subtitle.setAlignment(QtCore.Qt.AlignHCenter)
        subtitle.setObjectName("Subtitle")
        card_layout.addWidget(subtitle)

        self.username_input = QtWidgets.QLineEdit(card)
        self.username_input.setPlaceholderText("Username")
        self.username_input.setObjectName("usernameInput")
        card_layout.addWidget(self.username_input)

        self.password_input = QtWidgets.QLineEdit(card)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("passwordInput")
        card_layout.addWidget(self.password_input)

        self.error_label = QtWidgets.QLabel(card)
        self.error_label.setObjectName("ErrorLabel")
        self.error_label.setVisible(False)
        card_layout.addWidget(self.error_label)

        self.login_button = QtWidgets.QPushButton("Sign In", card)
        self.login_button.clicked.connect(self._emit_login)
        card_layout.addWidget(self.login_button)

        switch_row = QtWidgets.QHBoxLayout()
        switch_row.addStretch()
        register_btn = QtWidgets.QPushButton("Create account", card)
        register_btn.setFlat(True)
        register_btn.setObjectName("LinkButton")
        register_btn.clicked.connect(self.registerNavigate.emit)
        switch_row.addWidget(QtWidgets.QLabel("New here?", card))
        switch_row.addWidget(register_btn)
        switch_row.addStretch()
        card_layout.addLayout(switch_row)

        card_layout.addStretch()
        backdrop_layout.addWidget(card)
        backdrop_layout.addStretch()
        wrapper_layout.addWidget(backdrop)

    def _apply_styles(self) -> None:
        # Remove inline palette/style; use global QSS instead
        self.setAutoFillBackground(False)

    def _emit_login(self) -> None:
        self.error_label.setVisible(False)
        self.loginRequested.emit(self.username_input.text(), self.password_input.text())

    def set_error(self, message: str) -> None:
        self.error_label.setText(message)
        self.error_label.setVisible(bool(message))

    def reset_fields(self) -> None:
        self.username_input.clear()
        self.password_input.clear()
        self.set_error("")
        self.username_input.setFocus()
