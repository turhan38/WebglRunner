import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import webglMain


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("600x183+660+210")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(0,  0)
        top.title("Webgl Runner")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.05, rely=0.219, height=41, width=84)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Project Path :''')

        self.pathLabel = tk.Label(self.top)
        self.pathLabel.place(relx=0.2, rely=0.273, height=21, width=344)
        self.pathLabel.configure(anchor='w')
        self.pathLabel.configure(background="#d9d9d9")
        self.pathLabel.configure(compound='left')
        self.pathLabel.configure(disabledforeground="#a3a3a3")
        self.pathLabel.configure(foreground="#000000")

        self.pathButton = tk.Button(self.top)
        self.pathButton.place(relx=0.85, rely=0.273, height=24, width=42)
        self.pathButton.configure(activebackground="#ececec")
        self.pathButton.configure(activeforeground="#000000")
        self.pathButton.configure(background="#d9d9d9")
        self.pathButton.configure(compound='left')
        self.pathButton.configure(disabledforeground="#a3a3a3")
        self.pathButton.configure(foreground="#000000")
        self.pathButton.configure(highlightbackground="#d9d9d9")
        self.pathButton.configure(highlightcolor="black")
        self.pathButton.configure(pady="0")
        self.pathButton.configure(text='''Select''')
        self.pathButton.configure(command=webglMain.getProjectPath)

        self.RunButton = tk.Button(self.top)
        self.RunButton.place(relx=0.383, rely=0.546, height=54, width=137)
        self.RunButton.configure(activebackground="#ececec")
        self.RunButton.configure(activeforeground="#000000")
        self.RunButton.configure(background="#d9d9d9")
        self.RunButton.configure(compound='left')
        self.RunButton.configure(disabledforeground="#a3a3a3")
        self.RunButton.configure(foreground="#000000")
        self.RunButton.configure(highlightbackground="#d9d9d9")
        self.RunButton.configure(highlightcolor="black")
        self.RunButton.configure(pady="0")
        self.RunButton.configure(text='''Run''')
        self.RunButton.configure(command=webglMain.RunWebgl)

def start_up():
    webglMain.main()


if __name__ == '__main__':
    webglMain.main()
