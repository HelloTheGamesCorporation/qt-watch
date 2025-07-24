from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit)

from PyQt6.QtCore import Qt, QTimer
import time
import sys

class Watch(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Watch")
        self.setFixedSize(425, 125)

        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.printWatch)
        self.timer.start(1000)

        self._createDisplay()

        self.printWatch()

    def _createDisplay(self):
        self.display = QTextEdit()
        self.display.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 24px;")
        self.display.setFixedHeight(100)
        self.generalLayout.addWidget(self.display)

    def printWatch(self):
        self.time = time.ctime(time.time())
        self.time = self.time.split()
        self.ftime = self.time[3]
        del self.time[3]
        self.date = " ".join(self.time)
        self.text = f"Текущая дата: {self.date}\n\nТекущее время: {self.ftime}"
        self.display.setText(self.text)
        

def main():
    app = QApplication(sys.argv)
    watch = Watch()
    watch.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
