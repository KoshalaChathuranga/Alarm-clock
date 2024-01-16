import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class TimerApp(QWidget):
    def __init__(self):
        super(TimerApp, self).__init__()

        self.elapsed_time = QTime(0, 0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)

        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Timer')

        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 24px;")
        self.update_label()

        self.start_stop_button = QPushButton('Start', self)
        self.start_stop_button.clicked.connect(self.start_stop)

        self.reset_button = QPushButton('Reset', self)
        self.reset_button.clicked.connect(self.reset)

        layout = QVBoxLayout()
        layout.addWidget(self.time_label)
        layout.addWidget(self.start_stop_button)
        layout.addWidget(self.reset_button)

        self.setLayout(layout)

    def start_stop(self):
        if not self.timer.isActive():
            self.timer.start(1000)  # Update time every 1000 milliseconds (1 second)
            self.start_stop_button.setText('Stop')
        else:
            self.timer.stop()
            self.start_stop_button.setText('Start')

    def reset(self):
        self.timer.stop()
        self.elapsed_time = QTime(0, 0)
        self.update_label()
        self.start_stop_button.setText('Start')

    def update_time(self):
        self.elapsed_time = self.elapsed_time.addSecs(1)
        self.update_label()

    def update_label(self):
        self.time_label.setText(self.elapsed_time.toString("mm:ss"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer_app = TimerApp()
    timer_app.show()
    sys.exit(app.exec_())
