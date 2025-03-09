import tkinter as tk
from tkinter import messagebox, filedialog
import pyperclip

#Let's start encrypting!
# We're using CeaserCipher
def encrypt():
    text = text_entry.get()
    shift = shift_entry.get()

    if text == "":
        messagebox.showerror("Error", "Please enter text to encrypt.")
        return
    if not shift.isdigit() or shift == "":
        messagebox.showerror("Error", "Shift value must be a number.")
        return

    shift = int(shift)
    encrypted_text = ''.join(chr(ord(char) + shift) for char in text)
    text_entry.delete(0, tk.END)
    text_entry.insert(0, encrypted_text)


def decrypt():
    text = text_entry.get()
    shift = shift_entry.get()

    if text == "":
        messagebox.showerror("Error", "Please enter text to decrypt.")
        return
    if not shift.isdigit() or shift == "":
        messagebox.showerror("Error", "Shift value must be a number.")
        return

    shift = int(shift)
    decrypted_text = ''.join(chr(ord(char) + shift) for char in text)
    text_entry.delete(0, tk.END)
    text_entry.insert(0, decrypted_text)



def copy_text():
    text = text_entry.get()
    pyperclip.copy(text)

def paste_text():
    text = pyperclip.paste()
    text_entry.delete(0, tk.END)
    text_entry.insert(0, text)


def clear_text():
    text_entry.delete(0, tk.END)
    shift_entry.delete(0, tk.END)


def save_to_file():
    text = text_entry.get()
    if not text:
        messagebox.showerror("Error", "No text to save!")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
             file.write(text)
        messagebox.showinfo("Success", "Text Saved successfully!")

def load_from_file():
    file_path =  filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text = file.read()
            text_entry.delete(0, tk.END)
            text_entry.insert(0, text)

#   GUI setup
root = tk.Tk()
root.title("Cyber Encryption-Decryption Tool")
root.geometry("700x620")
root.config(bg="black")

# Create Labels
tk.Label(root, text="Enter Text:", fg="red", bg="black", font=("Arial", 12)).pack()
text_entry = tk.Entry(root, width=50)
text_entry.pack()

tk.Label(root, text="Enter Shift Value:", fg="red", bg="black", font=("Arial", 12)).pack()
shift_entry = tk.Entry(root, width=15)
shift_entry.pack()


# BUTTONS
button_style = {"bg": "red", "fg": "black", "font": ("Arial", 10 , "bold"), "width": 20, "height": 1}

tk.Button(root, text="Encrypt", command=encrypt, **button_style).pack(pady=2)
tk.Button(root, text="Decrypt", command=decrypt, **button_style).pack(pady=2)
tk.Button(root, text="Copy Text", command=copy_text, **button_style).pack(pady=2)
tk.Button(root, text="Paste Text", command=paste_text, **button_style).pack(pady=2)
tk.Button(root, text="Save to File", command=save_to_file, **button_style).pack(pady=2)
tk.Button(root, text="Load from File", command=load_from_file, **button_style).pack(pady=2)
tk.Button(root, text="Clear Text", command=clear_text, **button_style).pack(pady=2)

root.mainloop()




