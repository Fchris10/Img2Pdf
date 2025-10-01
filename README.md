# Img2Pdf
Image-PDF Converter is a desktop application with a graphical user interface (GUI) developed in Python that allows you to convert image files (JPEG, PNG, etc.) to PDF files. It's easy to use and requires no special technical knowledge.

[GUI_app](GUI.png)


---
# 🔥Features

- Image file selection via dialog
- Easy image-to-PDF conversion
- Success or error notification
- Modern graphical interface based on **CustomTkinter**
- Works on Windows and Linux (Python installed)
---
# Requirements

- Python 3.8+
- Python libraries:
```
pip install customtkinter Pillow
```
Note: The fpdf library is optional if you want to use the alternative method which also allows you to create multi-page PDFs.
---
# 📦Creating a Standalone App

To create an executable app (.exe on Windows) with PyInstaller and the icon:
1. Install PyInstaller:
```
pip install pyinstaller
```
2. Run the following command:
```
pyinstaller --onefile --windowed --icon=logo.png TkMain.py
```
- **--onefile**: Creates a single executable
- **--windowed**: Skips the terminal window
- **--icon=logo.png**: Sets the app icon
