from tkinter import *
import tkinter as tk
from tkinter import messagebox
from plyer import notification
from PIL import Image, ImageTk
import time

def get_details():
    get_title = title.get()
    get_msg = message.get()
    get_time = time1.get()
    # print(get_title, get_msg, get_time)

    if get_title == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All fields are required!")

    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        messagebox.showinfo("notifier set", "Notification set")
        notifier.destroy()
        time.sleep(min_to_sec)

        notification.notify(title = get_title,
                             message = get_msg,
                             app_name = "Notifier",
                             app_icon = "icon/main.ico",
                             toast = True,
                             timeout = 20)


notifier = tk.Tk()
notifier.title('Desktop Notifier')
notifier.geometry("600x430")
notifier.configure(bg = "#000000")
my_canvas = Canvas(notifier, width = 700, height = 430, bd = 0, highlightthickness = 0, relief = "ridge")
my_canvas.place(x = 0, y = 0)

logo = Image.open("logo/DNlogo.png")
resized_logo = logo.resize((600, 50), Image.ANTIALIAS)
new_logo = ImageTk.PhotoImage(resized_logo)
logo_n = my_canvas.create_image(295,55, image = new_logo)

my_canvas.create_text(155,130, text="Title to notify", fill='black', font=('gabriola', 14))
entry0_img = PhotoImage(file = f"other/Ipbar.png")
entry0_bg = my_canvas.create_image(300, 160, image = entry0_img)
title = Entry(bd = 0, font=('Gabriola', 12),bg = "#2c2c2c", fg = '#ffffff', highlightthickness = 0)
title.place(x = 113, y = 145, width = 375, height = 25)

my_canvas.create_text(170,210, text="Message to display", fill='black', font=('gabriola', 14))
entry1_img = PhotoImage(file = f"other/Ipbar.png")
entry1_bg = my_canvas.create_image(300, 240, image = entry1_img)
message = Entry(bd = 0, font=('Gabriola', 12), bg = "#2c2c2c", fg = '#ffffff', highlightthickness = 0)
message.place(x = 113, y = 225, width = 375, height = 25)

my_canvas.create_text(165,290, text="Time (in Minute)", fill='black', font=('gabriola', 14))
entry2_img = PhotoImage(file = f"other/Ipbar.png")
entry2_bg = my_canvas.create_image(300, 320, image = entry2_img)
time1 = Entry(bd = 0, font=('Gabriola', 12), bg = "#2c2c2c", fg = '#ffffff', highlightthickness = 0)
time1.place(x = 113, y = 307, width = 375, height = 25)

# Button
but = Button(notifier, text="SET NOTIFICATION", font=("gabriola", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised",
             command=get_details)
but.place(x=230, y=360)

notifier.resizable(False, False)
notifier.mainloop()