import tkinter
from PIL import Image, ImageTk

current_window = "button3"


# 创建子窗口
def show_window(title):
    global current_window
    #
    # # 在主窗口中显示子窗口的内容
    # frame_window1.pack_forget()
    # frame_window2.pack_forget()
    # frame_window3.pack_forget()

    if title == "button3":
        frame_window1.pack()
        frame_window2.pack_forget()
        frame_window3.pack_forget()
        current_window = "button3"
    elif title == "button4":
        frame_window2.pack()
        frame_window1.pack_forget()
        # frame_window2.pack_forget()
        frame_window3.pack_forget()
        current_window = "button4"
    elif title == "button5":
        frame_window3.pack()
        frame_window1.pack_forget()
        frame_window2.pack_forget()
        current_window = "button5"


root = tkinter.Tk()
root.title("管理员界面")
root.geometry("800x600")

frame = tkinter.Frame(root, width=800, height=600)
frame.pack()


def administrator():
    # 添加图像控件
    logo = ImageTk.PhotoImage(file="logo.png")
    label1 = tkinter.Label(frame, image=logo, width=20, height=20)
    label1.place(x=0, y=0)

    # 添加标签控件
    label2 = tkinter.Label(frame, text="5G潜在用户分析系统")
    label2.place(x=300, y=0)

    # 添加按钮控件
    button1 = tkinter.Button(frame, text='button1')
    button1.place(x=680, y=0)

    button2 = tkinter.Button(frame, text='button2')
    button2.place(x=740, y=0)

    button3 = tkinter.Button(frame, text="button3", bg="red", width=30, command=lambda: show_window("button3"))
    button3.place(x=0, y=100)

    button4 = tkinter.Button(frame, text="button4", width=30, command=lambda: show_window("button4"))
    button4.place(x=260, y=100)

    button5 = tkinter.Button(frame, text="button5", width=30, command=lambda: show_window("button5"))
    button5.place(x=500, y=100)

administrator()
frame_window1 = tkinter.Frame(root)
# # 添加图像控件
# logo = ImageTk.PhotoImage(file="logo.png")
# label1 = tkinter.Label(frame_window1, image=logo, width=20, height=20)
# label1.place(x=0, y=0)
#
# # 添加标签控件
# label2 = tkinter.Label(frame_window1, text="5G潜在用户分析系统")
# label2.place(x=300, y=0)
#
# # 添加按钮控件
# button1 = tkinter.Button(frame_window1, text='button1')
# button1.place(x=680, y=0)
#
# button2 = tkinter.Button(frame_window1, text='button2')
# button2.place(x=740, y=0)
#
# button3 = tkinter.Button(frame_window1, text="button3", bg="red", width=30, command=lambda: show_window("button3"))
# button3.place(x=0, y=100)
#
# button4 = tkinter.Button(frame_window1, text="button4", width=30, command=lambda: show_window("button4"))
# button4.place(x=260, y=100)
#
# button5 = tkinter.Button(frame_window1, text="button5", width=30, command=lambda: show_window("button5"))
# button5.place(x=500, y=100)

frame_window2 = tkinter.Frame(root)
# # 添加图像控件
# logo = ImageTk.PhotoImage(file="logo.png")
# label1 = tkinter.Label(frame_window2, image=logo, width=20, height=20)
# label1.place(x=0, y=0)
#
# # 添加标签控件
# label2 = tkinter.Label(frame_window2, text="5G潜在用户分析系统")
# label2.place(x=300, y=0)
#
# # 添加按钮控件
# button1 = tkinter.Button(frame_window2, text='button1')
# button1.place(x=680, y=0)
#
# button2 = tkinter.Button(frame_window2, text='button2')
# button2.place(x=740, y=0)
#
# button3 = tkinter.Button(frame_window2, text="button3", width=30, command=lambda: show_window("button3"))
# button3.place(x=0, y=100)
#
# button4 = tkinter.Button(frame_window2, text="button4", width=30, bg="red", command=lambda: show_window("button4"))
# button4.place(x=260, y=100)
#
# button5 = tkinter.Button(frame_window2, text="button5", width=30, command=lambda: show_window("button5"))
# button5.place(x=500, y=100)
#
frame_window3 = tkinter.Frame(root)
# # 添加图像控件
# logo = ImageTk.PhotoImage(file="logo.png")
# label1 = tkinter.Label(frame_window3, image=logo, width=20, height=20)
# label1.place(x=0, y=0)
#
# # 添加标签控件
# label2 = tkinter.Label(frame_window3, text="5G潜在用户分析系统")
# label2.place(x=300, y=0)
#
# # 添加按钮控件
# button1 = tkinter.Button(frame_window3, text='button1')
# button1.place(x=680, y=0)
#
# button2 = tkinter.Button(frame_window3, text='button2')
# button2.place(x=740, y=0)
#
# button3 = tkinter.Button(frame_window3, text="button3", width=30, command=lambda: show_window("button3"))
# button3.place(x=0, y=100)
#
# button4 = tkinter.Button(frame_window3, text="button4", width=30, command=lambda: show_window("button4"))
# button4.place(x=260, y=100)
#
# button5 = tkinter.Button(frame_window3, text="button5", width=30, bg="red", command=lambda: show_window("button5"))
# button5.place(x=500, y=100)
#

# administrator()

show_window("button3")
root.mainloop()

# button3 = tkinter.Button(frame, text="button3", width=30, command=lambda: show_window("button3"))
# button3.place(x=0, y=100)
#
# button4 = tkinter.Button(frame, text="button4", width=30, command=lambda: show_window("button4"))
# button4.place(x=260, y=100)
#
# button5 = tkinter.Button(frame, text="button5", width=30, command=lambda: show_window("button5"))
# button5.place(x=500, y=100)

# def administrator():
#     # 创建一个tk对象
#     tk = tkinter.Tk()
#     tk.title('管理员页面')
#     tk.geometry("800x600")
#
#     # 创建一个Frame用于显示界面
#     frame = tkinter.Frame(tk, width=800, height=600)
#     frame.pack()
#
#     # 添加图像控件
#     logo = ImageTk.PhotoImage(file="logo.png")
#     label1 = tkinter.Label(frame, image=logo, width=20, height=20)
#     label1.place(x=0, y=0)
#
#     # 添加标签控件
#     label2 = tkinter.Label(frame, text="5G潜在用户分析系统")
#     label2.place(x=300, y=0)
#
#     # 添加按钮控件
#     button1 = tkinter.Button(frame, text='button1')
#     button1.place(x=680, y=0)
#
#     button2 = tkinter.Button(frame, text='button2')
#     button2.place(x=740, y=0)
#
#     button3 = tkinter.Button(frame, text="button3", width=30, bg="green")
#     button3.place(x=0, y=100)
#
#     button4 = tkinter.Button(frame, text="button4", width=30, command=lambda: show_window("button4"))
#     button4.place(x=260, y=100)
#
#     button5 = tkinter.Button(frame, text="button5", width=30, command=lambda: show_window("button5"))
#     button5.place(x=500, y=100)
#
#
#     tk.mainloop()
