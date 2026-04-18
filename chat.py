import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QHBoxLayout, QTextEdit, QLineEdit, QPushButton, 
                               QDialog, QFormLayout, QDialogButtonBox)

# --- 1. 설정 창 (Dialog) 클래스 ---
class SettingsDialog(QDialog):
    def __init__(self, current_username, parent=None):
        super().__init__(parent)
        self.setWindowTitle("채팅방 설정")
        self.setMinimumWidth(250)
        
        # 레이아웃 설정
        self.layout = QVBoxLayout(self)
        self.form_layout = QFormLayout()
        
        # 닉네임 입력 필드
        self.name_input = QLineEdit(self)
        self.name_input.setText(current_username)
        self.form_layout.addRow("사용자 닉네임:", self.name_input)
        self.layout.addLayout(self.form_layout)
        
        # 확인/취소 버튼
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.button_box.accepted.connect(self.accept) # '확인' 누르면 창 닫히며 성공 신호
        self.button_box.rejected.connect(self.reject) # '취소' 누르면 창 닫히며 취소 신호
        self.layout.addWidget(self.button_box)

    def get_new_username(self):
        """변경된 닉네임을 반환하는 메서드"""
        return self.name_input.text().strip()


# --- 2. 메인 채팅 창 클래스 ---
class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6 나만의 채팅")
        self.resize(400, 500)
        
        # 초기 설정값
        self.username = "익명"
        
        # 메인 위젯 설정 (QMainWindow는 중앙 위젯이 필수입니다)
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        
        # [상단 영역] 설정 버튼
        top_layout = QHBoxLayout()
        self.settings_btn = QPushButton("⚙️ 설정")
        self.settings_btn.clicked.connect(self.open_settings)
        top_layout.addStretch() # 버튼을 오른쪽으로 밀어냅니다.
        top_layout.addWidget(self.settings_btn)
        main_layout.addLayout(top_layout)
        
        # [중간 영역] 채팅 내역 창 (읽기 전용)
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        main_layout.addWidget(self.chat_display)
        
        # [하단 영역] 메시지 입력 창 & 전송 버튼
        bottom_layout = QHBoxLayout()
        self.msg_input = QLineEdit()
        self.msg_input.setPlaceholderText("메시지를 입력하세요...")
        self.msg_input.returnPressed.connect(self.send_message) # 엔터키 지원
        
        self.send_btn = QPushButton("전송")
        self.send_btn.clicked.connect(self.send_message)
        
        bottom_layout.addWidget(self.msg_input)
        bottom_layout.addWidget(self.send_btn)
        main_layout.addLayout(bottom_layout)
        
        # 시작 안내 메시지
        self.chat_display.append("<b>[시스템] 채팅방에 입장하셨습니다. (기본 이름: 익명)</b><br>")

    # --- 기능 구현 메서드 ---
    def send_message(self):
        text = self.msg_input.text().strip()
        if text: # 내용이 있을 때만 전송
            # HTML 태그를 사용해 닉네임을 굵게 표시합니다.
            self.chat_display.append(f"<b>{self.username}</b>: {text}")
            self.msg_input.clear() # 입력창 비우기

    def open_settings(self):
        # 설정 다이얼로그 객체 생성
        dialog = SettingsDialog(self.username, self)
        
        # dialog.exec()는 창이 닫힐 때까지 코드를 멈추고 대기합니다. (모달 창)
        if dialog.exec(): 
            new_name = dialog.get_new_username()
            if new_name and new_name != self.username:
                self.chat_display.append(f"<i>[시스템] 닉네임이 '{new_name}'(으)로 변경되었습니다.</i><br>")
                self.username = new_name

# --- 3. 프로그램 실행 ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec())
