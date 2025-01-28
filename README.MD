# Ivi Test Project
Фреймворк для тестирования API сервиса `ivi_test_project`
____

Установка необходимых пакетов:
```shell
pip3 install -r requirements.txt 
```

Запуск тестов:
```shell
pytest --login your_login --password your_password --host http://host
```
Для запуска отчета allure, в Makefile, указать строку выше.