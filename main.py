import engine
import basics
import pygame
import assets
import random
import gamegen
startxwall = 0
startywall = 0
def spawnWall(entity, entities, allEntities):
    global startywall, startxwall
    if pygame.mouse.get_pressed()[0] and startxwall == 0:
        startxwall = entity.components['position'].x
        startywall = entity.components['position'].y
    if not pygame.mouse.get_pressed()[0] and startxwall > 0:
        for i in entities:
            if entity.components['camera'].camName == i.name:
                #allEntities.append(engine.entity('wall', True, {'camera': basics.camera('floor'),'rigidbody': basics.rigidbody(entity.components['position'].x-startxwall, entity.components['position'].y-startywall), 'position': basics.position(startxwall, startywall), 'image': basics.image('player.png')}))
                print("{'x':"+str(startxwall)+",'y':"+str(startywall)+",'w':"+str(entity.components['position'].x-startxwall)+",'h':"+str(entity.components['position'].y-startywall)+"},")
                startxwall = 0
def spawnButton(entity, entities, allEntities):
    if pygame.mouse.get_pressed()[0]:
        if len(list(filter(lambda x: x.name == 'startButton', entities))) == 0:
            entities.append(engine.entity('startButton', True, { 'position': basics.position(entity.components['position'].x, entity.components['position'].y), 'image': basics.image('start.png')}))
        else:
            for k,i in enumerate(entities):
                if i.name == 'startButton':
                    i = (engine.entity('startButton', True, {'rigidbody': basics.rigidbody(16, 16), 'position': basics.position(entity.components['position'].x, entity.components['position'].y), 'image': basics.image('player.png')}))
def startGame(entity, entities, allEntities):
    for i in allEntities:
        if i.active:
            i.active = False
        if i.name in ['player', 'wallSpawner', 'floor', 'display']:
            i.active = True

def camera(entity, entities, allEntities):
    for i in entities:
        if i.name == 'player':
            entity.components['position'].x = -max(i.components['position'].x-320, 0)
            entity.components['position'].y = -max(i.components['position'].y-180, 0)

def collide(entity, other, entities):
    print(other.name)
    for i in entities:
        if i.active:
            i.active = False
        if i.name in ['samosa', 'backgroundSamosa', 'basket','display']:
            print('ohin87disçlzç')
            i.active = True

def collideSamosa(entity, other, entities):
    entity.components['position'].y = -50
    entity.components['position'].x = random.random()*360
def out(entity, entities, allEntities):
    if entity.components['position'].y > 360:
        entity.components['position'].y = -50
        entity.components['position'].x = 0
        for i in allEntities:
            if i.active:
                i.active = False
            if (i.name in ['player','wallSpawner','display','floor','walls','wall', 'samosa0']):
                i.active = True
# menu = engine.entity('menu', False, {'position': basics.position(0, 0), 'image': basics.image('menu.png')})
# startSpawner = engine.entity('startSpawner', False, {'script': basics.script(spawnButton), 'position': basics.position(0, 0), 'image': basics.image('start.png'), 'mouse': basics.mouse()})
player = engine.entity('player', True, {'rigidbody': basics.rigidbody(16, 16), 'position': basics.position(958, 1272), 'speed': basics.speed(5, 5), 'image': basics.image('player.png', 0, 0, 32, 32), 'axis': basics.axis(), 'camera': basics.camera('floor')})
wallSpawner = engine.entity('wallSpawner', True, {'camera': basics.camera('floor'), 'image': basics.image('player.png', 0, 0, 16, 16), 'script': basics.script(spawnWall),'position': basics.position(0, 0), 'mouse': basics.mouse()})
display = engine.entity('display', True, {'display': basics.display(640, 360)})
floor = engine.entity('floor', True, {'script': basics.script(camera), 'position': basics.position(0, 0), 'image': basics.image('floor.png')})
wall = engine.entity('walls', True, {'script': basics.script(camera), 'position': basics.position(0, 0), 'image': basics.image('wall.png')})
entities = [floor, player, display, wallSpawner, wall,
            engine.entity('samosa0', True, {'rigidbody': basics.rigidbody(74,61,collide), 'position': basics.position(104,658)}),
            engine.entity('basket', False, {'speed': basics.speed(3, 0), 'axis': basics.axis(), 'rigidbody': basics.rigidbody(100,50), 'position': basics.position(0,330), 'image': basics.image('start.png')}),
            engine.entity('samosa', False, {'script': basics.script(out), 'speed': basics.speed(0, 6), 'kinetic': basics.kinetic(),'rigidbody': basics.rigidbody(100,50,collideSamosa), 'position': basics.position(0,0), 'image': basics.image('start.png')}),
            ]
for i in assets.walls:
    entities.append(engine.entity('wall', True, {'camera': basics.camera('floor'),'rigidbody': basics.rigidbody(i['w'], i['h']), 'position': basics.position(i['x'], i['y']), }))
systems = [basics.walk(), basics.click(), basics.draw(), basics.flip(), basics.move(), basics.mouseFollow(), basics.scriptRun(), basics.collide()]
while True:
    start = pygame.time.Clock().get_time()
    actives = list(filter(lambda x: x.active, entities))
    preActives = list(map(lambda x: x.active, entities))
    print(len(actives))
    for i in systems: 
        for j in actives:
            i.run(j, actives, entities)
    end = pygame.time.Clock().get_time()
    if end - start < 16:
        pygame.time.delay(16 - (end - start))
    
