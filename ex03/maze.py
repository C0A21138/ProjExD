import tkinter as tk # tkinterモジュールをtkとして読み込む
import maze_maker as mm # maze_makerモジュールをmmとして読み込む
import tkinter.messagebox as tkm # tkinterモジュール内にあるmessageboxモジュールをtkmとして読み込む
from random import randint # randomモジュール内にある関数randintを読み込む

def key_down(event): # キーが押された時に処理を行う関数を定義
    global key # グローバル宣言
    key = event.keysym # 押されたキーのシンボルkeysymをグローバル変数keyに代入する


def key_up(event): # キーが離された時に処理を行う関数を定義
    global key # グローバル宣言
    key = "" # グローバル変数keyに空文字""を代入


def main_proc():
    global cx, cy, mx, my, count # グローバル宣言
    if key == "Up" and maze_bg[my-1][mx] == 0: # 押されたキーが「Up」 かつ　移動先が床のとき
        my -= 1 # 上に1マス移動する
        count += 1 # 移動回数を1増やす
        
    elif key == "Down" and maze_bg[my+1][mx] == 0: # 押されたキーが「Down」 かつ　移動先が床のとき
        my += 1 # 下に1マス移動する
        count += 1 # 移動回数を1増やす

    elif key == "Left" and maze_bg[my][mx-1] == 0: # 押されたキーが「Left」 かつ　移動先が床のとき
        mx -= 1 # 左に1マス移動する
        count += 1 # 移動回数を1増やす

    elif key == "Right" and maze_bg[my][mx+1] == 0: # 押されたキーが「Right」 かつ　移動先が床のとき
        mx += 1 # 右に1マス移動する
        count += 1 # 移動回数を1増やす
    
    elif count == 50: # 移動回数が50回になったとき
        tkm.showerror("脱出失敗", "脱出に失敗しました…") # タイトルが脱出失敗のウインドウ内に"脱出に失敗しました…"を表示
        quit() # ゲーム終了(プログラムを終了)

    entry.delete(0, tk.END)
    entry.insert(tk.END, count)
    cx, cy = mx*100+50, my*100+50 # 移動幅を1マスに設定
    canvas.coords("tori", cx, cy) # こうかとんの座標を更新する
    root.after(100, main_proc) # 100ミリ秒後に関数main_proc()を呼び出す

    if mx == g_x and my == g_y:
        mx, my = cx, cy
        tkm.showinfo("脱出成功", "脱出に成功しました！") # タイトルが脱出成功のウインドウ内に"脱出に成功しました！"を表示
        quit() # ゲーム終了(プログラムを終了)

if __name__ == "__main__":
    maze_x = 15 # 横：15
    maze_y = 9 # 縦：9

    root = tk.Tk() # tkモジュールにあるTkのインスタンスを作成

    count = 0 # 移動回数を0で初期化

    entry = tk.Entry(root, width = 100, text = count, font = ("Times New Roman", 40)) # 上に移動回数を表示するentryを表示
    entry.pack() # entryを表示する

    root.title("迷えるこうかとん") # titleを"迷えるこうかとん"に設定
    canvas = tk.Canvas(root, width=1500, height=900, bg="black") # 幅1500、高さ900、背景色"black"のcanvasを作成
    canvas.pack() # canvasを表示

    maze_bg = mm.make_maze(maze_x, maze_y) # 1：壁 / 0：床を表す二次元リスト
    mm.show_maze(canvas, maze_bg) # canvasにmaze_bgを描く

    canvas.create_rectangle(100, 100, 200, 200, fill = "lightgreen") # スタート地点の色を"lightgreen"に変更

    g_x = randint(1, maze_x) # ゴール地点のx座標をランダムに設定
    g_y = randint(1, maze_y) # ゴール地点のy座標をランダムに設定
    while maze_bg[g_y][g_x] != 0 or (g_x == 1 and g_y == 1): # ランダムに設定した座標先が床じゃない、または、スタート地点の場合
        # 再度ゴール地点の座標を設定
        g_x = randint(1, maze_x-1)
        g_y = randint(1, maze_y-1)
    canvas.create_rectangle(g_x*100, g_y*100, g_x*100+100, g_y*100+100, fill = "yellow") # ゴール地点の色を"yellow"に設定し作成

    tori = tk.PhotoImage(file="fig/0.png") # figフォルダにある画像「0.png」を読み込み、インスタンスを生成
    mx, my = 1, 1 # 変数mx、myをそれぞれ1で初期化
    cx, cy = mx*100+50, my*100+50 # 横：150、縦：150の座標をそれぞれcx、cyに代入する。
    canvas.create_image(cx, cy, image=tori, tag="tori") # 画像を表示

    key = "" # 変数keyを空文字""で初期化
    root.bind("<KeyPress>", key_down) # キーが押されたとき、関数key_down()を呼び出す
    root.bind("<KeyRelease>", key_up) # キーが離されたとき、関数key_up()を呼び出す

    main_proc() # 関数main_proc()を呼び出す

    root.mainloop() # ウィンドウを表示する
