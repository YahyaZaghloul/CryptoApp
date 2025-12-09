from PyQt5 import QtCore, QtGui, QtWidgets


class WelcomeWidget(QtWidgets.QWidget):
    """Landing page with navigation to Login or Register screens."""

    loginNavigate = QtCore.pyqtSignal()
    registerNavigate = QtCore.pyqtSignal()

    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("AppRoot")
        self._build_ui()
        self._apply_styles()

    def _build_ui(self) -> None:
        root = QtWidgets.QVBoxLayout(self)
        root.setContentsMargins(40, 40, 40, 40)
        root.setSpacing(0)

        spacer_top = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        root.addItem(spacer_top)

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

        title = QtWidgets.QLabel("Welcome to CryptoApp", card)
        title.setObjectName("Title")
        title.setAlignment(QtCore.Qt.AlignHCenter)
        card_layout.addWidget(title)

        subtitle = QtWidgets.QLabel("Secure authentication with layered encryption.", card)
        subtitle.setObjectName("Subtitle")
        subtitle.setAlignment(QtCore.Qt.AlignHCenter)
        subtitle.setWordWrap(True)
        card_layout.addWidget(subtitle)

        button_row = QtWidgets.QHBoxLayout()
        button_row.addStretch()

        self.login_btn = QtWidgets.QPushButton("Sign In", card)
        self.login_btn.clicked.connect(self.loginNavigate.emit)
        button_row.addWidget(self.login_btn)

        self.register_btn = QtWidgets.QPushButton("Create Account", card)
        self.register_btn.clicked.connect(self.registerNavigate.emit)
        button_row.addWidget(self.register_btn)

        button_row.addStretch()
        card_layout.addLayout(button_row)

        root.addWidget(card, 0, QtCore.Qt.AlignHCenter)

        spacer_bottom = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        root.addItem(spacer_bottom)

    def _apply_styles(self) -> None:
        # Use global QSS, avoid inline styling
        self.setAutoFillBackground(False)

