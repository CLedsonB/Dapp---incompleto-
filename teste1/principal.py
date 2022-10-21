from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
#from kivy.uix.screenmanager import ScreenManager, Screen


#class jInicio(ScreenManager):
#    pass

#class jMenu(Screen):
#    pass

#class jCondutor(Screen):
#    pass

#class jContator(Screen):
#    pass

#class jRele(Screen):
#    pass

#class jFusivel(Screen):
#    pass

#class jCorrente(Screen):
#    pass


inicio = Builder.load_file('principal.kv')

class Dapp(App):
    def build(self):
        return inicio
        
if __name__ == '__main__':
    Dapp().run()