import sys

class Map:
    def __init__(self):
        self.mainers = []
        self.centres = []
        self.crystals = []
        self.obstacles = []
        self.marines = []

    def getMainers(self):
        sys.path.append('..')
        from core import Mainer 
        sys.path.pop()
        self.mainers.append(Mainer('red',(200,310)))
        self.mainers.append(Mainer('red',(200,323)))
        self.mainers.append(Mainer('red',(220,312)))
        self.mainers.append(Mainer('blue',(500,410)))
        self.mainers.append(Mainer('blue',(100,310)))
        self.mainers.append(Mainer('blue',(600,320)))
        self.mainers.append(Mainer('blue',(600,210)))
        self.mainers.append(Mainer('blue',(456,1100)))
        self.mainers.append(Mainer('blue',(700,1903)))
        self.mainers.append(Mainer('blue',(900,2345)))
        self.mainers.append(Mainer('blue',(600,2345)))
        self.mainers.append(Mainer('blue',(620,2345)))
        self.mainers.append(Mainer('blue',(640,2345)))
        del Mainer
        return self.mainers
		
		
		
    def getMarines(self):
        sys.path.append('..')
        from core import Marine 
        sys.path.pop()
        self.marines.append(Marine('red',(300,310)))
        self.marines.append(Marine('blue',(300,343)))
        del Marine
        return self.marines
	
    def getCentres(self):
        sys.path.append('..')
        from core import Centre 
        sys.path.pop()
        self.centres.append(Centre('red',(0,0)))
        self.centres.append(Centre('red',(250,600)))
        self.centres.append(Centre('red',(590,100)))
        self.centres.append(Centre('red',(100,250)))
        self.centres.append(Centre('blue',(450,1400)))
        self.centres.append(Centre('blue',(590,1040)))
        self.centres.append(Centre('blue',(100,1504)))
        del Centre
        return self.centres
		
    def getCrystals(self):
        sys.path.append('..')
        from core import Crystal 
        sys.path.pop()
        self.crystals.append(Crystal((150,400)))
        self.crystals.append(Crystal((500,500)))
        self.crystals.append(Crystal((600,310)))
        self.crystals.append(Crystal((450,900)))
        self.crystals.append(Crystal((600,1300)))
        self.crystals.append(Crystal((700,1310)))
        del Crystal
        return self.crystals
		
    def getObstacles(self):
        sys.path.append('..')
        from core import Obstacle 
        sys.path.pop()
        self.obstacles.append(Obstacle((165,500)))
        self.obstacles.append(Obstacle((215,500)))
        self.obstacles.append(Obstacle((265,500)))
        self.obstacles.append(Obstacle((315,500)))
        self.obstacles.append(Obstacle((365,500)))
        self.obstacles.append(Obstacle((415,500)))
        self.obstacles.append(Obstacle((415,500)))
        self.obstacles.append(Obstacle((165,450)))
        self.obstacles.append(Obstacle((165,500)))
        self.obstacles.append(Obstacle((165,550)))
        self.obstacles.append(Obstacle((165,600)))
        self.obstacles.append(Obstacle((165,700)))
        self.obstacles.append(Obstacle((165,650)))
        self.obstacles.append(Obstacle((165,800)))
        self.obstacles.append(Obstacle((165,750)))
        y = -200
        x = -200
        while (x<1000):
                self.obstacles.append(Obstacle((x,y)))
                x+=50
        y = -200
        x = -200
        while (y<3000):
                self.obstacles.append(Obstacle((x,y)))
                y+=50
        y = 3000
        x = 1000
        while (x>=(-200)):
                self.obstacles.append(Obstacle((x,y)))
                x-=50
        y = 3000
        x = 1000
        while (y>=(-200)):
                self.obstacles.append(Obstacle((x,y)))
                y-=50
        del Obstacle
        return self.obstacles
		
