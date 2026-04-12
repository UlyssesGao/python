import tkinter as tk
from tkinter import ttk

# 计算函数
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()
        if op == "加法":
            result = num1 + num2
        elif op == "除法":
            if num2 == 0:
                label_result.config(text="❌ 不能除以零！")
                return
            result = num1 / num2
        label_result.config(text=f"✅ 计算结果：{result}")
    except ValueError:
        label_result.config(text="❌ 请输入有效数字！")

# 主窗口
root = tk.Tk()
root.title("✨ 美化版计算器")
root.geometry("400x350")
root.resizable(False, False)  # 禁止拉伸窗口
root.config(bg="#f5f5f5")     # 浅灰背景

# 样式设置
style = ttk.Style()
style.configure("TLabel", font=("微软雅黑", 11), background="#f5f5f5")
style.configure("TButton", font=("微软雅黑", 11, "bold"), padding=8)
style.configure("TEntry", font=("微软雅黑", 11))

# 标题
title_label = ttk.Label(root, text="计算器", font=("微软雅黑", 16, "bold"), background="#f5f5f5")
title_label.pack(pady=15)

# 输入框1
frame1 = ttk.Frame(root)
frame1.pack(pady=5)
label1 = ttk.Label(frame1, text="第一个数字：")
label1.grid(row=0, column=0, padx=5)
entry1 = ttk.Entry(frame1, width=20)
entry1.grid(row=0, column=1)

# 输入框2
frame2 = ttk.Frame(root)
frame2.pack(pady=5)
label2 = ttk.Label(frame2, text="第二个数字：")
label2.grid(row=0, column=0, padx=5)
entry2 = ttk.Entry(frame2, width=20)
entry2.grid(row=0, column=1)

# 操作选择
operation_label = ttk.Label(root, text="选择操作：")
operation_label.pack(pady=5)
operation = ttk.Combobox(root, values=["加法", "除法"], state="readonly")
operation.set("加法")
operation.pack(pady=5)

# 计算按钮
btn = ttk.Button(root, text="🔢 开始计算", command=calculate, style="TButton")
btn.pack(pady=15)

# 结果标签
label_result = ttk.Label(root, text="", font=("微软雅黑", 12), background="#f5f5f5")
label_result.pack(pady=10)

# 运行主循环
root.mainloop()

# 结果显示
label_result = ttk.Label(root, text="📝 等待计算...", font=("微软雅黑", 12), background="#f5f5f5")
label_result.pack(pady=5)

# 启动
root.mainloop()