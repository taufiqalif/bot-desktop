import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from bot import send_message


class BotWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Bot Desktop')
        self.layout = QVBoxLayout()
        self.label = QLabel()
        self.layout.addWidget(self.label)
        self.input_field = QLineEdit()
        self.layout.addWidget(self.input_field)
        self.send_button = QPushButton('Send')
        self.layout.addWidget(self.send_button)
        self.send_button.clicked.connect(self.send_message)
        self.setLayout(self.layout)

    def send_message(self):
        user_input = self.input_field.text()
        bot_response = get_bot_response(user_input)
        self.label.setText(bot_response)
        self.input_field.clear()


def get_bot_response(user_input):
    # Gunakan modul pemrosesan teks, seperti NLTK atau spaCy,
    # untuk memproses masukan pengguna dan menghasilkan respons bot
    # Di sini, kami hanya mengirim masukan pengguna ke fungsi send_message yang ada

    return send_message(user_input)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BotWindow()
    window.show()
    sys.exit(app.exec_())
