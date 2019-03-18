# Validate XML -> XSD

## Инструкция RUS

1. Установить зависимости 
```bash 
$ pip install -r requirements.txt
```
2. Запустить веб-вервис 
```bash 
$ python3 "путь до скрипта app.py" 
```
По следующему адресу запустится веб-сервис
```
http://127.0.0.1:5000/validate
```
3. Для тестирования передать GET запрос с параметрами "xml='Путь до xml файла' ", "xsd='путь до xsd файла'"

4. Пример тела ответа
```"count": 1,"filename": "some_file.XML","line": 4,"text": "filename: some_file.XML Error: Element \'DATE\': Incorrect field layout in structure. Expected field -  ( NAME ).Number line: 4"```

## Inctruction ENG

1. Install dependencies
```bash 
$ pip install -r requirements.txt
```
2. Run the web-service 
```bash 
$ python3 "path to app.py" 
```
On next url will starting web-service
```
http://127.0.0.1:5000/validate
```
3. For example, you must send GET query with params "xml='path to xml file' ", "xsd='path to xsd file'"

4. Example response body
```"count": 1,"filename": "some_file.XML","line": 4,"text": "filename: some_file.XML Error: Element \'DATE\': Incorrect field layout in structure. Expected field -  ( NAME ).Number line: 4"```
