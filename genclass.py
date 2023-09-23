import pygame
import gamegen

class World:
    def __init__(self):
        self.actuallyWorld = []
        self.worlds = [0]
    def appendWorld(self, n, m):
        self.worlds.append(n);
        self.worlds.append(m);
    def setWorld(self, n):
        for i in range(1,len(self.worlds)):
            if (i%2) == 1:
                if n==self.worlds[i]:
                    self.actuallyWorld = self.worlds[i+1]
                    break


class Sprites:
    def __init__(self):
        self.spriteData = []
        self.etspriteData = [];
        self.lengthSpr = []
    
    def setLength(self, l):
        self.lengthSpr = l

    def entitiesInAct(self, en):
        self.etspriteData = en

    def deleteSprite(self, n):
        for i in range(len(self.spriteData)):
            if (self.spriteData[i].name == n):
                self.spriteData.pop(i)
                for b in range(len(self.etspriteData)):
                    if (self.etspriteData[b] == i):
                        self.etspriteData.pop(b)
                        break
                break

    def appendSprite(self,n,r,e,t):
        class spmodel:
            def __init__(self, n, r,e, t):
                self.name = n
                self.colisible = r
                self.x = 0
                self.y = 0
                self.texture = pygame.image.load(t).convert()
                self.entity = e
                self.ct = [0,0,gamegen.sprites.lengthSpr[0], gamegen.sprites.lengthSpr[1]]
            
            def setCropArea(self, la):
                self.ct = la

            def setPosition(self, xs ,ys):
                self.x = xs
                self.y = ys

            def predictColision(self, d):
                sides = []
                
                if self.entity == True:
                    for i in range(len(gamegen.sprites.etspriteData)):
                        if gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].colisible==True:
                            if self.x < gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].x + gamegen.sprites.lengthSpr[0] + 1 and self.x > gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].x + gamegen.sprites.lengthSpr[0] -1 and ((self.y < gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].y + gamegen.sprites.lengthSpr[1] and self.y >= gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].y) or (self.y + gamegen.sprites.lengthSpr[1] < gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].y + gamegen.sprites.lengthSpr[1] and self.y + gamegen.sprites.lengthSpr[1] >= gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].y)) and self.name  != gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].name:
                                sides.append('ewest')
                            if self.x + gamegen.sprites.lengthSpr[0]-1 > gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].x -2 and self.x + gamegen.sprites.lengthSpr[0]-1 < gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].x and ((self.y < gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].y + gamegen.sprites.lengthSpr[1] and self.y >= gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].y) or (self.y + gamegen.sprites.lengthSpr[1] < gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].y + gamegen.sprites.lengthSpr[1] and self.y + gamegen.sprites.lengthSpr[1] >= gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].y)) and self.name  != gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].name:
                                sides.append('elest')
                            if self.y + gamegen.sprites.lengthSpr[0]-1 < gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].y and self.y + gamegen.sprites.lengthSpr[0]-1 > gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].y-2 and ((self.x >= gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].x and self.x < gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].x + gamegen.sprites.lengthSpr[0]) or (self.x + gamegen.sprites.lengthSpr[0] >= gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].x and self.x + gamegen.sprites.lengthSpr[0] < gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].x + gamegen.sprites.lengthSpr[0])) and self.name  != gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].name:
                                sides.append('esouth')
                            if self.y > gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].y + gamegen.sprites.lengthSpr[1] -1 and self.y  < gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].y + gamegen.sprites.lengthSpr[1] +1 and ((self.x >= gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].x and self.x < gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].x + gamegen.sprites.lengthSpr[0]) or (self.x + gamegen.sprites.lengthSpr[0] >= gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].x and self.x + gamegen.sprites.lengthSpr[0] < gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].x + gamegen.sprites.lengthSpr[0])) and self.name  != gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].name:
                                sides.append('enorth')
                            
                if gamegen.sprites.spriteData[gamegen.world.actuallyWorld[int(self.y/gamegen.sprites.lengthSpr[1])][int((self.x -d)/gamegen.sprites.lengthSpr[0])]].colisible==True or gamegen.sprites.spriteData[gamegen.world.actuallyWorld[int((self.y + gamegen.sprites.lengthSpr[1] -1)/gamegen.sprites.lengthSpr[1])][int((self.x -d)/gamegen.sprites.lengthSpr[0])]].colisible==True:
                    sides.append('west');
                if gamegen.sprites.spriteData[gamegen.world.actuallyWorld[int(self.y/gamegen.sprites.lengthSpr[1])][int((self.x + gamegen.sprites.lengthSpr[0] - 1 + d)/gamegen.sprites.lengthSpr[0])]].colisible==True or gamegen.sprites.spriteData[gamegen.world.actuallyWorld[int((self.y + gamegen.sprites.lengthSpr[1] -1)/gamegen.sprites.lengthSpr[1])][int((self.x + gamegen.sprites.lengthSpr[0] - 1 + d)/gamegen.sprites.lengthSpr[0])]].colisible==True:
                    sides.append('lest')
                if gamegen.sprites.spriteData[gamegen.world.actuallyWorld[int((self.y + gamegen.sprites.lengthSpr[1] - 1 + d)/gamegen.sprites.lengthSpr[1])][int((self.x)/gamegen.sprites.lengthSpr[0])]].colisible==True or gamegen.sprites.spriteData[gamegen.world.actuallyWorld[int((self.y + gamegen.sprites.lengthSpr[1] - 1 + d)/gamegen.sprites.lengthSpr[1])][int((self.x + gamegen.sprites.lengthSpr[0] -1)/gamegen.sprites.lengthSpr[0])]].colisible==True:
                    sides.append('south')
                if gamegen.sprites.spriteData[gamegen.world.actuallyWorld[int((self.y - d)/gamegen.sprites.lengthSpr[1])][int((self.x)/gamegen.sprites.lengthSpr[0])]].colisible==True or gamegen.sprites.spriteData[gamegen.world.actuallyWorld[int((self.y -d)/gamegen.sprites.lengthSpr[1])][int((self.x + gamegen.sprites.lengthSpr[0] -1)/gamegen.sprites.lengthSpr[0])]].colisible==True:
                    sides.append('north')

        

                return sides
        self.spriteData.append(spmodel(n,r,e, t))

    def sprite(self, n):
        for i in range(len(self.spriteData)):
            if (self.spriteData[i].name == n):
                return i



class Camera:
    def __init__(self):
        self.focus = 0;
        self.videoMode = []
        self.act="";

    def focusedIn(self, index):
        self.focus = index

    def setVideoMode(self, v, a):
        self.videoMode = v
        self.act = a

    def test(self):
        self.act.blit(gamegen.sprites.spriteData[gamegen.world.actuallyWorld[0][0]].texture, (0, 0), gamegen.sprites.spriteData[gamegen.world.actuallyWorld[0][0]].ct)

    def frame(self):
        ty = int(self.videoMode[1]/gamegen.sprites.lengthSpr[1])
        tx = int(self.videoMode[0]/gamegen.sprites.lengthSpr[0])

        px = int(gamegen.sprites.spriteData[self.focus].x)
        py = int(gamegen.sprites.spriteData[self.focus].y)

        offx = px%gamegen.sprites.lengthSpr[0]
        offy = py%gamegen.sprites.lengthSpr[1]

        rpx = int(px/gamegen.sprites.lengthSpr[0])
        rpy = int(py/gamegen.sprites.lengthSpr[1])

        sbx = rpx - int(tx/2)
        fbx = rpx + int(tx/2) + 2

        sby = rpy - int(ty/2)
        fby = rpy + int(ty/2)  + 2
        
        ac = [False, False]

        kpx=0;
        kpy=0;

        if sbx<0:
            offx =0
            sbx=0
            ac[0] = True
            fbx = tx + 2
        if sby<0:
            offy = 0
            sby = 0
            ac[1] = True
            fby = ty + 2
    
        if sbx + tx >= len(gamegen.world.actuallyWorld[0]):
            offx = 0
            ac[0] = True
            sbx = len(gamegen.world.actuallyWorld[0]) - tx
            fbx = len(gamegen.world.actuallyWorld[0])
            kpx = sbx*gamegen.sprites.lengthSpr[0]
            
        if sby + ty >= len(gamegen.world.actuallyWorld):
            offy =0
            ac[1] = True
            sby = len(gamegen.world.actuallyWorld[1]) - ty
            fby = len(gamegen.world.actuallyWorld[1])
            kpy = sby*gamegen.sprites.lengthSpr[1]
            
        for x in range(sbx, fbx):
            for y in range(sby, fby):
                at = [];
                try:
                    at = gamegen.world.actuallyWorld[y][x]
                except:
                    at = 0
                if (type(at) == type(0)):
                    self.act.blit(gamegen.sprites.spriteData[at].texture, ((x - sbx)*gamegen.sprites.lengthSpr[0] - offx, (y - sby)*gamegen.sprites.lengthSpr[1] - offy), gamegen.sprites.spriteData[at].ct)
                else:
                    for i in range(at.length):
                        self.act.blit(gamegen.sprites.spriteData[at].texture, ((x - (rpx - int(tx/2)))*gamegen.sprites.lengthSpr[0] - offx, (y - (rpy - int(ty/2)))*gamegen.sprites.lengthSpr[1] - offy), gamegen.sprites.spriteData[at].ct)
        
        ppx = int(tx/2)
        ppy = int(ty/2)
        if ac[0]:
            ppx = (gamegen.sprites.spriteData[self.focus].x-kpx)/gamegen.sprites.lengthSpr[0]
        if ac[1]:
            ppy = (gamegen.sprites.spriteData[self.focus].y-kpy)/gamegen.sprites.lengthSpr[1]
        self.act.blit(gamegen.sprites.spriteData[self.focus].texture, (ppx * gamegen.sprites.lengthSpr[0],ppy * gamegen.sprites.lengthSpr[1]), gamegen.sprites.spriteData[self.focus].ct)
        for i in range(len(gamegen.sprites.etspriteData)):
                if (gamegen.sprites.etspriteData[i] != self.focus):
                    self.act.blit(gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].texture, (gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].x - (sbx *  gamegen.sprites.lengthSpr[0]) -offx, gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].y - (sby *  gamegen.sprites.lengthSpr[1]) - offy), gamegen.sprites.spriteData[gamegen.sprites.etspriteData[i]].ct)