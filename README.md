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
* ['Демонстрация приложения с двумя секретными страницами (Basic Auth)'](https://github.com/BorisPlus/otus_webpython_003/tree/master/examples_usage/app_basic_auth)


### Руководство разработчика

1. Папка **_dummy_wsgi_framework_** - это и есть фреймворк с функциональным ядром в папке **_dummy_wsgi_framework/core_** и примером базового одностраничного приложения в папке **_dummy_wsgi_framework/app.template_**.
2. Создайте папку вашего приложения (где угодно) **_app_**.
3. Для быстрого старта, скопируйте в **_app_** содержимое папки **_app.template_**, указав соответствующие пути до фреймворка и вашего конфигурационного файла приложения.
4. Подробнее о структуре приложения:
     
    Файл **_config.py_** содержит конфигурационные переменные, и предпочтительно без должного опыта не изменять существующие (но это возможно, см. конфигурацию примера ['Демонстрация с переопределением путей хранения файлов контроллеров и представлений'](https://github.com/BorisPlus/otus_webpython_003/blob/master/examples_usage/app_test_other_dirs/config.py)) и добавлять свои конфигурационные переменные именно сюда.
    
Приведите в соответствие маршруты до контроллелов в файле **_routes.py_**, изменив словарь:
```python
    path_info_routes = {
        ...
        '/page_by_url': 'page_by_url.py',
        ...
    }
```
или, переопределив базовые маршруты фреймворка:
```python
from dummy_wsgi_framework.core.routes import base_path_info_routes

path_info_routes = base_path_info_routes.copy()
path_info_routes.update(
    **{
        '/homework_rebuke': 'homework_rebuke.py',
        '/string_methods': 'string_methods.py',
        '/controller_file_does_not_exists': 'controller_file_does_not_exists.py',
        '/controller_with_missing_view_file': 'controller_with_missing_view_file.py',
    }
)
```
, где:
* ключ словаря _'/page_by_url'_ - это PATH_INFO, последующая после доменного имени или ip адреса часть URL
* а значение _'page_by_url.py'_ - это Python-файл контроллера, реализующего логику реакции на переход по соответствующей (указаной в ключе) ссылке.
Python-файл контроллера необходимо разместить в подпапке controllers.

За перенаправление http-запросов к контроллерам в соответствии с маршрутами из **_routes.py_** отвечает диспетчер вашего приложения **_application.py_** (файл называть именно так необязательно). Его и нужно будет запускать в качестве основной входной точки вашего WSGI-приложения.

```python
# Content of: app/application.py
from app import config as app_config

def application(environ, start_response):
    return controllers_dispatcher(environ, start_response, app_config)
```
Запустим:

```bash
uwsgi --http 127.0.0.1:9093 --wsgi-file /<absolute_path>/app/application.py
```
, но об этом позже.
    
Создайте свои контроллеры, реализовав их логику работы (можно взять шаблонные с подгрузкой HTML-файла и без, или реализовать свои, например, с посылкой специальных HTTP-заголовков для _Basic Access Authentication_, см. пример ['Демонстрация приложения с двумя секретными страницами (Basic Auth)'](https://github.com/BorisPlus/otus_webpython_003/tree/master/examples_usage/app_basic_auth)). 

Внимательно следите за тем, какие части каких приложений Вы импортируете.
    
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
Основным методом в интерфейсе вызова вашего контроллера является функция **_controller_response_**. Обязательно реализуйте ее, иначе диспетчер контроллеров ядра фреймворка не сможет вызвать ваш соответствующий контроллер.
    
Контроллеры могут использовать HTML-файлы представлений, которые вы можете разместить в своем приложении в отведенном для них месте **_/app/views_** (это предпочтительно, но не обязательно, так как в **_config.py_** можно переопределить расположение файлов представлений, см. конфигурацию примера ['Демонстрация с переопределением путей хранения файлов контроллеров и представлений'](https://github.com/BorisPlus/otus_webpython_003/blob/master/examples_usage/app_test_other_dirs/config.py))

Это пример вызова контроллером диспетчера представлений ядра фреймворка.
```python
from dummy_wsgi_framework.core.dispatchers import views_dispatcher

def controller_response(environ, start_response, app_config):
    return views_dispatcher(
        environ,
        start_response,
        app_config,     # по сути указываем диспетчеру 
                        #  фреймворка какое из ваших приложений использовать
        __file__        # на это имя опирается диспетчер представлений, 
                        # он отсечет .py от имени файла и будет искать имя с ".html"
    )
```

5. запустите свое приложение удобным Вам способом, например,
    
```bash
uwsgi --http 127.0.0.1:9093 --wsgi-file /<absolute_path>/app/application.py
```
Таким образом у Вас есть возможность создать несколько приложений, запуская их на разных портах серверов. 
    
Диспетчер вашего приложения (_**app/application.py:** def application()..._), передаст полученные аргументы запроса диспетчеру контроллеров ядра фреймворка (_**core/dispatchers.py:** def controllers_dispatcher()..._) вместе с отсылкой на конфигурационные данные вашего приложения, тот в соответствии с переданным ему PATH_INFO по имеющимя данным в маршрутах вашего приложения (_**app/routes.py:** path_info_routes_) вызовет соответствующий данному маршруту контроллер (**_core/routes.py:** def get_controller_by_path_info()..._), который в свою очередь ответит "представлением" по "зашитому" в него функционалу или передаст полученные им параметры диспетчеру представлений ядра фреймворка (**_core/dispatchers.py:** def views_dispatcher()..._), который "загрузит" статический HTML-файл вашего представления (_app/views/controller_view.html_).
    
**Схематично.** 

**_START_** -> **app**/application.py -> [call] ->  
 -> dummy_wsgi_framework/**core**/controllers_dispatcher -> [get controller by path_info in app/routes] ->  
 -> **app**/controllers/path_info_controller.controller_response -> [optional call] ->  
 -> dummy_wsgi_framework/**core**/views_dispatcher -> [load] ->  
 -> **app**/views/path_info_controller_view -> **_END_**
   
### Разбор примера

### О примере ['Демонстрация возможностей фреймворка'](https://github.com/BorisPlus/otus_webpython_003/tree/master/examples_usage/app_features_demonstration)

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

### О примере ['Демонстрация приложения с двумя секретными страницами (Basic Auth)'](https://github.com/BorisPlus/otus_webpython_003/tree/master/examples_usage/app_basic_auth)

Пусть маршруты будут таковы:
```python
path_info_routes = {
    '/index_1': 'first_secret_page.py',
    '/index_2': 'second_secret_page.py',
    '': 'first_secret_page.py',
}
```

А теперь о логике запроса логина и пароля.
* Контроллер приложения пошлет клиенту заголовок запроса Basic авторизации.
* Браузет продемонстрирует форму.
* Вы введете логин и проль.
* Они конкатенируются с использованием двоеточия ":" и закодируюся (браузером) по протоколу BASE64.
* Приложение должно будет декодировать и проверить на валидность переданную пару "ЛОГИН:ПАРОЛЬ". В случае успеха вы получите доступ к "секретной информации" :)

Итак:
```python
# Content of 'first_secret_page.py'
import base64

def controller_response(environ, start_response, app_config):
    if environ.get('HTTP_AUTHORIZATION', '').startswith('Basic '):  # пришел ли заголовок
        login_password_at_b64 = environ.get('HTTP_AUTHORIZATION', '')[6:]
        login_password = base64.b64decode(login_password_at_b64)  # декодируем
        if login_password == b'user:user':
            start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
            return [
                bytes(
                    "Привет. <br>"
                    "Я <a href='/index_1'><b>секретная стартовая</b></a> страница приложения \"%s\". <br>"
                    "А тут <a href='/index_2'><b>вторая секретная</b></a> с "
                    "другим пролем." % app_config.APP_ROOT_DIR_NAME
                    , 'utf-8'
                )
            ]
    # ЛОГИН:ПАРОЛЬ пришли неверные или не пришли вовсе, приложение перезапросит
    start_response('401 Access Denied', [
        ('Content-Type', 'text/html; charset=utf-8'),
        ('WWW-Authenticate', 'Basic realm="Dummy WSGI Framework"'),
        ('Content-Length', '0'),
    ])
    return b'Basic Auth'
```

А на "второй секретной" странице может быть совершенно другая пара ЛОГИН:ПАРОЛЬ, например, admin:admin.

## Лицензия

Распространяется свободно.

## Дополнительные сведения

Проект в рамках трехдневного домашнего задания курса "Web-разработчик на Python" на https://otus.ru/learning

Прошу понять и простить.

Но Вам не кажется, что **Dummy WSGI Framework** не так уж и "глуп"?

