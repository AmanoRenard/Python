import tkinter
import time
import sys
import subprocess
win=tkinter.Tk()
win.title("我的第一个软件")
win.geometry('800x600')
print("Please enter your name.")
print("Your name is ",sys.stdin.readline())
win.mainloop()
subprocess.Popen(cmd, close_fds=True)