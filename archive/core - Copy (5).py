import pygame, sys, math, time
from pygame.locals import *
class Resours:
    def __init__(self,res=(0,0)):
        self.res = list(res)

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
        self.give_1 = 0
        self.cost = 0
		
    def supply(self):
        return self.cost
		
    def queue_m(self):
        self.give_1 = 0
		
    def switching(self):
        self.give_1+=1	
        if self.give_1>15: self.give_1 = 0
		
    def update(self,x,y):
        self.pos[0]+=x
        self.pos[1]+=y
	
    def getPosition_x(self):
        return self.pos[0]
		
    def getPosition_y(self):
        return self.pos[1]		
		
class Mainer:
    def __init__(self,pos=(0,0),rot=(0,0,0),data_protections=(100,10,10,10)):
        self.pos = list(pos)
        self.rot = list(rot)
        self.data_protections = list(data_protections)
        self.dog = pygame.image.load('pictures/mainer.png')
        self.take = 1
        self.take_1 = 0
        self.r_size = 14.1
        self.speed = 1
        self.cos = 0
        self.sin = 1
        self.cost = 0
		
    def update(self,x,y):
        self.pos[0]+=x
        self.pos[1]+=y
	
    def getPosition_x(self):
        return self.pos[0]
		
    def getPosition_y(self):
        return self.pos[1]		
		
    def getChosen(self):
        if self.take == 1:
    	     distance = 1500
    	     for item in crystals:
    	         x = item.pos[0]
    	         y = item.pos[1]
    	         x_main = self.pos[0]			
    	         y_main = self.pos[1]
    	         x-=x_main
    	         y-=y_main
    	         xd=math.sqrt(y*y+x*x)
    	         xd = int(xd)
    	         if distance >= xd: 
    	             distance = xd 
    	             self.choose = item
				  
        if self.take == 0:
    	     distance = 1500
    	     for item in centres:
    	         x = item.pos[0]
    	         y = item.pos[1]
    	         x_main = self.pos[0]			
    	         y_main = self.pos[1]
    	         x-=x_main
    	         y-=y_main
    	         xd=math.sqrt(y*y+x*x)
    	         xd = int(xd)
    	         if distance >= xd: 
      	             distance = xd 
      	             self.choose = item
        return self.choose				

    def getVector(self):
        self.choosItem = self.getChosen()
        distance_X = self.choosItem.pos[0] - self.pos[0]
        distance_Y = self.choosItem.pos[1] - self.pos[1]
        distance_C = math.sqrt(distance_Y*distance_Y+distance_X*distance_X)
        if distance_C == 0: 
             self.cos = 0
             self.sin = 0
        else:
             self.cos = distance_X/distance_C
             self.sin = distance_Y/distance_C
        preposition_x = self.pos[0]
        preposition_y = self.pos[1]
        cheker = 0
        for object in mainers:
             avoid = []
             cheker = 0
             cheker_2 = 0
             preposition_x = self.pos[0] + self.cos*object.r_size*4
             preposition_y = self.pos[1] + self.sin*object.r_size*4
             nearposition_x = self.pos[0] + self.cos*self.r_size*1.5
             nearposition_y = self.pos[1] + self.sin*self.r_size*1.5
             if object == self:
                 cheker-=10
                 cheker_2-=10  				 
             if object.pos[0]+object.r_size>preposition_x>object.pos[0]-object.r_size: cheker+=1
             if object.pos[1]+object.r_size>preposition_y>object.pos[1]-object.r_size: cheker+=1
             if object.pos[0]+object.r_size+1>=nearposition_x>object.pos[0]-object.r_size-1: cheker_2+=1
             if object.pos[1]+object.r_size+1>=nearposition_y>object.pos[1]-object.r_size-1: cheker_2+=1
             if cheker == 2:
                 if self.rot[1]<42: self.rot[1]+=3
                 break
             elif self.rot[1]>0.1 and cheker<2: self.rot[1]-=0.1
        self.cos = self.cos*math.cos(math.radians(self.rot[1]))-self.sin*math.sin(math.radians(self.rot[1]))
        self.sin = self.sin*math.cos(math.radians(self.rot[1]))+self.cos*math.sin(math.radians(self.rot[1]))
        self.pos[0]+=self.cos*self.speed
        self.pos[1]+=self.sin*self.speed
        rot_cos = math.acos(self.cos)/math.pi*180
        if self.pos[0]<=self.choosItem.pos[0] and self.pos[1]>=self.choosItem.pos[1]: self.rot[0] = 180 + rot_cos
        if self.pos[0]<=self.choosItem.pos[0] and self.pos[1]<=self.choosItem.pos[1]: self.rot[0] = 180 - rot_cos
        if self.pos[0]>=self.choosItem.pos[0] and self.pos[1]>=self.choosItem.pos[1]: self.rot[0] = 180 + rot_cos
        if self.pos[0]>=self.choosItem.pos[0] and self.pos[1]<=self.choosItem.pos[1]: self.rot[0] = 180 - rot_cos
        if distance_C < self.choosItem.r_size: 
                    if self.take == 0:
                         if self.choosItem.give_1 == 15: 
                             self.take = 1
                             resours.res[0]+=self.cost
                             self.cost = self.choosItem.supply()
                             self.choosItem.give_1 = 0
                    elif self.take == 1:  
                         if self.choosItem.give_1 == 200: 
                             self.take = 0
                             resours.res[0]+=self.cost
                             self.cost = self.choosItem.supply()
                             self.choosItem.give_1 = 0

class Crystal:
    def __init__(self,pos=(0,0),data_protections=(100,10)):
        self.pos = list(pos)
        self.data_protections = list(data_protections)
        self.dog = pygame.image.load('pictures/resours1.png')
        self.r_size = 1.41*15
        self.give_1 = 0
        self.cost = 5
		
    def getPosition_x(self):
        return self.pos[0]
		
    def getPosition_y(self):
        return self.pos[1]
		
    def supply(self):
        return self.cost
		
    def switching(self):
        self.give_1+=1	
        if self.give_1>200: self.give_1 = 0
		
verts = (10,50),(100,50),(50,150),(550,350)
verts2 = (120,50),(40,50),(520,150),(250,350),(850,350)
minerals = 0
resours = Resours((0,0))
cam = Cam((0,0))
mainers = [] 
mainers.append(Mainer((200,310)))
mainers.append(Mainer((200,323)))
mainers.append(Mainer((220,312)))
mainers.append(Mainer((500,410)))
mainers.append(Mainer((100,310)))
mainers.append(Mainer((600,320)))
mainers.append(Mainer((600,210)))
mainers.append(Mainer((456,1100)))
mainers.append(Mainer((600,1903)))
mainers.append(Mainer((1600,2345)))
mainers.append(Mainer((600,2345)))
mainers.append(Mainer((1620,2345)))
mainers.append(Mainer((1640,2345)))


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
        mainer.getVector()
    for centre in centres:			
        centre.switching()
    for crystal in crystals:
        crystal.switching()

    text = font.render("Minerals: "+str(resours.res[0]),True,black)
    sc.blit(text, [0,0])
    time.sleep(0.01)
    pygame.display.flip()

    key = pygame.key.get_pressed()
    cam.update(dt,key)
	
	