from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController



__ = False

app = Ursina()






class Player(FirstPersonController):
    def __init__(self):
        super().__init__(
        speed = 10,
        model = 'cube',
        collider = 'mesh',
        scale = 1,
        position = (0,0,0)
        )

class Warp(Entity):
    def __init__(self, x, y):
        super().__init__(
            warp = Entity(
             model = 'cube', 
                scale = (5, 5, 5,),
                position = (x * 5, 1, y * 5),
                colluder = 'box',
                texture = 'stone_wall_04_diff_4k.jpg'  
            )
        )      
        self.a = player

        def update(self):
            self.abcd()


        def abcd(self): 
            if self.warp.intersects(a):
                self.a.position = (95, 3, 90)






class Exit (Entity) :
    def __init__(self,i,j):
        super().__init__(
            modal = 'cube',
            scale = (5, 5, 5,),
            color = color.black90,
            postiton = (i*5, 0, j*5,),
            Collider = 'box'
            )
        self.player = player
        self.text = Text(
            text = 'escape',
            scale = 2,
            origin = (0, 0),
            visible = False
            )
    def update(self):
        self.clear()
    def clear(self):
        dis = (self.player.position - self.position).length()
        print(dis)
        if dis < 3:
            self.player.enabled = False
            self.text.visible = True


player = Player()
EditorCamera()
def input(key):
    if key == 'escape':
        app.quit()


MAP = [
    [11,'p',13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,33,22,33,22,33],
    [11,__,13,14,__,16,__,18,19,20,21,22,__,24,25,26,27,28,29,__,__,__,__,33,22,33,22,33],
    [11,__,13,__,__,16,__,__,__,20,21,22,__,24,25,26,27,28,29,__,31,32,__,__,__,__,__,33],
    [11,__,13,__,15,16,__,18,__,20,__,22,__,__,__,__,__,__,29,__,31,32,33,33,22,33,__,33],
    [11,__,13,__,15,__,__,18,__,20,__,__,__,24,25,26,__,28,29,__,31,32,33,33,22,33,__,33],
    [11,__,13,__,__,__,17,18,__,__,__,22,__,24,25,26,__,__,__,__,31,32,__,33,22,33,__,33],
    [11,__,13,14,15,16,17,18,19,20,__,22,__,24,25,26,27,28,29,30,31,32,__,__,__,__,__,33],
    [11,__,13,14,15,16,__,__,__,__,__,22,__,24,__,__,__,28,29,30,31,32,__,33,22,33,22,33],
    [11,__,13,14,15,16,__,18,__,20,21,22,__,__,__,26,__,28,29,30,31,32,__,33,22,33,__,33],
    [11,__,13,14,15,__,__,18,__,__,21,22,23,24,25,26,27,28,__,__,31,32,__,33,__,__,__,33],
    [11,__,13,14,__,__,17,18,19,__,21,22,23,24,25,26,27,28,29,__,__,__,__,__,__,33,__,33],
    [11,__,__,__,__,16,17,18,19,__,21,__,__,__,__,__,__,__,__,__,31,32,33,33,22,33,__,33],
    [11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,33,22,33,'e',33]

    ]

for i in range( len (MAP) ):
    for j in range(len ( MAP [i] ) ):
        if MAP[i][j] == 'p':
            player.position = (i * 5, 1, j * 5),
            continue
            
        if MAP[i][j] == 'e':
            exitdoor = Exit (i,j),
            continue

        if MAP[i][j] =='w':
            warp = warp (i, j),
            continue

        if MAP[i][j]:
            wall = Entity(
                model = 'cube',
                #color = color.blue,
                scale = (5, 5, 5,),
                position = (i * 5, 1, j * 5),
                colluder = 'box',
                texture = 'stone_wall_04_diff_4k.jpg'            
                
                
                ) 




ground = Entity (
model = 'plane',
color = color.gray,
position = (0, 0, 0),
scale = (500, 1, 500),
collider = 'mesh'
)

app.run()
