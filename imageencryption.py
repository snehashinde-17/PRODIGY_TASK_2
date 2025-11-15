import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryptor")

        # Variables
        self.image_path = None
        self.image = None

        # Create GUI elements
        self.label = tk.Label(root, text="Select an image to encrypt or decrypt:")
        self.label.pack(pady=10)

        self.load_button = tk.Button(root, text="Select a  Image", command=self.load_image)
        self.load_button.pack()

        self.encrypt_button = tk.Button(root, text="Encrypt Image", command=self.encrypt_image)
        self.encrypt_button.pack(pady=5)

        self.decrypt_button = tk.Button(root, text="Decrypt Image", command=self.decrypt_image)
        self.decrypt_button.pack()

        self.image_label = tk.Label(root)
        self.image_label.pack(pady=10)

    def load_image(self):
        filetypes = [("Image files", "*.jpg *.jpeg *.png *.bmp")]
        self.image_path = filedialog.askopenfilename(filetypes=filetypes)
        if self.image_path:
            try:
                self.image = Image.open(self.image_path)
                self.image.thumbnail((300, 300))
                photo = ImageTk.PhotoImage(self.image)
                self.image_label.config(image=photo)
                self.image_label.image = photo
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image. Error: {e}")
        else:
            messagebox.showerror("Error", "No image selected.")

    def encrypt_image(self):
        if not self.image:
            messagebox.showerror("Error", "No image loaded.")
            return

        try:
            encrypted_image = self.image.point(lambda p: p ^ 255)  # XOR with 255 for encryption
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
            if save_path:
                encrypted_image.save(save_path)
                messagebox.showinfo("Encryption", f"Image encrypted and saved as {save_path}.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to encrypt image. Error: {e}")

    def decrypt_image(self):
        if not self.image:
            messagebox.showerror("Error", "No image loaded.")
            return

        try:
            decrypted_image = self.image.point(lambda p: p ^ 255)  # XOR with 255 for decryption
            save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
            if save_path:
                decrypted_image.save(save_path)
                messagebox.showinfo("Decryption", f"Image decrypted and saved as {save_path}.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to decrypt image. Error: {e}")

def main():
    root = tk.Tk()
    app = ImageEncryptorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
