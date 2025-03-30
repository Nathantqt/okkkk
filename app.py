from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from plyer import gps

class GPSApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(text="Récupération GPS...", font_size=20)

    def build(self):
        return self.label

    def on_start(self):
        try:
            gps.configure(on_location=self.on_location)
            gps.start()
        except NotImplementedError:
            self.label.text = "Le GPS n'est pas supporté sur cet appareil."

    def on_location(self, **kwargs):
        lat = kwargs.get('lat', 'N/A')
        lon = kwargs.get('lon', 'N/A')
        self.label.text = f"Latitude: {lat}\nLongitude: {lon}"

if __name__ == '__main__':
    GPSApp().run()
