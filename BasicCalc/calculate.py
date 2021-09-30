from tkinter import *
root = Tk()
root.geometry("444x700")
root.title("Calculator")
root.wm_iconbitmap("calc.ico")


def click(event):
    global scvalue
    text = event.widget.cget("text")  # cget is used to get text from a widget
    # print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

Label(root, text="Calculator", font="bookman 30 bold").pack()
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8)

f = Frame(root, bg="black")

for i in range(1, 4):
    b = Button(f, text=str(i), font="lucida 35 bold")
    b.pack(side=LEFT, padx=13, pady=10)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="black")
for i in range(4, 7):
    b = Button(f, text=str(i), font="lucida 35 bold")
    b.pack(side=LEFT, padx=13, pady=10)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="black")
for i in range(7, 10):
    b = Button(f, text=str(i), font="lucida 35 bold")
    b.pack(side=LEFT, padx=13, pady=10)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="black")
for i in ["0", ".", "=", "C"]:
    b = Button(f, text=str(i), font="lucida 35 bold")
    b.pack(side=LEFT, padx=12, pady=10)
    b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="black")
for i in ["+", "-", "*", " / "]:
    b = Button(f, text=str(i), font="lucida 35 bold")
    b.pack(side=LEFT, padx=12, pady=10)
    b.bind("<Button-1>", click)
f.pack()

root.mainloop()