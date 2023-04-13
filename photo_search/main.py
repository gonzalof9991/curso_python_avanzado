from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests
from bs4 import BeautifulSoup as bs
Builder.load_file('frontend.kv')

class FirstScreen(Screen):

    def get_image_link(self):
        query = self.manager.current_screen.ids.text_input.text
        # Get wikipedia page and the first image
        page = wikipedia.page(query)
        print(page)
        image_link  = page.images[0]
        print(image_link)
        return image_link
    def download_image(self):
        try:
            # Download the image
            req = requests.get(self.get_image_link())
            soup = bs(req.content, 'html.parser')
            imagepath = 'files/picture.jpg'
            with open(imagepath, 'wb') as f:
                f.write(requests.get(soup.find_all('img')[0]['src']).content)
            return imagepath
        except Exception as e:
            print(e)
            return 'files/placeholder.jpg'
        # Set the image to the image source
    def set_image(self):
        self.manager.current_screen.ids.img.source = self.download_image()

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
