

from kivy.app import App
from kivy.lang import Builder
#importar o app, builder (GUI)

GUI = Builder.load_file("tela.kv")

#criar app

class MeuAplicativo(App):
    def build(self):
        return GUI