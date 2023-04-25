import random
import math
import pygame as pg

import sys

def check_bound(scr_rect:pg.Rect,obj_rect:pg.Rect):
    """
    if obj in scr:
        return (x,y)
    x,y == True or False
    in -> True
    out -> False
    """
    x,y = False,False
    if scr_rect.top < obj_rect.top and scr_rect.bottom > obj_rect.bottom:
        y = True
    if scr_rect.left < obj_rect.left and scr_rect.right > obj_rect.right:
        x = True
    return (x,y) 

def main():
    width,height = 1600, 900
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((width, height))
    clock = pg.time.Clock()
    bg_img = pg.image.load("../ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("../ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rect = kk_img.get_rect()
    kk_rect.centerx,kk_rect.centery = 900,400
    tmr = 0

    key_list = {
            pg.K_UP:(0,-1),
            pg.K_DOWN:(0,1),
            pg.K_LEFT:(-1,0),
            pg.K_RIGHT:(1,0)
    }
    #print(pg.font.get_fonts())
    #char init
    font1 = pg.font.SysFont("liberationsansnarrow", 150)
    text1 = font1.render("GAME OVER", True, (255,0,0))
    draw_sfc = pg.Surface((20,20))
    pg.draw.circle(draw_sfc, ( 255,0,0), (10,10), 10)
    draw_sfc.set_colorkey((0,0,0))
    x,y = random.randint(0,width),random.randint(0,height)
    bb_pos = type("bb_pos",(),{"x":random.randint(0,width),"y":random.randint(0,height),"vx":1,"vy":1,"size":1})
    screen.blit(draw_sfc,[bb_pos.x,bb_pos.y])
    bb_rect = draw_sfc.get_rect()
    bb_rect.centerx,bb_rect.centery = x,y
    while True:
        screen.blit(bg_img, [0, 0])
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1
        #kk        
        kk_move_init = (kk_rect.centerx,kk_rect.centery)
        key_lst = pg.key.get_pressed()
        for v,item in key_list.items():
            if key_lst[v]:
                kk_rect.move_ip(item[0],item[1])
                if check_bound(screen.get_rect(),kk_rect) != (True,True):
                    kk_rect.move_ip(-item[0],-item[1])
        else:
            kk_move_touple = (kk_rect.centerx - kk_move_init[0],kk_rect.centery - kk_move_init[1])
            roted_kk_img = pg.transform.rotozoom(kk_img, math.degrees(math.asin(kk_move_touple[1]) ), 1.0)
            if kk_move_touple[0] == 1:
                roted_kk_img = pg.transform.flip(roted_kk_img,True,False)
            screen.blit(roted_kk_img, [kk_rect.left, kk_rect.top])            
        #bb
        bb_rect.move_ip(bb_pos.vx,bb_pos.vy)
        if check_bound(screen.get_rect(),bb_rect) == (False,True):
            bb_rect.move_ip(-bb_pos.vx,-bb_pos.vy)
            bb_pos.vx *= -1
        if check_bound(screen.get_rect(),bb_rect) == (True,False):
            bb_rect.move_ip(-bb_pos.vx,-bb_pos.vy)
            bb_pos.vy *= -1
        if check_bound(screen.get_rect(),bb_rect) == (False,False):
            bb_rect.move_ip(-bb_pos.vx,-bb_pos.vy)
            bb_pos.vx *= -1
            bb_pos.vy *= -1


        size = min((10+ tmr)/10+20 ,200)
        screen.blit(pg.transform.scale(draw_sfc,(size,size)),[bb_rect.x,bb_rect.y])
        pg.display.update()
        text1 = font1.render(f"{tmr}", True, (255,0,0))
        clock.tick(1000)


        #hit player bb
        if check_bound(kk_rect,bb_rect) == (True,True):
            screen.blit(text1,(screen.get_rect().centerx,screen.get_rect().centery))
            pg.display.update()
            clock.tick(0.5)

            return



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
