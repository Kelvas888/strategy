import pygame, sys, math, time
from pygame.locals import *

class Cam:
    def __init__(self,pos=(0,0),rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)

    def update(self,dt,key):
        s = dt*40

        if key[pygame.K_w]: self.pos[1]+=s
        if key[pygame.K_s]: self.pos[1]-=s

        if key[pygame.K_a]: self.pos[0]+=s
        if key[pygame.K_d]: self.pos[0]-=s
		
class Centre:
    def __init__(self,pos=(0,0),rot=(0,0),data_protections=(1000,100,100,100)):
        self.pos = list(pos)
        self.rot = list(rot)
        self.data_protections = list(data_protections)
        self.dog = pygame.image.load('pictures/BB.png')
        self.r_size = 1.41*25

		
    def update(self,x,y):
        self.pos[0]+=x
        self.pos[1]+=y
	
    def getPosition_x(self):
        return self.pos[0]
		
    def getPosition_y(self):
        return self.pos[1]		
		
class Mainer:
    def __init__(self,pos=(0,0),rot=(0,0),data_protections=(100,10,10,10)):
        self.pos = list(pos)
        self.rot = list(rot)
        self.data_protections = list(data_protections)
        self.dog = pygame.image.load('pictures/mainer.png')
        self.take = 1
        self.r_size = 14.1

		
    def update(self,x,y):
        self.pos[0]+=x
        self.pos[1]+=y
	
    def getPosition_x(self):
        return self.pos[0]
		
    def getPosition_y(self):
        return self.pos[1]		

class Crystal:
    def __init__(self,pos=(0,0),data_protections=(100,10)):
        self.pos = list(pos)
        self.data_protections = list(data_protections)
        self.dog = pygame.image.load('pictures/resours1.png')
        self.r_size = 1.41*15
		
    def getPosition_x(self):
        return self.pos[0]
		
    def getPosition_y(self):
        return self.pos[1]

verts = (10,50),(100,50),(50,150),(550,350)
verts2 = (120,50),(40,50),(520,150),(250,350),(850,350)

cam = Cam((0,0))
mainers = [] 
mainers.append(Mainer((200,310)))
mainers.append(Mainer((500,410)))
mainers.append(Mainer((600,210)))
mainers.append(Mainer((456,1100)))
mainers.append(Mainer((600,1903)))
mainers.append(Mainer((600,2345)))

centres = [] 
centres.append(Centre((0,0)))
centres.append(Centre((450,100)))
centres.append(Centre((590,100)))
centres.append(Centre((100,250)))
centres.append(Centre((450,1400)))
centres.append(Centre((590,1040)))
centres.append(Centre((100,1504)))
crystals = [] 
crystals.append(Crystal((150,420)))
crystals.append(Crystal((500,500)))
crystals.append(Crystal((600,310)))
crystals.append(Crystal((450,900)))
crystals.append(Crystal((600,1300)))
crystals.append(Crystal((700,1310)))
clock = pygame.time.Clock()
list = []
list.extend(mainers)
list.extend(centres)
list.extend(crystals)
pygame.init()

black = (0,0,0)
sc = pygame.display.set_mode((800, 500), FULLSCREEN)
sc.fill((100, 150, 200))
pygame.display.set_caption("Окно игры")


#with open('pictures/0.bmp', 'rb') as f:
    #data = bytearray(f.read()) 
font = pygame.font.Font(None, 15)
#text = font.render("Score: "+str(data),True,black)
#print(data)	
while True:
    dt = clock.tick()/1000+1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: mainLoop = False; pygame.quit(); sys.exit()
 
    sc.fill((100, 150, 200))
    #sc.blit(text, [0,0])
			
    for mainer in mainers:	
        dog_rect = mainer.dog.get_rect(bottomright=(mainer.r_size+mainer.pos[0]+cam.pos[0],mainer.r_size+mainer.pos[1]+cam.pos[1]))
        dog = pygame.transform.rotate(mainer.dog, mainer.rot[0])
        sc.blit(dog, dog_rect)
		
    for centre in centres:	
        dog_rect = centre.dog.get_rect(bottomright=(centre.r_size+centre.pos[0]+cam.pos[0],centre.r_size+centre.pos[1]+cam.pos[1]))
        sc.blit(centre.dog, dog_rect)
		
    for crystal in crystals:	
        dog_rect = crystal.dog.get_rect(bottomright=(crystal.r_size+crystal.pos[0]+cam.pos[0],crystal.r_size+crystal.pos[1]+cam.pos[1]))
        sc.blit(crystal.dog, dog_rect)
		
    for mainer in mainers:	
	    if mainer.take == 1:
             distance = 1500
             for item in crystals:
                 x = item.pos[0]
                 y = item.pos[1]
                 x_main = mainer.pos[0]			
                 y_main = mainer.pos[1]
                 x-=x_main
                 y-=y_main
                 xd=math.sqrt(y*y+x*x)
                 xd = int(xd)
                 if distance >= xd: 
                    distance = xd 
                    choosItem = item
	    if mainer.take == 0:
             distance = 1500
             for item in centres:
                 x = item.pos[0]
                 y = item.pos[1]
                 x_main = mainer.pos[0]			
                 y_main = mainer.pos[1]
                 x-=x_main
                 y-=y_main
                 xd=math.sqrt(y*y+x*x)
                 xd = int(xd)
                 if distance >= xd: 
                    distance = xd 
                    choosItem = item
   					

	    distance_X = choosItem.pos[0] - mainer.pos[0]
	    distance_Y = choosItem.pos[1] - mainer.pos[1]
	    distance_C = math.sqrt(distance_Y*distance_Y+distance_X*distance_X)
	    cos = distance_X/distance_C
	    sin = distance_Y/distance_C
	    mainer.pos[0]+=cos
	    mainer.pos[1]+=sin
	    rot_sin = math.asin(sin)/math.pi*180
	    rot_cos = math.acos(cos)/math.pi*180
	    if mainer.pos[0]<choosItem.pos[0] and mainer.pos[1]>choosItem.pos[1]: mainer.rot[0] = 180 + rot_cos
	    if mainer.pos[0]<choosItem.pos[0] and mainer.pos[1]<choosItem.pos[1]: mainer.rot[0] = 180 - rot_cos
	    if mainer.pos[0]>choosItem.pos[0] and mainer.pos[1]>choosItem.pos[1]: mainer.rot[0] = 180 + rot_cos
	    if mainer.pos[0]>choosItem.pos[0] and mainer.pos[1]<choosItem.pos[1]: mainer.rot[0] = 180 - rot_cos
	    if distance_C < choosItem.r_size: 
                    if mainer.take == 0:  mainer.take = 1
                    elif mainer.take == 1:  mainer.take = 0
					
    text = font.render("Score: cos "+str(rot_cos)+"Score sin "+str(rot_sin),True,black)
    sc.blit(text, [0,0])
    time.sleep(0.01)
    pygame.display.flip()

    key = pygame.key.get_pressed()
    cam.update(dt,key)