import tkinter.messagebox as tkm # tkinterモジュール内にあるmessageboxモジュールをtkmとして読み込む
from random import randint     # randomモジュール内にあるrandint関数を読み込む
import pygame as pg            # pygameモジュールをpgとして読み込む
import time
import sys                     # sysモジュールを読み込む


def main():
    count = 0

    clock = pg.time.Clock()                       # 時間計測用のオブジェクト
    pg.display.set_caption("逃げろ！こうかとん")  # タイトルバーに「逃げろ！こうかとん」を表示する
    screen_sfc = pg.display.set_mode((1600, 900)) # Surface
    screen_rect = screen_sfc.get_rect()           # Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")    # Surface
    bgimg_rect = bgimg_sfc.get_rect()             # Rect

    # Screen_sfc Surfaceにbgimg_sfc Surfaceを bgimg_rectに従って貼り付ける
    screen_sfc.blit(bgimg_sfc, bgimg_rect)

    toriimg_sfc = pg.image.load("fig/3.png")                  # Surface
    toriimg_sfc = pg.transform.rotozoom(toriimg_sfc, 0, 2.0)  # Surface
    toriimg_rect = toriimg_sfc.get_rect()                     # Rect
    
    # x座標900, y座標400の位置にこうかとんを表示する
    toriimg_rect.center = 900, 400

    bmimg_sfc = pg.Surface((20, 20)) # Surface
    bmimg_sfc.set_colorkey((0, 0, 0)) # 爆弾の背景を透明にする

    raimg_sfc = pg.Surface((250, 250)) #Surface
    raimg_sfc.set_colorkey((0, 0, 0)) # レーザーの背景を透明にする

    # レーザーを作成
    pg.draw.circle(raimg_sfc, (255, 0, 0), (10, 10), 500)

    # 爆弾を作成
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10)
    pg.draw.circle(bmimg_sfc, (191, 0, 0), (10, 10),  7)
    pg.draw.circle(bmimg_sfc, (127, 0, 0), (10, 10),  5)
    pg.draw.circle(bmimg_sfc, ( 63, 0, 0), (10, 10),  3)
    pg.draw.circle(bmimg_sfc, (  1, 0, 0), (10, 10),  1)

    #raimg_rect = raimg_sfc.get_rect() # Rect

    bmimg_rect = bmimg_sfc.get_rect() # Rect
    bmimg_rect.centerx = randint(0, screen_rect.width)  # 爆弾のx座標をランダムに設定する
    bmimg_rect.centery = randint(0, screen_rect.height) # 爆弾のy座標をランダムに設定する
    vx, vy = +1, +1


    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rect)      # 背景を表示する

        for event in pg.event.get():  # イベントを繰り返して処理
            if event.type == pg.QUIT: # ウィンドウのXボタンをクリックしたら
                return

        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP] == True:    # y座標を-1
            toriimg_rect.centery -= 1
        if key_states[pg.K_DOWN] == True:  # y座標を+1
            toriimg_rect.centery += 1
        if key_states[pg.K_LEFT] == True:  # x座標を-1
            toriimg_rect.centerx -= 1
        if key_states[pg.K_RIGHT] == True: # x座標を+1
            toriimg_rect.centerx += 1
        if check_bound(toriimg_rect, screen_rect) != (1, 1): # 領域外のとき
            if key_states[pg.K_UP] == True:    # y座標を+1
                toriimg_rect.centery += 1
            if key_states[pg.K_DOWN] == True:  # y座標を-1
                toriimg_rect.centery -= 1
            if key_states[pg.K_LEFT] == True:  # x座標を+1
                toriimg_rect.centerx += 1
            if key_states[pg.K_RIGHT] == True: # x座標を-1
                toriimg_rect.centerx -= 1

        screen_sfc.blit(toriimg_sfc, toriimg_rect)  # こうかとんを表示する

        bmimg_rect.move_ip(vx, vy) # x座標をvx, y座標をvy移動させる

        #screen_sfc.blit(raimg_sfc, raimg_rect)  # レーザーを表示する
        #raimg_rect.move_ip(+2, +2) # x座標をvx, y座標をvy移動させる

        screen_sfc.blit(bmimg_sfc, bmimg_rect)  # 爆弾を表示する

        yoko, tate = check_bound(bmimg_rect, screen_rect)
        vx *= yoko
        vy *= tate

        if toriimg_rect.colliderect(bmimg_rect): # こうかとんが爆弾に当たったとき
            return "GAME_OVER"
        #if toriimg_rect.colliderect(raimg_rect): # こうかとんが爆弾に当たったとき
            return "GAME_OVER"
        if count >= 20:
            return "CLEAR"

        # if bmimg_rect.colliderect(bmimg_rect): # 爆弾がこうかとんに当たったとき
        #     return

        font = pg.font.Font(None, 80)
        txt = font.render(str(f"Time:{int(count)}"), True, "BLACK")
        screen_sfc.blit(txt, (10, 10))

        count += 0.006 # 1000fpsを1秒に換算

        pg.display.update()  # 画面を更新する
        clock.tick(1000)     # 1000fpsの時を刻む


def check_bound(rect, screen_rect):
    # [1] rect: こうかとん or 爆弾のRect
    # [2] scr_rect: スクリーンのRect
    yoko, tate = +1, +1
    if rect.left < screen_rect.left or screen_rect.right < rect.right:
        yoko = -1
    if rect.top < screen_rect.top or screen_rect.bottom < rect.bottom:
        tate = -1
    return yoko, tate


if __name__ == "__main__":
    pg.init()
    check = main()
    if check == "CLEAR":
        tkm.showinfo("GAME CLEAR", "爆弾から逃げ切ることができました！")
    if check == "GAME_OVER":
        tkm.showinfo("GAME OVER", "爆弾に当たってしまいました…")
    pg.quit()
    sys.exit()