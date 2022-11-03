from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

inicio = Builder.load_file('Main.kv')

class jInicio(Screen):
   pass

class jCondutor(Screen):
    pass

class jcCorrente(Screen):
    pass

class jcQueda(Screen):
    pass

class jcAxm(Screen):
    pass
    
#class jContator(Screen):
#    pass

#class jRele(Screen):
#    pass

class jFusivel(Screen):
    pass

class jCorrenteN(Screen):
    pass
    
class jCorrenteP(Screen):
    pass

class IPin(Screen):
    pass
    
class IPfs(Screen):
    pass
               
class Dapp(App):
    def build(self):
        
        tela = ScreenManager()
        
        tela.add_widget(jInicio(name="jInicio"))
        tela.add_widget(jCondutor(name='jCondutor'))
        tela.add_widget(jcCorrente(name='jcCorrente'))
        tela.add_widget(jcQueda(name='jcQueda'))
        tela.add_widget(jcAxm(name='jcAxm'))
#        tela.add_widget(jContator(name="jContator"))
#        tela.add_widget(jRele(name='jRele'))
        tela.add_widget(jFusivel(name="jFusivel"))
        tela.add_widget(jCorrenteN(name='jCorrenteN'))
        tela.add_widget(jCorrenteP(name='jCorrenteP'))
        tela.add_widget(IPin(name='IPin'))
        tela.add_widget(IPfs(name='IPfs'))
      
        return tela
        
if __name__ == '__main__':
    Dapp().run()