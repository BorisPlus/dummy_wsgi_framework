# Dummy WSGI Framework

Проект "глупенького" WSGI-фрейморка (хотя он не так уж и "глуп", как кажется). 

Методологически состоит из т.н. "контроллеров" и "представлений".

В базовом варианте позволяет отображать представления, генерируемые внутри контроллеров или подгружаемые из HTML-файлов. Расширяем за счет открытых WSGI-интерфейсов контроллеров приложения. Вы можете испольтзовать его в качестве каркаса для своих простеньких Веб-приложений. Ссылаться на реализацию, указывая на использование вами "Dummy WSGI Framework", совсем не обязательно. Но мне бы хотелось иметь публичный отзыв, даже если он не положительный.

## Как пользоваться

### Требования

Не имеет. 

### Установка

_"Dummy WSGI Framework"_ включен в реест пакетов PyPI (Python Package Index) - https://pypi.org/project/dummy-wsgi-framework/

Его установка возможна с использованием _**pip**_
```
pip install dummy-wsgi-framework
```

Или иным возможным образом, например:
```
$ cd <your_project_dir>
$ git clone git://github.com/BorisPlus/dummy-wsgi-framework.git
```
или по ссылке для скачивания master-ветки проекта [Zip](https://github.com/BorisPlus/dummy-wsgi-framework/archive/master.zip)


### Примеры

Примеры реализованных приложений:
* ['Одностраничное приложение'](https://github.com/BorisPlus/dummy-wsgi-framework/tree/master/examples_usage/app_one_page)
* ['Демонстрация базовых_возможностей фреймворка'](https://github.com/BorisPlus/dummy-wsgi-framework/tree/master/examples_usage/app_base_features_demonstration)
* ['Демонстрация с переопределением путей хранения файлов контроллеров и представлений'](https://github.com/BorisPlus/dummy-wsgi-framework/tree/master/examples_usage/app_one_page_other_dirs)
* ['Демонстрация приложения с двумя секретными страницами (Basic Auth)'](https://github.com/BorisPlus/dummy-wsgi-framework/tree/master/examples_usage/app_basic_auth)
* ['Демонстрация приложения с передачей и оработкой допущенных параметров'](https://github.com/BorisPlus/dummy-wsgi-framework/tree/master/examples_usage/app_get_allowed_params_from_route_link)

### Руководство разработчика

1. Папка **_dummy_wsgi_framework_** - это и есть фреймворк с функциональным ядром в папке **_dummy_wsgi_framework/core_** и примером базового одностраничного приложения в папке **_dummy_wsgi_framework/app.template_**.
2. Создайте папку вашего приложения **_app_** (где угодно).
3. Для быстрого старта, скопируйте в **_app_** содержимое папки **_app.template_**.
4. Подробнее о структуре приложения:
     
    Файл **_config.py_** содержит конфигурационные переменные, и предпочтительно без должного опыта не изменять существующие их значения (хотя это возможно, см. [конфигурацию](https://github.com/BorisPlus/dummy-wsgi-framework/blob/master/examples_usage/app_test_other_dirs/config.py) примера ['Демонстрация с переопределением путей хранения файлов контроллеров и представлений'](https://github.com/BorisPlus/dummy-wsgi-framework/blob/master/examples_usage/app_one_page_other_dirs)) и добавлять свои конфигурационные переменные именно сюда.
    
Приведите в соответствие маршруты до ваших контроллелов в файле **_routes.py_**, изменив:
```python
routes_of_uri_regexps = (
    dict(uri_regexp=r'/index/', controller='index.py'),
    dict(uri_regexp=r'/', controller='index.py'),
)
```
или, подгрузив базовые маршруты фреймворка:
```python
from dummy_wsgi_framework.core.routes import base_routes_of_uri_regexps


routes_of_uri_regexps = [dict(uri_regexp='^/page_one/$',
                              controller='page_one.py'),
                         dict(uri_regexp='^/page_two/$',
                              controller='page_two.py')
                         ] + list(base_routes_of_uri_regexps).copy()
```
, где:
* значение ключа _uri_regexp_ - это _REQUEST_URI_, последующая после доменного имени или IP-адреса часть URL. Знак "/" в конце _uri_regexp_ обязателен, так как вызов диспетчера контроллеров ядра фреймворка контролирует двойственность ссылок ".../page_by_url" и ".../page_by_url/", и если в конце _REQUEST_URI_ знака "/" нет, то делается дополнение им, и происходит вызов соответствующего редиректа.
* а значение ключа _controller_ - это Python-файл контроллера, реализующего логику реакции на переход по ссылке, соответствующей _uri_regexp_. Python-файл контроллера необходимо разместить в подпапке _controllers_ (но возможно переопределить).

Будте внимательны, срабатывает первый по порядку маршрут (сверху вниз). Алгоритм сопоставления опирается на успех _re.compile(uri_regexp).findall(REQUEST_URI)_. Что сделано для того, чтоб было возможно использование передачи параметров по ссылке (['Демонстрация приложения с передачей и оработкой допущенных параметров'](https://github.com/BorisPlus/dummy-wsgi-framework/tree/master/examples_usage/app_get_allowed_params_from_route_link)).

Функции "редиректа" и "404ой ошибки" реализованы в ядре фреймворка:
```python
# File: core/controllers/redirect.py
def controller_response(environ, start_response, app_config, location):
    start_response('301 Moved Permanently', [('Location', location)])
    return b''
```
и

```python
# File: core/controllers/error404.py
def controller_response(environ, start_response, app_config, message):
    start_response('404 Not found', [('Content-Type', 'text/html; charset=utf-8')])
    return [
        # some template
    ]
```

За перенаправление HTTP-запросов к контроллерам в соответствии с маршрутами из **_routes.py_** отвечает диспетчер вашего приложения **_application.py_** (файл называть именно так не обязательно). Его и нужно будет запускать в качестве основной входной точки вашего WSGI-приложения.

```python
# Content of: app/application.py
import config as app_config
from dummy_wsgi_framework.core.dispatchers import get_controller_response

def application(environ, start_response):
    return get_controller_response(environ, start_response, app_config)
```
Запустим:

```bash
uwsgi --http 127.0.0.1:8080 --wsgi-file /<absolute_path>/app/application.py
```
, но об этом позже.
    
Создайте свои контроллеры, реализовав их логику работы (можно взять шаблонные с подгрузкой HTML-файла и без, или реализовать свои с посылкой специальных HTTP-заголовков, например, для _Basic Access Authentication_ как в примере ['Демонстрация приложения с двумя секретными страницами (Basic Auth)'](https://github.com/BorisPlus/dummy-wsgi-framework/tree/master/examples_usage/app_basic_auth)). 

Внимательно следите за тем, какие части каких приложений Вы импортируете в своих приложениях.

Например,
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
Основным методом в программном протоколе вызова вашего контроллера является функция **_get_response_**. Обязательно реализуйте ее, иначе диспетчер контроллеров ядра фреймворка не сможет вызвать соответствующий контроллер, и будет сгененрировано исключение _ControllerFileIsInvalid_ с указанием отсутствия метода **_get_response_**
    
Контроллеры могут использовать HTML-файлы представлений, которые располагаются в отведенном для них месте **_/app/views_** (это предпочтительно, но не обязательно, так как в **_config.py_** можно переопределить расположение файлов представлений, см. конфигурацию примера ['Демонстрация с переопределением путей хранения файлов контроллеров и представлений'](https://github.com/BorisPlus/otus_webpython_003/blob/master/examples_usage/app_test_other_dirs/config.py))

Это пример загрузки контроллером приложения HTML-файла представления.
```python
from dummy_wsgi_framework.core.dispatchers import get_view_response


def get_response(environ, start_response, app_config):
    return get_view_response(
        environ,
        start_response,
        app_config,     # указываем диспетчеру контроллеров ядра фреймворка 
                        # какое из ваших приложений использовать
        'index.html'    # на это имя опирается диспетчер представлений, 
                        # обычно в качестве данного параметра я использую вызов
                        # from dummy_wsgi_framework.core.dispatchers import resolve_name_by_python_file_name
                        # resolve_name_by_python_file_name(__file__, '%s.html')
                        # что обяжет файл представления иметь тоже имя, что и у файла контроллера 
                        # и упростит возможный рефакторинг
    )
```

5. запустите свое приложение удобным Вам способом, например,
    
```bash
uwsgi --http 127.0.0.1:80 --wsgi-file /<absolute_path>/app/application.py
```
Таким образом у Вас есть возможность создать несколько приложений, запуская их на разных портах серверов. 
    
Точка входа вашего приложения (_**app/application.py:** def application()..._), передаст полученные аргументы запроса диспетчеру контроллеров ядра фреймворка (_**core/dispatchers.py:** def get_controller_response()..._) вместе с отсылкой на конфигурационные данные вашего приложения. Тот в соответствии с переданным ему _REQUEST_URI_ по имеющимя данным в маршрутах вашего приложения (_**app/routes.py:** routes_of_uri_regexps_) вызовет по успеху (**_core/routes.py:** def get_controller_by_uri_regexp()..._) соответствующий данному маршруту контроллер (_**app/controllers/<action>.py:** def get_response()), который в свою очередь ответит представлением по "зашитому" в него функционалу или передаст (если вы так реализуете) полученные им параметры дальше методу (**_core/dispatchers.py:** def load_view()..._), который "загрузит" статический HTML-файл вашего представления (_app/views/<action>.html_).

   
### Разбор примеров

### Пример ['Демонстрация базовых_возможностей фреймворка'](https://github.com/BorisPlus/dummy-wsgi-framework/tree/master/examples_usage/app_base_features_demonstration)

Пример ['Демонстрация базовых_возможностей фреймворка'](https://github.com/BorisPlus/dummy-wsgi-framework/tree/master/examples_usage/app_base_features_demonstration) содержит демонстрационный вариант реализации Веб-приложения, а именно:
* реализацию вызова контроллера без представления;
* реализацию вызова контроллера с загрузкой представления в виде HTML-файла;
* демонстрацию штатного отлова на уровне ядра фреймворка исключения RouteDoesNotExist - отсутствие маршрута, удовлетворяющего HTTP запросу;
* демонстрацию штатного отлова на уровне ядра фреймворка исключения ControllerFileDoesNotExist - отсутствие файла контроллера, маршрут до которого есть;
* демонстрацию штатного отлова на уровне ядра фреймворка исключения ControllerFileIsInvalid - отсутствие у файла контроллера, маршрут до которого есть, тебуемого фреймворком метода _get_response_;
* демонстрацию штатного отлова на уровне ядра фреймворка исключения ViewDoesNotExist - отсутствие подгружаемого в методе _get_response_ контроллера, маршрут до которого есть,  файла представления (иногда их называют "шаблон" или "template").

Кроме того, с целью возможного использования сторонними разработчиками каких-либо шаблонизаторов отдельно продемонстрирвана возможность декорирования функции загрузки файла представления:
* "как есть" - загрузка шаблона фреймворком, реализованная в ядре фреймворка;
* "чем-то" самописным - загрузка шаблона и замена сответствующих лексем, если таковые переданы, возможным вашим собственным методом;
* с использованием Jinja2 - загрузка шаблона и его обработка с помощью Jinja2.

Я не хотел вносить зависимость от Jinja2 в ядро фреймворка, так как считаю эту связь слишком жесткой. При это dummy-wsgi-framework изначально должен быть простым, базовым. При этом, понимая, что этого может быть не достаточно остальным и имея свой интерес по разработке подобной архитектуры фреймворка, я реализовал декоратор функцию загрузки файла представления в ядре фреймворка. 

Декоратор _@decorate_loaded_view_function_for_response_ производит проверку существования файла представления и передает функции обработки этого файла полученные ею аргументы 

То есть для загрузки "как есть", реализованной в ядре фреймворка, файла представления предполагается вызов в контроллере _load_view_ ядра фреймворка:
```python
# Framework solution
from dummy_wsgi_framework.core.dispatchers import load_view


def get_response(environ, start_response, app_config):
    return load_view(
        environ,
        start_response,
        app_config,
        'load_me.html'      # файл представления, шаблон
    )
```
Для "чего-то" самописного у вас есть возможность реализовать функцию загрузки файла представления, например, с заменой сответствующих лексем шаблона, необходимо лишь применить к вашей функции декоратор _@decorate_loaded_view_function_for_response_ из ядра фреймворка:

```python
# Your self realization
from dummy_wsgi_framework.core.dispatchers import decorate_loaded_view_function_for_response


@decorate_loaded_view_function_for_response
def yourself_load_view_function(view_path, **kwargs):
    with open(view_path, 'rb') as f:
        response_body = f.read()
        for k in kwargs:
            response_body = response_body.replace(
                ("{{ %s }}" % k).encode(), 
                str(kwargs[k]).encode()
            )
    return response_body


def get_response(environ, start_response, app_config):
    return yourself_load_view_function(
        environ,
        start_response,
        app_config,
        'load_me.html',     # файл представления, шаблон
        id=1,               # некие переменные, которые будут переданы в шаблон и
        value=2,            # будут участвовать в замене в response_body.replace
        other=4
    )

```


Для использования шаблонизаторов, например, Jinja2, вышеописанный код может выглядеть так:
```python
from dummy_wsgi_framework.core.dispatchers import decorate_loaded_view_function_for_response
from dummy_wsgi_framework.core.exceptions import ExistViewFileIsInvalid, ViewDoesNotExist
from examples_usage.app_base_features_demonstration import config
import jinja2
import os


@decorate_loaded_view_function_for_response
def load_jinja2_view_template(view_template_path, **kwargs):
    try:
        environment = jinja2.Environment(loader=jinja2.FileSystemLoader(config.APP_VIEWS_DIR))
        template = environment.get_template(os.path.basename(view_template_path))
        return template.render(**kwargs).encode()
    except jinja2.exceptions.TemplateSyntaxError as e:
        raise ExistViewFileIsInvalid('File "%s" - %s' % (view_template_path, e.message))
    except jinja2.exceptions.TemplateNotFound as e:
        raise ViewDoesNotExist('File "%s" not found %s' % (view_template_path, e.message))


def get_response(environ, start_response, app_config):
    return load_jinja2_view_template(
        environ,
        start_response,
        app_config,
        'load_me.html',     # файл представления, шаблон в формате Jinja2, возможно с базовым.
        id=1,               # некие переменные, которые будут переданы в шаблон и
        value=2,            # будут участвовать в замене в template.render
        other=4
    )
```
Рекомендую вынести подобные _load_jinja2_view_template_ функции в отдельный файл в вашем приложении, наприемер, как в данном примере - _user_def.py_. Это представляется методологически правильней для повторного использования подобных _load_jinja2_view_template_ функций, например, в других контроллерах.

### Пример ['Демонстрация приложения с двумя секретными страницами (Basic Auth)'](https://github.com/BorisPlus/otus_webpython_003/tree/master/examples_usage/app_basic_auth)

Пусть маршруты будут таковы:
```python
routes_of_uri_regexps = (
    dict(uri_regexp=r'^/index_1/$', controller='first_secret_page.py'),
    dict(uri_regexp=r'^/index_2/$', controller='second_secret_page.py'),
    dict(uri_regexp=r'^/$', controller='first_secret_page.py'),
)
```

О логике запроса логина и пароля.
* Контроллер приложения пошлет клиенту заголовок запроса Basic авторизации.
* Браузет продемонстрирует форму.
* Вы введете логин и проль.
* Они конкатенируются с использованием двоеточия ":", закодируюся браузером по протоколу Base64 и передадутся на сервер.
* Приложение должно будет декодировать и проверить на валидность переданную пару "login:password". В случае успеха вы получите доступ к "секретной" информации :)

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
                # some template
            ]
    # "login:password" is empty or not valid
    start_response('401 Access Denied', [
        ('Content-Type', 'text/html; charset=utf-8'),
        ('WWW-Authenticate', 'Basic realm="Dummy WSGI Framework"'),
        ('Content-Length', '0'),
    ])
    return b'Basic Auth'
```

А на "второй секретной" странице может быть совершенно другие "login:password", например, "admin:admin".

### Пример ['Демонстрация приложения с передачей и оработкой допущенных параметров'](https://github.com/BorisPlus/dummy-wsgi-framework/tree/master/examples_usage/app_get_allowed_params_from_route_link)

С целью возможного вами использования параметров в ссылках был реализован механизм назначения маршрутам допустимых параметров (в нотации "key=value" ) и их получения соответствующим контроллером с возможной их последующей передачей дальше в представление.

Ключевым моментом для использования параметров является правильное написание регулярного выражения в соответствующем uri_regexp
```python
routes_of_uri_regexps = (
    ...
    dict(uri_regexp=r'^(/view_random/\?(id=[0-9]*)&(value=[A-F0-9]*)/)$', controller='view.py'),
    ...
)
```

При формировании в _uri_regexp_ регулярного выражения необходимо придерживаться следующих правил:
* сформировать path_info, например, "/path/info/"
* определиться с набором параметров, необходимых для указанного в ключе controller контроллера, например, это "id", "hex", "word"
* сформировать пары из параметров и их шаблонных типов значений, например, "id=id_value_type", "hex=hex_value_type", "word=word_value_type"
* заключить пары в скобки и сконкатенировать их, используя "&", например, "(id=id_value_type)**&**(hex=hex_value_type)**&**(word=word_value_type)"
* сконкатенировать полученное с path_info, используя "\?", например, "/path/info/**\?**(id=id_value_type)&(hex=hex_value_type)&(word=word_value_type)"
* поставить в конце "/", например, "/path/info/\?(id=id_value_type)&(hex=hex_value_type)&(word=word_value_type)**/**"
* заключить в круглые скобки, например, "**(**/path/info/\?(id=id_value_type)&(hex=hex_value_type)&(word=word_value_type)/**)**"
* поставить знак начала "^" и конца "$" регулярного выражения, например, "**^**(/path/info/\?(id=id_value_type)&(hex=hex_value_type)&(word=word_value_type)/)**$**"
* заменить шаблонные типы значений на их шаблоны в нотации регулярных выражений, например,
    * для "id_value_type" - "[0-9]*"
    * для "hex_value_type" - "[0-9A-Fa-f]*"
    * для "word_value_type" - "[0-9A-Za-z_]*" или "\w*"
    * и как итог в _uri_regexp_ внести "^(/path/info/\?(id=[0-9]*)&(hex=[0-9A-Fa-f]*)&(word=[0-9A-Za-z_]*)/)$"
    
В примере контроллер `list` генерирует представление со ссылками, где указаны шестнадцатиричные значения в верхнем регистре и их id, присвоенные им в порядке их генерации.

А контроллер `view` отображает переданные ему шестнадцатиричные значения в верхнем регистре и id. Можете проверить (или поверить), отсутствие необходимых параметров, передача иных параметров или необходимых параметров, но с недопустимыми значениями, даже шестнадчатиричных в нижнем регистре, приведет в вызову исключения _RouteDoesNotExist_, ведь действительно нет маршрута удовлетворяющего шаблону _uri_regexp_.



## Лицензия

Распространяется свободно.

## Дополнительные сведения

Проект в рамках домашнего задания курса "Web-разработчик на Python" на https://otus.ru/learning
 
 Изначально решил не использовать классы, так как о них не говорилось при постановке задачи, а также не использовать чужие библиотеки. Пример использования Jinja2 реализовал через введение в фреймворк декоратора функции загрузки шаблона.

Прошу понять и простить.

И Вам не кажется... что **Dummy WSGI Framework** не так уж и "глуп"?
