import sys
import csv
import winsound
import threading
import time
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QSpinBox, QListWidget


waiting = False

def play_sound(sound_path):
    global waiting
    waiting = True
    winsound.PlaySound(sound_path, winsound.SND_FILENAME)
    waiting = False

def buzzerOn():
    global waiting
    sound_path = 'alarm-buzzer.wav'

    sound_thread = threading.Thread(target=play_sound, args=(sound_path,))
    sound_thread.start()

    print("Sound has finished playing.")
        
        
def goto_home():
    home_page = Home()
    widget.addWidget(home_page)
    widget.setCurrentIndex(widget.currentIndex() + 1)
    

def goto_Alarm():
    Alarm_page = Alarm()
    widget.addWidget(Alarm_page)
    widget.setCurrentIndex(widget.currentIndex() + 1)


def goto_Stopwatch():
    Stopwatch_page = Stopwatch()
    widget.addWidget(Stopwatch_page)
    widget.setCurrentIndex(widget.currentIndex() + 1)
    
    
def goto_Timer():
    Timer_page = Timer()
    widget.addWidget(Timer_page)
    widget.setCurrentIndex(widget.currentIndex() + 1)


class Alarm(QWidget):
    def __init__(self):
        super(Alarm, self).__init__()
        loadUi("Alarm.ui", self)   
        
        self.buzzer_time_str = '' 
           
        self.back_B.clicked.connect(goto_home)
        self.save_B.clicked.connect(self.save_alarm)
        self.start_B.clicked.connect(self.start_alarm)
        
        
        self.listWidget.itemClicked.connect(self.update_alarm)
        
    def save_alarm(self):
        current_Hr = self.Hr_Box.value()
        current_Min = self.Min_Box.value()
        selected_Meridiem = self.comboBox.currentText()

        alarm_to_save = f"{current_Hr:02d}:{current_Min:02d} {selected_Meridiem}"
        self.listWidget.addItem(alarm_to_save)
        
        with open('Alarm_log.csv', 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([alarm_to_save])
            print("Alarm saved:", alarm_to_save)
        
    def load_alarms(self):
        try:
            with open('Alarm_log.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader: 
                    if row:
                        print(row)
                        alarm = row[0]
                        self.listWidget.addItem(alarm)
        except Exception as e:
            print("Error loading alarms:", str(e))
                
    def update_alarm(self, item):
        self.buzzer_time_str = item.text()
        print(f'buzzer_time_str: {self.buzzer_time_str}')
        self.alm_lbl.setText(item.text())
    
    def start_alarm(self):
        current_time_str = QTime.currentTime().toString('hh:mm AP')
        print(f'current_time_str: {current_time_str}')
        print(f'buzzer_time_str: {self.buzzer_time_str}')

        while not waiting:
            if self.buzzer_time_str:
                alarm_time = QTime.fromString(self.buzzer_time_str, 'hh:mm AP')
                if alarm_time == QTime.currentTime():
                    buzzerOn()
        
class Stopwatch(QWidget):
    def __init__(self):
        super(Stopwatch, self).__init__()
        loadUi("Stopwatch.ui", self)
        
        self.elapsed_time = QTime(0, 0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        
        self.lap_times = []
        
        self.back_B.clicked.connect(goto_home)
        self.start_B.clicked.connect(self.start_stop)
        self.reset_B.clicked.connect(self.reset)  # Connect to the reset method
        self.lap_B.clicked.connect(self.lap)
    
    def start_stop(self):
        if not self.timer.isActive():
            self.timer.start(100)  # Update time every 100 milliseconds
            self.start_B.setText('Stop')
        else:
            self.timer.stop()
            self.start_B.setText('Start')

    def reset(self):
        self.timer.stop()
        self.elapsed_time = QTime(0, 0)
        self.update_label()
        self.start_B.setText('Start')
    
    def lap(self):
        if self.timer.isActive():
            lap_time_str = self.elapsed_time.toString("hh:mm:ss.zzz")       
            self.listWidget.addItem(lap_time_str)

    def update_time(self):
        self.elapsed_time = self.elapsed_time.addMSecs(100)
        self.update_label()

    def update_label(self):
        self.SW_label.setText(self.elapsed_time.toString("hh:mm:ss.zzz"))


class Timer(QWidget):
    def __init__(self):
        super(Timer, self).__init__()
        loadUi("Timer.ui", self)
        self.back_B.clicked.connect(goto_home)
        self.start_B.clicked.connect(self.start_stop)
        self.reset_B.clicked.connect(self.reset)

        self.remaining_time = QTime(0, 0, 0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)

    def start_stop(self):
        if not self.timer.isActive():
            minutes = self.Min_Box.value()
            seconds = self.Sec_Box.value()
            self.remaining_time = QTime(0, minutes, seconds)
            
            self.timer.start(1000)  # Update time every 1000 milliseconds (1 second)
            self.start_B.setText('Stop')
        else:
            self.timer.stop()
            self.start_B.setText('Start')

    def reset(self):
        print('reset timer pressed')
        self.timer.stop()
        self.remaining_time = QTime(0, 0, 0)
        self.update_label()
        self.start_B.setText('Start')

    def update_time(self):
        if self.remaining_time == QTime(0, 0, 0):
            self.timer.stop()
            self.start_B.setText('Start')
            buzzerOn() 
        else:
            self.remaining_time = self.remaining_time.addSecs(-1)
            self.update_label()

    def update_label(self):
        print(self.remaining_time)
        self.time_label.setText(self.remaining_time.toString("mm:ss"))
    
        
class Home(QWidget):
    def __init__(self):
        super(Home, self).__init__()
        loadUi("Clock.ui", self)
        
        self.setWindowIcon(QIcon('icon.png'))
        self.setWindowTitle('Alarm & clock')
        
        timer = QTimer(self)
        timer.timeout.connect(self.showDateTime)
        timer.start(1000)

        self.showDateTime()
                
        self.B_Am.clicked.connect(goto_Alarm)
        self.B_Sw.clicked.connect(goto_Stopwatch)
        self.B_Tm.clicked.connect(goto_Timer)
        
    def showDateTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()

        time_display = current_time.toString('hh:mm:ss AP')  
        date_display = current_date.toString('MMMM dd, yyyy')  

        self.time_label.setText(time_display)
        self.date_label.setText(date_display)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_code = Home()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(app_code)

    alarm_page = Alarm()
    alarm_page.load_alarms()
    
    widget.show()

    try:
        sys.exit(app.exec_())
    except Exception as e:
        print("Exiting:", str(e))