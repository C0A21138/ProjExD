import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num == "=":
        eqn = entry.get() # 入力された数字、数式の文字列全体を変数eqnに格納する。
        res = eval(eqn)
        entry.delete(0, tk.END) # 入力された数字、数式の文字列全体を削除する。
        entry.insert(tk.END, res) # 演算結果を上に表示する。

    elif num == "TEL":
        eqn = entry.get()
        if eqn == "": # 何も入力されていない場合
            tkm.showerror("Error", "何も入力されていません") # エラー、文字列"何も入力されていません"を表示
        elif eqn == "110": # "110"が入力されている場合
            tkm.showwarning("警告", "警察に電話を掛けます")
            tkm.showwarning("警告", "いたずら電話はやめましょう。")
        elif eqn == "123-4567-8910":  # "123-4567-8910"が入力されている場合
            tkm.showwarning("警告", f"{eqn}に電話を掛けます") # 警告、"[入力されている数字列]に電話を掛けます"を表示
            for i in range(5): # 5回繰り返す
                tkm.showwarning("警告", "あなたは呪われました。") # 警告、"あなたは呪われました。"を表示
        else:
            tkm.showwarning("警告", f"{eqn}に電話を掛けます") # 警告、"[入力されている数字列]に電話を掛けます"を表示
            tkm.showerror("Error", "繋がりませんでした。")
        entry.delete(0, tk.END) # 入力された数字、数式の文字列全体を削除する。

    elif num == "DEL":
        entry.delete(0, tk.END) # 入力された数字、数式の文字列全体を削除する。

    else:
        # tkm.showinfo("", f"{num}のボタンを押しました")
        entry.insert(tk.END, num)

if __name__ == "__main__":
    root = tk.Tk() # tkモジュールにあるTkのインスタンスを作成
    root.title("calculator") # タイトルに"calculator"を表示
    # root.geometry("300x500") # 300x500のウィンドウを作成
                               # （設定しない場合は、自動的に全てのウィジェットが表示されるサイズに設定される）

    entry = tk.Entry(width = 10, font = ("Times New Roman", 40)) # 幅 10、fontを"Times New Roman"、fontサイズを40に設定。
    entry.grid(row = 0, column = 0, columnspan = 3) # 横方向に3マス結合

    r, c = 1, 0 # r：行番号 c：列番号
    for i, num in enumerate([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, "+", "=", "-", "TEL", "DEL"]): # 変数i, numにボタンの文字の数字や文字列を格納する。
        btn = tk.Button(root,
                        text = f"{num}",
                        width = 4,  # 幅 4
                        height = 2, # 高さ 2
                        font = ("Times New Roman", 30) # fontを"Times New Roman"、fontサイズを30に設定。
                        )
        btn.bind("<1>", button_click)
        btn.grid(row = r, column = c)

        c += 1

        if (i+1)%3 == 0:
            r += 1
            c = 0

    root.mainloop() # ウィンドウを表示する
