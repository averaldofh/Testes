import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu
from cryptography.fernet import Fernet
from tkinter.filedialog import askopenfilename
import random

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "ui.ui")
key = ""

def encrypt(inp_path):  
    global key
    global enc
    fernet = Fernet(key)
    with open(inp_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(inp_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt(inp_path):
    global key
    global enc
    fernet = Fernet(key)
    with open(inp_path, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(inp_path, 'wb') as dec_file:
        dec_file.write(decrypted)

class UiApp:
    def __init__(self, master=None):
        # build ui
        self.MainApp = tk.Tk() if master is None else tk.Toplevel(master)
        self.lfr_inputfile = ttk.Labelframe(self.MainApp)
        self.ent_filepath = ttk.Entry(self.lfr_inputfile)
        self.ent_filepath.configure(state='readonly')
        _text_ = '''Choose file to (de)crypt...'''
        self.ent_filepath['state'] = 'normal'
        self.ent_filepath.delete('0', 'end')
        self.ent_filepath.insert('0', _text_)
        self.ent_filepath['state'] = 'readonly'
        self.ent_filepath.pack(expand='true', fill='x', ipady='2', side='left')
        self.but_inpath = ttk.Button(self.lfr_inputfile)
        self.but_inpath.configure(text='Open...')
        self.but_inpath.pack(side='right')
        self.but_inpath.configure(command=self.cmd_openfile)
        self.lfr_inputfile.configure(height='50', text='Input File:', width='200')
        self.lfr_inputfile.place(anchor='center', relwidth='1.0', relx='0.5', rely='0.22', x='0', y='0')
        self.lfr_kf = ttk.Labelframe(self.MainApp)
        self.ent_kf = ttk.Entry(self.lfr_kf)
        self.ent_kf.configure(state='readonly')
        _text_ = '''Choose KeyFile...'''
        self.ent_kf['state'] = 'normal'
        self.ent_kf.delete('0', 'end')
        self.ent_kf.insert('0', _text_)
        self.ent_kf['state'] = 'readonly'
        self.ent_kf.pack(expand='true', fill='x', ipady='2', side='left')
        self.button2 = ttk.Button(self.lfr_kf)
        self.button2.configure(text='Open...')
        self.button2.pack(side='right')
        self.button2.configure(command=self.cmd_openkf)
        self.lfr_kf.configure(height='50', text='Key File:', width='200')
        self.lfr_kf.place(anchor='center', relwidth='1.0', relx='0.5', rely='0.45', x='0', y='0')
        self.lfr_actions = ttk.Labelframe(self.MainApp)
        self.btn_dec = ttk.Button(self.lfr_actions)
        self.btn_dec.configure(state='disabled', text='Decrypt...')
        self.btn_dec.pack(expand='true', fill='x', side='right')
        self.btn_dec.configure(command=self.cmd_dec)
        self.btn_enc = ttk.Button(self.lfr_actions)
        self.btn_enc.configure(state='disabled', text='Encrypt')
        self.btn_enc.pack(expand='true', fill='x', side='left')
        self.btn_enc.configure(command=self.cmd_enc)
        self.btn_genKF = ttk.Button(self.lfr_actions)
        self.btn_genKF.configure(text='Gen Key')
        self.btn_genKF.pack(expand='true', fill='x', side='right')
        self.btn_genKF.configure(command=self.cmd_genKF)
        self.lfr_actions.configure(height='50', labelanchor='n', text='Actions:', width='200')
        self.lfr_actions.place(anchor='center', relwidth='1.0', relx='0.5', rely='0.68', x='0', y='0')
        self.lfr_general = ttk.Labelframe(self.MainApp)
        self.btn_close = ttk.Button(self.lfr_general)
        self.btn_close.configure(text='Exit')
        self.btn_close.pack(expand='true', fill='x', side='right')
        self.btn_close.configure(command=self.cmd_close)
        self.btn_openout = ttk.Button(self.lfr_general)
        self.btn_openout.configure(state='disabled', text='Open File')
        self.btn_openout.pack(expand='true', fill='x', side='left')
        self.btn_openout.configure(command=self.cmd_openout)
        self.lfr_general.configure(height='50', labelanchor='n', width='200')
        self.lfr_general.place(anchor='s', relwidth='1.0', relx='0.5', rely='1.0', x='0', y='0')
        self.lbl_title = ttk.Label(self.MainApp)
        self.lbl_title.configure(font='{calibri} 16 {bold}', justify='center', text='Fernet Encrypter/Decrypter')
        self.lbl_title.pack(side='top')
        self.MainApp.configure(height='200', width='200')
        self.MainApp.geometry('320x220')
        self.MainApp.resizable(False, False)
        self.MainApp.title('(De)Crypter')

        # Main widget
        self.mainwindow = self.MainApp
    
    def cmd_openfile(self):
        file = askopenfilename()
        self.ent_filepath['state'] = tk.NORMAL
        self.ent_filepath.delete('0','end')
        self.ent_filepath.insert('0',file)
        self.ent_filepath['state'] = 'readonly'
        self.btn_openout['state'] = tk.NORMAL

    def cmd_openkf(self):
        global key
        file = askopenfilename(filetypes=[("Key files", ".ey")])
        self.ent_kf['state'] = tk.NORMAL
        self.ent_kf.delete('0','end')
        self.ent_kf.insert('0',file)
        self.ent_kf['state'] = 'readonly'
        with open(file, 'rb') as filekey:
            key = filekey.read()
        fernet = Fernet(key)
        self.btn_dec['state'] = tk.NORMAL
        self.btn_enc['state'] = tk.NORMAL

    def cmd_dec(self):
        fpath = self.ent_filepath.get()
        decrypt(fpath)

    def cmd_enc(self):
        global enc
        fpath = self.ent_filepath.get()
        encrypt(fpath)

    def cmd_genKF(self):
        global key
        key = Fernet.generate_key()
        wd = os.getcwd()
        keyname = str(random.randint(0,500)) + '.ey'
        with open(str(keyname), 'wb') as filekey:
            filekey.write(key)
        self.ent_kf['state'] = tk.NORMAL
        self.ent_kf.delete('0','end')
        self.ent_kf.insert('0',wd+'\\'+keyname)
        self.ent_kf['state'] = 'readonly'
        file = self.ent_kf.get()
        with open(file, 'rb') as filekey:
            key = filekey.read()
            fernet = Fernet(key)
            self.btn_dec['state'] = tk.NORMAL
            self.btn_enc['state'] = tk.NORMAL

    def cmd_close(self):
        self.MainApp.quit()

    def cmd_openout(self):
        fpath = self.ent_filepath.get()
        os.system(fpath)

    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    app = UiApp()
    app.run()

