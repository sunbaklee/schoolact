import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTextEdit,
    QLineEdit, QPushButton, QLabel, QDialog, QFormLayout
)

# 설정 다이얼로그
class SettingsDialog(QDialog):
    def __init__(self, username, roomname):
        super().__init__()
        self.setWindowTitle("채팅 설정")

        self.username_input = QLineEdit(username)
        self.room_input = QLineEdit(roomname)

        layout = QFormLayout()
        layout.addRow("사용자 이름:", self.username_input)
        layout.addRow("채팅방 이름:", self.room_input)

        self.save_btn = QPushButton("저장")
        self.save_btn.clicked.connect(self.accept)
        layout.addWidget(self.save_btn)

        self.setLayout(layout)

    def get_values(self):
        return self.username_input.text(), self.room_input.text()


# 메인 채팅 창
class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.username = "User"
        self.roomname = "기본 채팅방"

        self.setWindowTitle("간단 채팅 프로그램")

        self.layout = QVBoxLayout()

        self.info_label = QLabel(self.get_info_text())
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)

        self.input_line = QLineEdit()
        self.send_btn = QPushButton("전송")
        self.settings_btn = QPushButton("설정")

        self.layout.addWidget(self.info_label)
        self.layout.addWidget(self.chat_display)
        self.layout.addWidget(self.input_line)
        self.layout.addWidget(self.send_btn)
        self.layout.addWidget(self.settings_btn)

        self.setLayout(self.layout)

        # 이벤트 연결
        self.send_btn.clicked.connect(self.send_message)
        self.input_line.returnPressed.connect(self.send_message)
        self.settings_btn.clicked.connect(self.open_settings)

    def get_info_text(self):
        return f"사용자: {self.username} | 채팅방: {self.roomname}"

    def send_message(self):
        text = self.input_line.text()
        if text:
            self.chat_display.append(f"{self.username}: {text}")
            self.input_line.clear()

    def open_settings(self):
        dialog = SettingsDialog(self.username, self.roomname)
        if dialog.exec():
            self.username, self.roomname = dialog.get_values()
            self.info_label.setText(self.get_info_text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.resize(400, 500)
    window.show()
    sys.exit(app.exec())
