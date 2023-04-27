import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # 创建按钮用于触发页面跳转
        self.redirect_button = tk.Button(self)
        self.redirect_button["text"] = "跳转页面"
        self.redirect_button["command"] = self.redirect_to_another
        self.redirect_button.pack(side="top")

    def redirect_to_another(self):
        # 销毁当前窗口并显示另一个窗口
        self.master.destroy()
        root = tk.Tk()
        app = AnotherApplication(master=root)
        app.mainloop()

class AnotherApplication(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # 创建标签用于显示页面内容
        self.message_label = tk.Label(self)
        self.message_label["text"] = "这是另一个页面"
        self.message_label.pack(side="top")

root = tk.Tk()
app = Application(master=root)
app.mainloop()