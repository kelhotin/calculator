import tkinter as tk
from functools import partial

"""
Simple stackbased calculator
"""
class Calc:
    def __init__(self):
        self.m_stack = []
    
        self.m_window = tk.Tk()

        self.m_res = 0
        self.m_resLabel = tk.Label(self.m_window, text='0')
        self.m_resLabel.grid(row=0,column=2)
        tk.Label(self.m_window, text='Input').grid(row=0)
        self.m_input = tk.Entry(self.m_window)
        self.m_input.grid(row=0, column=1)

        tk.Button(self.m_window, text='Close', command=self.m_window.destroy).grid(row=1, column=1)
        tk.Button(self.m_window, text='Enter', command=self.addStack).grid(row=1, column=0)
        
        tk.Button(self.m_window, text='+', command=self.add).grid(row=2, column=0)
        tk.Button(self.m_window, text='-', command=self.add).grid(row=3, column=0)
        tk.Button(self.m_window, text='*', command=self.add).grid(row=4, column=0)
        tk.Button(self.m_window, text='/', command=self.add).grid(row=5, column=0)

    def run(self):
        self.m_window.mainloop()

    def addStack(self):
        self.m_stack.append(int(self.m_input.get()))
        self.m_input.delete(0, 'end')

    def add(self):
        a = self.m_stack.pop()
        self.m_res += a
        self.setResult()

    def sub(self):
        a = self.m_stack.pop()
        self.m_res -= a
        self.setResult()

    def mul(self):
        a = self.m_stack.pop()
        self.m_res *= a
        self.setResult()

    def div(self):
        a = self.m_stack.pop()
        if(a != 0):
            self.m_res /= a
            self.setResult()
        else:
            self.m_resLabel.configure(text="NaN")

        

    def setResult(self):
        self.m_resLabel.configure(text=self.m_res)
        
#m.mainloop()

if __name__=='__main__':
    c = Calc()
    c.run()
    
