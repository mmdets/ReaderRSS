from bs4 import BeautifulSoup
import re
import requests
import sqlite3
import kivy
#kivy.require('1.10.1')
import sys
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager 
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

links = sqlite3.connect("database.db")  #подключаем базу данных
cursor = links.cursor()

class MainScreen(Screen):
	def __init__(self, **kwargs):
		super(MainScreen, self).__init__(**kwargs)

	def go2addScreen(self,*args): 
		self.manager.current = 'addScreen'

	def go2delete_linkScreen(self,*args): 
		self.manager.current = 'delete_linkScreen'

	def go2showScreen(self,*args): 
		self.manager.current = 'showScreen'

	def go2find_by_keywordScreen(self,*args): 
		self.manager.current = 'find_by_keywordScreen'

	def go2showAllLinksScreen(self,*args): 
		self.manager.current = 'showAllLinksScreen'

	def quit_press(self):
		sys.exit()


class AddScreen(Screen):
	def __init__(self, **kwargs):
		super(AddScreen, self).__init__(**kwargs)

	def add(self, link): #Добавление нового адреса
		cursor.execute("""INSERT INTO links VALUES ('%s')""" % link)
		links.commit()
		self.ids['la2'].text = 'Successfully done'

	def go2mainScreen(self,*args):
		self.manager.current = 'mainScreen'
		self.ids['new_link'].text = ''


class Delete_linkScreen(Screen):
	def __init__(self, **kwargs):
		super(Delete_linkScreen, self).__init__(**kwargs)

	def delete(self,link):
		sql = 'DELETE FROM links WHERE link = \'' + link + '\''
		cursor.execute(sql)
		links.commit()
		self.ids['ld2'].text = 'Successfully done'

	def go2mainScreen(self,*args):
		self.manager.current = 'mainScreen'
		self.ids['link_to_delete'].text = ''


class ShowScreen(Screen):
	def __init__(self, **kwargs):
		super(ShowScreen, self).__init__(**kwargs)

	def show_all(self):
		t = ''
		sql = "SELECT * FROM links"
		for row in cursor.execute(sql):
			xml = requests.get(row[0])
			soup = BeautifulSoup(xml.content.decode(xml.encoding), 'xml')
			l = soup.find_all('item')

			for i in range(len(l)):
				t = t+'\n**' + l[i].title.string + '**\n\n'+l[i].description.string + '\n*'+l[i].link.string+'*\n'
		self.ids['text'].text = (t)

	def go2mainScreen(self,*args):
		self.manager.current = 'mainScreen'


class Find_by_keywordScreen(Screen):
	def __init__(self, **kwargs):
		super(Find_by_keywordScreen, self).__init__(**kwargs)

	def find_by_key(self,key):
		t = ''
		sql = "SELECT * FROM links"
		for row in cursor.execute(sql):
			xml = requests.get(row[0])
			soup = BeautifulSoup(xml.content.decode(xml.encoding), 'xml')
			l = soup.find_all('item')
			for i in range(len(l)):
				h = l[i].title.string
				if key.lower() in h.lower():
					t = t+'\n**' + h + '**\n\n'+l[i].description.string + '\n*'+l[i].link.string+'*\n'
		self.ids['text2'].text = (t)

	def go2mainScreen(self,*args):
		self.manager.current = 'mainScreen'
		self.ids['key_word'].text = ''


class ShowAllLinksScreen(Screen):
	def __init__(self, **kwargs):
		super(ShowAllLinksScreen, self).__init__(**kwargs)

	def show_db(self):
		t = ''
		sql = "SELECT * FROM links"
		for row in cursor.execute(sql):
			t = t + str(row[0])+ '\n'
		self.ids['label1'].text = t

	def go2mainScreen(self,*args):
		self.manager.current = 'mainScreen'


class RSSreader(App):
	def build(self):
		root = ScreenManager()
		mainScreen = MainScreen(name='mainScreen')
		addScreen = AddScreen(name='addScreen')
		delete_linkScreen = Delete_linkScreen(name='delete_linkScreen')
		showScreen = ShowScreen(name='showScreen')
		find_by_keywordScreen = Find_by_keywordScreen(name='find_by_keywordScreen')
		showAllLinksScreen = ShowAllLinksScreen(name='showAllLinksScreen')

		root.add_widget(mainScreen)
		root.add_widget(addScreen)
		root.add_widget(delete_linkScreen)
		root.add_widget(showScreen)
		root.add_widget(find_by_keywordScreen)
		root.add_widget(showAllLinksScreen)

		return root

if __name__ == '__main__':
	RSSreader().run()