from panda3d.core import loadPrcFileData, CardMaker
from panda3d.core import WindowProperties, NodePath
from direct.showbase.ShowBase import ShowBase

loadPrcFileData("","win-size 800 600")
loadPrcFileData("","window-title Quadrado na tela")

class MyApp(ShowBase):
    def __init__(self):
        super().__init__()
        self.disable_mouse()

        cm = CardMaker("meu_quadrado")
        cm.setFrame(-0.1, 0.1, -0.1, 0.1)
        quadrado = NodePath(cm.generate())
        quadrado.setColor(-50,0,0,-50)
        


        quadrado.setPos(-0.8,0,0)

        quadrado.reparentTo(self.render2d)

MyApp().run()

