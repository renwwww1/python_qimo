# 导入tkinter库
import tkinter

from PIL import Image, ImageTk
# from numba.cuda import event


def guan():
    tk = tkinter.Tk()  # 创建一个tk对象
    tk.title('管理员页面')  # 设置图形框名
    tk.geometry("800x600")
    # image = Image.open("logo.png")
    # logo = ImageTk.PhotoImage(image)
    logo = ImageTk.PhotoImage(file="logo.png")
    label1 = tkinter.Label(tk, image=logo, width=20, height=20).place(x=0, y=0)
    label2 = tkinter.Label(tk, text="5G潜在用户分析系统").place(x=300, y=0)
    # label.pack(side=tkinter.TOP) # 默认放置
    button1 = tkinter.Button(tk, text='button1').place(x=680, y=0)
    # button1.pack(anchor=tkinter.NE) # 将button1靠左放置
    button2 = tkinter.Button(tk, text='button2').place(x=740, y=0)
    button3 = tkinter.Button(tk, text="button3",  width=30, command=tk.destroy).place(x=0, y=100)
    button4 = tkinter.Button(tk, text="button4",  width=30,  command=tk.destroy).place(x=260, y=100)
    button5 = tkinter.Button(tk, text="button5",  width=30).place(x=500, y=100)

    tk.mainloop()  # 进入消息循环，即显示窗口

guan()
root2=tkinter.Tk()
root2.title("页面")
lab_2=tkinter.Label(root2, text="第三个界面", height=3).place(x=0, y=0)
root2.mainloop()

guan()
root=tkinter.Tk()
root.title("5G潜在用户页面")
lab_1=tkinter.Label(root, text="第二个界面", height=3).place(x=0, y=0)
root.mainloop()





































