import tkinter as tk
from functools import partial
from osrsbotbot import Bot

INSERT = '1'
MSG_RUNNING = 'running'
MSG_STOPPED = 'stopped'

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        print('initializing App')

        self.bot = Bot()

        self.create_widgets()

    def number_validation(self, text, action_code):
        if action_code == INSERT:
            if not text.isdigit():
                return False
        return True

    def number_validation_error(self, text):
        print(f'{text} must be a number')

    def create_info_window(self):
        self.info_window = tk.Toplevel(self)
        self.info_text = tk.Text(self.info_window)
        self.info_text.grid(row=0)
        self.info_text.insert(
            '0.0',
            'Welcome to autochat.\n\n'
            'Define a lower wait time, upper wait time and a command to send, and then press start.\n'
            'The program will wait for 5 seconds before sending the first command; make sure to put your cursor where you want your text sent.\n'
            'After each command is sent, the program sleeps for a random duration between the lower and upper limits, and then sends the command again.\n\n'
            'Press stop or quit to stop the program from sending commands.\n\n'
            'https://github.com/ksarge/autochat'
        )
        self.info_text.config(state=tk.DISABLED)

    def start(self, cmd, lower_limit, upper_limit):
        self.bot.start(cmd, int(lower_limit), int(upper_limit))
        self.status_string.set(MSG_RUNNING)
        self.status_label.config(fg='green')

    def stop(self):
        self.bot.stop()
        self.status_string.set(MSG_STOPPED)
        self.status_label.config(fg='red')

    def quit(self):
        self.stop()
        super().quit()

    def create_widgets(self):
        tk.Label(self, text='Lower wait time').grid(row=0)
        tk.Label(self, text='Upper wait time').grid(row=1)
        tk.Label(self, text='Command').grid(row=2)

        tk.Label(self, text='Status:').grid(row=3, column=0)

        self.status_string = tk.StringVar()
        self.status_string.set(MSG_STOPPED)

        self.status_label = tk.Label(self, textvariable=self.status_string)
        self.status_label.grid(row=3, column=1, sticky=tk.W)

        nvc = (self.register(self.number_validation), '%P', '%d')
        nvec = (self.register(self.number_validation_error), '%P')

        self.lower_entry = tk.Entry(self, validate='key', validatecommand=nvc, invalidcommand=nvec, textvariable=tk.StringVar(value='35'))
        self.upper_entry = tk.Entry(self, validate='key', validatecommand=nvc, invalidcommand=nvec, textvariable=tk.StringVar(value='36'))
        self.cmd_entry = tk.Entry(self)

        self.lower_entry.grid(row=0, column=1)
        self.upper_entry.grid(row=1, column=1)
        self.cmd_entry.grid(row=2, column=1)

        self.start_button = tk.Button(self, text='Start', command=lambda: self.start(self.cmd_entry.get(), self.lower_entry.get(), self.upper_entry.get()))
        self.start_button.grid(row=4, column=0, sticky=tk.W, pady=4)

        self.stop_button = tk.Button(self, text='Stop', command=self.stop)
        self.stop_button.grid(row=4, column=1, sticky=tk.W, pady=4)

        self.info_button = tk.Button(self, text='Info', command=self.create_info_window)
        self.info_button.grid(row=5, column=0, stick=tk.W, pady=4)

        self.quit_button = tk.Button(self, text='Quit', command=self.quit)
        self.quit_button.grid(row=5, column=1, sticky=tk.W, pady=4)


def main():
    app = Application()
    app.mainloop()


if __name__ == '__main__':
    main()
