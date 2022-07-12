import sys              # sysモジュールを読み込む
import pygame as pg     # pygameモジュールをpgとして読み込む
from random import randint     # randomモジュール内にあるrandint関数を読み込む
import tkinter.messagebox as tkm # tkinterモジュール内にあるmessageboxモジュールをtkmとして読み込む


# Screen クラスを定義
class Screen:
    def __init__(self, title, wh, image):   # wh:幅高さタプル, image:背景画像ファイル名
        pg.display.set_caption(title)       # タイトルバーにtitleを表示
        self.sfc = pg.display.set_mode(wh)      # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.bgi_sfc = pg.image.load(image)     # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()  # Rect  

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct) 


class Bird:
    def __init__(self, image, size, xy):    # image:画像ファイル名, size:拡大率, xy:初期座標タプル
        self.sfc = pg.image.load(image)                        # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)    # Surface
        self.rct = self.sfc.get_rect()                         # Rect
        self.rct.center = xy    # こうかとんを表示する座標をxyに設定
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]:
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]:
            self.rct.centery += 1
        if key_states[pg.K_LEFT]:
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]:
            self.rct.centerx += 1
        # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]:
                self.rct.centery += 1
            if key_states[pg.K_DOWN]:
                self.rct.centery -= 1
            if key_states[pg.K_LEFT]:
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 1
        self.blit(scr)


class Bomb:
    def __init__(self, color, size, vxy, scr: Screen):       # color:色タプル、size:半径
        self.sfc = pg.Surface((2*size, 2*size))              # Surface
        self.sfc.set_colorkey((0, 0, 0))                     # 爆弾の背景を透明にする
        pg.draw.circle(self.sfc, color, (size, size), size)  # 爆弾を作成
        self.rct = self.sfc.get_rect()                       # Rect
        self.rct.centerx = randint(0, scr.rct.width)         # 爆弾のx座標をランダムに設定する
        self.rct.centery = randint(0, scr.rct.height)        # 爆弾のy座標をランダムに設定する
        self.vx, self.vy = vxy # 練習6
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr: Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        # 練習5
        self.blit(scr)


# main 関数を定義
def main():
    clock = pg.time.Clock()     # 時間計測用のオブジェクト
    HP = 100
    time_count = 0
    damage_count = 0
    tori = "fig/3.png"
    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    kkt = Bird(tori, 2.0, (900, 400))
    bkd1 = Bomb((255, 0, 0), 50, (+2, +2), scr)
    bkd2 = Bomb((255, 0, 0), 40, (+2, +4), scr)
    bkd3 = Bomb((255, 0, 0), 30, (+2, +7), scr)
    bkd4 = Bomb((255, 0, 0), 20, (+6, +5), scr)
    bkd5 = Bomb((255, 0, 0), 10, (+8, +3), scr)

    while True:
        scr.blit()
        Score = time_count*100 - damage_count*5

        if Score <= 500:
            time_count = int(pg.time.get_ticks()/1000)

        # 練習2
        for event in pg.event.get():  # イベントを繰り返して処理
            if event.type == pg.QUIT: # ウィンドウのXボタンをクリックしたら
                return                # 終了

        kkt.update(scr)
        bkd1.update(scr)
        bkd2.update(scr)
        bkd3.update(scr)
        bkd4.update(scr)
        bkd5.update(scr)
        if kkt.rct.colliderect(bkd1.rct) or kkt.rct.colliderect(bkd2.rct) or kkt.rct.colliderect(bkd3.rct) or kkt.rct.colliderect(bkd4.rct) or kkt.rct.colliderect(bkd5.rct): # こうかとんが爆弾に当たったとき
            Damage(scr.sfc, 0.5)
            damage_count += 1
            HP -= 1
        
        if HP <= 0:
            HP = 0
            bkd1 = Bomb((255, 0, 0), 0, (+2, +2), scr)
            bkd2 = Bomb((255, 0, 0), 0, (+2, +4), scr)
            bkd3 = Bomb((255, 0, 0), 0, (+2, +7), scr)
            bkd4 = Bomb((255, 0, 0), 0, (+6, +5), scr)
            bkd5 = Bomb((255, 0, 0), 0, (+8, +3), scr)
            bkd1.update(scr)
            bkd2.update(scr)
            bkd3.update(scr)
            bkd4.update(scr)
            bkd5.update(scr)
            tori = "fig/6.png"
            kkt = Bird(tori, 2.0, (800, 400))
            success_txt = font.render(("GAME CLEAR"), True, "BLACK")
            scr.sfc.blit(success_txt, (610, 400))
            return "LOSER"

        if Score >= 500:
            bkd1 = Bomb((255, 0, 0), 0, (+2, +2), scr)
            bkd2 = Bomb((255, 0, 0), 0, (+2, +4), scr)
            bkd3 = Bomb((255, 0, 0), 0, (+2, +7), scr)
            bkd4 = Bomb((255, 0, 0), 0, (+6, +5), scr)
            bkd5 = Bomb((255, 0, 0), 0, (+8, +3), scr)
            bkd1.update(scr)
            bkd2.update(scr)
            bkd3.update(scr)
            bkd4.update(scr)
            bkd5.update(scr)
            tori = "fig/6.png"
            kkt = Bird(tori, 2.0, (800, 400))
            success_txt = font.render(("GAME CLEAR"), True, "BLACK")
            scr.sfc.blit(success_txt, (610, 400))
        
        font = pg.font.Font(None, 80)
        txt = font.render(str(f"Time:{(str(time_count))}"), True, "BLACK")
        scr.sfc.blit(txt, (10, 10))

        txt2 = font.render(str(f"HP:{int(HP)}"), True, "BLACK")
        scr.sfc.blit(txt2, (600, 10))

        txt3 = font.render(str(f"Score:{int(Score)}"), True, "BLACK")
        scr.sfc.blit(txt3, (1200, 10))

        pg.display.update()   # 画面を更新する
        clock.tick(1000)      # 1000fpsの時を刻む


def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate


def Damage(surface, scale):
    GB = min(255, max(0, round(255 * (1-scale))))
    surface.fill((255, GB, GB), special_flags = pg.BLEND_MULT)


if __name__ == "__main__":
    pg.init()
    check = main()
    if check == "LOSER":
        tkm.showinfo("LOSER", "負けてしまいました…")
    pg.quit()
    sys.exit()