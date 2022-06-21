import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        eqn = entry.get()
        res = eval(eqn)
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)

    elif num == "TEL":
        eqn = entry.get()
        if eqn == "":
            tkm.showerror("Error", "何も入力されていません")
        elif eqn == "110":
            tkm.showwarning("警告", "警察に電話を掛けます")
            tkm.showwarning("警告", "いたずら電話はやめましょう。")
        elif eqn == "123-4567-8910":
            tkm.showwarning("警告", f"{eqn}に電話を掛けます")
            for i in range(5):
                tkm.showwarning("警告", "あなたは呪われました。")
        else:
            tkm.showwarning("警告", f"{eqn}に電話を掛けます")
            tkm.showerror("Error", "繋がりませんでした。")
        entry.delete(0, tk.END)
        entry.insert(tk.END, res)

    elif num == "DEL":
        entry.delete(0, tk.END)

    else:
        # tkm.showinfo("", f"{num}のボタンを押しました")
        entry.insert(tk.END, num)

if __name__ == "__main__":
    root = tk.Tk() # tkモジュールにあるTkのインスタンスを作成
    root.title("calculator") # タイトルに"calculator"を表示
    # root.geometry("300x500") # 300x500のウィンドウを作成

    entry = tk.Entry(width = 10, font = ("Times New Roman", 40))
    entry.grid(row = 0, column = 0, columnspan = 3)

    r, c = 1, 0 # r：行番号 c：列番号
    for i, num in enumerate([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, "+", "=", "-", "TEL", "DEL"]):
        btn = tk.Button(root,
                        text = f"{num}",
                        width = 4,
                        height = 2,
                        font = ("Times New Roman", 30)
                        )
        btn.bind("<1>", button_click)
        btn.grid(row = r, column = c)

        c += 1

        if (i+1)%3 == 0:
            r += 1
            c = 0

    root.mainloop() # ウィンドウを表示する
