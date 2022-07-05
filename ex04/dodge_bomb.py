from random import randint     # randomモジュール内にあるrandint関数を読み込む
import pygame as pg            # pygameモジュールをpgとして読み込む
import sys                     # sysモジュールを読み込む

def main():
    clock = pg.time.Clock()                       # 時間計測用のオブジェクト
    pg.display.set_caption("逃げろ！こうかとん")  # タイトルバーに「逃げろ！こうかとん」を表示する
    screen_sfc = pg.display.set_mode((1600, 900)) # Surface
    screen_rect = screen_sfc.get_rect()           # Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")    # Surface
    bgimg_rect = bgimg_sfc.get_rect()             # Rect

    # Screen_sfc Surfaceにbgimg_sfc Surfaceを bgimg_rectに従って貼り付ける
    screen_sfc.blit(bgimg_sfc, bgimg_rect)

    toriimg_sfc = pg.image.load("fig/6.png")                  # Surface
    toriimg_sfc = pg.transform.rotozoom(toriimg_sfc, 0, 2.0)  # Surface
    toriimg_rect = toriimg_sfc.get_rect()                     # Rect
    
    # x座標900, y座標400の位置にこうかとんを表示する
    toriimg_rect.center = 900, 400

    bmimg_sfc = pg.Surface((20, 20)) # Surface
    bmimg_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10) # 爆弾を作成
    bmimg_rect = bmimg_sfc.get_rect() # Rect
    bmimg_rect.centerx = randint(0, screen_rect.width)
    bmimg_rect.centery = randint(0, screen_rect.height)
    vx, vy = +1, +1


    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rect)      # 背景を表示する

        for event in pg.event.get():  # イベントを繰り返して処理
            if event.type == pg.QUIT: # ウィンドウのXボタンをクリックしたら
                return

        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP] == True: # y座標を-1
            toriimg_rect.centery -= 1
        if key_states[pg.K_DOWN] == True: # y座標を+1
            toriimg_rect.centery += 1
        if key_states[pg.K_LEFT] == True: # x座標を-1
            toriimg_rect.centerx -= 1
        if key_states[pg.K_RIGHT] == True: # x座標を+1
            toriimg_rect.centerx += 1
        screen_sfc.blit(toriimg_sfc, toriimg_rect)  # こうかとんを表示する

        bmimg_rect.move_ip(vx, vy) # x座標をvx, y座標をvy移動させる

        screen_sfc.blit(bmimg_sfc, bmimg_rect)  # 爆弾を表示する

        pg.display.update()  # 画面を更新する
        clock.tick(1000)     # 1000fpsの時を刻む


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()