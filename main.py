import pymem
import pymem.process
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Made by Nitroxit

def apply_styles(window):
    style = ttk.Style()

    # Set theme
    style.theme_use('clam')  # or 'default', 'alt', 'clam', etc.

    # Global styling
    style.configure("TButton", font=('Helvetica', 12, 'bold'), foreground='#ffffff', background='#4CAF50', padding=10)
    style.map("TButton", background=[('active', '#45a049')])

    style.configure("TLabel", font=('Helvetica', 12), foreground='#ffffff', background='#333333')
    style.configure("TEntry", font=('Helvetica', 12), padding=10)

    style.configure("TCheckbutton", font=('Helvetica', 12), foreground='#ffffff', background='#333333')
    style.map("TCheckbutton", foreground=[('active', '#ffffff')], background=[('active', '#4CAF50')])

    # Window background color
    window.configure(background='#2C3E50')

# Memory modification function for Money
def change_money(value):
    try:
        pm = pymem.Pymem('testing-Win64-Shipping.exe')
        module = pymem.process.module_from_name(pm.process_handle, "testing-Win64-Shipping.exe").lpBaseOfDll
        base_address = module + 0x0597CB58
        offsets = [0x108, 0x110, 0x1A0, 0x20, 0xC0, 0x20, 0x6A0]

        address = pm.read_longlong(base_address)
        for offset in offsets[:-1]:
            address = pm.read_longlong(address + offset)

        final_address = address + offsets[-1]
        pm.write_float(final_address, value)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to modify memory: {e}")

# Memory modification function for Stamina
def change_stamina(value):
    try:
        pm = pymem.Pymem('testing-Win64-Shipping.exe')
        module = pymem.process.module_from_name(pm.process_handle, "testing-Win64-Shipping.exe").lpBaseOfDll
        base_address = module + 0x058404A0
        offsets = [0x1B0, 0x500, 0xA60, 0x220, 0x10, 0x50, 0x868]

        address = pm.read_longlong(base_address)
        for offset in offsets[:-1]:
            address = pm.read_longlong(address + offset)

        final_address = address + offsets[-1]
        pm.write_float(final_address, value)

    except Exception as e:
        messagebox.showerror("Error", f"Failed to modify memory: {e}")

# GUI
def main_window():
    window = tk.Tk()
    window.geometry('200x200')
    apply_styles(window)
    window.title("Fair-ish HBV Trainer")

    # Money Section
    money_label = tk.Label(window, text="Enter Money Value:")
    money_label.pack(pady=5)

    money_entry = tk.Entry(window)
    money_entry.pack(pady=5)

    def on_money_button_click():
        try:
            value = float(money_entry.get())
            change_money(value)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for Money.")

    money_button = tk.Button(window, text="Set Money", command=on_money_button_click)
    money_button.pack(pady=5)

    # Stamina Section
    stamina_label = tk.Label(window, text="Enter Stamina Value:")
    stamina_label.pack(pady=5)

    stamina_entry = tk.Entry(window)
    stamina_entry.pack(pady=5)

    def on_stamina_button_click():
        try:
            value = float(stamina_entry.get())
            change_stamina(value)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for Stamina.")

    stamina_button = tk.Button(window, text="Set Stamina", command=on_stamina_button_click)
    stamina_button.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    main_window()
