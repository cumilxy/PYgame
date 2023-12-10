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
        if keys[K_LEFT] and self.rect.x > 0: #vlivo2
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
        if self.rect.x > 390:
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

#створення вікна
window = display.set_mode((800,600))
display.set_caption('Лабіринт')
picture = transform.scale(image.load("bnacckck.png"),(800,600))

chuvak1 = Object("chuvak1.png",90,200,60,50,4)
chuvak2 = Object("chuvak2.jpg",30,100,60,50,8)
chuvak3 = Object("b.png",500,100,60,50,4)
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
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.blit(picture,(0,0))
    chuvak1.reset()
    chuvak3.reset()
    chuvak2.reset()
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
    if sprite.collide_rect(chuvak2,chuvak1) or sprite.collide_circle(chuvak2,chuvak3):
        game = False
        
    
  

    display.update()
    clock.tick(60)
