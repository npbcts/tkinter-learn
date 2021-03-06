import tkinter as tk

window = tk.Tk()
window.title('my window')

# 窗口尺寸
window.geometry('500x300')

var1 = tk.StringVar()  # 创建变量
lb = tk.Label(window, bg='yellow', width=4, textvariable=var1)
lb.pack()


def print_selection():
    value = lb.get(lb.curselection())  # 获取当前选中的文本
    var1.set(value)  # 为label设置值


b1 = tk.Button(window,
               text='print selection',
               width=15,
               height=2,
               command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((11, 22, 33, 44))  # 为变量设置值

# 创建Listbox

lb = tk.Listbox(window, listvariable=var2)  # 将var2的值赋给Listbox

# 创建一个list并将值循环添加到Listbox控件中
list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert('end', item)  # 从最后一个位置开始加入值
lb.insert(1, 'first')  # 在第一个位置加入'first'字符
lb.insert(2, 'second')  # 在第二个位置加入'second'字符
lb.delete(2)  # 删除第二个位置的字符
lb.pack()


def del_lb():
    lb.delete(lb.curselection())


# 按钮删除选中的值
button_del_lb = tk.Button(
    window,
    text='del_lb',
    width=15,
    height=2,
    command=del_lb)
button_del_lb.pack()

# 显示主窗口
window.mainloop()
