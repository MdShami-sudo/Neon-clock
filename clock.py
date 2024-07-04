import tkinter as tk
import time

class NeonClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Neon Clock")

        self.label = tk.Label(root, font=('Helvetica', 48), bg='black', fg='cyan')
        self.label.pack(anchor='center')

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S')
        self.label.config(text=current_time)
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    clock = NeonClock(root)
    root.mainloop()
import tkinter as tk
import time

class NeonClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Neon Clock")
        self.root.configure(bg='black')

        self.shadow_label = tk.Label(root, font=('Helvetica', 48), bg='black', fg='cyan')
        self.shadow_label.place(x=5, y=5) 


        self.label = tk.Label(root, font=('Helvetica', 48), bg='black', fg='cyan')
        self.label.pack(anchor='center')


        self.update_clock()

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S')
        self.label.config(text=current_time)
        self.shadow_label.config(text=current_time)
        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    clock = NeonClock(root)
    root.mainloop()
