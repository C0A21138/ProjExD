import tkinter as tk

def key_down(event):
    global key
    key = event.keysym


def key_up(event):
    global key
    key = ""


def main_proc():
    global cx, cy
    if key == "Up": # 押されたキーが「Up」のとき
        cy -= 20 # 上に20移動する
        
    elif key == "Down":
        cy += 20

    elif key == "Left":
        cx -= 20

    elif key == "Right":
        cx += 20

    canvas.coords("tori", cx, cy)
    root.after(100, main_proc)

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
    root.bind("<KeyRelease>", key_up)

    main_proc() # 関数main_proc()を呼び出す

    root.mainloop() # ウィンドウを表示する
