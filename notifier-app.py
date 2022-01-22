from tkinter import *
from plyer import notification
from tkinter import messagebox
import time

t = Tk()
t.title('Notifier')
t.geometry("500x300")

# get details
def get_details():
    get_category = category_value.get()
    get_msg = msg.get()
    get_time = time1.get()
    # print(get_title,get_msg, tt)

    if get_category == "" or get_msg == "" or get_time == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = int(float(get_time))
        min_to_sec = int_time * 60
        messagebox.showinfo("notifier set", "set notification ?")
        t.destroy()
        time.sleep(min_to_sec)

        notification.notify(title=get_category,
                            message=get_msg,
                            app_name="Notifier",
                            app_icon="",
                            toast=True,
                            timeout=10)

# Selection Menu for Category
category_options = ["Hydration", "Wholesome Motivation"]

# Label - Category
category_label = Label(t, text="Category",font=("poppins", 10))
category_label.place(x=12, y=70)

# Option menu - Category
# variable to keep track of option
category_value = StringVar(t)
category_value.set("Select a category of reminders")
category_menu = OptionMenu(t, category_value, *category_options)
category_menu.pack()
category_menu.place(x=123, y=70)

# Label - Message
m_label = Label(t, text="Display Message", font=("poppins", 10))
m_label.place(x=12, y=120)

# ENTRY - Message
msg = Entry(t, width="40", font=("poppins", 13))
msg.place(x=123,height=30, y=120)

# Label - Time
time_label = Label(t, text="Set Time", font=("poppins", 10))
time_label.place(x=12, y=175)

# ENTRY - Time
time1 = Entry(t, width="5", font=("poppins", 13))
time1.place(x=123, y=175)

# Label - min
time_min_label = Label(t, text="min", font=("poppins", 10))
time_min_label.place(x=175, y=180)

# Button
but = Button(t, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised",
             command=get_details)
but.place(x=170, y=230)

t.resizable(0,0)
t.mainloop()