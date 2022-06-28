import tkinter as tk # tkinterモジュールをtkとして読み込む
import maze_maker as mm # maze_makerモジュールをmmとして読み込む

def key_down(event): # キーが押された時に処理を行う関数を定義
    global key # グローバル宣言
    key = event.keysym # 押されたキーのシンボルkeysymをグローバル変数keyに代入する


def key_up(event): # キーが離された時に処理を行う関数を定義
    global key # グローバル宣言
    key = "" # グローバル変数keyに空文字""を代入


def main_proc():
    global cx, cy, mx, my # グローバル宣言
    if key == "Up" and maze_bg[my-1][mx] == 0: # 押されたキーが「Up」 かつ　移動先が床のとき
        my -= 1 # 上に1マス移動する
        
    elif key == "Down" and maze_bg[my+1][mx] == 0: # 押されたキーが「Down」 かつ　移動先が床のとき
        my += 1 # 下に1マス移動する

    elif key == "Left" and maze_bg[my][mx-1] == 0: # 押されたキーが「Left」 かつ　移動先が床のとき
        mx -= 1 # 左に1マス移動する

    elif key == "Right" and maze_bg[my][mx+1] == 0: # 押されたキーが「Right」 かつ　移動先が床のとき
        mx += 1 # 右に1マス移動する

    cx, cy = mx*100+50, my*100+50 # 移動幅を1マスに設定
    canvas.coords("tori", cx, cy) # こうかとんの座標を更新する
    root.after(100, main_proc) # 100ミリ秒後に関数main_proc()を呼び出す

if __name__ == "__main__":
    root = tk.Tk() # tkモジュールにあるTkのインスタンスを作成

    root.title("迷えるこうかとん") # titleを"迷えるこうかとん"に設定
    canvas = tk.Canvas(root, width=1500, height=900, bg="black") # 幅1500、高さ900、背景色"black"のcanvasを作成
    canvas.pack() # canvasを表示

    maze_bg = mm.make_maze(15, 9) # 1：壁 / 0：床を表す二次元リスト
                                  # 横：15、縦：9
    mm.show_maze(canvas, maze_bg) # canvasにmaze_bgを描く

    tori = tk.PhotoImage(file="fig/0.png") # figフォルダにある画像「0.png」を読み込み、インスタンスを生成
    mx, my = 1, 1 # 変数mx、myをそれぞれ1で初期化
    cx, cy = mx*100+50, my*100+50 # 横：150、縦：150の座標をそれぞれcx、cyに代入する。
    canvas.create_image(cx, cy, image=tori, tag="tori") # 画像を表示

    key = "" # 変数keyを空文字""で初期化
    root.bind("<KeyPress>", key_down) # キーが押されたとき、関数key_down()を呼び出す
    root.bind("<KeyRelease>", key_up) # キーが離されたとき、関数key_up()を呼び出す

    main_proc() # 関数main_proc()を呼び出す

    root.mainloop() # ウィンドウを表示する
