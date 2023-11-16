![image](https://github.com/takry/Split_pdf/assets/63951434/9eb57be4-66e9-49b7-b47c-69af214d0eb8)# Split_pdf
Python + 1c
Разделитель пдф файлов по штрихкодам на python + обработка для 1с.

Инструкция по установке/настройке для windows:

1) Устанавливаем себе python - https://www.python.org/downloads/windows/
2) Чаще всего, путь установки выглядит так - C:\Users\[ИМЯ ПОЛЬЗОВАТЕЛЯ]\AppData\Local\Programs\Python\Python312\python.exe
3) Устанавливаем нужные пакеты из файла requirements.txt:
  3.1) Пуск -> выполнить -> cmd -> python -m pip install -r requirements.txt
  3.2) requirements.txt из пунка 3.1 это путь к файлу requirements.txt, скачанному из этого репозитория
4) Открываем РазделитьСканПоШтрихКодам.epf с помощью конфигуратора 1с
5) В модуле Формы, в процедуре Заполнить имеется строка: ЗапуститьПриложение(СтрШаблон("C:\Users\F0621069\AppData\Local\Programs\Python\Python312\python.exe C:\ProjectPDF\2.py -f %1", " " + КаталогВыгрузкиДок), , Истина);
Где: 
- C:\Users\F0621069\AppData\Local\Programs\Python\Python312\python.exe - путь до python.exe из пункта 2, где F0621069 - имя пользователя;
- C:\ProjectPDF\2.py - путь до скрипта python, 2.py надо заменить на script.py

Инструкция по использованию:

![image](https://github.com/takry/Split_pdf/assets/63951434/60da542b-ce62-4de7-8861-6e4bc7bd439d)

