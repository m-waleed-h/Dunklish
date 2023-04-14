from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('login.kv')
    def loginFunc(self):
        self.root.ids.welcome_label.text = f'Hi {self.root.ids.user.text}'


    def passReset(self):
        #do nothing
        self.root.ids.welcome_label.text = f'you are blocked {self.root.ids.user.text}'


MainApp().run()
