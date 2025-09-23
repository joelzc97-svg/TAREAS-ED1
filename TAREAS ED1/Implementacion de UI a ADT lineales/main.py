from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from controller import MainController

class MainView(BoxLayout):
    pass

class MainApp(App):
    def build(self):
        view = MainView()
        self.controller = MainController(view)
        return view

if __name__ == "__main__":
    MainApp().run()
