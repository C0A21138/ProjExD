import tkinter as tk # tkinterモジュールをtkとして読み込む
import maze_maker as mm

def key_down(event):
    global key # グローバル宣言
    key = event.keysym # 押されたキーのシンボルkeysymをグローバル変数keyに代入する


def key_up(event):
    global key # グローバル宣言
    key = "" # グローバル変数keyに空文字""を代入


def main_proc():
    global cx, cy # グローバル宣言
    if key == "Up": # 押されたキーが「Up」のとき
        cy -= 20 # 上に20移動する
        
    elif key == "Down": # 押されたキーが「Down」のとき
        cy += 20 # 下に20移動する

    elif key == "Left": # 押されたキーが「Left」のとき
        cx -= 20 # 左に20移動する

    elif key == "Right": # 押されたキーが「Right」のとき
        cx += 20 # 右に20移動する

    canvas.coords("tori", cx, cy) # こうかとんの座標を更新する
    root.after(100, main_proc) # 100ミリ秒後に関数main_proc()を呼び出す

if __name__ == "__main__":
    root = tk.Tk() # tkモジュールにあるTkのインスタンスを作成

    root.title("迷えるこうかとん") # titleを"迷えるこうかとん"に設定
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack() # canvasを表示

    tori = tk.PhotoImage(file="fig/0.png") # figフォルダにある画像「0.png」を読み込み、インスタンスを生成
    cx, cy = 300, 400 # 横：300、縦：400の座標をそれぞれcx、cyに代入する。
    canvas.create_image(cx, cy, image=tori, tag="tori")

    key = ""
    root.bind("<KeyPress>", key_down) # キーが押されたとき、関数key_down()を呼び出す
    root.bind("<KeyRelease>", key_up) # キーが離されたとき、関数key_up()を呼び出す

    main_proc() # 関数main_proc()を呼び出す

    root.mainloop() # ウィンドウを表示する
