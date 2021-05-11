import tkinter as tk
import PyPDF2
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

app = tk.Tk()

# Size of the GUI app
canvas = tk.Canvas(app, width=1200, height=300)
canvas.grid(columnspan=3, rowspan=3)

# Logo for the Interface
logo = Image.open('picture.png', )
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# Text to be displayed
text = tk.Label(app, text='Select the PDF to extract the text', font='Raleway')
text.grid(columnspan=5, column=0, row=3)


def read_file():
    button_text.set("loading...")
    file = askopenfile(parent=app, mode='rb', title='Select a file to be read', filetype=[("PDF File", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        # text box where text is to be displayed
        text_box = tk.Text(app, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_config("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        button_text.set("Browse")


# button to choose the file
button_text = tk.StringVar()
button = tk.Button(app, textvariable=button_text, command=lambda: read_file(), font='Raleway')
button_text.set("Browse")
button.grid(column=1, row=1)

canvas = tk.Canvas(app, width=1200, height=250)
canvas.grid(columnspan=3)

app.mainloop()
