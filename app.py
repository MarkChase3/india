import pygame
import gamegen
def run(entity, entities, allEntities):

    # configurando o tamanho do display e dos sprites
    gamegen.camera.setVideoMode((640, 360), pygame.display.set_mode((640, 360)))
    gamegen.sprites.setLength((40,40))


    # iniciando os sprites/ nome do sprite/ é colisivo ? / é uma entidade ?/ imagem do personagem
    gamegen.sprites.appendSprite('gray', False, False, "block.png")
    gamegen.sprites.appendSprite('red', True, False, "red.png")
    gamegen.sprites.appendSprite('player', True, True, "player.png")
    gamegen.sprites.appendSprite('monkey', True, True, "monkey.png")
    gamegen.sprites.appendSprite('bar', True, False, "bar.png")

    #setando posiçôes dos sprites
    gamegen.sprites.spriteData[gamegen.sprites.sprite('monkey')].setPosition(3000, 240)

    gamegen.sprites.spriteData[gamegen.sprites.sprite('player')].setPosition(600,545)

    #setando as entidades dessa parte do jogo
    gamegen.sprites.entitiesInAct([gamegen.sprites.sprite('monkey'),gamegen.sprites.sprite('player')])

    #criando um mundo
    wt = []
    for i in range(100):
        line = []
        for b in range(100):
            line.append(gamegen.sprites.sprite('gray'));
        wt.append(line)

    wt[0][0] = 1
    wt[20][14] = 1
    wt[20][15] = 1
    wt[20][16] = 1
    wt[20][17] = 1
    wt[20][18] = 1
    wt[20][19] = 1
    wt[20][10] = 1
    wt[20][11] = 1
    wt[20][12] = 1
    wt[20][13] = 1
    wt[19][13] = 1
    wt[18][13] = 1
    wt[17][13] = 1
    wt[16][13] = 1

    for i in range(100):
        wt[i][i] = 1
        wt[i][99 - i] = 1
        wt[i][0] = 4
        wt[0][i] = 4
        wt[i][99] = 4
        wt[99][i] = 4

    wt[5][99 - 5] = 0
    wt[95][99 - 95]= 0
    wt[5][5] = 0

    #incluindo um mundo à biblioteca de mundos
    gamegen.world.appendWorld('world1', wt)

    #selecionando o mundo na biblioteca de mundos
    gamegen.world.setWorld('world1')

    #escolhendo algum personagem para focar a câmera
    gamegen.camera.focusedIn(gamegen.sprites.sprite('player'))

    pos = False
    status = True
    while (status):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                status = False

        keys = pygame.key.get_pressed() 

        #verificando colisões
        if keys[pygame.K_RIGHT] and ('lest' in gamegen.sprites.spriteData[gamegen.sprites.sprite('player')].predictColision(1)) == False:
            gamegen.sprites.spriteData[gamegen.sprites.sprite('player')].x+=1
        if keys[pygame.K_LEFT] and ('west' in gamegen.sprites.spriteData[gamegen.sprites.sprite('player')].predictColision(1)) == False:
            gamegen.sprites.spriteData[gamegen.sprites.sprite('player')].x-=1
        if keys[pygame.K_UP] and ('north' in gamegen.sprites.spriteData[gamegen.sprites.sprite('player')].predictColision(1)) == False:
            gamegen.sprites.spriteData[gamegen.sprites.sprite('player')].y-=1
        if keys[pygame.K_DOWN] and ('south' in gamegen.sprites.spriteData[gamegen.sprites.sprite('player')].predictColision(1)) == False:
            gamegen.sprites.spriteData[gamegen.sprites.sprite('player')].y+=1

        #movimentando o macaco
        if (pos==False):
            gamegen.sprites.spriteData[gamegen.sprites.sprite('monkey')].x+=0.5
        else:
            gamegen.sprites.spriteData[gamegen.sprites.sprite('monkey')].x-=0.5
        if (int(gamegen.sprites.spriteData[gamegen.sprites.sprite('monkey')].x) == 3500):
            pos=True
        if (int(gamegen.sprites.spriteData[gamegen.sprites.sprite('monkey')].x) == 2500):
            pos=False


        #colidiu com o macaco de qualquer lado, o player volta pra pos inicial/ obs: as colisões da entidade ficam como "elest","ewest","enorth","esouth"
        if(len(gamegen.sprites.spriteData[gamegen.sprites.sprite('monkey')].predictColision(1)) != 0):
                gamegen.sprites.spriteData[gamegen.sprites.sprite('player')].setPosition(600, 545)

        #atualiza a câmera
        gamegen.camera.frame()
        pygame.display.flip()
        if (int(gamegen.sprites.spriteData[gamegen.sprites.sprite('monkey')].y) < 0):
            status = False           
    gamegen.sprites.deleteSprite(gamegen.sprites.sprite('player'))
    gamegen.sprites.deleteSprite(gamegen.sprites.sprite('monkey'))
    pygame.quit()
