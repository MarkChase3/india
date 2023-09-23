import engine
import basics
import pygame
import assets
import random
import app
pygame.init()
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
        if i.name in ['player', 'playerMini']:
            entity.components['position'].x = -max(i.components['position'].x-320, 0)
            entity.components['position'].y = -max(i.components['position'].y-180, 0)

def collide(entity, other, entities):
    for i in entities:
        if i.active:
            i.active = False
        if i.name in ['samosa', 'backgroundSamosa', 'basket','display', 'back']:
            i.active = True
def animate(entity, other, entities):
    keys = pygame.key.get_pressed()
    if entity.components['image'].x < 176 and pygame.time.get_ticks()%5 == 0:
        entity.components['image'].x += 30
    if keys[pygame.K_RIGHT] and pygame.time.get_ticks()%5 == 0:
        if (not entity.components['image'].x < 330) or (not entity.components['image'].x > 210):
            entity.components['image'].x = 210
        entity.components['image'].x += 30
    if keys[pygame.K_LEFT] and pygame.time.get_ticks()%5 == 0:
        if (not entity.components['image'].x > 330) or (not entity.components['image'].x < 510):
            entity.components['image'].x = 330
        entity.components['image'].x += 30
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
            if (i.name in ['player','wallSpawner','display','floor','walls','wall', 'samosa0', 'samosa1', 'portal', 'dance']):
                i.active = True
def endMinigame(entity, entities, allEntities):
    if entity.components['position'].y > 600 and entity.components['position'].x > 1150:
        entity.components['position'].y = 150
        entity.components['position'].x = 127
        for i in allEntities:
            if i.active:
                i.active = False
            if (i.name in ['player','wallSpawner','display','floor','walls','wall', 'samosa0', 'samosa1', 'portal', 'dance']):
                i.active = True
def fn(entity, other, allEntities):
    if other.name == 'playerMini':
        other.components['position'].x = 150
        other.components['position'].y = 127
        other.components['rigidbody'].preX = 150
        other.components['rigidbody'].preY = 127
# menu = engine.entity('menu', False, {'position': basics.position(0, 0), 'image': basics.image('menu.png')})
# startSpawner = engine.entity('startSpawner', False, {'script': basics.script(spawnButton), 'position': basics.position(0, 0), 'image': basics.image('start.png'), 'mouse': basics.mouse()})
def enterDance(entity, entities, allEntities):
    for i in allEntities:
        if i.active:
            i.active = False

        if (i.name in ['display', 'back', 'playerDance', 'arrowSpawner']):
            i.active = True
def minigameEnter(entity, entities, allEntities):
    for i in allEntities:
        if i.active:
            i.active = False

        if (i.name in ['display', 'minigame', 'playerMini', 'wallSpawner2', 'fence']):
            i.active = True
def die(entity, entities, allEntities):
    keys = pygame.key.get_pressed()
    if entity.components['position'].y < 0:
        for i in allEntities:
            if i.active:
                i.active = False
            if (i.name in ['player','wallSpawner','display','floor','walls','wall', 'samosa0', 'samosa1', 'portal', 'dance']):
                i.active = True
    if entity.components['image'].x == 0:
        if keys[pygame.K_LEFT]:
            entity.active = False
    else:
        if keys[pygame.K_RIGHT]:
            entity.active = False
def spawnArrows(entity, entities, allEntities):
    if pygame.time.get_ticks()%50 == 0:
        allEntities.append(engine.entity('arrow', True, {'position': basics.position(random.random()*320+160, 360), 'script': basics.script(die),'speed': basics.speed(0,-8),'image':basics.image('arrows.png', round(random.random())*48, 20, 20, 20), 'kinetic': basics.kinetic}))
arrowSpawner = engine.entity('arrowSpawner', False, {'script': basics.script(spawnArrows)})
dance = engine.entity('dance', True, {'rigidbody': basics.rigidbody(110, 88, enterDance), 'position': basics.position(904, 621)})
trash = engine.entity('minigame', False, {'rigidbody': basics.rigidbody(32, 32, fn),'position': basics.position(324, 260), 'image': basics.image('trash.png'),'camera': basics.camera('minigame')})
minigame = engine.entity('minigame', False, {'position': basics.position(0, 0), 'script': basics.script(camera), 'image': basics.image('minigame.png')})
playerDance = engine.entity('playerDance', False, {'position': basics.position(310, 290) , 'script': basics.script(animate), 'image': basics.image('playerDance.png', 0, 0, 32, 64)})
playerMini = engine.entity('playerMini', False, {'script': basics.script(endMinigame), 'rigidbody': basics.rigidbody(32, 32), 'position': basics.position(150, 127), 'speed': basics.speed(5, 5), 'image': basics.image('player.png', 0, 0, 32, 32), 'axis': basics.axis(), 'camera': basics.camera('minigame')})
player = engine.entity('player', True, {'rigidbody': basics.rigidbody(16, 16), 'position': basics.position(958, 1200), 'speed': basics.speed(6, 6), 'image': basics.image('player.png', 0, 0, 32, 32), 'axis': basics.axis(), 'camera': basics.camera('floor')})
wallSpawner = engine.entity('wallSpawner', True, {'camera': basics.camera('floor'), 'image': basics.image('player.png', 0, 0, 16, 16), 'script': basics.script(spawnWall),'position': basics.position(0, 0), 'mouse': basics.mouse()})
wallSpawner2 = engine.entity('wallSpawner2', True, {'camera': basics.camera('minigame'), 'image': basics.image('player.png', 0, 0, 16, 16), 'script': basics.script(spawnWall),'position': basics.position(0, 0), 'mouse': basics.mouse()})
display = engine.entity('display', True, {'display': basics.display(640, 360)})
floor = engine.entity('floor', True, {'script': basics.script(camera), 'position': basics.position(0, 0), 'image': basics.image('floor.png')})
back = engine.entity('back', True, {'position': basics.position(0, 0), 'image': basics.image('background.png')})
wall = engine.entity('walls', True, {'script': basics.script(camera), 'position': basics.position(0, 0), 'image': basics.image('wall.png')})
pygame.mixer.init()
s = pygame.mixer.Sound('audio.mp3')
entities = [dance,back,playerDance, minigame, playerMini, trash, floor, player, display, wallSpawner, wallSpawner2, wall,arrowSpawner,
            engine.entity('samosa0', True, {'rigidbody': basics.rigidbody(74,61,collide), 'position': basics.position(104,658)}),
            engine.entity('samosa1', True, {'rigidbody': basics.rigidbody(74,61,collide), 'position': basics.position(2000,658)}),
            engine.entity('portal', True, {'rigidbody': basics.rigidbody(200,100,minigameEnter), 'position': basics.position(873,55)}),
            engine.entity('basket', False, {'speed': basics.speed(5, 0), 'axis': basics.axis(), 'rigidbody': basics.rigidbody(100,50), 'position': basics.position(0,330), 'image': basics.image('player.png', 0, 0, 32, 32)}),
            engine.entity('samosa', False, {'script': basics.script(out), 'speed': basics.speed(0, 4), 'kinetic': basics.kinetic(),'rigidbody': basics.rigidbody(100,50,collideSamosa), 'position': basics.position(0,0), 'image': basics.image('samosa.png')}),
            ]
for i in assets.walls:
    entities.append(engine.entity('wall', True, {'camera': basics.camera('floor'),'rigidbody': basics.rigidbody(i['w'], i['h']), 'position': basics.position(i['x'], i['y']), }))
for i in assets.walls2:
    entities.append(engine.entity('fence', False, {'camera': basics.camera('minigame'),'rigidbody': basics.rigidbody(i['w'], i['h']), 'position': basics.position(i['x'], i['y']), }))
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
    
