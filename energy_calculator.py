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

        fixedChargeLabel = Label(centerFrame,text="Fixed Fees")
        fixedChargeLabel.pack()
        
        fixedCharge = Entry(centerFrame,bd=5)
        fixedCharge.pack()
        self.fixedChrg = fixedCharge 

        daysChargedLabel = Label(centerFrame,text="Days Charged")
        daysChargedLabel.pack()
        
        daysCharged = Entry(centerFrame,bd=5)
        daysCharged.pack()
        self.daysChrg = daysCharged 

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
        # kwhUsed = math.ceil(currentKwh - startKwh)*0.1
        kwhUsed = math.ceil(currentKwh - startKwh)

        energyCost = kwhUsed*0.095
        fixedCharge = float(root.fixedChrg.get())/2
        regulatedCharges = kwhUsed*0.00844
        otherRegulatedFees = kwhUsed*0.0069

        airPolutionFees = kwhUsed*0.17
        efkFee = kwhUsed*0.0022

        daysCharged = int(root.daysChrg.get())
        communityFee = (64*1.27)*(daysCharged/365)
        communityVat = (64*0.18)*(daysCharged/365)

        propertyTax = 64*950*0.7*0.00035*(daysCharged/365)

        ertFee = (daysCharged/365)*36.00

        totalCharge = energyCost+fixedCharge+regulatedCharges+otherRegulatedFees+airPolutionFees+efkFee+communityFee+communityVat+propertyTax+ertFee
        # finalCharge = round(totalCharge,1)
        root.resultLabel.config(text=totalCharge)
if __name__ == "__main__":
    root = tk.Tk()
    EnergyCalculator(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
