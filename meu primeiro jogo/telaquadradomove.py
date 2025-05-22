from panda3d.core import loadPrcFileData, CardMaker, NodePath
from direct.showbase.ShowBase import ShowBase

loadPrcFileData("","win-size 800 600")
loadPrcFileData("","window-title Quadrado na tela")

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()
        self.disable_mouse()

        cm = CardMaker("quadrado")
        cm.setFrame(-0.1, 0.1, -0.1, 0.1)

        self.quadrado = NodePath(cm.generate())
        self.quadrado.setColor(1,0,0,1)
        self.quadrado.setPos(0,0,0)
        self.quadrado.reparentTo(self.render2d)

        self.velocidade = 0.09


        self.accept("arrow_up", self.mover,[0,1])
        self.accept("arrow_down", self.mover,[0,-1])
        self.accept("arrow_left",self.mover,[-1,0])
        self.accept("arrow_right",self.mover,[1,0])

    def mover(self,dx,dz):
        x = self.quadrado.getX()
        z = self.quadrado.getZ()
        self.quadrado.setPos(x + dx * self.velocidade, 0, z + dz * self.velocidade)

MyApp().run()















