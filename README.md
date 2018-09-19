# Dummy WSGI Framework

**_Dummy WSGI Framework_** - это WSGI-фрейморк, "простенький" и "глупенький" (хотя на самом деле он не так уж "прост" и "глуп", как может показаться на первый взгляд), разработан как _Just4Fun_-проект. 

**_Dummy WSGI Framework_** методологически состоит из "контроллеров" и "представлений", как паттерн "Model-View-Controller", но без "Model".

Он позволяет работать с представлениями, генерируемыми внутри контроллеров или подгружаемыми из файлов, например, в базовом варианте фреймворка это просто HTML-файлы. 

**_Dummy WSGI Framework_** расширяем:
* в силу открытого доступа к WSGI-интерфейсу на уровне контроллеров приложения, разработанного на его (фреймворка) основе;
* в силу возможности использования произвольных шаблонизаторов за счет реализованного в ядре фреймворка декоратора функции загрузки файлов представлений;
* и, в конце концов, это же Python, тут многое возможно.

Вы можете свободно испольтзовать **_Dummy WSGI Framework_** в качестве каркаса для своих Веб-приложений или основы для своего Веб-фреймворка. Ссылаться на факт использования Вами **_Dummy WSGI Framework_** не обязательно, но мне бы хотелось иметь публичный отзыв, даже если он и не положительный.

## Оглавление текущего описания

* [Требования](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Требования)
* [Установка](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Установка)
* [Руководство разработчика](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Руководство-разработчика)
    * [Описание структуры приложения](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Описание-структуры-приложения)
        * [Конфигурация](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Конфигурация)
        * [Маршруты](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Маршруты)
        * [Диспетчер контроллеров](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Диспетчер-контроллеров)
        * [Контроллеры](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Контроллеры)
        * [Представления](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Представления)
    * [Описание логики работы приложения](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Описание-логики-работы-приложения)
* [Примеры](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Примеры)
    * [Полный список примеров](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Полный-список-примеров)
    * [Пример _'Демонстрация базовых возможностей фреймворка'_](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Пример-Демонстрация-базовых-возможностей-фреймворка)
    * [Пример _'Приложение с двумя секретными страницами (Basic access authentication)'_](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Пример-Приложение-с-двумя-секретными-страницами-basic-access-authentication)
    * [Пример _'Приложение с оработкой допущенных параметров'_](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Пример-Приложение-с-оработкой-допущенных-параметров)
* [Лицензия](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Лицензия)
* [Дополнительные сведения](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Дополнительные-сведения)

## Требования

Не имеет. 

## Установка

**_Dummy WSGI Framework_** включен в реест пакетов PyPI (Python Package Index) - https://pypi.org/project/otus_webpython_003/

Его установка возможна с использованием _**pip**_
```
$ pip install dummy-wsgi-framework
```

Или иным возможным образом, например (команда для OS Debian):
```
$ cd <your_project_dir>
$ git clone git://github.com/BorisPlus/dummy-wsgi-framework.git
```
или, например, по ссылке для скачивания master-ветки проекта [Zip](https://github.com/BorisPlus/otus_webpython_003/archive/master.zip) (команда для OS Debian):
```
$ wget https://github.com/BorisPlus/otus_webpython_003/archive/master.zip
```

[↑ наверх в оглавление](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Оглавление)

## Руководство разработчика

Директория **_dummy_wsgi_framework_** - это и есть фреймворк с функциональным ядром в директории **_dummy_wsgi_framework/core_** и примером базового одностраничного приложения в директории **_dummy_wsgi_framework/app.template_**.

Для быстрого старта:
1. Создайте директорию вашего приложения **_app_** (где угодно).
2. Cкопируйте в директорию **_app_** содержимое директории **_dummy_wsgi_framework/app.template_**.
3. Запустите приложение:
```bash
uwsgi --http 127.0.0.1:8080 --wsgi-file /<absolute_path>/app/application.py
```

[↑ наверх в оглавление](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Оглавление)

### Описание структуры приложения
     
#### Конфигурация

Файл **_config.py_** вашего приложения содержит конфигурационные переменные, и предпочтительно, без должного опыта, не изменять существующие их значения (хотя это возможно, см. [конфигурацию](https://github.com/BorisPlus/otus_webpython_003/blob/regexp_routes/examples_usage/app_test_other_dirs/config.py) примера ["Приложение с переопределенными путями хранения файлов контроллеров и представлений"](https://github.com/BorisPlus/otus_webpython_003/blob/regexp_routes/examples_usage/app_one_page_other_dirs)) и добавлять свои конфигурационные переменные именно сюда.

[↑ наверх в оглавление](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Оглавление)
    
#### Маршруты

Файл **_routes.py_** приложения содержит так называемые "маршруты" - соответствие HTTP-запросов (на самом деле их масок) и контроллелов приложения.

Маршруты задаются в виде:
```python
routes_of_uri_regexps = (
    dict(uri_regexp='/index/', controller='index.py'),
    dict(uri_regexp='/', controller='index.py'),
)
```
или с подгрузкой базовых маршрутов фреймворка:
```python
from dummy_wsgi_framework.core.routes import base_routes_of_uri_regexps


routes_of_uri_regexps = tuple([
    dict(uri_regexp='^/page_one/$',
         controller='page_one.py'),
    dict(uri_regexp='^/page_two/$',
         controller='page_two.py')
    ] + list(base_routes_of_uri_regexps).copy())
```
, где:
* значение ключа _uri_regexp_ - это _REQUEST_URI_, последующая после доменного имени или IP-адреса часть HTTP-запроса. Знак косой черты "/" в конце _uri_regexp_ обязателен, так как диспетчер контроллеров через функционал ядра фреймворка контролирует маршруты HTTP-запросов, и если в конце _REQUEST_URI_ знак косой черты "/" отсутствует, то происходит редирект (перенаправление HTTP-запроса) на _REQUEST_URI_ с приписанной в конец косой чертой "/".
* значение ключа _controller_ - это сам Python-файл контроллера, соответствующего _uri_regexp_ и реализующего логику реакции на HTTP-запрос. 

Будте внимательны, срабатывает первый по порядку (сверху вниз) маршрут. Алгоритм сопоставления опирается на успех функции _re.compile(uri_regexp).findall(REQUEST_URI)_. Функционал регулярных выражений в uri_regexp был введен в ядро фреймворка для возможности назначения и использования в маршрутах именованных параметров HTTP-запросов (["Приложение с оработкой допущенных параметров"](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes/examples_usage/app_get_allowed_params_from_route_link)).

[↑ наверх в оглавление](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Оглавление)

#### Диспетчер контроллеров

За направление HTTP-запросов к контроллерам в соответствии с маршрутами из **_routes.py_** отвечает функция _application()_ - так называемый "диспетчер контроллеров" приложения, расположенный в **_application.py_** (файл называть не обязательно именно так). Этот файл выступает в качестве входной точки вашего WSGI-приложения.

```python
# Content of: app/application.py
import config as app_config
from dummy_wsgi_framework.core.dispatchers import get_controller_response

def application(environ, start_response):
    return get_controller_response(environ, start_response, app_config)
```
В итоге приложение запускается так:

```bash
uwsgi --http 127.0.0.1:8080 --wsgi-file /<absolute_path>/app/application.py
```
Таким образом у Вас есть возможность создать на основе **_Dummy WSGI Framework_** несколько отдельных приложений, запуская их на разных портах сервера. 

[↑ наверх в оглавление](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Оглавление)
    
#### Контроллеры

"Контроллеры" это Python-файлы, реализующие логику реакции на HTTP-запросы в соответствии с объявленными маршрутами.

Создайте свои контроллеры, реализовав их логику работы (можно взять типовые с подгрузкой шаблонов и без, или реализовать свои с посылкой специальных HTTP-заголовков, например, для _Basic Access Authentication_ как в примере ["Приложения с двумя секретными страницами (Basic access authentication)"](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes/examples_usage/app_basic_auth)). 

Контроллеры размещаются в директории _controllers_ в корневой директории приложения (что не обязательно, так как в **_config.py_** можно переопределить базовое расположение файлов контроллеров, см. конфигурацию примера ["Приложение с переопределенными путями хранения файлов контроллеров и представлений"](https://github.com/BorisPlus/otus_webpython_003/blob/regexp_routes/examples_usage/app_one_page_other_dirs/config.py)).

Основным методом в программном протоколе вызова контроллера приложения является функция **_get_response()_**. Обязательно реализуйте ее, иначе диспетчер контроллеров не сможет вызвать соответствующий контроллер, и будет сгененрировано исключение _ControllerFileIsInvalid_ с указанием отсутствия у контроллера функции **_get_response()_**

Контроллеры "редиректа" и "404-ой ошибки" реализованы в ядре фреймворка:
```python
# File: core/controllers/redirect.py
def get_response(environ, start_response, app_config, location):
    start_response('301 Moved Permanently', [('Location', location)])
    return b''
```
и

```python
# File: core/controllers/error404.py
def get_response(environ, start_response, app_config, message):
    start_response('404 Not found', [('Content-Type', 'text/html; charset=utf-8')])
    return [
        # some template
    ]
```

[↑ наверх в оглавление](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Оглавление)

#### Представления

Контроллеры могут непосредственно овечать на HTTP-запрос или же загружать заранее подготовленные в приложении файлы представлений, иногда их так же называют "шаблоны".

Python-файлы представлений размещаются в директории _views_ в корневой директории приложения (что не обязательно, так как в **_config.py_** можно переопределить базовое расположение файлов представлений, см. конфигурацию примера ["Приложение с переопределенными путями хранения файлов контроллеров и представлений"](https://github.com/BorisPlus/otus_webpython_003/blob/regexp_routes/examples_usage/app_one_page_other_dirs/config.py)).

Подробное описание реализации загрузки контроллером файла представления приведено [здесь](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#decorate_loaded_view_function_for_response) в примере ["Демонстрация базовых_возможностей фреймворка"](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes/examples_usage/app_base_features_demonstration).

[↑ наверх в оглавление](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Оглавление)

### Описание логики работы приложения
    
Точка входа вашего приложения (_**app/application.py:** def application()..._), передаст полученные аргументы базовому диспетчеру контроллеров (_**core/dispatchers.py:** def get_controller_response()..._) вместе с отсылкой на конфигурационные данные текущего приложения. Базовый диспетчер контроллеров в соответствии с переданным ему _REQUEST_URI_ по имеющимя данным в маршрутах текущего приложения (_**app/routes.py:** routes_of_uri_regexps_) вызовет по успеху (_**core/routes.py:** def get_controller_by_uri_regexp()..._) соответствующий данному маршруту контроллер (_**app/controllers/ACTION.py:** def get_response()), который в свою очередь ответит представлением по "зашитому" в него функционалу или передаст (если вы так реализуете) полученные им параметры дальше методу (_**core/dispatchers.py:** def load_view()..._), который "загрузит" файл вашего представления (_app/views/ACTION.html_).

[↑ наверх в оглавление](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Оглавление)
   
## Примеры

### Полный список примеров

Примеры разработанных на основе **Dummy WSGI Framework** приложений:
* ["Одностраничное приложение"](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes/examples_usage/app_one_page)
* ["Демонстрация базовых_возможностей фреймворка"](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes/examples_usage/app_base_features_demonstration)
* ["Приложение с переопределенными путями хранения файлов контроллеров и представлений"](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes/examples_usage/app_one_page_other_dirs)
* ["Приложение с двумя секретными страницами (Basic access authentication)"](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes/examples_usage/app_basic_auth)
* ["Приложение с оработкой допущенных параметров"](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes/examples_usage/app_get_allowed_params_from_route_link)

[↑ наверх в оглавление](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Оглавление)

### Пример _"Демонстрация базовых возможностей фреймворка"_

Пример ["Демонстрация базовых_возможностей фреймворка"](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes/examples_usage/app_base_features_demonstration) содержит демонстрационный вариант Веб-приложения, а именно:
* реализацию вызова контроллера без представления;
* реализацию вызова контроллера с загрузкой представления из HTML-файла;
* демонстрацию штатного отлова на уровне ядра фреймворка исключения RouteDoesNotExist заведомо отсутствующего какого-либо маршрута, удовлетворяющего пришедшему HTTP-запросу;
* демонстрацию штатного отлова на уровне ядра фреймворка исключения ControllerFileDoesNotExist при заведомо отсутствующем файле контроллера, маршрут до которого существует;
* демонстрацию штатного отлова на уровне ядра фреймворка исключения ControllerFileIsInvalid при заведомо отсутствующем у файла контроллера, маршрут до которого существует, необходимой функции _get_response()_;
* демонстрацию штатного отлова на уровне ядра фреймворка исключения ViewDoesNotExist при заведомо отсутствующем файле представления, подгружаемого в функции _get_response()_ контроллера, маршрут до которого существует.

[Кроме того](#decorate_loaded_view_function_for_response), с целью возможного использования разработчиками каких-либо шаблонизаторов отдельно продемонстрирвана возможность декорирования функции загрузки файла представления:
* "как есть" - загрузка шаблона фреймворком, реализованная в ядре фреймворка;
* "чем-то" самописным - загрузка шаблона и замена сответствующих лексем, если таковые переданы, возможным вашим собственным методом;
* с использованием Jinja2 - загрузка шаблона и его обработка с помощью Jinja2.

Мне не хотелось вносить зависимость от Jinja2 в ядро фреймворка, так как я считаю подобную связь слишком жесткой, а **_Dummy WSGI Framework_** изначально задумывался как "базовый", "каркасный", "простенький" и "глупенький". При этом, понимая, что этого может быть не достаточно сторонним разработчикам, и имея интерес по реализации подобной архитектуры фреймворка, я реализовал в ядре фреймворка декоратор для функции загрузки файла представления. 

Декоратор _@decorate_loaded_view_function_for_response_ производит проверку существования файла представления и передает функции обработки этого файла полученные ею аргументы.

То есть для загрузки файла представления "как есть", реализованной в ядре фреймворка,предполагается вызов в контроллере функции _load_view()_ ядра фреймворка:
```python
# Framework solution
from dummy_wsgi_framework.core.dispatchers import load_view


def get_response(environ, start_response, app_config):
    return load_view(
        environ,
        start_response,
        app_config,     # указываем базовому диспетчеру контроллеров
                        # какое из ваших приложений использовать
        'load_me.html'  # имя файла представления, 
                        # обычно в качестве данного параметра я использую вызов
                        # 
                        # from dummy_wsgi_framework.core.dispatchers import (
                        #   resolve_name_by_python_file_name
                        # )
                        # resolve_name_by_python_file_name(__file__, '%s.html')
                        # 
                        # что обяжет файл представления иметь тоже имя, 
                        # что и у файла контроллера и упростит возможный рефакторинг
    )
```

А для "чего-то" самописного у вас есть возможность реализовать функцию загрузки файла представления, например, с заменой сответствующих лексем шаблона. Необходимо лишь применить к вашей функции загрузки файла представления декоратор _@decorate_loaded_view_function_for_response_:

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
# Jinja2 realization
from dummy_wsgi_framework.core.dispatchers import (
    decorate_loaded_view_function_for_response
)
from dummy_wsgi_framework.core.exceptions import (
    ExistViewFileIsInvalid, 
    ViewDoesNotExist
)
import config
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
        'load_me.html',     # шаблон в формате Jinja2, возможно с базовым.
        id=1,               # некие переменные, которые будут переданы в шаблон и
        value=2,            # будут участвовать в замене в template.render
        other=4
    )
```

Рекомендую выносить функции, подобные _load_jinja2_view_template()_, в разрабатываемом приложении в отдельный файл, например, как здесь - _user_def.py_, так как это представляется методологически верным для повторного использования функций, подобных _load_jinja2_view_template()_, например, для использования _load_jinja2_view_template()_ в других контроллерах.

[↑ наверх в оглавление](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Оглавление)

### Пример _'Приложение с двумя секретными страницами (Basic Auth)'_

Когда выше говорилось, что **_Dummy WSGI Framework_** расширяем в силу открытого доступа к WSGI-интерфейсу на уровне контроллеров приложения, то имелось в виду, что у разработчика приложения существует возможность посылать заголовки и иную служебную информацию непосредственно в контроллерах своего приложения, разработанного на основе **_Dummy WSGI Framework_**. Тому может служить пример ["Приложение с двумя секретными страницами (Basic access authentication)"](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes/examples_usage/app_basic_auth)

```text
Замечание о протоколе запроса логина и пароля:
* Веб-приложения (в нашем случае это отдельный контроллер) пошлет клиенту HTTP-заголовок запроса Basic авторизации.
* Браузет продемонстрирует форму.
* Вы введете логин и проль.
* Они конкатенируются с использованием двоеточия ":", закодируюся браузером по протоколу Base64 и передадутся на сервер.
* Приложение должно будет декодировать и проверить на валидность переданную пару "login:password".
* В случае успеха вы получите доступ к "секретной" информации :)
```

Пусть маршруты будут таковы:
```python
routes_of_uri_regexps = (
    dict(uri_regexp=r'^/index_1/$', controller='first_secret_page.py'),
    dict(uri_regexp=r'^/index_2/$', controller='second_secret_page.py'),
    dict(uri_regexp=r'^/$', controller='first_secret_page.py'),
)
```

Контроллер:
```python
# Content of 'first_secret_page.py'
import base64

def get_response(environ, start_response, app_config):
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

[↑ наверх в оглавление](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Оглавление)

### Пример _'Приложение с оработкой допущенных параметров'_

С целью возможной необходимости использования вами в вашем приложении параметров HTTP-запросов был реализован механизм назначения именнованных параметров (в нотации "name=value") для маршрута, допустимых в HTTP-запросе и необходимых для его контроллера, с последующей их "передачей" дальше в представление (в той же нотации "name=value"). Это продемонстировано в примере ["Приложения с оработкой допущенных параметров"](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes/examples_usage/app_get_allowed_params_from_route_link)


Ключевым моментом для использования параметров является правильное написание регулярного выражения в соответствующем uri_regexp.

```python
routes_of_uri_regexps = (
    ...
    dict(uri_regexp=r'^(/view_random/\?(id=[0-9]*)&(value=[A-F0-9]*)/)$', controller='view.py'),
    ...
)
```

При формировании в _uri_regexp_ регулярного выражения необходимо придерживаться следующих правил:
* сформировать корневой HTTP-путь, так называемый _PATH_INFO_, например, "/path/info/"
* определиться с набором параметров, передаваемых контроллеру, указанному в ключе _controller_, например, это "id", "hex", "word"
* сформировать пары из параметров и их шаблонных типов значений, например, "id=id_value_type", "hex=hex_value_type", "word=word_value_type"
* заключить пары в скобки и сконкатенировать их, используя "&", например, "(id=id_value_type)**&**(hex=hex_value_type)**&**(word=word_value_type)"
* сконкатенировать полученное с корневым HTTP-путем, используя "\\?", например, "/path/info/**\\?**(id=id_value_type)&(hex=hex_value_type)&(word=word_value_type)"
* поставить в конце знак косой черты "/", например, "/path/info/\?(id=id_value_type)&(hex=hex_value_type)&(word=word_value_type)**/**"
* заключить в круглые скобки, например, "**(**/path/info/\?(id=id_value_type)&(hex=hex_value_type)&(word=word_value_type)/**)**"
* поставить знаки начала "^" и конца "$" регулярного выражения, например, "**^**(/path/info/\?(id=id_value_type)&(hex=hex_value_type)&(word=word_value_type)/)**$**"
* заменить шаблонные типы значений на их шаблоны в нотации регулярных выражений, например:
    * для "id_value_type" - "[0-9]*"
    * для "hex_value_type" - "[0-9A-Fa-f]*"
    * для "word_value_type" - "[0-9A-Za-z_]*" или "\w*"
* как итог в _uri_regexp_ внести "^(/path/info/\?(id=[0-9]*)&(hex=[0-9A-Fa-f]*)&(word=[0-9A-Za-z_]*)/)$"
    
В текущем примере контроллер _list_ генерирует представление со списком ссылок, где указаны шестнадцатиричные значения в верхнем регистре и их id, присвоенные им в порядке их генерации.

А контроллер _view_ отображает переданные в HTTP-запросе id и шестнадцатиричное значение в верхнем регистре . Можете проверить (или поверить), наличие необходимых параметров с недопустимыми значениями, даже шестнадчатиричными в нижнем регистре, а также отсутствие необходимых параметров или наличие иных параметров приведут в вызову исключения _RouteDoesNotExist_, ведь действительно нет маршрута удовлетворяющего подобному _uri_regexp_.

[↑ наверх в оглавление](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Оглавление)

## Лицензия

Вы можете свободно испольтзовать **_Dummy WSGI Framework_** в качестве каркаса для своих Веб-приложений или основы для своего Веб-фреймворка. Ссылаться на факт использования Вами **_Dummy WSGI Framework_** не обязательно, но мне бы хотелось иметь публичный отзыв, даже если он и не положительный.

[↑ наверх в оглавление](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Оглавление)

## Дополнительные сведения

Проект был начат в рамках домашнего задания курса "Web-разработчик на Python" на https://otus.ru/learning и продолжен.
 
 Изначально было решено не использовать классы, так как о них при постановке задачи не говорилось, а также не использовать и сторонние библиотеки, чтобы **Dummy WSGI Framework** был максимально "чистым". 
 
Прошу понять и простить.

Теперь, надеюсь, и Вам кажется, что **Dummy WSGI Framework** не так уж и "прост" и "глуп". 

[↑ наверх в оглавление](https://github.com/BorisPlus/otus_webpython_003/tree/regexp_routes#Оглавление)