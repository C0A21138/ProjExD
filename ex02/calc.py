import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    # tkm.showinfo("", f"{num}のボタンを押しました")
    entry.insert(tk.END, num)

if __name__ == "__main__":
    root = tk.Tk() # tkモジュールにあるTkのインスタンスを作成
    root.title("calculator") # タイトルに"calculator"を表示
    # root.geometry("300x500") # 300x500のウィンドウを作成

    entry = tk.Entry(width = 10, font = ("Times New Roman", 40))
    entry.grid(row = 0, column = 0)

    r, c = 1, 0 # r：行番号 c：列番号
    for i, num in enumerate([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, "+"]):
        btn = tk.Button(root,
                        text = f"{num}",
                        width = 4,
                        height = 2,
                        font = ("Times New Roman", 30)
                    )
        btn.bind("<1>", button_click)
        btn.grid(row = r, column = c)

        c += 1

        if (i-1) % 3 == 0:
            r += 1
            c = 0

    root.mainloop() # ウィンドウを表示する
