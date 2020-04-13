import tkinter as tk
from functools import partial
from osrsbotbot import Bot

INSERT = '1'


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

    def create_widgets(self):
        tk.Label(self, text="Lower wait time").grid(row=0)
        tk.Label(self, text="Upper wait time").grid(row=1)
        tk.Label(self, text="Command").grid(row=2)

        nvc = (self.register(self.number_validation), '%P', '%d')
        pec = (self.register(self.number_validation_error), '%P')

        self.lower_entry = tk.Entry(self, validate='key', validatecommand=nvc, invalidcommand=pec)
        self.upper_entry = tk.Entry(self, validate='key', validatecommand=nvc, invalidcommand=pec)
        self.cmd_entry = tk.Entry(self)

        self.lower_entry.grid(row=0, column=1)
        self.upper_entry.grid(row=1, column=1)
        self.cmd_entry.grid(row=2, column=1)

        self.start_button = tk.Button(self, text='Start', command=lambda: self.bot.start(self.cmd_entry.get(), int(self.lower_entry.get()), int(self.upper_entry.get())))
        self.start_button.grid(row=3, column=0, sticky=tk.W, pady=4)

        self.stop_button = tk.Button(self, text='Stop', command=self.bot.stop)
        self.stop_button.grid(row=3, column=1, sticky=tk.W, pady=4)

        self.info_button = tk.Button(self, text='Info')
        self.info_button.grid(row=4, column=0, stick=tk.W, pady=4)

        self.quit_button = tk.Button(self, text='Quit', command=self.quit)
        self.quit_button.grid(row=4, column=1, sticky=tk.W, pady=4)


if __name__ == '__main__':
    app = Application()
    app.mainloop()
