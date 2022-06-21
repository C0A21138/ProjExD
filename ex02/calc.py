import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk() # tkモジュールにあるTkのインスタンスを作成
root.title("calculator") # タイトルに"calculator"を表示
root.geometry("300x500") # 300x500のウィンドウを作成




root.mainloop() # ウィンドウを表示する


if __name__ == "__main__":
    r, c = 0, 0
    for num in range(9, -1, -1):
        btn = tk.Button(root,
                        text = f"{num}",
                        width = 4,
                        height = 2,
                        font = ("Times New Roman", 30)
                    )
