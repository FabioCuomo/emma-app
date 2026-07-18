from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.clearcolor = (0.5, 0.5, 0.5, 1)


class EmmaApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)

        titolo = Label(text='EMMA', font_size='48sp', size_hint=(1, 0.15))
        spazio = Widget()
        bottone = Button(text='Exit', font_size='24sp', size_hint=(1, 0.15))
        bottone.bind(on_press=self.chiudi)

        layout.add_widget(titolo)
        layout.add_widget(spazio)
        layout.add_widget(bottone)
        return layout

    def chiudi(self, istanza):
        self.stop()


if __name__ == '__main__':
    EmmaApp().run()
