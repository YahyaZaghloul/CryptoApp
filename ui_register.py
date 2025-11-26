from PyQt5 import QtCore, QtGui, QtWidgets


class RegisterWidget(QtWidgets.QWidget):
    """Registration form with validation hints and navigation back to login."""

    registerRequested = QtCore.pyqtSignal(str, str, str)
    backToLogin = QtCore.pyqtSignal()

    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("AppRoot")
        self._build_ui()
        self._apply_styles()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)

        card = QtWidgets.QFrame(self)
        card.setObjectName("Card")
        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(50)
        shadow.setOffset(0, 20)
        shadow.setColor(QtGui.QColor(10, 14, 39, 200))
        card.setGraphicsEffect(shadow)
        card_layout = QtWidgets.QVBoxLayout(card)
        card_layout.setContentsMargins(32, 32, 32, 32)
        card_layout.setSpacing(18)

        title = QtWidgets.QLabel("Create Account", card)
        title.setObjectName("Title")
        title.setAlignment(QtCore.Qt.AlignHCenter)
        card_layout.addWidget(title)

        subtitle = QtWidgets.QLabel("Protect your credentials with layered encryption.", card)
        subtitle.setObjectName("Subtitle")
        subtitle.setAlignment(QtCore.Qt.AlignHCenter)
        subtitle.setWordWrap(True)
        card_layout.addWidget(subtitle)

        self.username_input = QtWidgets.QLineEdit(card)
        self.username_input.setPlaceholderText("Username (min 3 chars)")
        card_layout.addWidget(self.username_input)

        self.password_input = QtWidgets.QLineEdit(card)
        self.password_input.setPlaceholderText("Password (min 8 chars)")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        card_layout.addWidget(self.password_input)

        self.confirm_input = QtWidgets.QLineEdit(card)
        self.confirm_input.setPlaceholderText("Confirm password")
        self.confirm_input.setEchoMode(QtWidgets.QLineEdit.Password)
        card_layout.addWidget(self.confirm_input)

        self.error_label = QtWidgets.QLabel(card)
        self.error_label.setObjectName("ErrorLabel")
        self.error_label.setVisible(False)
        card_layout.addWidget(self.error_label)

        self.success_label = QtWidgets.QLabel(card)
        self.success_label.setObjectName("FeedbackLabel")
        self.success_label.setVisible(False)
        card_layout.addWidget(self.success_label)

        self.register_button = QtWidgets.QPushButton("Register", card)
        self.register_button.clicked.connect(self._emit_register)
        card_layout.addWidget(self.register_button)

        switch_row = QtWidgets.QHBoxLayout()
        switch_row.addStretch()
        login_btn = QtWidgets.QPushButton("Back to login", card)
        login_btn.setFlat(True)
        login_btn.setObjectName("LinkButton")
        login_btn.clicked.connect(self.backToLogin.emit)
        switch_row.addWidget(QtWidgets.QLabel("Already have an account?", card))
        switch_row.addWidget(login_btn)
        switch_row.addStretch()
        card_layout.addLayout(switch_row)

        layout.addStretch()
        layout.addWidget(card)
        layout.addStretch()

    def _apply_styles(self) -> None:
        self.setAutoFillBackground(False)

    def _emit_register(self) -> None:
        self.error_label.setVisible(False)
        self.registerRequested.emit(
            self.username_input.text(),
            self.password_input.text(),
            self.confirm_input.text(),
        )

    def set_error(self, message: str) -> None:
        self.error_label.setText(message)
        self.error_label.setVisible(bool(message))

    def show_success(self, message: str) -> None:
        self.success_label.setText(message)
        self.success_label.setVisible(True)

    def reset_styles(self) -> None:
        self.error_label.setVisible(False)
        self.success_label.setVisible(False)

    def reset_fields(self) -> None:
        self.username_input.clear()
        self.password_input.clear()
        self.confirm_input.clear()
        self.reset_styles()
        self.username_input.setFocus()
