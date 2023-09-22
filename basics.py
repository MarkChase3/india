import pygame
import sys
import engine
def noop(a,b,c):
    pass
# display é um componente para uma entidade ser uma tela
class display(engine.component):
    def __init__(self, w, h):
        self.display = pygame.display.set_mode((w,h))
        super().__init__('display')

class kinetic(engine.component):
    def __init__(self):
        super().__init__('display')
class speed(engine.component):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__('speed')

class position(engine.component):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        super().__init__('position')

class image(engine.component):
    def __init__(self, path, x=None, y=None, w=None, h=None):
        self.img = pygame.image.load(path)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        if type(x) != type(0):
            self.x = 0
            self.y = 0
            self.w = self.img.get_width()
            self.h = self.img.get_height()
        super().__init__('image')

# axis é um componente que sinaliza que o objeto se locomove com os direcionais
class axis(engine.component):
    def __init__(self):
        super().__init__('axis')

# axis é um componente que sinaliza que o objeto se locomove com o mouse
class mouse(engine.component):
    def __init__(self):
        super().__init__('mouse')
# um script é só uma função que vai ser executada todo frame
class script(engine.component):
    def __init__(self, fn):
        self.fn = fn
        super().__init__('script')
# um rigidbody é um componente que indica que a entidade é sólida e cria colisão entre entidades com rigidbody e position
class rigidbody(engine.component):
    def __init__(self, w, h, fn=noop):
        self.w = w
        self.h = h
        self.fn = fn
        super().__init__('rigidbody')
class clickable(engine.component):
    def __init__(self, fn):
        self.fn = fn
        super().__init__('clickable')

class camera(engine.component):
    def __init__(self, name):
        self.camName = name
        super().__init__('camera')
# um sistema que desenha tudo que possui um componente imagem e 
class draw(engine.system):
    def fn(self, entity, entities, allEntities):
        for i in entities:
            if 'display' in i.components.keys():
                if 'camera' in entity.components:
                    for j in entities:
                        if j.name == entity.components['camera'].camName:
                            i.components['display'].display.blit(entity.components['image'].img, (entity.components['position'].x+j.components['position'].x, entity.components['position'].y+j.components['position'].y), (entity.components['image'].x,entity.components['image'].y,entity.components['image'].w,entity.components['image'].h))
                else:
                    i.components['display'].display.blit(entity.components['image'].img, (entity.components['position'].x, entity.components['position'].y), (entity.components['image'].x,entity.components['image'].y,entity.components['image'].w,entity.components['image'].h))
    def run(self, entity, entities, allEntities):
        super().run(entity, entities, allEntities)
    def __init__(self):
        super().__init__(self.fn, ['position', 'image'])
class flip(engine.system):
    def fn(self, entity, entities, allEntities):
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        entity.components['display'].display.fill((0, 0, 0))
    def run(self, entity, entities, allEntities): 
        super().run(entity, entities, allEntities)
    def __init__(self):
        pygame.init()
        super().__init__(self.fn, ['display'])
class move(engine.system):
    def fn(self, entity, entities, allEntities):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            entity.components['position'].y -= 1*entity.components['speed'].y
        if keys[pygame.K_s]:
            entity.components['position'].y += 1*entity.components['speed'].y
        if keys[pygame.K_a]:
            entity.components['position'].x -= 1*entity.components['speed'].x
        if keys[pygame.K_d]:
            entity.components['position'].x += 1*entity.components['speed'].x
    def run(self, entity, entities, allEntities):
        super().run(entity, entities, allEntities)
    def __init__(self):
        pygame.init()
        super().__init__(self.fn, ['axis', 'position', 'speed'])
class mouseFollow(engine.system):
    def fn(self, entity, entities, allEntities):
        entity.components['position'].x, entity.components['position'].y = pygame.mouse.get_pos()
        if 'camera' in entity.components:
            for i in entities:
                if entity.components['camera'].camName == i.name:
                    entity.components['position'].x -= i.components['position'].x
                    entity.components['position'].y -= i.components['position'].y
    def run(self, entity, entities, allEntities):
        super().run(entity, entities, allEntities)
    def __init__(self):
        pygame.init()
        super().__init__(self.fn, ['mouse', 'position'])
class scriptRun(engine.system):
    def fn(self, entity, entities, allEntities):
        entity.components['script'].fn(entity, entities, allEntities)
    def run(self, entity, entities, allEntities):
        super().run(entity, entities, allEntities)
    def __init__(self):
        super().__init__(self.fn, ['script'])
class collide(engine.system):
    def fn(self, entity, entities, allEntities):
        for i in entities:
            if i.name != entity.name:
                posI = i.components['position'] if 'position' in i.components else None
                rigidI = i.components['rigidbody']  if 'rigidbody' in i.components else None
                posEnt = entity.components['position']
                rigidEnt = entity.components['rigidbody']
                if rigidI:
                    if posI.x + rigidI.w > posEnt.x and posEnt.x + rigidEnt.w > posI.x and posI.y + rigidI.h > posEnt.y and posEnt.y + rigidEnt.h > posI.y:
                        rigidEnt.fn(entity, i, allEntities)
                        rigidI.fn(i, entity, allEntities)
                        if not (posI.x + rigidI.w > rigidEnt.preX and rigidEnt.preX + rigidEnt.w > posI.x):
                            entity.components['position'].x = entity.components['rigidbody'].preX
                        elif not (posI.y + rigidI.h > rigidEnt.preY and rigidEnt.preY + rigidEnt.h > posI.y):
                            entity.components['position'].y = entity.components['rigidbody'].preY
                        else:
                            entity.components['position'].x = entity.components['rigidbody'].preX
                            entity.components['position'].y = entity.components['rigidbody'].preY
        entity.components['rigidbody'].preX, entity.components['rigidbody'].preY = entity.components['position'].x, entity.components['position'].y
    def run(self, entity, entities, allEntities):
        super().run(entity, entities, allEntities)
    def __init__(self):
        super().__init__(self.fn, ['rigidbody', 'position'])
class click(engine.system):
    def fn(self, entity, entities, allEntities):
        posI = pygame.mouse.get_pos()
        posEnt = entity.components['position']
        rigidEnt = entity.components['rigidbody']
        if posI[0] > posEnt.x and posEnt.x + rigidEnt.w > posI[0] and posI[1] > posEnt.y and posEnt.y + rigidEnt.h > posI[1]:
            entity.components['clickable'].fn(entity, entities, allEntities)
        entity.components['rigidbody'].preX, entity.components['rigidbody'].preY = entity.components['position'].x, entity.components['position'].y
    def run(self, entity, entities, allEntities):
        super().run(entity, entities, allEntities)
    def __init__(self):
        super().__init__(self.fn, ['rigidbody', 'position', 'clickable'])
class walk(engine.system):
    def fn(self, entity, entities, allEntities):
        entity.components['position'].x += entity.components['speed'].x
        entity.components['position'].y += entity.components['speed'].y
    def run(self, entity, entities, allEntities):
        super().run(entity, entities, allEntities)
    def __init__(self):
        super().__init__(self.fn, ['position', 'speed', 'kinetic'])