from pygame import *
 
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height

        # картинка стіни - прямокутник потрібних розмірів і кольору
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
# кожен спрайт має зберігати властивість rect - прямокутник
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Object(sprite.Sprite):
    def __init__(self,player_image,x,y,w,h,speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

    
    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 100: #vlivo2
            self.rect.x -= self.speed
            for w in walls:
                if sprite.collide_rect(chuvak2,w):
                    self.rect.x += self.speed
        if keys[K_UP] and self.rect.y >0:  #vgoru2
            self.rect.y -= self.speed
            for w in walls:
                if sprite.collide_rect(chuvak2,w):
                    self.rect.y += self.speed
        if keys[K_RIGHT] and self.rect.x < 650: #vpravo2
            self.rect.x += self.speed
            for w in walls:
                if sprite.collide_rect(chuvak2,w):
                    self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.y <550:  #vnyz2
            self.rect.y += self.speed
            for w in walls:
                if sprite.collide_rect(chuvak2,w):
                    self.rect.y -= self.speed

    direction = 'right'
    def move2(self):
        if self.rect.x > 300:
            self.direction = 'left'
        if self.rect.x < 100:
            self.direction = 'right'

        if self.direction == 'right':
            self.rect.x += 4
        else:
            self.rect.x -= 4
    
    direction2 = 'down'
    def move3(self):
        if self.rect.y > 250:
            self.direction2 = 'up'
        if self.rect.y < 10:
            self.direction2 = 'down'

        if self.direction2 == 'up':
            self.rect.y -= 4
        else:
            self.rect.y += 4

    def fire(self):
        bullet = Bullet('bullleeett-removebg-preview.png',self.rect.centerx,self.rect.centery,15,15,10)
        bullets.add(bullet)
    
    def fire2(self):
        bullet = Bullet2('bullleeett--removebg-preview.png',self.rect.centerx,self.rect.centery,15,15,10)
        bullets2.add(bullet)

class Bullet(Object):
    def update(self):
        self.rect.y += 10
        if self.rect.y > 1000:
            self.kill()
bullets = sprite.Group()

class Bullet2(Object):
    def update(self):
        self.rect.y -= 10
        if self.rect.y > 1000:
            self.kill()
bullets2 = sprite.Group()
settings = display.set_mode((400,400))
menu = display.set_mode((400,400))
display.set_caption("Лабіринт")

#knopky
start_btn = Rect(50,100,100,50)
exit_btn = Rect(250,100,100,50)
settings_btn = Rect(250,300,100,50)
changetheme_btn = Rect(50,100,100,50)

font.init()
menu_font = font.Font(None, 20)
settings_font = font.Font(None, 20)

menug = True
settingss = False
while menug:
    for e in event.get():
        if e.type == QUIT:
            menug = False
        elif e.type == MOUSEBUTTONDOWN and e.button == 1:
            if exit_btn.collidepoint(mouse.get_pos()):
                menug = False 
                game = False
            
            elif start_btn.collidepoint(mouse.get_pos()):
                menug = False
                game = True
            elif settings_btn.collidepoint(mouse.get_pos()):
                menug = False
                settings = True
                
    while settingss:
        for e in event.get():
            if e.type == QUIT:
                settings = False
            elif e.type == MOUSEBUTTONDOWN and e.button == 1:
                if changetheme_btn.collidepoint(mouse.get_pos()):
                    menu.fill((255,255,255))
                    settings.fill((255,255,255))
                
                    
        
    
    menu.fill((0,0,0))
    draw.rect(menu,(103, 163, 109), start_btn)
    draw.rect(menu,(255,0,0), exit_btn)
    draw.rect(menu,(163,165,173), settings_btn)
    draw.rect(menu,(163,165,173), changetheme_btn)
    theme_text = settings_font.render('Change Theme',True, (0,0,0))
    start_text = menu_font.render('Play Game', True, (0,0,0))
    exit_text = menu_font.render('Exit Game', True, (0,0,0))
    setting_text = menu_font.render('Settings', True, (0,0,0))
    menu.blit(theme_text,(changetheme_btn.x+20,changetheme_btn.y+20 ))
    menu.blit(start_text,(start_btn.x+20, start_btn.y+20))
    menu.blit(exit_text,(exit_btn.x+20, exit_btn.y+20))
    menu.blit(setting_text,(settings_btn.x+20, settings_btn.y+20))
    display.update()

display.quit()
display.init()
#створення вікна
window = display.set_mode((800,600))
display.set_caption('Лабіринт')

picture = transform.scale(image.load("OIP.jpg"),(800,600))

chuvak1 = Object("chuvak1-removebg-preview.png",90,200,60,50,4)
chuvak2 = Object("chuvak2-removebg-preview.png",30,100,60,50,8)
chuvak3 = Object("b-removebg-preview.png",500,100,60,50,4)
coin = Object("coin-removebg-preview.png",650,400,60,50,4)
coin2 = Object("coin2.png",650,400,60,50,4)
coin3 = Object("coin3.png",450,100,60,50,4)
coin4 = Object("coin4.png",470,200,60,50,4)
coin5 = Object("coin5.png",350,80,60,50,4)
coin6 = Object("coin6.png",50,550,60,50,4)
coin7 = Object("coin7.png",150,40,60,50,4)
coin8 = Object("coin8.png",200,400,60,50,4)
chuvak4 = Object("chuvak4-removebg-preview.png",650,350,60,50,4)
keyforwall = Object("key-removebg-preview.png",400,100,60,50,4)
clock  = time.Clock()



#створення стін
wall1 = Wall(61,94,158,300,100,200,10)
wall2 = Wall(61,94,158,100,200,10,150)
wall3 = Wall(61,94,158,250,200,10,150)
wall4 = Wall(61,94,158,100,100,200,10)
wall5 = Wall(61,94,158,180,100,10,150)
wall6 = Wall(61,94,158,250,190,200,10)
wall7 = Wall(61,94,158,60,350,200,10)
wall8 = Wall(61,94,158,400,100,220,10)
wall9 = Wall(61,94,158,400,190,220,10)
wall10 = Wall(61,94,158,500,100,250,10)
wall11 = Wall(61,94,158,610,200,10,250)
wall12 = Wall(61,94,158,740,110,10,340)
wall13 = Wall(61,94,158,0,350,200,10)


walls = []
walls.append(wall1)
walls.append(wall2)
walls.append(wall3)
walls.append(wall4)
walls.append(wall5)
walls.append(wall6)
walls.append(wall7)
walls.append(wall8)
walls.append(wall9)
walls.append(wall10)
walls.append(wall11)
walls.append(wall12)
#створення головного циклу

level1 = True
level2 = False
level3 = False
while game:
    if level1:
        for e in event.get():
            if e.type == QUIT:
                game = False
            elif e.type == KEYDOWN:
                if e.key == K_e:
                    
                    chuvak2.fire()
        
        
        
        window.blit(picture,(0,0))

        bullets.update()
        bullets.draw(window)

        chuvak1.reset()
        chuvak3.reset()
        chuvak2.reset()
        chuvak4.reset()
        coin.reset()
        chuvak2.move()
        chuvak1.move2()
        chuvak3.move3()

        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        wall6.draw_wall()
        wall7.draw_wall()
        wall8.draw_wall()
        wall9.draw_wall()
        wall10.draw_wall()
        wall11.draw_wall()
        wall12.draw_wall()
        wall13.draw_wall()
       
        if sprite.collide_rect(chuvak2,chuvak1) or sprite.collide_circle(chuvak2,chuvak3) or sprite.collide_rect(chuvak2,chuvak4):
            menug = True

        if sprite.spritecollide(chuvak4,bullets,True):
            chuvak4.rect.x = 2000
        if sprite.collide_rect(chuvak2,coin):
            level1 = False
            level2 = True
            chuvak1 = Object("chuvak1.png",90,200,60,50,4)
            chuvak2 = Object("chuvak2.jpg",30,100,60,50,8)
            chuvak3 = Object("b.png",500,100,60,50,4)
            coin = Object("coin-removebg-preview.png",650,400,60,50,4)
            keyforwall = Object("key-removebg-preview.png",400,100,50,60,4)
            clock  = time.Clock()




            #створення стін
            wall1 = Wall(61,94,158,300,0,50,450)
            wall2 = Wall(61,94,158,300,450,200,50)
            wall3 = Wall(61,94,158,600,400,50,300)
            wall4 = Wall(61,94,158,330,0,70,450)
            wall5 = Wall(61,94,158,600,350,200,50)

            walls = []
            walls.append(wall1)
            walls.append(wall2)
            walls.append(wall3)
            walls.append(wall4)
            walls.append(wall5)
            
    
    if level2:
        for e in event.get():
            if e.type == QUIT:
                game = False
            elif e.type == KEYDOWN:
                if e.key == K_e:
                    
                    chuvak2.fire2()
        
        window.blit(picture,(0,0))
        
        
        
        bullets2.update()
        bullets2.draw(window)
        chuvak1.reset()
        chuvak3.reset()
        chuvak2.reset()
        coin.reset()
        keyforwall.reset()
        chuvak2.move()
        chuvak1.move2()
        chuvak3.move3()

        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
       
        if sprite.collide_rect(chuvak2,chuvak1) or sprite.collide_circle(chuvak2,chuvak3):
            menug = True
        
        if sprite.collide_rect(chuvak2,keyforwall):
            wall5.rect.x = 2500
            keyforwall.rect.x = 2700
        
        if sprite.spritecollide(chuvak3,bullets2,True):
            chuvak3.rect.x = 100000
        
       
        if sprite.collide_rect(chuvak2,coin):
            
            level2 = False
            level3 = True
            chuvak2 = Object("chuvak2.jpg",30,100,60,50,8)
            coin = Object("coin-removebg-preview.png",650,400,60,50,4)
            coin2 = Object("coin2.png",650,400,60,50,4)
            coin3 = Object("coin3.png",450,100,60,50,4)
            coin4 = Object("coin4.png",470,200,60,50,4)
            coin5 = Object("coin5.png",350,80,60,50,4)
            coin6 = Object("coin6.png",50,550,60,50,4)
            coin7 = Object("coin7.png",150,40,60,50,4)
            coin8 = Object("coin8.png",200,400,60,50,4)
    
            
    
    
    if level3:
        for e in event.get():
            if e.type == QUIT:
                game = False
            elif e.type == KEYDOWN:
                if e.key == K_e:
                    
                    chuvak2.fire2()
        
        window.blit(picture,(0,0))

        bullets2.update()
        bullets2.draw(window)
        coin.reset()
        coin2.reset()
        coin3.reset()
        coin4.reset()
        coin5.reset()
        coin6.reset()
        coin7.reset()
        coin8.reset()
        chuvak2.reset()
        
        chuvak2.move()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        wall5.draw_wall()
        
        
        
        if sprite.collide_rect(chuvak2, coin) or sprite.collide_rect(chuvak2, coin2) or sprite.collide_rect(chuvak2, coin3) or sprite.collide_rect(chuvak2, coin4) or sprite.collide_rect(chuvak2, coin6) or sprite.collide_rect(chuvak2, coin7) or sprite.collide_rect(chuvak2, coin8):
            game = False
            

        


    
    display.update()
    clock.tick(60)
