from tkinter import *
from PIL import Image, ImageTk
app = Tk()
app.geometry("400x400")

def get_x_and_y(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

def draw_smth(event):
    global lasx, lasy
    canvas.create_line((lasx, lasy, event.x, event.y), fill='red', width=2)
    lasx, lasy = event.x, event.y

def paint(event):
    color = 'red'
    x1, y1 = (event.x-1), (event.y-1)
    x2, y2 = (event.x+1), (event.y+1)
    canvas.create_oval(x1,y1,x2,y2, fill=color, outline=color)

def delete_line():

    canvas.delete('all')

canvas = Canvas(app, bg='black')
canvas.pack(anchor='nw', fill='both', expand=1)

# canvas.bind("<Button-1>", get_x_and_y)
# canvas.bind("<B1-Motion>", draw_smth)

canvas.bind("<B1-Motion>", paint)
canvas.bind("<Button-2>", delete_line)

image = Image.open("images.jpg")
image = image.resize((400,400), Image.LANCZOS)
image = ImageTk.PhotoImage(image)
canvas.create_image(0,0, image=image, anchor='nw')

message_1 = Label(app, text='Press LEFT mouse and Drag to draw')
message_2 = Label(app, text='RIGHT click to delete all')
canvas.grid(row=0, column=0)
message_1.grid(row=1, column=0)
message_2.grid(row=2, column=0)


app.mainloop()