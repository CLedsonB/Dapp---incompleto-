import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
from kivy.uix.widget import Widget
import time as t


class Dapp(App):
    def build(self):
        corFundo = '#DDDDDD'
        corFundoBotao = '#22FF22'
        corTextoBotao = '#FFFFFF'
        corTextoLabel = '#CCCCCC'
        fonteTamanho = '18sp'
        
        box = BoxLayout(
        orientation='vertical',
        spacing = 10,
        padding = 10
        )
        
        label1 = Label(
        text='[b]Dimensionamento[/b]',
        markup = True,
        font_size = '20sp',
        color = corTextoLabel
        )
        
        button1 = Button(
        text = 'Condutor',
        background_color = corFundoBotao,
        font_size = fonteTamanho
        )
        
        button2 = Button(
        text = 'Contator',
        background_color = corFundoBotao,
        font_size = fonteTamanho
        )
        
        button3 = Button(
        text = 'Fusível',
        background_color = corFundoBotao,
        font_size = fonteTamanho
        )
        
        button4 = Button(
        text = 'Relé Térmico',
        background_color = corFundoBotao,
        font_size = fonteTamanho
        )
        
        label2 = Label(
        text='[b]Ferramentas Extra[/b]',
        markup = True,
        font_size = '20sp',
        color = corTextoLabel
        )
        
        button5 = Button(
        text = 'Corrente de Partida',
        background_color = corFundoBotao,
        font_size = fonteTamanho
        )
        
        button6 = Button(
        text = 'Ver Formulas',
        background_color = corFundoBotao,
        font_size = fonteTamanho
        )

        box.add_widget(label1)
        box.add_widget(button1)
        box.add_widget(button2)
        box.add_widget(button3)
        box.add_widget(button4)
        box.add_widget(label2)
        box.add_widget(button5)
        box.add_widget(button6)
        return box
        
Dapp().run()
















