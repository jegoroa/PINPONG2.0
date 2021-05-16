from pygame import*

w = 700
h = 500

class Main(sprite.Sprite):
    def __init__(self,x,y,w,h,speed,pic_name):
        self.rect = Rect(x,y,w,h)
        self.image = image.load("ball.jpg")
        self.image = transform.scale(self.image, (w,h))
        self.speed = speed

    def reset(self):
        win.blit( self.image , (self.rect.x, self.rect.y) )

class Ball(Main):
    def __init__(self,x,y,w,h,speed,pic_name,vface,hface):
        super().__init__(x,y,w,h,speed,pic_name)
        self.vface = vface
        self.hface = hface

    def update(self):
        if self.hface == "right":
            self.rect.x += self.speed
            if self.rect.x > w:
                self.hface = "left"

        if self.hface == "left":
            self.rect.x -= self.speed
            if self.rect.x < 0:
                self.hface = "right"

        self.reset()

ball = Ball(x=50,y=50,w=50,h=50,speed=1,
    pic_name="ball.jpg",vface='up',hface='right')

win = display.set_mode((w,h))


game_mode = "игра"
while True:

    win.fill( (0,225,0) ) #ДОБАВИЛИ!!!!
    if game_mode == "игра":
        ball.update() #ИЗМЕНИЛИ!!!

    for e in event.get():
        if e.type == QUIT:
            exit()

    display.update()
