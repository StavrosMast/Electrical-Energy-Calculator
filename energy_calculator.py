import math
import customtkinter as tk
from customtkinter import CTkButton,CTkFrame,CTkLabel,CTkEntry

class EnergyCalculator(tk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        tk.CTkFrame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        centerFrame = CTkFrame(root)
        centerFrame.pack()

        startingLabel = CTkLabel(centerFrame,text="Starting KWh")
        startingLabel.pack()

        startingKwh = CTkEntry(centerFrame)
        startingKwh.pack()
        self.startKwh = startingKwh

        currentLabel = CTkLabel(centerFrame,text="Current KWh")
        currentLabel.pack()

        currentKwh = CTkEntry(centerFrame)
        currentKwh.pack()
        self.currKwh = currentKwh

        fixedChargeLabel = CTkLabel(centerFrame,text="Fixed Fees")
        fixedChargeLabel.pack()
        
        fixedCharge = CTkEntry(centerFrame)
        fixedCharge.pack()
        self.fixedChrg = fixedCharge 

        daysChargedLabel = CTkLabel(centerFrame,text="Days Charged")
        daysChargedLabel.pack()
        
        daysCharged = CTkEntry(centerFrame)
        daysCharged.pack()
        self.daysChrg = daysCharged 

        result = CTkLabel(centerFrame)
        result.pack()
        self.resultLabel = result

        showResultButton = CTkButton(root,text='Show Result',command=self.showResult)
        showResultButton.pack()

        closeButton = CTkButton(root,text='Quit',command=root.quit)
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
        restCharges = kwhUsed*0.00008
        airPolutionFees = kwhUsed*0.017
        efkFee = kwhUsed*0.0022

        daysCharged = int(root.daysChrg.get())
        communityFee = (64*1.27)*(daysCharged/365)
        communityVat = (64*0.18)*(daysCharged/365)

        propertyTax = 64*950*0.7*0.00035*(daysCharged/365)

        ertFee = (daysCharged/365)*36.00

        totalCharge = energyCost+fixedCharge+regulatedCharges+otherRegulatedFees+restCharges+airPolutionFees+efkFee+communityFee+communityVat+propertyTax+ertFee
        # finalCharge = round(totalCharge,1)
        root.resultLabel.configure(text=totalCharge)
if __name__ == "__main__":
    root = tk.CTk()
    EnergyCalculator(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
