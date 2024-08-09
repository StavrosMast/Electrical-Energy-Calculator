import tkinter as tk
from tkinter import Label,Frame,Button,Entry,Text
import math

import tkinter as tk

class EnergyCalculator(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        centerFrame = Frame(root)
        centerFrame.pack()

        startingLabel = Label(centerFrame,text="Starting KWh")
        startingLabel.pack()

        startingKwh = Entry(centerFrame,bd=5)
        startingKwh.pack()
        self.startKwh = startingKwh

        currentLabel = Label(centerFrame,text="Current KWh")
        currentLabel.pack()

        currentKwh = Entry(centerFrame,bd=5)
        currentKwh.pack()
        self.currKwh = currentKwh

        result = Label(centerFrame)
        result.pack()
        self.resultLabel = result

        showResultButton = Button(root,text='Show Result',command=self.showResult)
        showResultButton.pack()

        closeButton = Button(root,text='Quit',command=root.quit)
        closeButton.pack()
    def showResult(root):
        startKwh = float(root.startKwh.get())
        currentKwh = float(root.currKwh.get())
        kwhUsed = math.ceil(currentKwh - startKwh)*0.1


        root.resultLabel.config(text=kwhUsed)
if __name__ == "__main__":
    root = tk.Tk()
    EnergyCalculator(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
