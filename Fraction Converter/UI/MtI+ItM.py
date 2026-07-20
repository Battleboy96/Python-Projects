import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Fraction Converter")
root.geometry("400x350")

ImproperMixedFrame = ttk.Frame(root)
ImproperMixedFrame.pack(fill="both", expand=True)

WholeFrame = ttk.Frame(ImproperMixedFrame)
WholeFrame.pack(pady=70, padx=10, side="left", anchor="n")
ImproperWholeInput = ttk.Entry(WholeFrame)
ImproperWholeInput.pack()
WholeHint = ttk.Label(WholeFrame, text="Whole Number", foreground="grey", font=("Arial", 10, "italic"))
WholeHint.pack(pady=5)

NumeratorFrame = ttk.Frame(ImproperMixedFrame)
NumeratorFrame.pack(pady=30, padx=10)
NumeratorInput = ttk.Entry(NumeratorFrame)
NumeratorInput.pack()
NumeratorHint = ttk.Label(NumeratorFrame, text="Numerator", foreground="grey", font=("Arial", 10, "italic"))
NumeratorHint.pack(pady=5)

DenominatorFrame = ttk.Frame(ImproperMixedFrame)
DenominatorFrame.pack(pady=5, padx=10)
DenominatorInput = ttk.Entry(DenominatorFrame)
DenominatorInput.pack()
DenominatorHint = ttk.Label(DenominatorFrame, text="Denominator", foreground="grey", font=("Arial", 10, "italic"))
DenominatorHint.pack(pady=5)

root.mainloop()