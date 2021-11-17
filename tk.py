#!/usr/bin/python3

import tkinter as tk
import random
from PIL import Image, ImageTk

idiom = [
    '世上任何生命都不是尽善尽美的',
    '让我们怀着善良的心去做成人之美之事',
    '心存大爱，则无可阻之道',
    '心存美好，则无可恼之事',
    '做人无德不足以立身',
    '微笑可以减轻紧张的情绪和压力',
    '退一步，海阔天空',
    '心存善良，则无可恨之人',
    '人生的最佳状态是淡定从容',
    '以责人之心责己，以恕己之心恕人',
    '一个人的涵养，来自一颗包容的心',
    '善良是心湖绽放柔媚的花朵',
    '努力是一种生活态度，与年龄无关',
    '不为困苦所屈服',
    '人生因有梦想而充满动力',
    '坚持，是生命的一种毅力',
    '努力是一种生活态度，与年龄无关'
]


def create_win(title=None, width=None, height=None):
    __main_win = tk.Tk()
    if title:
        __main_win.title('新的标题')
    if width and height:
        __main_win.geometry('%dx%d' % (width, height))
    __main_win.resizable(width=False, height=False)
    return __main_win


def create_label(win, text, width, height, click, is_image=False):
    if is_image:
        __label = tk.Label(win, image=text, width=width, height=height)
    else:
        __label = tk.Label(win, text=text, width=width, height=height)
    if click:
        __label.bind('<Button-1>', lambda event: click(__label))
    __label.pack(side=tk.LEFT)
    return __label


def get_text(index=None):
    if index:
        return idiom[index]
    return idiom[random.randint(0, len(idiom) - 1)]


def label_click_handle(label):
    print(label)
    label['text'] = get_text(None)
    print(get_text(None))


def create_button(win, text, click):
    return tk.Button(win, text=text, command=lambda: click(win, text))


def button_click_handle(win, text):
    win.title(text)


def create_radio(win, texts, choose):
    var = tk.IntVar()
    for i in range(len(texts)):
        box_ = tk.Radiobutton(win, text=texts[i], variable=var, value=i, command=lambda: choose(win, var, texts))
        box_.pack()


def radio_click_handle(win, radio, texts):
    win.title(texts[radio.get()])


def create_check(win, texts, choose):
    var_list = []
    for i in range(len(texts)):
        var_list.append(tk.IntVar())
    for i in range(len(texts)):
        check = tk.Checkbutton(win, text=texts[i], variable=var_list[i], onvalue=1, offvalue=0,
                               command=lambda: choose(win, texts, var_list))
        check.pack()


def check_choose_handle(win, texts, var_list):
    choose_check = []
    for i in range(len(texts)):
        if var_list[i].get() == 1:
            choose_check.append(texts[i])
    win.title(' '.join(choose_check))


class Calculator(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.create_widget()
        self.pack()

    def create_widget(self):
        self.input = tk.Label(self, text='请输入：')
        self.input.grid(row=0)
        self.entry = tk.Entry(self)
        self.entry.grid(row=0, column=1)
        self.result = tk.Label(self, text='结果')
        self.result.grid(row=2, column=0)
        self.re = tk.Label(self, text='输出结果的位置')
        self.re.grid(row=2, column=1)
        self.calc_button = tk.Button(self)
        self.calc_button.grid(row=3, column=1)
        self.calc_button['text'] = '计算'
        self.calc_button['fg'] = 'red'
        self.calc_button['command'] = self.calc

    def calc(self):
        input_str = self.entry.get()
        __input_str = eval(str(input_str).replace('^', '**'))
        __input_str = str(__input_str)
        __input_str = input_str + '=' + __input_str
        self.re['text'] = __input_str
        self.entry.delete(0, tk.END)


def multiplication(win):
    for i in range(1, 10):
        for j in range(1, i+1):
            label = tk.Label(win, text='%dx%d=%d' % (j, i, i*j))
            label.grid(row=i-1, column=j-1)



if __name__ == '__main__':
    main_win = create_win('新的标题', 640, 1080)
    # img = ImageTk.PhotoImage(Image.open('/Users/liuhuiliang/img/splash1.jpeg'))
    # create_label(main_win, img, 640, 1080, None, True)
    # create_label(main_win, get_text(1), 380, 60, label_click_handle)
    # button1 = create_button(main_win, '按钮1', button_click_handle)
    # button1.grid(row=0, column=0)
    # button2 = create_button(main_win, '按钮2', button_click_handle)
    # button2.grid(row=0, column=1)
    # create_radio(main_win, ['text1', 'text2', 'text3'], radio_click_handle)
    # create_check(main_win, ['text1', 'text2', 'text3'], check_choose_handle)
    # app = Calculator(main_win)
    multiplication(main_win)
    main_win.mainloop()
