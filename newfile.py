import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Line
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen




#class MyGrid(Widget):
#    name = ObjectProperty(None)
#    
#    def btn(self):
#        print("kek")
#    
#    pass

def nadji_linije(suma):
	a = 0
	b = 1
	lines = []
	dots =[]
	dict = {}
	
	for i in suma:
		dots.append(koor[i])
		
	return dots
	
koor = {
	"1" : (270, 740+1300),
	"2" : (540, 740+1300),
	"3" : (810, 740+1300),
	"4" : (270, 470+1300),
	"5" : (540, 470+1300),
	"6" : (810, 470+1300),
	"7" : (810, 200+1300),
	"8" : (540, 200+1300),
	"9" : (270, 200+1300)
}


suma = "2463867"


class MainScreen(Screen):
    datum = ObjectProperty(None)
    pass
    


class Output(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        
        
        self.dots = nadji_linije(suma)
        	
        
        
           
        with self.canvas:
            Line(points=[220, 2090, 860, 2090, 860, 1450, 220, 1450, 220, 2090], width=10)
            Line(points=self.dots, width=7)
    
    
class WindowManager(ScreenManager):
    pass
    
kv =  Builder.load_file("my.kv")    
    
class MyApp(App):
    def change(suma):
            suma += 1
            return suma 
    def build(self):
        return kv
        
        
if __name__ == "__main__":
    MyApp().run()