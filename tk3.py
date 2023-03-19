
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
import threading
import queue
import 录件

# 创建一个队列用于通信
q = queue.Queue()

# 创建主窗口
root = tk.Tk()
root.title("一体化平台自动录件系统")



# 第一行：输入框，提示用户输入 key
key_label = tk.Label(root, text="Key:", font=("Arial", 12), bg="#F0F0F0")
key_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
key_entry = tk.Entry(root, font=("Arial", 12), width=50)
key_entry.grid(row=0, column=1, padx=10, pady=10,  sticky='w', columnspan=2)
record_button = tk.Button(root, text="获取key", font=("Arial", 12))
record_button.grid(row=0, column=3, sticky='w', padx=10, pady=10)

# 第二行：多个输入框，提示用户输入录件条数、推送条数、评价条数
record_label = tk.Label(root, text="1.录件条数:", font=("Arial", 12), bg="#F0F0F0")
record_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')
record_entry = tk.Entry(root, font=("Arial", 12), width = 10)
record_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')
record_button = tk.Button(root, text="开始录件", font=("Arial", 12))
record_button.grid(row=1, column=2,padx=10, pady=10, sticky='w')

# 第三行：多个输入框，提示用户输入录件条数、推送条数、评价条数
shencha_button = tk.Button(root, text="2.1推送待审查", font=("Arial", 12))
shencha_button.grid(row=2, column=0,padx=10, pady=10, sticky='w')
jueding_button = tk.Button(root, text="2.2推送待决定", font=("Arial", 12))
jueding_button.grid(row=2, column=1,padx=10, pady=10, sticky='w')
zhizheng_button = tk.Button(root, text="2.3推送待制证", font=("Arial", 12))
zhizheng_button.grid(row=2, column=2,padx=10, pady=10, sticky='w')
fazheng_button = tk.Button(root, text="2.4推送待发证", font=("Arial", 12))
fazheng_button.grid(row=2, column=3,padx=10, pady=10, sticky='w')

# 第四行：评价相关
review_label = tk.Label(root, text="3.评价条数:", font=("Arial", 12), bg="#F0F0F0")
review_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')
review_entry = tk.Entry(root, font=("Arial", 12),width = 10)
review_entry.grid(row=3, column=1, padx=10, pady=10, sticky='w')
review_button = tk.Button(root, text="3.1系统件评价", font=("Arial", 12))
review_button.grid(row=3, column=2, sticky='w', padx=10, pady=10)
daorupingjia_button = tk.Button(root, text="3.2导入件评价", font=("Arial", 12))
daorupingjia_button.grid(row=3, column=3, sticky='w', padx=10, pady=10)

# 第五行：暂存件
zancun_button = tk.Button(root, text="4.暂存件清理", font=("Arial", 12))
zancun_button.grid(row=4, column=0, sticky='w', padx=10, pady=10)

# 第6行：create a text widget to display the output
text = scrolledtext.ScrolledText(root)
text.grid(row=5, column=0, sticky='w', columnspan=3, padx=10, pady=10,rowspan=5)
notice_label = tk.Label(root, text="注意:本软件仅作为学习使用，目的在于减少人工录入的错误，节约人工录入时间.\n\n本软件不会给服务器造成压力.\n\n录入数据需按真实情况填写在imEx.xlsx表格中，本软件不提供数据来源", font=("Arial", 11), bg="#F0F0F0",wraplength=150)
notice_label.grid(row=5, column=3, padx=10, pady=10, sticky='w', columnspan=4,rowspan=5)
def on_record_button_click():

    # 获取输入框中的值
    key = key_entry.get()
    record_count = record_entry.get()
    # push_count = push_entry.get()
    # review_count = review_entry.get()


    # 禁用按钮，避免重复启动任务
    record_button.config(state=tk.DISABLED)

    worker_thread = threading.Thread(target=录件.run, args=(q,))
    worker_thread.start()



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

