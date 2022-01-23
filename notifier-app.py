from tkinter import *
from plyer import notification
from tkinter import messagebox
import time
import random
from PIL import ImageTk,Image
import os

t = Tk()
t.title('-aquadaily-')
t.geometry("600x450")
t.configure(bg="light blue")

messageHydration = ["“Keep calm and drink water.”",
                    "“Drink water, stay HEALTHY!”",
                    "“Water is the best of all things.”  -Pindar ",
                    "“Sometimes i drink water to surprise my liver.”",
                    "“Dehydration can get ugly! Drink water, stay pretty!”",
                    "“ Feel thirsty? It’s time to hydrate yourself!!”",
                    "“ A man of wisdom delights in water.” -Confucius",
                    "“Love is the water of life, drink deeply!” - Micheal Scott",
                    "“Drink more water. Your skin, your hair, your mind and body will thank you!”",
                    "“Feel moody and fatigued? Drink Up!”",
                    "“Don’t forget to drink water and get some sun. You are basically a houseplant with more complicated emotions. “",
                    "“Water is your best friend”",
                    "“70% of the human body is made of water, remember to hydrate!”",
                    "“ Drinking water is like washing out your insides!” ",
                    "“What time is it? IT’S TIME TO HYDRATE !”",
                    ]

messageWholesome = ["“Time flies, it's up to you to be the navigator. “",
                    "“The most wasted of days is one without laughter.”",
                    "“It’s OK if all you did today was survive.”",
                    "“Life is a mountain, your goal is to find your path, not to reach the top.”",
                    "“Even the darkest night will end and the sun will rise” - Victor Hugo ",
                    "“Don’t give up on yourself. There is a reason why you started.”",
                    "“Do not feel lonely, the entire universe is inside you”",
                    "“It’s not whether you get knocked down; it’s whether you get up.”",
                    "“I know you are tired and sad, don’t worry, with a little time and love, things will get better”",
                    "“ Strive for progress, not perfection.”",
                    "“The purpose of our lives is to be happy.”",
                    "“Negativity is a choice.”",
                    "“Positive mind, positive vibes, positive life.”",
                    "“Don’t let the silly little things steal your happiness.”",
                    "“There are so many beautiful reasons to be happy!”",

                    ]

all_images = os.listdir("images")

def hide():
    choice = var.get()
    if choice == 1:
        repeat_opt.place(x=250, y=245)
        nb_repeat_label.place(x=45, y=245)
    else:
        repeat_opt.place_forget()
        nb_repeat_label.place_forget()

# get details
def get_details():
    get_category = category_value.get()
    get_hours = time1.get()
    get_min = time2.get()
    get_repeat = repeat_opt.get()

    # check if time and repeat inputs are numbers/ints
    check_hours = get_hours.replace('.', '', 1).isdigit()
    check_min = get_min.replace('.', '', 1).isdigit()
    if get_repeat != "":
        check_repeat = get_repeat.isdigit()
    else:
        check_repeat = True

    # input validation
    if get_category == "Select a category of reminders" or get_hours == "" or get_min == "":
        messagebox.showerror("Alert", "All fields are required!")

    elif not (check_hours) or not (check_min) or not (check_repeat):
        messagebox.showerror("Alert", "Please enter a number in the time fields or/and repeat field!")

    elif get_repeat != "" and not (1 <= int(get_repeat) <= 10):
        messagebox.showerror("Alert", "Please enter an integer value between 1 and 10 inclusively in the repeat field!")

    else:
        hours = float(get_hours)
        hour_to_min = hours * 60
        min = float(get_min)
        min_to_sec = (hour_to_min + min) * 60
        messagebox.showinfo("notifier set", "set notification ?")
        t.destroy()
        if get_repeat == "":
            nb_repeat = 1
        else:
            nb_repeat = int(get_repeat)

        times = 1
        while times <= nb_repeat:
            time.sleep(min_to_sec)
            notification.notify(title=get_category,
                                message=display_msg(),
                                app_name="Notifier",
                                app_icon="icon.ico",
                                toast=True,
                                timeout=10)
            times += 1

def display_msg():
    if category_value.get() == "Hydration":
        return messageHydration[random.randint(0, 14)]
    elif category_value.get() == "Wholesome Motivation":
        return messageWholesome[random.randint(0, 14)]

def randomize_img():
    return all_images[random.randint(0, len(all_images)-1)]

# Label - Title
m_label = Label(t, text="Aquadaily Reminders", font=("verdana", 25), fg="#004d80")
m_label.place(x=160, y=15)
m_label.configure(bg="light blue")

# Selection Menu for Category
category_options = ["Hydration", "Wholesome Motivation"]

# Label - Category
category_label = Label(t, text="Category:",font=("times new roman", 14))
category_label.place(x=40, y=80)
category_label.configure(bg="light blue")

# Option menu - Category
# variable to keep track of option
category_value = StringVar(t)
category_value.set("Select a category of reminders")
category_menu = OptionMenu(t, category_value, *category_options)
category_menu.pack()
category_menu.place(x=140, y=80)
category_menu.configure(bg="light blue")


# Label - Time
time_label = Label(t, text="Set Time:", font=("times new roman", 14))
time_label.place(x=40, y=135)
time_label.configure(bg="light blue")

# ENTRY - Time (hour)
time1 = Entry(t, width="3", font=("times new roman", 14), justify="right")
time1.place(x=140, y=135)


# Label - hour
time_hour_label = Label(t, text="hour", font=("times new roman", 14))
time_hour_label.place(x=175, y=137)
time_hour_label.configure(bg="light blue")

# ENTRY - Time (min)
time2 = Entry(t, width="3", font=("times new roman", 14), justify="right")
time2.place(x=220, y=135)

# Label - min
time_min_label = Label(t, text="min", font=("times new roman", 14))
time_min_label.place(x=255, y=137)
time_min_label.configure(bg="light blue")

# Image - a random meme
# open image
img_chosen = randomize_img()
img_path = "images/" + img_chosen
my_img = Image.open(img_path)
# resize image
resized = my_img.resize((200,200), Image.ANTIALIAS, )
new_img = ImageTk.PhotoImage(resized)
my_label = Label(image=new_img)
my_label.pack(pady=20)
# move image
my_label.place(x=350, y = 175)

# Label - repeat
repeat_label = Label(t, text="Repeat?", font=("times new roman", 14))
repeat_label.place(x=40, y=190)
repeat_label.configure(bg="light blue")

# Radiobuttons - yes or no to repeat
var = IntVar()
rb_1 = Radiobutton(t, text="Yes", variable=var, value=1, command=hide, font=("times new roman", 14))
rb_1.pack()
rb_1.place(x=140, y=190)
rb_1.configure(bg="light blue")
rb_2 = Radiobutton(t, text="No", variable=var, value=2, command=hide, font=("times new roman", 14))
rb_2.pack()
rb_2.place(x=210, y=190)
rb_2.configure(bg="light blue")

# (Optional/Hidden) Repeat options
nb_repeat_label = Label(t, text="Number of repeats (1-10)", font=("times new roman", 14))
nb_repeat_label.place(x=40, y=245)
nb_repeat_label.configure(bg="light blue")
repeat_opt = Entry(t, width="3", font=("times new roman", 14), justify="right")
repeat_opt.place(x=250, y=245)


# Button
but = Button(t, text="SET NOTIFICATION", font=("times new roman", 10, "bold"), fg="#004d80", bg="#97c9de", width=20,
             relief="raised",
             command=get_details)
but.place(x=100, y=320)
but.configure(bg="light blue")

t.resizable(0, 0)
t.mainloop()