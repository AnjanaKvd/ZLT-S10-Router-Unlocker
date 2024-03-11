import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMessageBox, QProgressBar
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time

from request import RouterRequester

class RequestThread(QThread):
    emit_progress = pyqtSignal(int, str)
    finished = pyqtSignal()

    def run(self):
        try:
            router_requester = RouterRequester()
            router_requester.send_request_1()
            self.emit_progress.emit(40, "First request sent")
            time.sleep(1)

            router_requester.send_request_2()
            self.emit_progress.emit(70, "Second request sent")
            time.sleep(15)
        
            router_requester.send_request_2()
            self.emit_progress.emit(100, "Third request sent")
            time.sleep(2)
            self.finished.emit()
        except Exception as e:
            QMessageBox.critical(None, "Error", f"An error occurred: {str(e)}")
            self.finished.emit()

class RouterRequesterGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Unlock router")
        self.setGeometry(100, 100, 400, 350)
        self.setFixedSize(400, 350)

        self.label = QLabel("Click the button to unlock router:", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(50, 50, 300, 30)

        self.button = QPushButton("Click Me", self)
        self.button.setGeometry(100, 100, 200, 50)
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 18px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.button.clicked.connect(self.send_requests)

        self.progressbar = QProgressBar(self)
        self.progressbar.setGeometry(100, 160, 200, 20)
        self.progressbar.setVisible(False)

        self.progress_label = QLabel("", self)
        self.progress_label.setAlignment(Qt.AlignCenter)
        self.progress_label.setGeometry(50, 200, 300, 30)

    def send_requests(self):
        self.button.setEnabled(False)
        self.progressbar.setVisible(True)

        self.thread = RequestThread()
        self.thread.emit_progress.connect(self.update_progress)
        self.thread.finished.connect(self.requests_completed)
        self.thread.start()

    def update_progress(self, value, message):
        self.progressbar.setValue(value)
        self.progress_label.setText(message)

    def requests_completed(self):
        self.button.setEnabled(True)
        self.progressbar.setVisible(False)
        self.progress_label.setText("Unlocked !")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = RouterRequesterGUI()
    gui.show()
    sys.exit(app.exec_())
