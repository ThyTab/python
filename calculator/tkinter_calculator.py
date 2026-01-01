import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("简易计算器")
        self.root.geometry("300x400")  # 窗口大小
        self.root.resizable(False, False)  # 禁止调整窗口大小

        # 显示区域
        self.display = ttk.Entry(root, font=('Arial', 20), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

        # 按钮布局（按行排列）
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('DEL', 5, 1), ('(', 5, 2), (')', 5, 3)
        ]

        # 创建按钮
        for (text, row, col) in buttons:
            button = ttk.Button(root, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')

        # 调整网格权重（让按钮自适应窗口大小）
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            # 清空显示
            self.display.delete(0, tk.END)
        elif char == 'DEL':
            # 删除最后一个字符
            current = self.display.get()
            self.display.delete(len(current)-1, tk.END)
        elif char == '=':
            # 计算结果
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            # 输入数字或运算符
            self.display.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
