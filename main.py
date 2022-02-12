import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.graphics import Line
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

import time
from datetime import date, timedelta


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
	"1" : (270, 2040),
	"2" : (540, 2040),
	"3" : (810, 2040),
	"4" : (270, 1770),
	"5" : (540, 1770),
	"6" : (810, 1770),
	"7" : (270, 1500),
	"8" : (540, 1500),
	"9" : (810, 1500)
}

class Output(Screen):
    
    
    danas = ObjectProperty(date.today())
    linije = ObjectProperty((270, 1850, 810, 1850, 350, 1500, 540, 2040, 730, 1500, 270, 1850))
    
    def calculate(self):
        datum_rodenja = int((self.ids.datum_rodenja.text).replace(".", ""))
        suma = str(int((self.danas).strftime("%d.%m.%Y.").replace(".", "")) + datum_rodenja).replace("0", "")
        self.linije = nadji_linije(suma)
        
    def next_day(self):
        self.danas += timedelta(days = 1) 
       
    def previous_day(self):
        self.danas -= timedelta(days = 1)

    
class WindowManager(ScreenManager):
    pass
    
    
kv =  Builder.load_file("my.kv")     

    
class MyApp(App):
    def build(self):
        return kv
        
        
if __name__ == "__main__":
    MyApp().run()
