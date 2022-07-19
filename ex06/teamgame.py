import sys              # sysモジュールを読み込む
import pygame as pg     # pygameモジュールをpgとして読み込む
from random import randint     # randomモジュール内にあるrandint関数を読み込む


bar_num = 5  # 落ちてくる障害物の最大数
HP = 500     # 体力の設定
time = 0     # timeを0で初期化
score = 0    # scoreを0で初期化


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


# Player クラスを定義
class Player:
    def __init__(self, image, size, xy):    # image:画像ファイル名, size:拡大率, xy:初期座標タプル
        self.sfc = pg.image.load(image)                        # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)    # Surface
        self.rct = self.sfc.get_rect()                         # Rect
        self.rct.center = xy    # こうかとんを表示する座標をxyに設定
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_LEFT]:
            self.rct.centerx -= 2.0
        if key_states[pg.K_RIGHT]:
            self.rct.centerx += 2.0
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_LEFT]:
                self.rct.centerx += 2.0
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 2.0
        self.blit(scr)

    # 移動するキャラクターがビームを打つメソッド
    def atack(self, scr: Screen):
        key_states = pg.key.get_pressed()
        
        if key_states[pg.K_SPACE]:
            pass


class Bar:
    def __init__(self, size, color, scr: Screen):
        self.sfc = pg.Surface(size)
        pg.Surface.fill(self.sfc, color)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width-self.rct.width)
        self.rct.centery = -randint(0, 500)
        self.w, self.h = size
        self.rct.width = randint(8, self.w)
        self.vy  = 2.5
    
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)
        
    def update(self, scr: Screen):
        self.rct.move_ip(0, self.vy)
        if self.rct.centery > scr.rct.height:
            self.rct.centerx = randint(0, scr.rct.width-self.rct.width)
            self.rct.centery = -randint(0, 500)
            self.rct.width = randint(80, self.w)
        scr.sfc.blit(self.sfc, self.rct)


def check_bound(rct, scr_rct):
    
    # [1] rct: こうかとん or 爆弾のRect
    # [2] scr_rct: スクリーンのRect

    yoko, tate = 1, 1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right:
        yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom:
        tate = -1 # 領域外
    return yoko, tate


def Damage(surface, scale):
    GB = min(255, max(0, round(255 * (1-scale))))
    surface.fill((255, GB, GB), special_flags = pg.BLEND_MULT)


def main():
    global HP, time, score
    clock = pg.time.Clock()  # 時間計測用のオブジェクト
    screen = Screen("", (700, 900), "fig/pg_bg.jpg")
    screen.blit()

    player = Player("fig/5.png", 1.5, (350, 848))

    bars = [0 for i in range(bar_num)] # 障害物の最大数
    for i in range(bar_num): # 障害物の最大数だけ処理を繰り返す
        bars[i] = Bar((120, 30), (0,0,0), screen) # barを作成し、barリストに格納する
        bars[i].blit(screen) # barsリスト内のbarをscreenに表示する

    while True:
        screen.blit() # screenを表示する
        score = time*500 # scoreの計算式

        if HP != 0: # HPが0ではない間
            time = int(pg.time.get_ticks()/1000) # 時間を計測する

        for event in pg.event.get():
            if event.type == pg.QUIT: # ウィンドウのXボタンが押されたとき
                return # 終了
        
        player.update(screen) # こうかとんを更新する

        for bar in bars:
            bar.update(screen) # barを更新する
        
            if player.rct.colliderect(bar.rct): # こうかとんがbarに当たっているとき
                Damage(screen.sfc, 0.5) # 画面を赤く変化させる
                HP -= 1 # HPが1ずつ減少
        
        if HP <= 0:
            HP = 0
            player = Player("fig/8.png", 1.5, (350, 390)) # 画面の真ん中にこうかとんを移動させ、固定する
            over_txt = font.render(("GAME OVER"), True, "BLACK") # GAME OVERテキストの設定
            screen.sfc.blit(over_txt, (170, 450)) # 画面の真ん中にGAME OVERを表示する
            bars.clear() # 全てのbarを削除
     
        font = pg.font.Font(None, 80) # fontの設定
        txt1 = font.render(str(f"Time:{(str(time))}"), True, "BLACK") # 経過時間表示テキストの設定
        screen.sfc.blit(txt1, (10, 10)) # txt1を表示

        txt2 = font.render(str(f"HP:{int(HP)}"), True, "BLACK") # HP表示テキストの設定
        screen.sfc.blit(txt2, (500, 10)) # txt2を表示

        txt3 = font.render(str(f"Score:{int(score)}"), True, "BLACK") # スコア表示テキストの設定
        screen.sfc.blit(txt3, (10, 80)) # txt3を表示

        pg.display.update()   # 画面を更新する
        clock.tick(1000)      # 1000fpsの時を刻む


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()