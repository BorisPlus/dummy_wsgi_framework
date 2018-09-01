# Dummy WSGI Framework

Проект "глупенького" WSGI-фрейморка (хотя он не так уж и "глуп", как кажется). 

Методологически состоит из т.н. "контроллеров" и "представлений".

Позволяет отображать представления, генерируемые внутри контроллеров или подгружаемые из HTML-файлов. Расширяем за счет открытых WSGI-интерфейсов диспетчера контроллеров ядра фрейморка и самих контроллеров (вашего) приложения.

## Как пользоваться

### Требования

Не имеет. 

### Установка

Скопируйте к себе папку **_dummy_wsgi_framework_**.

### Примеры

Примеры реализованных приложений:
* ['Одностраничное приложение'](https://github.com/BorisPlus/otus_webpython_003/tree/master/examples_usage/app_first_app_with_one_page)
* ['Демонстрация возможностей фреймворка'](https://github.com/BorisPlus/otus_webpython_003/tree/master/examples_usage/app_features_demonstration)
* ['Демонстрация с переопределением путей хранения файлов контроллеров и представлений'](https://github.com/BorisPlus/otus_webpython_003/tree/master/examples_usage/app_test_other_dirs)


#### О примере ['Демонстрация возможностей фреймворка'](https://github.com/BorisPlus/otus_webpython_003/tree/master/examples_usage/app_features_demonstration)

Содержит демонстрационный вариант реализации Веб-приложения.

А именно:
* отработку контроллера без представления;
* отработку контроллера с представлением в виде HTML-файла;
* отработку отсутствующего маршрута (исключение RouteDoesNotExists);
* отработку отсутствующего файла контроллера, маршрут до которого есть (исключение ControllerFileDoesNotExists);
* отработку отсутствующего HTML-файла представления, чей файл контроллер существует (исключение ViewDoesNotExists).

Тестовый запуск примера:

```bash
uwsgi --http 127.0.0.1:9091 --wsgi-file /<absolute_path>/examples_usage/app_features_demonstration/application.py
```
    
#### Руководство разработчика

1. Папка **_dummy_wsgi_framework_** - это и есть фреймворк с функциональным ядром в папке **_dummy_wsgi_framework/core_** и примером базового одностраничного приложения в папке **_dummy_wsgi_framework/app.template_**.
2. Создайте папку вашего приложения (где угодно) **_app_**.
3. Для быстрого старта, скопируйте в **_app_** содержимое папки **_app.template_**, указав соответствующие пути до фреймворка и вашего конфигурационного файла приложения.
4. Подробнее о структуре приложения:
     
    Файл **_config.py_** содержит конфигурационные переменные, и предпочтительно без должного опыта не изменять существующие (но это возможно, см. конфигурацию примера ['Демонстрация с переопределением путей хранения файлов контроллеров и представлений'](https://github.com/BorisPlus/otus_webpython_003/blob/master/examples_usage/app_test_other_dirs/config.py)) и добавлять свои конфигурационные переменные именно сюда.
    
Приведите в соответствие маршруты до контроллелов в файле **_routes.py_**, изменив словарь:
```python
    uri_routes = {
        ...
        '/page_by_url': 'page_by_url.py',
        ...
    }
```
или, переопределив базовые маршруты фреймворка:
```python
from dummy_wsgi_framework.core.routes import base_uri_routes

uri_routes = base_uri_routes.copy()
uri_routes.update(
    **{
        '/homework_rebuke': 'homework_rebuke.py',
        '/string_methods': 'string_methods.py',
        '/controller_file_does_not_exists': 'controller_file_does_not_exists.py',
        '/controller_with_missing_view_file': 'controller_with_missing_view_file.py',
    }
)
```
, где:
* ключ словаря _'/page_by_url'_ - это URI, последующая после доменного имени или ip адреса часть URL
* а значение _'page_by_url.py'_ - это Python-файл контроллера, реализующего логику реакции на переход по соответствующей (указаной в ключе) ссылке.
Python-файл контроллера необходимо разместить в подпапке controllers.

За перенаправление http-запросов к контроллерам в соответствии с маршрутами из **_routes.py_** отвечает диспетчер вашего приложения **_application.py_**. Его и нужно будет запускать в качестве основной входной точки вашего WSGI-приложения.

```bash
uwsgi --http 127.0.0.1:9093 --wsgi-file /<absolute_path>/app/application.py
```
, но об этом позже.
    
Создайте свои контроллеры, реализовав их логику работы (можно взять шаблонные с подгрузкой html и без, или реализовать свои, например, с посылкой специальных HTTP-заголовков для _Basic Access Authentication_). Внимательно следите за тем, какие части каких приложений Вы импортируете.
    
```python
    from .app.config import (
        APP_ROOT_DIR_NAME,
    )
```
или (найдите одно отличие)

```python
    from .app_mine.config import (
        APP_ROOT_DIR_NAME,
    )
```
Основным методом в интерфейсе вызова вашего контроллера является функция **_controller_response_**. Обязательно реализуйте ее, иначе диспетчер контроллеров фреймворка не сможет вызвать ваш соответствующий контроллер.
    
Контроллеры могут использовать html-шаблоны страниц, которые вы можете разместить в совем приложении в отведенном для них месте **_/app/views_** (это предпочтительно, но не обязательно, так как в **_config.py_** можно переопределить расположение файлов представлений, см. конфигурацию примера ['Демонстрация с переопределением путей хранения файлов контроллеров и представлений'](https://github.com/BorisPlus/otus_webpython_003/blob/master/examples_usage/app_test_other_dirs/config.py))

5. запустите свое приложение удобным Вам способом, например,
    
```bash
uwsgi --http 127.0.0.1:9093 --wsgi-file /<absolute_path>/app/application.py
```
Таким образом у Вас есть возможность создать несколько приложений, запуская их на разных портах серверов. 
    
Диспетчер вашего приложения (_app/application.py: def application()..._), передаст полученные аргументы запроса диспетчеру контроллеров ядра фреймворка (_core/dispatchers.py: def controllers_dispatcher()..._) вместе с отсылкой на конфигурационные данные вашего приложения, тот в соответствии с переданным ему uri по имеющимя данным в маршрутах вашего приложения (_app/routes.py: uri_routes_) вызовет соответствующий (по uri) данному маршруту контроллер (_core/routes.py: def get_controller_by_uri()..._), который в свою очередь ответить "представлением" по "зашитому" в него функционалу или передаст полученные им параметры контроллеру представлений ядра фреймворка (_core/dispatchers.py: def views_dispatcher()..._), который "загрузит" статический HTML-файл вашего представления (_app/views/controller_view.html_).
    
**Схематично.** 

**_START_** -> app/application.py -> [call] ->  
 -> dummy_wsgi_framework/controllers_dispatcher -> [get controller by uri in app/routes] ->  
 -> app/controllers/uri_controller.controller_response -> [optional call] ->  
 -> app/views_dispatcher -> [load] ->  
 -> app/views/uri_controller_view -> **_END_**
        
## Лицензия

Распространяется свободно.

## Дополнительные сведения

Проект в рамках трехдневного домашнего задания курса "Web-разработчик на Python" на https://otus.ru/learning

Прошу понять и простить.

Но Вам не кажется, что **Dummy WSGI Framework** не так уж и "глуп"?

