import pygame
# entity é um objeto que representa uma entidade no jogo (o mapa, a tela, o player, uma parede etc)
class entity:
    def __init__(self, name, active, components={}):
        self.name = name
        self.components = components
        self.active = active

# system é um objeto que representa uma sistem do jogo (o player andar, as paredes spawnarem no modo editor etc)
class system:
    def __init__(self, fn, requiredComp):
        self.runInside = fn
        self.required = requiredComp
    def run(self, entity, entities, allEntities):
        if all([i in list(entity.components.keys()) for i in self.required]):
            self.runInside(entity, entities, allEntities)
# component é um objeto que representa todos os dados que a entidade pode ter como o componente de posição, velocidade e etc
class component:
    def __init__(self, name):
        self.name = name

