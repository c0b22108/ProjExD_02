import random
import pygame as pg

import sys

def main():
    width,height = 1600, 900
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((width, height))
    clock = pg.time.Clock()
    bg_img = pg.image.load("../ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("../ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    tmr = 0

  
    draw_sfc = pg.Surface((20,20))
    pg.draw.circle(draw_sfc, ( 255,0,0), (10,10), 10)
    draw_sfc.set_colorkey((0,0,0))
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        
        screen.blit(draw_sfc,[random.randint(0,width),random.randint(0,height)])

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
