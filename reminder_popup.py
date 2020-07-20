from tkinter import *
from tkinter import font
from datetime import datetime
import errno
import os
import time
import json
import configparser
from selenium_temperature import input_temperature

# path to config file
configpath = './config.ini'
config = configparser.ConfigParser()


if not os.path.isfile(configpath):
    raise FileNotFoundError(
        errno.ENOENT, os.strerror(errno.ENOENT), configpath)

else:
    config.read(configpath)

    # get params
    cred_url = config['CREDENTIALS']['url']
    cred_email = config['CREDENTIALS']['email']
    cred_password = config['CREDENTIALS']['password']

    first_am = config['REMINDER']['first_am']
    first_pm = config['REMINDER']['first_pm']
    # deadline_am = config['REMINDER']['deadline_am']
    # deadline_pm = config['REMINDER']['deadline_pm']
    # mode = int(config['REMINDER']['mode'])


    # path to reminders.txt file
    REM_FILE = "./reminders.txt"

    # list of reminders
    reminders = []

    # update reminder list
    reminders.append(("Please record AM temperature", int(first_am.split(":")[0]), int(first_am.split(":")[1]), 0))
    reminders.append(("Please record PM temperature", int(first_pm.split(":")[0]), int(first_pm.split(":")[1]), 0))

    # update list of reminders
    with open(REM_FILE, 'w+') as f:
        # reminders = json.loads(f.read())
        f.seek(0)
        # reminders.append((reminder, hrs, mins))
        f.write(json.dumps(reminders))
        f.truncate()


    class REMINDER():
        def __init__(self, reminder):
            # reminder info tuple
            self.reminder = reminder

            # root (top level element) config
            self.root = Tk()
            self.root.title("Reminder!")
            self.root["bg"] = "SteelBlue2"
            self.position_window()

            # main frame (inside root) config
            self.mainFrame = Frame(self.root, padx=10, pady=10, bg="SteelBlue2")
            self.mainFrame.pack(side="bottom", fill=BOTH, expand=1)

            # reminder label (inside main frame) config
            text = Label(self.mainFrame, text=self.reminder[0], bg="SteelBlue1",
                        font=font.Font(family="Times", size=12),
                        padx=20, pady=10, wraplength=300)
            text.pack(fill=BOTH, expand=1)

            text = Label(self.mainFrame, text='Temperature between 35 and 40 degrees', bg="SteelBlue1",
            font=font.Font(family="Times", size=12),
            padx=20, pady=10, wraplength=300)
            text.pack(fill=BOTH, expand=1)

            # first field frame (inside main frame) config
            self.fieldRow1 = Frame(self.mainFrame, padx=5, pady=5)
            Label(self.fieldRow1, text="Temperature:").grid(row=0, column=0)

            vcmd = (self.root.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
            self.rem = Entry(self.fieldRow1, validate='key', validatecommand= vcmd)
            self.rem.grid(row=0, column=1)
            self.rem.focus()
            self.fieldRow1.pack()

            # button frame (inside main frame) config
            self.buttonRow = Frame(self.mainFrame, padx=10,
                                pady=10, bg="SteelBlue2")
            # self.btn1 = Button(self.buttonRow, text="Dismiss",
            #                 command=self.dismissReminder, bg="SteelBlue3").grid(row=0, column=0)
            # self.btn2 = Button(self.buttonRow, text="Postpone",
            #                 command=self.postponeReminder, bg="SteelBlue3").grid(row=0, column=0)
            self.btn3 = Button(self.buttonRow, text="Record Now",
                            command=self.recordTemperature, bg="SteelBlue3").grid(row=0, column=0)
            self.buttonRow.grid_columnconfigure(1, minsize=10)
            self.buttonRow.pack()

            # call mainloop of Tk object
            self.root.mainloop()

        def validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
            if value_if_allowed:
                try:
                    float(value_if_allowed)
                    return True
                except ValueError:
                    return False
            elif value_if_allowed == '':
                return True
            else:
                return False

        def position_window(self):
            '''
            utiltiy function to position window
            at top right corner
            '''
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            x = screen_width /2
            y = screen_height/100
            self.root.geometry('+%d+%d' % (x, y))

        # def dismissReminder(self):
        #     '''
        #     utitlity function to remove reminder from list
        #     '''
        #     self.root.destroy()
        #     reminders.remove(self.reminder)
        #     with open(REM_FILE, 'w') as f:
        #         f.write(json.dumps(reminders))

        # def postponeReminder(self):
        #     '''
        #     utility function to postpone reminder by 5 minutes
        #     '''
        #     self.root.destroy()
        #     reminders.remove(self.reminder)
        #     self.reminder[2] += 5
        #     self.reminder[1] += self.reminder[2]/60
        #     self.reminder[2] %= 60
        #     reminders.append(self.reminder)
        #     with open(REM_FILE, 'w') as f:
        #         f.write(json.dumps(reminders))

        def recordTemperature(self):
            '''
            launch website and automatically record the temperature
            '''
            t = float(self.rem.get().strip())
            self.root.destroy()
            # self.root.iconify()
            input_temperature(cred_url, cred_email, cred_password, t)

            # time.sleep(60)

    def controller():
        '''
        Main function to update reminders list
        and show reminders.
        '''
        while(True):

            with open(REM_FILE, 'r') as f:
                updated_reminders = json.loads(f.read())
                for reminder in updated_reminders:
                    if reminder not in reminders:
                        reminders.append(reminder)

            # current hour and minute
            cur_hrs = datetime.now().hour
            cur_mins = datetime.now().minute

            # find reminders to show
            for reminder in reminders:
                # rem = reminder[1].split(":")
                rem_hrs = int(reminder[1])
                rem_mins = int(reminder[2])
                status = int(reminder[3])

                # # reset status if 00:00
                # if (cur_hrs == 0 and cur_mins == 0):
                #     reminder = (reminder[1], reminder[2], 0)

                if status == 0 and cur_hrs == rem_hrs and cur_mins == rem_mins:
                    # show reminder window
                    REMINDER(reminder)

            # delay
            time.sleep(6)


if __name__ == "__main__":
    controller()
