from tkinter import *
from tkinter.filedialog import askopenfile, askdirectory
from PIL import Image
import secrets
import os

# Image Upload
FONT_NAME = "Courier"
image_uploaded = None
water_marked_img = None
def open_file():
    global image_uploaded
    file_path = askopenfile(mode='r', filetypes=[('Images', '*.jpg *.png *.jpeg')])
    if file_path:
        image_uploaded =  file_path.name
    else:
        pass

def uploadFiles():
    global water_marked_img
    if image_uploaded:
        base_img = Image.open(image_uploaded)
        water_mark = Image.open('watermark2.png')
        water_mark.thumbnail((50, 50))
        width, height = base_img.size
        transparent = Image.new('RGBA', (width, height), (0,0,0,0))
        transparent.paste(base_img, (0, 0))
        transparent.paste(water_mark, (width - 60, height - 60), mask=water_mark)
        Label(text='File Uploaded Successfully!', foreground='green').grid(row=5, columnspan=3, pady=10)
        water_marked_img = transparent
    else:
        Label(text='No File Selected!', foreground='red').grid(row=5, columnspan=3, pady=10)


def show_watermarked():
    if water_marked_img:
        water_marked_img.show()
    else:
        Label(text='No File Added!', foreground='red').grid(row=8, columnspan=3, pady=10)

def save_watermarked():
    if water_marked_img:
        save_directory = askdirectory()
        filename = f'water_marked_{secrets.token_hex(5)}.png'
        file_path = os.path.join(save_directory, filename)
        water_marked_img.save(file_path)
        Label(text=f'Image Saved as {filename}', foreground='green').grid(row=8, columnspan=3, pady=10)
    else:
        Label(text='No File to Save!', foreground='red').grid(row=8, columnspan=3, pady=10)


window = Tk()
window.geometry('600x400')
window.title("Img WaterMarker")
window.config(pady=50, padx=50,background='#00ed89')
img = PhotoImage(file='watermark3.png')
icon = PhotoImage(file='watermark2.png')
window.iconphoto(False, icon)
canvas = Canvas(width=300, height=200, background="#00ed89", highlightthickness=0)
canvas.create_image(160, 100, image=img)
canvas.create_text(160, 180, text='Img Water Marker', fill='black', font=(FONT_NAME, 15, 'bold'))
canvas.grid(row=1, column=1, columnspan=2)

# # Upload Label
# select_label = Label(text="Image", padx=10)
# select_label.grid(row=2, column=0)

# File selection Widget
select_file = Button(text='Select Image...', width=33, command=open_file)
select_file.grid(row=2, column=1)

# Upload button
upload_file = Button(text='Upload', width=33, command=uploadFiles, background="#1AB6CF")
upload_file.grid(row=2, column=2)

# View Watermarked Label
view_watermarked = Label(text='View Watermarked Image 👇', background="#00ed89", font=(FONT_NAME, 9, 'bold'))
view_watermarked.grid(row=6, column=1)

# View button
view_file = Button(text='View', width=33,background="#1AB6CF", command=show_watermarked)
view_file.grid(row=7, column=1)

# View Watermarked Label
view_watermarked = Label(text='Save Watermarked Image 👇', background="#00ed89", font=(FONT_NAME, 9, 'bold'))
view_watermarked.grid(row=6, column=2)

# Save button
view_file = Button(text='Save', width=33, command=save_watermarked)
view_file.grid(row=7, column=2)




window.mainloop()