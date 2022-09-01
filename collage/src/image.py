import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

window = tk.Tk()
window.geometry('800x800')
window.title('COLLAGE')

#파일 선택 버튼
f_btn = tk.Button(window, text='파일 선택')
def open_f():
    global img_tk
    file = filedialog.askopenfilename(initialdir='/',
                           title='choose file',
                           filetypes=(('*.jpg','*jpg'),('*.png','*png')))
    image = Image.open(file)
    img = image.resize((210,300))
    img_tk = ImageTk.PhotoImage(img)
    img_label = tk.Label(window, image=img_tk)
    img_label.pack()

f_btn.config(width=6, height=2, command=open_f)
f_btn.pack()

window.mainloop()