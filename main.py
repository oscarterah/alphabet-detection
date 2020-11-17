from kivymd.app import MDApp 
from keras.models import load_model
import numpy as np
from kivy.config import Config
Config.set("graphics","width","480")
Config.set("graphics","height","480")
Config.write()
from keras.preprocessing import image
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Line, Color 
from kivy.uix.widget import Widget
from PIL import Image
global graph, model 
import tensorflow as tf
graph = tf.get_default_graph()
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
sess = tf.Session(config=config)


class Painter(Widget):
    def __init__(self, **kwargs):
        super().__init__()
 
    def on_touch_down(self, touch):
        with self.canvas:
            Color(0,0,0)
            touch.ud["line"] = Line(points = (touch.x, touch.y), width = 5)

    def on_touch_move(self, touch):
        touch.ud["line"].points += [touch.x, touch.y]

class MainWid(Screen):
    def __init__(self, **kwargs):
        super().__init__()
        self.StartWid = StartWid(self)
        self.clearbtn = ClearBtn(self)
        self.detectorbtn = DetectorBtn(self)

        wid = Screen(name='Start')
        wid.add_widget(self.StartWid)
        self.add_widget(wid)
        self.add_widget(self.clearbtn)
        self.add_widget(self.detectorbtn)


class ClearBtn(FloatLayout):
    def __init__(self, mainwid, **kwargs):
        super().__init__()
        self.mainwid = mainwid

    def clear_canvas(self):
        self.mainwid.StartWid.Painter.canvas.clear()
        re = self.mainwid.StartWid.ids.ab 
        re.text = ''
        
class DetectorBtn(FloatLayout):
    def __init__(self, mainwid, **kwargs):
        super().__init__()
        self.mainwid = mainwid

    def detects(self, *args):
        self.mainwid.StartWid.export_to_png('pic.png')
        img = Image.open("pic.png")
        dimension=(60, 60)
        resized = img.resize(dimension)
        resized.save("picr.png")

        model = load_model('terah.h5')
        test_image = image.load_img('picr.png', target_size = (32,32))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)        

        if result[0][0] == 1:
            t = self.mainwid.StartWid.ids.ab
            t.text = 'a'
        elif result[0][1] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'b'
        elif result[0][2] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'c'
        elif result[0][3] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'd'
        elif result[0][4] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'e'
        elif result[0][5] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'f'
        elif result[0][6] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'g'
        elif result[0][7] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'h'
        elif result[0][8] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'i'
        elif result[0][9] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'j'
        elif result[0][10] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'k'
        elif result[0][11] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'l'
        elif result[0][12] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'm'
        elif result[0][13] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'n'
        elif result[0][14] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'o'
        elif result[0][15] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'p'
        elif result[0][16] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'q'
        elif result[0][17] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'r'
        elif result[0][18] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 's'
        elif result[0][19] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 't'
        elif result[0][20] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'u'

        elif result[0][21] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'v'
        elif result[0][22] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'w'
        elif result[0][23] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'x'
        elif result[0][24] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'y'
        elif result[0][25] == 1:
            
            t = self.mainwid.StartWid.ids.ab
            t.text = 'z'

class StartWid(Screen):
    def __init__(self, mainwid, **kwargs):
        super().__init__()
        self.mainwid = mainwid 
        self.Painter = Painter()        
        self.add_widget(self.Painter)



class MainApp(MDApp):
    title = 'Detector'
    def build(self):
        return MainWid()


if __name__== '__main__':
    MainApp().run()
