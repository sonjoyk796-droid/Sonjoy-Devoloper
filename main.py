from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

DATA = {
 "1": ("UNION INFO", "Pakulla Union - Pride of Sonatala\nArea: 5953 Acre, Pop: 19524"),
 "2": ("CHAIRMAN", "Latifal Bari Tim Sarker\nPakulla Union Parishad"),
 "3": ("PAKULLA HAAT", "Famous Haat near Jamuna"),
 "4": ("VILLAGES", "16 Villages, 12 Mouza\nJamuna & Bangali River"),
 "5": ("EMERGENCY", "999\nThana: 01713-374901"),
 "6": ("DOCTOR", "Pakulla Bazar Doctors"),
 "7": ("GROCERY", "Karim Store, Bismillah Store"),
 "8": ("MOSQUE", "Pakulla Jame Masjid"),
 "9": ("SCHOOL", "Pakulla High School"),
 "10": ("BLOOD", "A+ Rakib, B+ Karim"),
 "11": ("MAP", "Pakulla, Sonatala, Bogura"),
 "12": ("ABOUT", "Made by Son of Pakulla - Rajshahi")
}

class PakullaApp(App):
 def build(self):
  root=BoxLayout(orientation='vertical',padding=10)
  root.add_widget(Label(text="PAKULLA UNION APP",size_hint_y=None,height=70))
  sv=ScrollView()
  grid=GridLayout(cols=1,spacing=8,size_hint_y=None)
  grid.bind(minimum_height=grid.setter('height'))
  for i in range(1,13):
   b=Button(text=f"{i}. {DATA[str(i)][0]}",size_hint_y=None,height=50)
   b.bind(on_press=lambda x,k=str(i): self.show(k))
   grid.add_widget(b)
  sv.add_widget(grid)
  root.add_widget(sv)
  return root
 def show(self,k):
  t,c=DATA[k]
  box=BoxLayout(orientation='vertical',padding=10)
  box.add_widget(Label(text=c))
  btn=Button(text="Close",size_hint_y=None,height=40)
  box.add_widget(btn)
  pop=Popup(title=t,content=box,size_hint=(0.85,0.65))
  btn.bind(on_press=pop.dismiss)
  pop.open()

PakullaApp().run()