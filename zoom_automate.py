import time as t
from datetime import datetime, date
from pynput.keyboard import Controller, Key
from data import lst
import webbrowser


keyboard = Controller()
isStarted = False
rejoin_required = False
date = date.today().strftime("%d-%m-%Y")

def length_in_minutes(h1,m1,h2,m2):
    if(h1 == h2):
        return(m2-m1)
    elif(h2-h1 == 1):
        return((60-m1) + m2)
    else:
        return((60-m1) + 60 + m2) 

def close_opened_web_window():
    # Change opened tab from Zoom app to web browser
    keyboard.press(Key.alt_l)
    keyboard.press(Key.tab)
    keyboard.release(Key.alt_l)
    keyboard.release(Key.tab)

    # Close opened new web browser tab
    t.sleep(1)
    keyboard.press(Key.ctrl_l)
    keyboard.press('w')
    keyboard.release('w')
    keyboard.release(Key.ctrl_l)

    # Come back to Zoom app tab
    t.sleep(1)
    keyboard.press(Key.alt_l)
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.release(Key.alt_l)

def end_meeting():
    keyboard.press('x')
    t.sleep(2)
    keyboard.release('x')
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def start_meeting():
    webbrowser.open(class_link)
    t.sleep(18)
    close_opened_web_window()

for i in lst:
    if(date!=i[3]):
        continue
    
    class_link = i[0]
    start_time = list(map(int, i[1].split(':')))
    end_time = list(map(int, i[2].split(':')))

    class_duration = length_in_minutes(start_time[0],start_time[1],end_time[0],end_time[1])
    if(class_duration>=40):
            rejoin_required = True

    form = '%H:%M:%S'
    time_now = datetime.now()
    time_now = str(time_now)[11:19]
    time_now = datetime.strptime(time_now,form)
    time = datetime.strptime(i[1],form)
    if(time-time_now).total_seconds()<0:
        continue

    while True:
        hour_now = datetime.now().hour             # returns int
        minute_now = datetime.now().minute         # returns int

        if isStarted == False:
            if hour_now == start_time[0] and minute_now == start_time[1]:
                start_meeting()
                isStarted = True

        elif isStarted:
            if hour_now == end_time[0] and minute_now == end_time[1]:
                end_meeting()
                isStarted = False
                break

            if rejoin_required:
                form = '%H:%M:%S'
                time_now = datetime.now()
                time_now = str(time_now)[11:19]
                time_now = datetime.strptime(time_now,form)

                if (time_now - time).total_seconds() == 39.8*60:
                    end_meeting()
                    t.sleep(60*5)
                    start_meeting()
                    rejoin_required = False