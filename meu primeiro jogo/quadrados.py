from panda3d.core import loadPrcFileData, CardMaker
from panda3d.core import WindowProperties, NodePath
from direct.showbase.ShowBase import ShowBase

loadPrcFileData("","win-size 800 600")
loadPrcFileData("","window-title Quadrado na tela")

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()
        self.disable_mouse()

        cm = CardMaker("quadrado1")
        cm.setFrame(-0.1, 0.1, -0.1, 0.1)
        self.quadrado1 = self.render2d.attachNewNode(cm.generate())
        self.quadrado1.setColor(-1,0,0,-1)
        self.quadrado1.setPos(-0.8,0,0)
        
        self.quadrado2 = self.render2d.attachNewNode(cm.generate())
        self.quadrado2.setColor(1,0,0,1)
        self.quadrado2.setPos(0.8,0,0)

        self.accept("arrow_up", self.mover,[self.quadrado1,0,0.1])
        self.accept("arrow_down", self.mover,[self.quadrado1,0,-0.1])
        self.accept("arrow_left",self.mover,[self.quadrado1,-0.1,0])
        self.accept("arrow_right",self.mover,[self.quadrado1,0.1,0])
        
        self.accept("w", self.mover,[self.quadrado2,0,0.1])
        self.accept("s", self.mover,[self.quadrado2,0,-0.1])
        self.accept("a",self.mover,[self.quadrado2,-0.1,0])
        self.accept("d",self.mover,[self.quadrado2,0.1,0])


    def mover(self,node,dx,dz):
        x = node.getX() + dx
        z = node.getZ() + dz
        x = max(-1 + 0.1, min(1 - 0.1, x))
        z = max(-1 + 0.1, min(1 - 0.1,z))
        node.setPos(x, 0, z)


MyApp().run()






