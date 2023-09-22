import engine
import basics
import pygame
import assets
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
# menu = engine.entity('menu', False, {'position': basics.position(0, 0), 'image': basics.image('menu.png')})
# startSpawner = engine.entity('startSpawner', False, {'script': basics.script(spawnButton), 'position': basics.position(0, 0), 'image': basics.image('start.png'), 'mouse': basics.mouse()})
player = engine.entity('player', True, {'rigidbody': basics.rigidbody(16, 16), 'position': basics.position(958, 1272), 'speed': basics.speed(5, 5), 'image': basics.image('player.png', 0, 0, 16, 16), 'axis': basics.axis(), 'camera': basics.camera('floor')})
wallSpawner = engine.entity('wallSpawner', True, {'camera': basics.camera('floor'), 'image': basics.image('player.png', 0, 0, 16, 16), 'script': basics.script(spawnWall),'position': basics.position(0, 0), 'mouse': basics.mouse()})
display = engine.entity('display', True, {'display': basics.display(640, 360)})
floor = engine.entity('floor', True, {'script': basics.script(camera), 'position': basics.position(0, 0), 'image': basics.image('floor.png', 0, 0, 16, 16)})
wall = engine.entity('walls', True, {'script': basics.script(camera), 'position': basics.position(0, 0), 'image': basics.image('wall.png', 0, 0, 16, 16)})
entities = [floor, player, display, wallSpawner, wall
            ]
for i in assets.walls:
    entities.append(engine.entity('wall', True, {'camera': basics.camera('floor'),'rigidbody': basics.rigidbody(i['w'], i['h']), 'position': basics.position(i['x'], i['y']), }))
systems = [basics.click(), basics.draw(), basics.flip(), basics.move(), basics.mouseFollow(), basics.scriptRun(), basics.collide()]
while True:
    start = pygame.time.Clock().get_time()
    actives = list(filter(lambda x: x.active, entities))
    preActives = list(map(lambda x: x.active, entities))
    for i in systems: 
        for j in actives:
            i.run(j, actives, entities)
    end = pygame.time.Clock().get_time()
    if end - start < 16:
        pygame.time.delay(16 - (end - start))
    
