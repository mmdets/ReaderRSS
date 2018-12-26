# ReaderRSS
<hr>
<h3> Лабораторная работа по предмету "Языки и методы программирования"
<h4> Выполнили: Софья Карпова, Мария Дец, СПбГЭУ, группа ПМ-1701 
  
<h6>
Первое, что необходимо сделать, это установить kivy и BeautifulSoup
  
```
python -m pip install kivy
python -m pip install bs4
```

Для начала работы с менеджером задач необходимо создать базу данных, для этого вам нужно запустить файл **database.py**

Далее запускам файл **window.py**

Перед вами открывается начальная страница.

![main](https://pp.userapi.com/c847122/v847122376/15ee01/JGPM501Cq_I.jpg)

При нажатии на кнокпу "Add New Links" происходит переход к экрану добавления новой ссылки. На этом экране вы можете ввести ссылку на источник, от которого вы хотите получать новости, и при нажатии на кнопку "Add" произойдёт добаление ссылки в базу данных.
![AddSource](https://pp.userapi.com/c847122/v847122376/15ee0a/cPHPwKF7vig.jpg)

При нажатии на кнопку "Show All Links" на главном экране происходит переход к экрану, который помогает просматривать какие источники уже были добавлены в базу данных.
![ShowAllLinks](https://pp.userapi.com/c847122/v847122376/15ee13/nh2D20D0IGY.jpg)

При нажатии на кнопку "DeleteLinks" на главном экране происходит переход к экрану на котором вы можете удалить какой-либо из имеющихся источников.
![DeleteLinks](https://pp.userapi.com/c847122/v847122376/15ee25/rdJxtYONuF0.jpg)

При нажатии на кнопку "Show News" на главном экране происходит переход к экрану на котором выводятся новости из имеющихся источников.
![Show News](https://pp.userapi.com/c850728/v850728253/7499c/Use3OWu-8Hs.jpg)

При нажатии на кнопку "Find Links By Key Words" на главном экране происходит переход к экрану на котором вы можете осуществлять поиск новостей по ключевому слову.
![FindLinksByKeyWords](https://pp.userapi.com/c850728/v850728253/749a5/P34gVkjwxf8.jpg)

На всех экранах кнопка "Go To Main Screen" осуществляет переход к главному экрану, а кнопка "Quit" на главном экране осуществляет выход из приложения.
