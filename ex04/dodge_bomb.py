import pygame as pg
import sys

def main():
    clock = pg.time.Clock()

    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc = pg.display.set_mode((1600, 900)) # Surface
    screen_rect = screen_sfc.get_rect()           # Rect
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")    # Surface
    bgimg_rect = bgimg_sfc.get_rect()             # Rect
    screen_sfc.blit(bgimg_sfc, bgimg_rect)        # Screen_sfc Surfaceにbgimg_sfc Surfaceを bgimg_rectに従って貼り付ける
    
    #pg.display.update()
    clock.tick(0.5)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()