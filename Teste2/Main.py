from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import math

inicio = Builder.load_file('Main.kv')

class jInicio(Screen):
   pass

class jCondutor(Screen):
    pass

class jcCorrente(Screen):
    def Ccondutor(self):
        c = float(self.ids.mcA.text)
        f = float(self.ids.mcFs.text)
        
        self.ids.Rmc.text = str(round(c*f, 3)) + 'A'
    pass
        
class jcQueda(Screen):
    
#    def radioOpcao(self, instancia,valor, numero):
#        if valor == True:
#            fc = numero
#            pass
#        else:
#            fc = numero
#        return fc
        
    def Qcondutor(self):
        p = float(self.ids.mqp.text)
        a = float(self.ids.mqA.text)
        fi = float(self.ids.mqfi.text)
        l = float(self.ids.mql.text)
        qv = float(self.ids.mqqv.text)
        v = float(self.ids.mqv.text)
        fc = radioOpcao()
        
        self.ids.Rmq.text = str(round((fc*p*a*l*fi)/(v/100*qv)),3) + 'mm^2'
    pass

class jcAxm(Screen):
    def AMcondutor(self):
        c = float(self.ids.mamA.text)
        f = float(self.ids.mamM.text)
        
        self.ids.Ram.text = str(round(c*f,3)) + 'Am'           
    pass
    
class jContator(Screen):
    def calcContator(self):
        c = float(self.ids.cA.text)
        f = float(self.ids.cFs.text)
        
        self.ids.Rc.text = str(round(c*f,3)) + 'A'      
    pass

class jRele(Screen):
        def calcRele(self):
            c = float(self.ids.rA.text)
            f = float(self.ids.rFs.text)
            
            self.ids.Rrl.text = str(round(c*f,2)) + 'A'
        pass

class jFusivel(Screen):
    def calcFusivel(self):
        c = float(self.ids.fA.text)
        f = float(self.ids.fFs.text)
        
        self.ids.Rf.text = str(round(c*f,2)) + 'A'        
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
        tela.add_widget(jContator(name="jContator"))
        tela.add_widget(jRele(name='jRele'))
        tela.add_widget(jFusivel(name="jFusivel"))
        tela.add_widget(jCorrenteN(name='jCorrenteN'))
        tela.add_widget(jCorrenteP(name='jCorrenteP'))
        tela.add_widget(IPin(name='IPin'))
        tela.add_widget(IPfs(name='IPfs'))
        
        return tela
        
if __name__ == '__main__':
    Dapp().run()