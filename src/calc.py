import tkinter as tk


m = tk.Tk()

close = tk.Button(m, text='Close', command=m.destroy)
close.pack()
m.mainloop()
