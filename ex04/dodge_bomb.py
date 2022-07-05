import pygame as pg
import sys

def main():
    clock = pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
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


    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rect)      # 背景
        screen_sfc.blit(toriimg_sfc, toriimg_rect)  # こうかとん

        for event in pg.event.get():  # イベントを繰り返して処理
            if event.type == pg.QUIT: # ウィンドウのXボタンをクリックしたら
                return
            
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()