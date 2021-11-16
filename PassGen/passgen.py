import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
import random
import math
import xerox as x

alpha = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"
password = []
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "ui.ui")

def generate_pass(length, array, is_alpha=False):
    for i in range(length):
        index = random.randint(0, len(array) - 1)
        character = array[index]
        if is_alpha:
            case = random.randint(0, 1)
            if case == 1:
                character = character.upper()
        password.append(character)

class UiApp:
    def __init__(self, master=None):
        # build ui
        self.MainApp = tk.Tk() if master is None else tk.Toplevel(master)
        self.fr_main = ttk.Frame(self.MainApp)
        self.title = ttk.Label(self.fr_main)
        self.title.configure(font='{Candara} 20 {bold}', text='''RANDOM PASSWORD
         GENERATOR''')
        self.title.pack(expand='true', fill='both', side='top')
        self.fr_main.configure(height='200', width='200')
        self.fr_main.pack(side='top')
        self.frame4 = ttk.Frame(self.MainApp)
        self.label3 = ttk.Label(self.frame4)
        self.label3.configure(font='{Calibri} 12 {}', text='Enter password length:')
        self.label3.pack(anchor='center', side='top')
        self.len_entry = ttk.Entry(self.frame4)
        self.pass_len = tk.StringVar(value='12')
        self.len_entry.configure(font='{calibri} 12 {}', textvariable=self.pass_len)
        _text_ = '''12'''
        self.len_entry.delete('0', 'end')
        self.len_entry.insert('0', _text_)
        self.len_entry.pack(anchor='center', side='top')
        self.frame4.configure(height='200', width='200')
        self.frame4.place(anchor='center', relheight='0.25', relwidth='1.0', relx='0.5', rely='0.47', x='0', y='0')
        self.frame5 = ttk.Frame(self.MainApp)
        self.cpy_but = ttk.Button(self.frame5)
        self.cpy_but.configure(default='normal', state='disabled', text='Copy to Clipboard')
        self.cpy_but.pack(anchor='n', expand='true', fill='x', side='right')
        self.cpy_but.configure(command=self.cmd_copy)
        self.gen_but = ttk.Button(self.frame5)
        self.gen_but.configure(text='Generate')
        self.gen_but.pack(side='top')
        self.gen_but.configure(command=self.cmd_genpass)
        self.frame5.configure(height='200', width='200')
        self.frame5.place(anchor='center', relheight='0.20', relwidth='1.0', relx='0.5', rely='0.7', x='0', y='0')
        self.frame6 = ttk.Frame(self.MainApp)
        self.exit_but = ttk.Button(self.frame6)
        self.exit_but.configure(text='Exit')
        self.exit_but.pack(anchor='s', expand='true', fill='x', side='bottom')
        self.exit_but.configure(command=self.cmd_exit)
        self.password_out = ttk.Entry(self.frame6)
        self.password_out.configure(state='readonly')
        self.password_out.pack(anchor='n', expand='true', fill='both', side='top')
        self.frame6.configure(height='200', width='200')
        self.frame6.place(anchor='center', relheight='0.25', relwidth='1.0', relx='0.5', rely='0.88', x='0', y='0')
        self.MainApp.geometry('255x200')
        self.MainApp.resizable(False, False)
        self.MainApp.title('Random Password Generator')

        # Main widget
        self.mainwindow = self.MainApp
    
    def cmd_copy(self):
        passcp = self.password_out.get()
        x.copy(passcp)
        pass

    def cmd_genpass(self):
        global password
        global pass_len 
        pass_len = self.len_entry.get()
        if int(pass_len) > 30:
            pass_len = 30
            self.len_entry.delete('0','end')
            self.len_entry.insert('0',str(pass_len))
        self.cpy_but['state'] = tk.NORMAL
        pass_len = int(pass_len)
        alpha_len = pass_len//2
        num_len = math.ceil(pass_len*30/100)
        special_len = pass_len-(alpha_len+num_len)
        generate_pass(alpha_len, alpha, True)
        generate_pass(num_len, num)
        generate_pass(special_len, special)
        random.shuffle(password)
        gen_password = ""
        for i in password:
            gen_password = gen_password + str(i)
        password = []
        self.password_out['state'] = tk.NORMAL
        self.password_out.delete('0','end')
        self.password_out.insert('0',gen_password)
        pass

    def cmd_exit(self):
        self.MainApp.quit()
        pass

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    app = UiApp()
    app.run()

