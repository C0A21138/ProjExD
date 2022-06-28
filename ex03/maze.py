import tkinter as tk # tkinterモジュールをtkとして読み込む
import maze_maker as mm # maze_makerモジュールをmmとして読み込む

def key_down(event): # キーが押された時に処理を行う関数を定義
    global key # グローバル宣言
    key = event.keysym # 押されたキーのシンボルkeysymをグローバル変数keyに代入する


def key_up(event): # キーが離された時に処理を行う関数を定義
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

    maze_bg = mm.make_maze(15, 9) # 1：壁 / 0：床を表す二次元リスト
    mm.show_maze(canvas, maze_bg) # canvasにmaze_bgを描く
    print(maze_bg)

    tori = tk.PhotoImage(file="fig/0.png") # figフォルダにある画像「0.png」を読み込み、インスタンスを生成
    cx, cy = 300, 400 # 横：300、縦：400の座標をそれぞれcx、cyに代入する。
    canvas.create_image(cx, cy, image=tori, tag="tori")

    key = ""
    root.bind("<KeyPress>", key_down) # キーが押されたとき、関数key_down()を呼び出す
    root.bind("<KeyRelease>", key_up) # キーが離されたとき、関数key_up()を呼び出す

    main_proc() # 関数main_proc()を呼び出す

    root.mainloop() # ウィンドウを表示する
