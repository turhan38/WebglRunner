import os
from pathlib import Path
import tkinter as tk
from tkinter import filedialog
import webglGui as webgl
from threading import Thread

projectPath = ""

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    global _top1, _w1
    _top1 = root
    _w1 = webgl.Toplevel1(_top1)
    root.mainloop()


def getProjectPath():
    global projectPath
    projectPath = filedialog.askdirectory()
    _w1.pathLabel["text"] = projectPath

def RunWebgl():
    _w1.RunButton.configure(bg="red")
    if projectPath != "" :
        thread = Thread(target=startWebgl)
        thread.start()
        _w1.RunButton.configure(bg="green")
       
def startWebgl():
    os.system('cmd /k "cd {} && python -m http.server 9401"'.format(Path(projectPath)))


if __name__ == '__main__':
    webgl.start_up()
