# ПРОЕКТ АСИНХРОННОГО ПАРСИНГА PEP  

## ТЕХНОЛОГИИ  
- Python 3.9  
- Scrapy 2.5  

## ОПИСАНИЕ ПРОЕКТА  
Программа парсер, которая асинхронно парсит данные с сайта [PEP документации](https://peps.python.org/). Результат работы парсера 2 csv файла `pep_ДатаВремя.csv` и `status_summary_ДатаВремя.csv`, которые сохраняются в корне проекта в папку `results`. 

## УСТАНОВКА И ЗАПУСК ПРОЕКТА  
Клонировать репозиторий  
```
git clone git@github.com:beta-Lilith/scrapy_parser_pep
```  
Перейти в директорию проекта  
```
cd scrapy_parser_pep/  
```  
Создать и активировать виртуальное окружение, установить зависимости  
```
python -m venv venv
```  
```
. venv/Script/activate
```  
```
pip install - r requirements.txt
```  
Из корневой директории запустите парсер:  
```
scrapy crawl pep
```  
Готово!  

## АВТОР  
Оскомова Ксения ([github](https://github.com/beta-Lilith))