import customtkinter as ctk
from tkinter import filedialog
import ImgToPdf as imgpdf


def open_explorer():
    label_confirm.pack_forget()
    label_error.pack_forget()

    selectedImg.delete(0, "end")
    filename = filedialog.askopenfilename(initialdir='/', title="Select an Image file")
    selectedImg.insert(0, filename)


def convert():
    img_path = selectedImg.get()

    if img_path:
        check = imgpdf.img_to_pdf(img_path)
        if check:
            label_confirm.pack(pady=10)
        else:
            label_error.pack(pady=10)
    return


if __name__ == "__main__":
    
    ctk.set_appearance_mode("dark")  
    ctk.set_default_color_theme("blue")

    window = ctk.CTk()
    window.geometry("400x300")
    window.title("Img2Pdf")
    window.resizable(False, False)

    title_label = ctk.CTkLabel(window, text="Image-PDF Converter", font=("Arial", 22, "bold"))
    title_label.pack(pady=20)

    button_select = ctk.CTkButton(window, text='Select Image', command=open_explorer, width=200)
    button_select.pack(pady=15)

    selectedImg = ctk.CTkEntry(window, width=350, placeholder_text="Select file path...")
    selectedImg.pack(pady=25)

    button_convert = ctk.CTkButton(window, text='Convert', command=convert, width=200)
    button_convert.pack(pady=15)

    label_confirm = ctk.CTkLabel(window, text="Conversion completed successfully!", text_color="green")
    label_error = ctk.CTkLabel(window, text="Something went wrong!", text_color="red")

    window.mainloop()