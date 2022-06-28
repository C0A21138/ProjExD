import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk() # tkモジュールにあるTkのインスタンスを作成
    
    root.title("迷えるこうかとん") # titleを"迷えるこうかとん"に設定
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")

    tori = tk.PhotoImage(file="fig/0.png") # figフォルダにある画像「0.png」を読み込み、インスタンスを生成
    cx, cy = 300, 400 # 横：300、縦：400の座標をそれぞれcx、cyに代入する。
    canvas.create_image(cx, cy, image=tori, tag="tori")

    key = ""

    canvas.pack()
    root.mainloop()
