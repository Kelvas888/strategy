import pygame, sys, math, time
from pygame.locals import *
from maps.dimention import Map

class Resours:
    def __init__(self,res=(0,0)):
        self.res = list(res)
        self.cheker = 0
        self.unit_dog = pygame.image.load('pictures/prorertiesUnit.png')
        self.dog_unit = self.unit_dog	
        self.queue = []	
        self.queue_place = 0	
        self.res[0] = 5050
        self.alliance = 'blue'	
		
		
class Cam:
    def __init__(self,pos=(0,0),rot=(0,0)):
        self.dt = 0
        self.s = 0
        self.corner = 1
        self.pos = list(pos)
        self.rot = list(rot)
        self.pos_m = (0,0)
        self.pos_p = (0,0)
        self.choosObject = list()
        self.onclick = 0
        self.mousemotion = 0
        self.object = 0
        self.width=sc.get_width()
        self.height=sc.get_height()
        self.choosArea = 0
        self.areaEvent = 0
        self.rectPosition = list((0,0,0,0))
        self.lshift = 0
        self.k_q = 0
        self.k_z = 0
        self.k_a = 0

    def update(self,key):
        self.s = self.dt*40

        if key[pygame.K_UP]: self.pos[1]+=self.s
        if key[pygame.K_DOWN]: self.pos[1]-=self.s

        if key[pygame.K_LEFT]: self.pos[0]+=self.s
        if key[pygame.K_RIGHT]: self.pos[0]-=self.s


    def findobject(self,pos_m=(0,0)):
        self.pos_m = pos_m
        for self.object in mainers:
             self.cheker = 0
             if self.object.pos[0]+self.object.r_size>pos_m[0]-self.pos[0]>self.object.pos[0]-self.object.r_size: self.cheker+=1
             if self.object.pos[1]+self.object.r_size>pos_m[1]-self.pos[1]>self.object.pos[1]-self.object.r_size: self.cheker+=1
             if self.cheker == 2:
                  self.object.dog = self.object.frame_dog
                  if self.choosObject.count(self.object) == 0: self.choosObject.append(self.object)
                  if self.onclick == 1 and self.choosObject[-1].takeclick == 0: self.choosObject[-1].takeclick = 1
                  break
             elif len(self.choosObject) != 0 and self.choosObject[-1].takeclick == 0:
                  self.choosObject[-1].dog = self.choosObject[-1].just_dog
                  if self.onclick == 0 and self.choosObject[-1].takeclick == 0: self.choosObject.pop()
             elif len(self.choosObject) != 0:
                  if self.onclick == 3 and self.choosObject[-1].takeclick == 1:
                         for select_object in self.choosObject:
                             select_object.takeclick = 0
                             select_object.dog = select_object.just_dog
                             self.choosObject = []
                         break
                  if self.onclick == 1 and self.choosObject[-1].takeclick == 1 and self.k_a == 1 and self.choosObject[-1].alliance == resours.alliance:
                         for select_object in self.choosObject:
                             select_object.attack((pos_m[0]-cam.pos[0],pos_m[1]-cam.pos[1]))
                         break
                  if self.onclick == 1 and self.choosObject[-1].takeclick == 1:
                         for select_object in self.choosObject:
                             if len(select_object.targets)>0 and self.lshift == 0: select_object.targets.clear()
                             select_object.targets.insert(0, Target(0,(pos_m[0]-cam.pos[0],pos_m[1]-cam.pos[1])))
                             select_object.targets[0].amouts = len(self.choosObject)
                             select_object.take = 3
                             select_object.calculator = 1
                             select_object.order_t = -1
                         break


        if self.mousemotion == 1:
             if pos_m[0]<self.width/4 and pos_m[1]<self.height/4: self.corner = 0.7
             elif pos_m[0]<self.width/4 and pos_m[1]>self.height-self.height/4: self.corner = 0.7
             elif pos_m[0]>self.width-self.width/4 and pos_m[1]<self.height/4: self.corner = 0.7
             elif pos_m[0]>self.width-self.width/4 and pos_m[1]>self.height-self.height/4: self.corner = 0.7
             else: self.corner = 1
             if pos_m[0]<self.width/4 and self.pos_p[0]>pos_m[0] or pos_m[0] == 0:
                  self.pos[0]+=self.s*self.corner
                  self.pos_p = pos_m
             if pos_m[0]>self.width-self.width/4 and self.pos_p[0]<pos_m[0]:
                  self.pos[0]-=self.s*self.corner
                  self.pos_p = pos_m
             if pos_m[1]<self.height/4 and self.pos_p[1]>pos_m[1]:
                  self.pos[1]+=self.s*self.corner
                  self.pos_p = pos_m
             if pos_m[1]>self.height-self.height/4 and self.pos_p[1]<pos_m[1]:
                  self.pos[1]-=self.s*self.corner
                  self.pos_p = pos_m

        if pos_m[0] == 0:
             self.pos[0]+=self.s*self.corner
             self.pos_p = pos_m
        if pos_m[0] >= self.width-1:
             self.pos[0]-=self.s*self.corner
             self.pos_p = pos_m
        if pos_m[1] == 0:
             self.pos[1]+=self.s*self.corner
             self.pos_p = pos_m
        if pos_m[1] >= self.height-1:
             self.pos[1]-=self.s*self.corner
             self.pos_p = pos_m

        if self.choosArea == 1:
             if self.areaEvent == 0:
                  self.rectPosition[0] = pos_m[0]-self.pos[0]
                  self.rectPosition[1] = pos_m[1]-self.pos[1]
                  self.rectPosition[2] = pos_m[0]-self.pos[0]
                  self.rectPosition[3] = pos_m[1]-self.pos[1]
                  self.areaEvent = 1

             if self.areaEvent == 1:
                  self.rectPosition[2] = pos_m[0]-self.pos[0]
                  self.rectPosition[3] = pos_m[1]-self.pos[1]
        else:
                  self.areaEvent = 0
                  self.rectPosition[0] = 0
                  self.rectPosition[1] = 0
                  self.rectPosition[2] = 0
                  self.rectPosition[3] = 0

        for self.object in mainers:
                  self.cheker = 0
                  if self.rectPosition[0]>=self.object.pos[0]>self.rectPosition[2]: self.cheker+=1
                  if self.rectPosition[1]>=self.object.pos[1]>self.rectPosition[3]: self.cheker+=1
                  if self.rectPosition[0]<=self.object.pos[0]<self.rectPosition[2]: self.cheker+=1
                  if self.rectPosition[1]<=self.object.pos[1]<self.rectPosition[3]: self.cheker+=1
                  if self.cheker == 2:
                     self.object.dog = self.object.frame_dog
                     if self.choosObject.count(self.object) == 0: self.choosObject.append(self.object)
                     if self.choosObject[-1].takeclick == 0: self.choosObject[-1].takeclick = 1




        for self.object in centres:
             self.cheker = 0
             if self.object.pos[0]+self.object.r_size>pos_m[0]-self.pos[0]>self.object.pos[0]-self.object.r_size: self.cheker+=1
             if self.object.pos[1]+self.object.r_size>pos_m[1]-self.pos[1]>self.object.pos[1]-self.object.r_size: self.cheker+=1
             if self.cheker == 2:
                  self.object.dog = self.object.frame_dog
                  if self.onclick == 1 and self.object.takeclick == 0: self.object.takeclick = 1
                  if resours.queue.count(self.object) == 0: resours.queue.append(self.object)
                  break
             elif len(resours.queue) != 0 and resours.queue[-1].takeclick == 0:
                  resours.queue[-1].dog = resours.queue[-1].just_dog
                  if self.onclick == 0 and resours.queue[-1].takeclick == 0: resours.queue.pop()
             elif len(resours.queue) != 0:
                  if self.onclick == 3 and resours.queue[-1].takeclick == 1:
                     for select_object in resours.queue: 
                         select_object.takeclick = 0
                         select_object.dog = select_object.just_dog
                         resours.queue = []
                     break
                  if self.onclick == 1 and resours.queue[-1].takeclick == 1:
                     for select_object in resours.queue:
                         select_object.position = (pos_m[0]-cam.pos[0],pos_m[1]-cam.pos[1])
                     break

        if len(resours.queue) != 0 and self.k_q == 1 and resours.res[0]>=50: self.produceUnit(0)
        if len(resours.queue) != 0 and self.k_z == 1 and resours.res[0]>=50: self.produceUnit(1)

    def produceUnit(self,type):
             self._min = 10
             for develop in resours.queue:
                  if len(develop.typeUnit) < self._min:
                     self._min = len(develop.typeUnit)
                     choosDevelop = develop
             try:
                  choosDevelop.typeUnit.append(type)
                  choosDevelop.timeUnit.append(400)
                  resours.res[0]-=50
             except UnboundLocalError: pass
             self.k_q = 3
             self.k_z = 3
			 
class Target:
    def __init__(self,type,pos=(0,0)):
        self.pos = pos
        self.r_size = 1
        self.type = type
        self.amoutsGet = 0


class Obstacle:
    def __init__(self,pos=(0,0),rot=(0,0),data_protections=(1000,100,100,100)):
        self.pos = list(pos)
        self.rot = list(rot)
        self.data_protections = list(data_protections)
        self.dog = obstacle_dog
        self.r_size = 1.41*25

class Centre:
    def __init__(self,alliance,pos=(0,0),rot=(0,0),data_protections=(1000,100,100,100)):
        self.alliance = alliance
        self.pos = list(pos)
        self.rot = list(rot)
        self.takeclick = 0
        self.data_protections = list(data_protections)
        self.frame_dog = pygame.image.load('pictures/'+self.alliance+'/frameBB.png')
        self.just_dog = pygame.image.load('pictures/'+self.alliance+'/BB.png')
        self.dog = self.just_dog
        self.unit_center = pygame.image.load('pictures/iconBB.png')
        self.center_unit = self.unit_center	
        self.r_size = 1.41*25
        self.give_1 = 0
        self.cost = 0
        self.typeUnit = []
        self.timeUnit = []
        self.__position = (self.pos[0]+self.r_size,self.pos[1]+self.r_size)

    @property
    def position(self):
        return self.__position
		
    @position.setter
    def position(self,position):
        self.__position = position

    def produceUnit(self):
        if len(self.timeUnit) > 0:
            if self.timeUnit[0]>0: self.timeUnit[0]-=1
            else: 
			
    	         if self.typeUnit[0] == 0: 
    	             newbee = Mainer(self.alliance,(self.pos[0],self.pos[1]))
    	             mainers.insert(0,newbee)
    	         if self.typeUnit[0] == 1: 
    	             newbee = Marine(self.alliance,(self.pos[0],self.pos[1]))
    	             mainers.insert(0,newbee)
    	             newbee.targets.insert(0, Target(0,(self.__position)))
    	             newbee.take = 3
    	             newbee.order_t = -1
    	         self.timeUnit.pop(0)
    	         self.typeUnit.pop(0)

		
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
    def __init__(self,alliance,pos=(0,0),rot=(0,0,0),data_protections=(100,10,10,10)):
        self.alliance = alliance
        self.pos = list(pos)
        self.rot = list(rot)
        self.data_protections = list(data_protections)
        self.frame_dog = pygame.image.load('pictures/'+self.alliance+'/framemainer.png')
        self.just_dog = pygame.image.load('pictures/'+self.alliance+'/mainer.png')
        self.dog = self.just_dog
        self.viewres = pygame.image.load('pictures/emptyres.png')
        self.takeclick = 0
        self.take = 1
        self.take_1 = 0
        self.r_size = 14.1
        self.speedNormal = 1
        self.speed = self.speedNormal
        self.cos = 0
        self.sin = 1
        self.cost = 0
        self.order_t = 0
        self.targets = []
        self.calculator = 1
        self.distance_C = 1


		
    def attack(self,select_position):
        whizzbangs.insert(0, Whizzbang(self.alliance,self.pos,select_position))

		
    def update(self,x,y):
        self.pos[0]+=x
        self.pos[1]+=y

    def getPosition_x(self):
        return self.pos[0]

    def getPosition_y(self):
        return self.pos[1]

    def getObstacle(self):
        nearposition_x = self.pos[0] + self.cos
        nearposition_y = self.pos[1] + self.sin
        for obstacle in obstacles:
    	     cheker_2 = 0
    	     if obstacle.pos[0]+obstacle.r_size>=nearposition_x>obstacle.pos[0]-obstacle.r_size: cheker_2+=1
    	     if obstacle.pos[1]+obstacle.r_size>=nearposition_y>obstacle.pos[1]-obstacle.r_size: cheker_2+=1
    	     if cheker_2 == 2: break
        if len(self.targets)>0 and self.targets[-1].type == 2: cheker_2 = 2
        return cheker_2

    def getPath(self, distance_C):
        nearposition_x = self.pos[0] + self.cos*self.r_size*4
        nearposition_y = self.pos[1] + self.sin*self.r_size*4
        if distance_C<self.r_size*4: breaker = 1
        else: breaker = 0
        for obstacle in obstacles:
    	     cheker_2 = 0
    	     if breaker == 1: break
    	     if obstacle.pos[0]+obstacle.r_size>=nearposition_x>obstacle.pos[0]-obstacle.r_size: cheker_2+=1
    	     if obstacle.pos[1]+obstacle.r_size>=nearposition_y>obstacle.pos[1]-obstacle.r_size: cheker_2+=1
    	     if cheker_2 == 2:
    	         nearposition_x = self.pos[0] + (self.cos*math.cos(math.radians(90))-self.sin*math.sin(math.radians(90)))*self.r_size*4
    	         nearposition_y = self.pos[1] + (self.sin*math.cos(math.radians(90))+self.cos*math.sin(math.radians(90)))*self.r_size*4
    	         if len(self.targets)>0 and self.targets[-1].type == 1: self.targets.pop()
    	         self.targets.append(Target(1,(nearposition_x,nearposition_y)))
    	         self.calculator = 1
    	         self.take = 3
    	         self.order_t = -1
    	         break

        return cheker_2

    def getChosen(self):
        self.calculator = 0

        if self.take == 3:
    	     self.choose = self.targets[self.order_t]


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

		
    def getDirection(self):
        distance_X = self.choosItem.pos[0] - self.pos[0]
        distance_Y = self.choosItem.pos[1] - self.pos[1]
        self.distance_C = math.sqrt(distance_Y*distance_Y+distance_X*distance_X)
        if self.distance_C == 0:
             self.cos = 0
             self.sin = 0
        else:
             self.cos = distance_X/self.distance_C
             self.sin = distance_Y/self.distance_C
		
		
    def getVector(self):
        if self.calculator == 1: 
             self.choosItem = self.getChosen()
        self.getDirection()
        preposition_x = self.pos[0]
        preposition_y = self.pos[1]
        cheker = 0
        for object in mainers:
             avoid = []
             cheker = 0
             preposition_x = self.pos[0] + self.cos*object.r_size*4
             preposition_y = self.pos[1] + self.sin*object.r_size*4
             if object == self: cheker-=10
             if object.pos[0]+object.r_size>preposition_x>object.pos[0]-object.r_size: cheker+=1
             if object.pos[1]+object.r_size>preposition_y>object.pos[1]-object.r_size: cheker+=1
             if cheker == 2:
                 if self.rot[1]<42: self.rot[1]+=3
                 break
             elif self.rot[1]>0.1 and cheker<2: self.rot[1]-=0.1
        if self.getObstacle() == 2: self.speed = 0
        else: self.speed = self.speedNormal
        self.getPath(self.distance_C)
        self.cos = self.cos*math.cos(math.radians(self.rot[1]))-self.sin*math.sin(math.radians(self.rot[1]))
        self.sin = self.sin*math.cos(math.radians(self.rot[1]))+self.cos*math.sin(math.radians(self.rot[1]))
        self.pos[0]+=self.cos*self.speed
        self.pos[1]+=self.sin*self.speed
        self.getRot()
        if self.distance_C < self.choosItem.r_size: self.getTake()

    def getRot(self):
        rot_cos = math.acos(self.cos)/math.pi*180
        if self.pos[1]>=self.choosItem.pos[1]: self.rot[0] = 180 + rot_cos
        if self.pos[1]<=self.choosItem.pos[1]: self.rot[0] = 180 - rot_cos
		
    def getTake(self):
        self.calculator = 1
        if self.take == 0:
             if self.choosItem.give_1 == 15:
                         self.take = 1
                         resours.res[0]+=self.cost
                         self.cost = self.choosItem.supply()
                         self.choosItem.give_1 = 0
                         self.viewres = pygame.image.load('pictures/emptyres.png')

        elif self.take == 1:
             if self.choosItem.give_1 == 200:
                         self.take = 0
                         resours.res[0]+=self.cost
                         self.cost = self.choosItem.supply()
                         self.choosItem.give_1 = 0
                         self.viewres = pygame.image.load('pictures/viewres.png')

        elif self.take == 3:
             if len(self.targets)>self.order_t*(-1):
                         #self.order_t-=1
                         self.targets.pop()
             else:
                         self.targets.pop()
                         if self.cost > 0: self.take = 0
                         if self.cost == 0: self.take = 1


class Marine(Mainer):
    def __init__(self,alliance,pos=(0,0),rot=(0,0,0),data_protections=(100,10,10,10)):
        super().__init__(alliance,pos,rot,data_protections)
        self.just_dog = pygame.image.load('pictures/'+self.alliance+'/marine.png')
        self.frame_dog = pygame.image.load('pictures/'+self.alliance+'/framemarine.png')
        self.targets.insert(0, Target(2,(self.pos[0]+self.cos*5,self.pos[1]+self.sin*5)))
        self.take = 1
        self.order_t = -1
        self.dog = self.just_dog
		
    def getChosen(self):
        self.calculator = 0
        if self.take == 3:
    	     if self.targets[self.order_t].type == 2: self.targets.pop()
    	     self.choose = self.targets[self.order_t]


        if self.take == 1:
    	     self.choose = self.targets[self.order_t]

        return self.choose

    def getTake(self):
        self.calculator = 1
        if self.take == 3:
             if len(self.targets)>self.order_t*(-1):
                         self.targets.pop()

             else:
                         self.targets.pop()
                         self.targets.insert(0, Target(2,(self.pos[0]+self.cos*50,self.pos[1]+self.sin*50)))
                         self.order_t = -1
                         self.take = 1

class Whizzbang(Mainer):
    def __init__(self,alliance,pos=(0,0),tar=(0,0)):
        super().__init__(alliance,pos)
        self.just_dog = pygame.image.load('pictures/whizzbang.png')
        self.dog = self.just_dog
        self.tar = list(tar)
        self.r_size = 1		
        self.speedNormal = 15
        self.speed = self.speedNormal
        self.targets.insert(0, Target(0,self.tar))
        self.take = 3
        self.order_t = -1
        self.__lifeTime = 30

    def getRot(self):
        if self.__lifeTime>=30:
             rot_cos = math.acos(self.cos)/math.pi*180
             if self.pos[1]>=self.choosItem.pos[1]: self.rot[0] = 180 + rot_cos
             if self.pos[1]<=self.choosItem.pos[1]: self.rot[0] = 180 - rot_cos

    def getDirection(self):
        if self.__lifeTime>=30:
             distance_X = self.choosItem.pos[0] - self.pos[0]
             distance_Y = self.choosItem.pos[1] - self.pos[1]
             self.distance_C = math.sqrt(distance_Y*distance_Y+distance_X*distance_X)
             self.cos = distance_X/self.distance_C
             self.sin = distance_Y/self.distance_C	
		
    def lifeTime(self,time):
        self.__lifeTime-=time
        if self.__lifeTime<1:
             whizzbangs.remove(self)   
             self.__del__()			 
             del self
		
    def __del__(self):
        pass		
		
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


pygame.init()
black = (0,0,0)
sc = pygame.display.set_mode((1000, 600), pygame.DOUBLEBUF)
#sc = pygame.display.set_mode((1000, 600), pygame.FULLSCREEN)
sc.fill((100, 150, 200))
pygame.display.set_caption("Окно игры")
resours = Resours((0,0))
cam = Cam((0,0))
obstacle_dog = pygame.image.load('pictures/obstacle.png')
map = Map()
mainers = []
centres = []
crystals = []
obstacles = []
whizzbangs = []
mainers.extend(map.getMainers())
mainers.extend(map.getMarines())
centres.extend(map.getCentres())
crystals.extend(map.getCrystals())
obstacles.extend(map.getObstacles())
clock = pygame.time.Clock()
list_object = []
list_object.extend(mainers)
list_object.extend(centres)
list_object.extend(crystals)
#with open('pictures/0.bmp', 'rb') as f:
    #data = bytearray(f.read())
font = pygame.font.Font(None, 15)
#text = font.render("Score: "+str(data),True,black)
#print(data)
while True:
    cam.dt = clock.tick()/1000*6
    cam.onclick = 0
    cam.mousemotion = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT: mainLoop = False; pygame.quit(); sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
                 if event.button == 1: cam.onclick = 1
                 if event.button == 3: cam.onclick = 3
        if event.type == pygame.MOUSEMOTION:
                 cam.mousemotion = 1
                 cam.choosArea = event.buttons[0]
        if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_LSHIFT: cam.lshift = 1
                 if event.key == pygame.K_q and cam.k_q != 3: cam.k_q = 1
                 if event.key == pygame.K_z and cam.k_z != 3: cam.k_z = 1
                 if event.key == pygame.K_a and cam.k_a == 0: cam.k_a = 1
                 elif event.key == pygame.K_a and cam.k_a == 1: cam.k_a = 0
        if event.type == pygame.KEYUP:
                 if event.key == pygame.K_LSHIFT: cam.lshift = 0
                 if event.key == pygame.K_q: cam.k_q = 0
                 if event.key == pygame.K_z: cam.k_z = 0
    sc.fill((100, 150, 200))
    #sc.blit(text, [0,0])

    for mainer in mainers:
        dog_rect = mainer.dog.get_rect(bottomright=(mainer.r_size+mainer.pos[0]+cam.pos[0],mainer.r_size+mainer.pos[1]+cam.pos[1]))
        dog = pygame.transform.rotate(mainer.dog, mainer.rot[0])
        viewres_rect  = mainer.viewres.get_rect(bottomright=(mainer.r_size/1.5+mainer.pos[0]+cam.pos[0],mainer.r_size/1.5+mainer.pos[1]+cam.pos[1]))
        viewres = pygame.transform.rotate(mainer.viewres, mainer.rot[0])
        sc.blit(dog, dog_rect)
        sc.blit(viewres, viewres_rect)

    for crystal in crystals:
        dog_rect = crystal.dog.get_rect(bottomright=(crystal.r_size+crystal.pos[0]+cam.pos[0],crystal.r_size+crystal.pos[1]+cam.pos[1]))
        sc.blit(crystal.dog, dog_rect)

    for obstacle in obstacles:
        cheker = 0
        if sc.get_height()+50>obstacle.r_size+obstacle.pos[1]+cam.pos[1] and sc.get_width()+50>obstacle.r_size+obstacle.pos[0]+cam.pos[0]: cheker+=1
        if (-50)<obstacle.r_size+obstacle.pos[1]+cam.pos[1] and (-50)<obstacle.r_size+obstacle.pos[0]+cam.pos[0]: cheker+=1
        if cheker == 2:
                dog_rect = obstacle.dog.get_rect(bottomright=(obstacle.r_size+obstacle.pos[0]+cam.pos[0],obstacle.r_size+obstacle.pos[1]+cam.pos[1]))
                sc.blit(obstacle.dog, dog_rect)

    for centre in centres:
        dog_rect = centre.dog.get_rect(bottomright=(centre.r_size+centre.pos[0]+cam.pos[0],centre.r_size+centre.pos[1]+cam.pos[1]))
        sc.blit(centre.dog, dog_rect)

    for whizzbang in whizzbangs:
        dog_rect = whizzbang.dog.get_rect(bottomright=(whizzbang.r_size+whizzbang.pos[0]+cam.pos[0],whizzbang.r_size+whizzbang.pos[1]+cam.pos[1]))
        dog = pygame.transform.rotate(whizzbang.dog, whizzbang.rot[0])
        sc.blit(dog, dog_rect)		
	
    dog_rect = resours.dog_unit.get_rect(bottomright=(cam.width/1.5,cam.height))
    sc.blit(resours.dog_unit, dog_rect)
    resours.queue_place = 0
    for centre in resours.queue:
        resours.queue_place+=centre.r_size
        dog_rect = centre.center_unit.get_rect(bottomright=(cam.width/25,resours.queue_place))
        sc.blit(centre.center_unit, dog_rect)	

    for whizzbang in whizzbangs:
        whizzbang.getVector()
        whizzbang.lifeTime(1)				
    for mainer in mainers:
        mainer.getVector()
    for centre in centres:
        centre.switching()
        centre.produceUnit()
    for crystal in crystals:
        crystal.switching()
    pygame.draw.lines(sc, (64, 128, 255), True, [[cam.rectPosition[0]+cam.pos[0], cam.rectPosition[1]+cam.pos[1]], [cam.rectPosition[2]+cam.pos[0], cam.rectPosition[1]+cam.pos[1]], [cam.rectPosition[2]+cam.pos[0], cam.rectPosition[3]+cam.pos[1]], [cam.rectPosition[0]+cam.pos[0], cam.rectPosition[3]+cam.pos[1]]], 2)
    pos = pygame.mouse.get_pos()
    text = font.render("Minerals: "+str(resours.res[0])+"Minerals: "+str(whizzbangs),True,black)
    sc.blit(text, [0,0])
    time.sleep(0.001)
    pygame.display.flip()

    key = pygame.key.get_pressed()
    cam.update(key)
    cam.findobject(pygame.mouse.get_pos())

