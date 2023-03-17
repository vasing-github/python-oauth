
import tkinter as tk
from tkinter import *
import io
import sys
from tkinter import scrolledtext
import asyncio
import threading
import queue

import 录件

# 创建一个队列用于通信
q = queue.Queue()

# 创建主窗口
root = tk.Tk()
root.title("一体化平台自动录件系统")

# 修改窗口背景颜色
root.configure(bg="#F0F0F0")

# 第一行：输入框，提示用户输入 key
key_label = tk.Label(root, text="Key:", font=("Arial", 14), bg="#F0F0F0")
key_label.grid(row=0, column=0, padx=10, pady=10)
key_entry = tk.Entry(root, font=("Arial", 24))
key_entry.grid(row=0, column=1, padx=10, pady=10)

# 第二行：多个输入框，提示用户输入录件条数、推送条数、评价条数
record_label = tk.Label(root, text="录件条数:", font=("Arial", 14), bg="#F0F0F0")
record_label.grid(row=1, column=0, padx=10, pady=10)
record_entry = tk.Entry(root, font=("Arial", 14))
record_entry.grid(row=1, column=1, padx=10, pady=10)

push_label = tk.Label(root, text="推送条数:", font=("Arial", 14), bg="#F1F1F1")
push_label.grid(row=1, column=2, padx=10, pady=10)
push_entry = tk.Entry(root, font=("Arial", 14))
push_entry.grid(row=1, column=3, padx=10, pady=10)

review_label = tk.Label(root, text="评价条数:", font=("Arial", 14), bg="#F0F0F0")
review_label.grid(row=1, column=4, padx=10, pady=10)
review_entry = tk.Entry(root, font=("Arial", 14))
review_entry.grid(row=1, column=5, padx=10, pady=10)

# 第三行：几个并排的按钮，分别是录件、推送、评价
record_button = tk.Button(root, text="录件", font=("Arial", 14))
record_button.grid(row=2, column=0)

push_button = tk.Button(root, text="推送", font=("Arial", 14))
push_button.grid(row=2, column=1)

review_button = tk.Button(root, text="评价", font=("Arial", 14))
review_button.grid(row=2, column=2)

def on_record_button_click():

    # 获取输入框中的值
    key = key_entry.get()
    record_count = record_entry.get()
    push_count = push_entry.get()
    review_count = review_entry.get()


    # 禁用按钮，避免重复启动任务
    record_button.config(state=tk.DISABLED)

    worker_thread = threading.Thread(target=录件.run, args=(q,))
    worker_thread.start()

# 第四行：create a text widget to display the output

text = scrolledtext.ScrolledText(root)
text.grid(row=3, column=1)

# 定义一个函数用于更新GUI
def update():
    # 如果队列不为空，就从队列中取出计数结果并更新标签
    if not q.empty():
        text.delete("1.0", END)
        # insert the new output into the text widget
        text.insert(END, str(q.get()))
        text.see(tk.END)
    # 每隔100毫秒调用一次自己，以保持更新频率
    root.after(1000, update)

# 绑定按钮的点击事件到start函数
record_button.config(command=on_record_button_click)

# 调用一次update函数
update()

# pass the root window object to print module
录件.root = root

# 运行主循环
root.mainloop()

