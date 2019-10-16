# encoding: utf-8
import kivy
kivy.require('1.11.1') 

from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class  MyGrid(GridLayout):
	def __init__(self, **kwargs):
		super(MyGrid, self).__init__(**kwargs)
		self.cols = 1

		self.toparea = GridLayout()
		self.toparea.cols = 2

		self.volumearea = GridLayout()
		self.volumearea.cols = 2
		self.volumearea.add_widget(Label(text="volume1"))
		self.volumearea.add_widget(Label(text="volume2"))
		self.volumearea.add_widget(Label(text="volume3"))
		self.volumearea.add_widget(Label(text="volume4"))
		self.volumearea.add_widget(Label(text="volume5"))
		self.volumearea.add_widget(Label(text="volume6"))

		self.toparea.add_widget(self.volumearea)

		self.valuearea = GridLayout()
		self.valuearea.cols = 1
		self.valuearea.add_widget(Label(text="temperature", font_size = 60))
		self.valuearea.add_widget(Label(text="humidity"))
		self.valuearea.add_widget(Label(text="pressure"))

		self.toparea.add_widget(self.valuearea)


		self.add_widget(self.toparea)


		self.buttonarea = GridLayout()
		self.buttonarea.cols = 4

		self.button1 = Button(text="Button1")
		self.buttonarea.add_widget(self.button1)

		self.button2 = Button(text="Button2")
		self.buttonarea.add_widget(self.button2)

		self.button3 = Button(text="Button3")
		self.buttonarea.add_widget(self.button3)

		self.button4 = Button(text="Button4")
		self.buttonarea.add_widget(self.button4)

		self.add_widget(self.buttonarea)




class MyApp(App):

    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run() 