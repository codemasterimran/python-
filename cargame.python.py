from ursina import *
app =Ursina()
camera.orthographic =True
camera.fov=10

car=Entity(
    model='quad',
    texture='car 2.jpg',
    collider='box',
    scale=(3,2),
   rotation_z=-90
)
road1 =Entity(
    model='quad',
    texture='road.jfif',
    scale=15,
    z=1

)
road2= duplicate(road1,y=15)
pair=[road1,road2]
enimies =[]
import random 
def  newEnemy():
    val=random.uniform(-2,2)
    new =duplicate(
        car,
        texture='car 2.jpg',
        x=2*val,
        y=25,
        color=color.random_color(),
        rotation_z=
        90 if val < 0  
        else -90 
    )
    enemies.append(new)
    invoke(newEnemy,delay=0.5)
    newEnemy()
def update():
    car.x -=held_keys['a']*5*time.dt
    car.x +=held_keys['d']*5*time.dt
    for road in pair:
        road.y-=6*time.dt 
        if road.y<-15:
            road.y +=30 
            for enemy in enimies:
                if enemy.x<0:
                    en.y-= 10*time.dt
                else:
                    enemy.y-= 5*time.dt    
                    
app.run()