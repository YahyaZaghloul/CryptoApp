from PyQt5 import QtCore, QtGui, QtWidgets


class HomeWidget(QtWidgets.QWidget):
    """Home screen summarizing the current session and listing registered users."""

    logoutRequested = QtCore.pyqtSignal()
    refreshRequested = QtCore.pyqtSignal()
    encryptRequested = QtCore.pyqtSignal(str)

    def __init__(self, parent: QtWidgets.QWidget | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("AppRoot")
        self._build_ui()
        self._apply_styles()

    def _build_ui(self) -> None:
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)

        header = QtWidgets.QHBoxLayout()

        self.welcome_label = QtWidgets.QLabel("Welcome", self)
        self.welcome_label.setObjectName("Title")
        header.addWidget(self.welcome_label)
        header.addStretch()

        self.refresh_button = QtWidgets.QPushButton("Refresh", self)
        self.refresh_button.clicked.connect(self.refreshRequested.emit)
        header.addWidget(self.refresh_button)

        self.logout_button = QtWidgets.QPushButton("Logout", self)
        self.logout_button.clicked.connect(self.logoutRequested.emit)
        header.addWidget(self.logout_button)
        layout.addLayout(header)

        self.encryption_card = QtWidgets.QFrame(self)
        self.encryption_card.setObjectName("Card")
        encrypt_layout = QtWidgets.QVBoxLayout(self.encryption_card)
        encrypt_layout.setSpacing(12)

        encrypt_title = QtWidgets.QLabel("Encrypt a new value", self.encryption_card)
        encrypt_title.setObjectName("Section")
        encrypt_layout.addWidget(encrypt_title)

        self.encrypt_input = QtWidgets.QLineEdit(self.encryption_card)
        self.encrypt_input.setPlaceholderText("Enter value to encrypt")
        self.encrypt_input.returnPressed.connect(self._emit_encrypt)
        encrypt_layout.addWidget(self.encrypt_input)

        encrypt_actions = QtWidgets.QHBoxLayout()
        encrypt_actions.addStretch()
        self.encrypt_button = QtWidgets.QPushButton("Encrypt", self.encryption_card)
        self.encrypt_button.clicked.connect(self._emit_encrypt)
        encrypt_actions.addWidget(self.encrypt_button)
        encrypt_layout.addLayout(encrypt_actions)

        self.encrypt_result = QtWidgets.QPlainTextEdit(self.encryption_card)
        self.encrypt_result.setReadOnly(True)
        self.encrypt_result.setPlaceholderText("Encrypted output will appear here")
        encrypt_layout.addWidget(self.encrypt_result)
        layout.addWidget(self.encryption_card)

        # Info message about where to see hashes
        self.info_label = QtWidgets.QLabel("return to excel sheet to see hashes", self)
        self.info_label.setObjectName("Subtitle")
        self.info_label.setWordWrap(True)
        layout.addWidget(self.info_label)

        self.stats_label = QtWidgets.QLabel("", self)
        self.stats_label.setObjectName("Stats")
        layout.addWidget(self.stats_label)

        self.table = QtWidgets.QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Username", "Password", "Status"])
        self.table.horizontalHeader().setStretchLastSection(False)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

        layout.addWidget(self.table)

        self.feedback_label = QtWidgets.QLabel("", self)
        self.feedback_label.setObjectName("FeedbackLabel")
        self.feedback_label.setVisible(False)
        layout.addWidget(self.feedback_label)

    def _apply_styles(self) -> None:
        self.setAutoFillBackground(False)

    def populate(self, username: str, users: list[tuple[str, str, str]]) -> None:
        self.welcome_label.setText(f"Welcome, {username}")
        self.stats_label.setText(f"Total registered users: {len(users)}")
        self.table.setRowCount(len(users))
        for row, (user_name, password, status) in enumerate(users):
            user_item = QtWidgets.QTableWidgetItem(user_name)
            # Prepare password display (truncate if very long)
            display_password = password if len(password) <= 180 else password[:180] + '…'
            pw_item = QtWidgets.QTableWidgetItem(display_password)
            if display_password.endswith('…'):
                pw_item.setToolTip(password)
            status_item = QtWidgets.QTableWidgetItem(status)
            self.table.setItem(row, 0, user_item)
            self.table.setItem(row, 1, pw_item)
            self.table.setItem(row, 2, status_item)
        self.table.resizeRowsToContents()
        # Adjust columns after data load: Username/Status to contents, Password stretches
        self.table.resizeColumnToContents(0)
        self.table.resizeColumnToContents(2)
        self.encrypt_result.clear()

    def show_feedback(self, message: str) -> None:
        self.feedback_label.setText(message)
        self.feedback_label.setVisible(bool(message))

    def clear_feedback(self) -> None:
        self.feedback_label.clear()
        self.feedback_label.setVisible(False)

    def show_encrypted_value(self, message: str) -> None:
        self.encrypt_result.setPlainText(message)

    def clear_encrypt_feedback(self) -> None:
        self.encrypt_input.clear()
        self.encrypt_result.clear()

    def _emit_encrypt(self) -> None:
        self.encryptRequested.emit(self.encrypt_input.text())
