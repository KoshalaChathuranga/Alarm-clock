# Alarm & Clock Application Readme

## Overview
This repository contains a simple Alarm and Clock application implemented in Python using the PyQt5 library. The application features a clock display, alarm functionality, stopwatch, and countdown timer.

## Features
- **Clock**: Displays the current time and date in a graphical user interface.
- **Alarm**: Allows users to set alarms and receive notifications.
- **Stopwatch**: Provides a stopwatch with start, stop, reset, and lap time features.
- **Timer**: Allows users to set countdown timers.

## Prerequisites
- Python 3.x
- PyQt5 library
- Sound file named 'alarm-buzzer.wav' for the alarm feature

## How to Run
1. Make sure you have Python installed on your machine.
2. Install the required dependencies using the following command:
   \`\`\`bash
   pip install PyQt5
   \`\`\`
3. Run the Alarm & Clock application by executing the following command in the terminal:
   \`\`\`bash
   python <main.py>
   \`\`\`

## File Structure
- **Alarm.ui**: UI file for the alarm screen.
- **Stopwatch.ui**: UI file for the stopwatch screen.
- **Timer.ui**: UI file for the timer screen.
- **Clock.ui**: UI file for the clock screen.
- **alarm-buzzer.wav**: Sound file for the alarm.
- **images/**: Folder containing images used in the application.

## Features Details

### Alarm
- Set alarms by specifying the hour, minute, and meridiem (AM/PM).
- Save alarms to 'Alarm_log.csv'.
- Load saved alarms from 'Alarm_log.csv'.
- Start an alarm, and the application will play the 'alarm-buzzer.wav' sound when the specified time is reached.

### Stopwatch
- Start, stop, and reset the stopwatch.
- Record lap times during active stopwatch time.

### Timer
- Set countdown timers by specifying minutes and seconds.
- Start, stop, and reset the timer.
- Receive notifications when the timer reaches zero.

### Clock
- Displays the current time and date.
- Updates every second.

## Credits
- This application was created by me.
