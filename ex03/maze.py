import tkinter as tk

def key_down(event):
    global key_down
    key = event.keysym

def key_up(event):
    global key
    key = ""

if __name__ == "__main__":
    root = tk.Tk() # tkモジュールにあるTkのインスタンスを作成
    
    root.title("迷えるこうかとん") # titleを"迷えるこうかとん"に設定
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    tori = tk.PhotoImage(file="fig/0.png") # figフォルダにある画像「0.png」を読み込み、インスタンスを生成
    cx, cy = 300, 400 # 横：300、縦：400の座標をそれぞれcx、cyに代入する。
    canvas.create_image(cx, cy, image=tori, tag="tori")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_down)

    root.mainloop()
