from panda3d.core import loadPrcFileData
from direct.showbase.ShowBase import ShowBase

loadPrcFileData("", "win-size 800 600")
loadPrcFileData("", "window-title Minha primeira janela")

class MyApp(ShowBase):
        def _init_(self):
            super()._init_()
            self.disable_mouse()

MyApp().run()

