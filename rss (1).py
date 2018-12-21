from bs4 import BeautifulSoup
import re
import requests
import sqlite3 

links = sqlite3.connect("database.db")  #подключаем базу данных
cursor = links.cursor()
data = dict()
xml = [row[1] for row in cursor.execute("SELECT rowid, * FROM database ORDER BY link")] #выбираем какой-то адрес

soup = BeautifulSoup(xml.content.decode(xml.encoding), 'xml')
l = soup.find_all('item')
for i in range(len(l)):
    print(l[i].title.string) #эта штука выводит заголовок
    print(l[i].description.string) #эта выводит описание
    print(l[i].link.string) #эта выводит ссылку

def add(): #Добавление нового адреса
	cursor.execute("""INSERT INTO database VALUES ('%s')""" % ИмяЯчейкиВводаВКоторуюБудетВведенНовыйАдрес.get())
	database.commit()
	ШтукаКудаБудутВыводитьсяСсылки.insert(END, ИмяЯчейкиВводаВКоторуюБудетВведенНовыйАдрес.get())
	xml.append(ИмяЯчейкиВводаВКоторуюБудетВведенНовыйАдрес.get())

def find(): #Поиск по ключевому слову
	aim = ИмяЯчейкиВводаВКоторуюБудетВведеноКлючевоеСловоДляПоиска.get()
	for i in data:
		for j in range(len(data[i])):
			for k in range(3):
				if aim in data[i][j][k]:
					ШтукаКудаБудутВыводитьсяНовости.insert(END, data[i][j][k])

