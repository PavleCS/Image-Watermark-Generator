from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
from PIL import Image, ImageDraw, ImageFont

image_path = ""

window = Tk()
window.title("Watermark Generator")
window.config(pady=50, padx=50, bg="#643843")

# ----- Text area -----
text_area = Text(
    font=("arial", 10, "bold"),
    height=10,
    width=34,
    bg="#99627A",
    highlightthickness=0
)
text_area.grid(row=0, column=0)
text_area.insert(END, "Please upload your image")


# ----- Custom Watermark Text -----
def click(self):
    custom_text_entry.delete(0, END)


custom_text_entry = Entry(
    bg="#99627A",
    highlightthickness=0,
    textvariable=StringVar(),
    font=("arial", 10, "bold"),
    width=34
)
custom_text_entry.insert(0, "Enter your text here")
custom_text_entry.bind("<Button-1>", click)
custom_text_entry.grid(row=1, column=0, pady=10)


# ----- Upload Action -----
def upload():
    global image_path
    filetypes = (
        ("PNG files", "*.png"),
        ("JPEG files", "*.jpg"),
        ("All files", "*.*")
    )

    path = fd.askopenfilename(
            title="Open an image",
            initialdir="/Desktop",
            filetypes=filetypes
    )

    showinfo(
            title="Selected image",
            message="Successfully uploaded"
    )
    text_area.delete(1.0, END)
    text_area.insert(1.0, "Your image is successfully uploaded. Please enter your text bellow and\npress generate to "
                          "add the watermark.")

    image_path = path


frame = Frame(
    window,
    width=15,
    bg="#E7CBCB",
)
frame.grid(row=0, column=1, padx=30)

# ----- Buttons -----
upload_button = Button(
    frame,
    text="Upload Image",
    font=("arial", 15, "bold"),
    highlightthickness=0,
    border=0,
    bg="#99627A",
    fg="#E7CBCB",
    width=12,
    command=upload
)
upload_button.grid(row=0, column=1, padx=10, pady=10)


def generate():
    watermark = custom_text_entry.get()

    text_area.delete(1.0, END)
    text_area.insert(1.0, "Your watermark is successfully added\nYou can upload your next image.")

    # ----- Creating Watermark -----

    image = Image.open(image_path)
    width, height = image.size

    draw = ImageDraw.Draw(image)
    text = watermark

    font = ImageFont.truetype("arial", 46)
    text_width, text_height = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 100
    x = width - text_width - margin
    y = height - text_height - margin

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font, fill='blue')
    image.show()

    image.save("watermark.png")


generate_button = Button(
    frame,
    text="Generate",
    font=("arial", 15, "bold"),
    highlightthickness=0,
    border=0,
    bg="#99627A",
    fg="#E7CBCB",
    width=12,
    command=generate
)
generate_button.grid(row=1, column=1, pady=5)

# download_button = Button(
#     frame,
#     text="Download",
#     font=("arial", 15, "bold"),
#     highlightthickness=0,
#     border=0,
#     bg="#99627A",
#     fg="#E7CBCB",
#     width=12,
# )
# download_button.grid(row=2, column=1, padx=10, pady=10)


window.mainloop()
