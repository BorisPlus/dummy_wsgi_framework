#!/usr/bin/python3
def get_response(environ, start_response, app_config):
    if environ:
        pass  # Lets ignore PyCharm warning about not usage
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return [
        bytes(
            "<b>Привет. Я стартовая страница приложения \"%s\".</b> <br>"
            "Посмотри: <br>"
            " * <a href='./'>'Стартовая страница'</a> - то, что сейчас видите<br>"
            ""
            " * <a href='./homework_rebuke'>'Типовые ошибки ДЗ'</a> - контроллер без представления<br>"
            ""
            " * <a href='./string_methods' target='_blank'>'Строковые методы (новое окно)'</a> - "
            " контроллер с HTML-представлением<br>"
            ""
            " * <a href='./a_priori_bad_route'>'Нет маршрута'</a> - в маршрутах приложения нет соответствия данному URI"  
            " (<i><b>проверка RouteDoesNotExist</b></i>)<br>"    
            ""
            " * <a href='./controller_file_does_not_exists'>'Нет файла контроллера'</a> - путь есть, "
            " а файл контроллера умышленно отсутствует</a>"  
            " (<i><b>проверка ControllerFileDoesNotExist</b></i>)<br>"    
            ""      
            " * <a href='./controller_with_missing_method'>'У контроллера нет метода'</a> - маршрут есть,"
            " файл контроллера есть, но в файле контроллера умышленно отсутствует метод get_response"
            " (<i><b>проверка ControllerFileIsInvalid</b></i>)<br>"
            ""
            " * <a href='./controller_with_missing_view_file'>'Нет файла представления'</a> - маршрут есть,"
            " контроллер есть, а HTML-файл представления умышленно отсутствует"
            " (<i><b>проверка ViewDoesNotExist</b></i>)<br>"
            ""
            "<br>"
            "<br>"
            "Демонстрация работы декорирования функции загрузки (одного и того же) файла представления "
            "(т.е. шаблона):<br>"
            ""      
            " * <a href='./load_view_by_framework'>\"как есть\"</a> - загрузка шаблона фреймворком,"
            " который изначально ыл настроен на загрузку только HTML-файлов представлений<br>"
            ""      
            " * <a href='./load_view_by_yourself'>\"чем-то\" самописным</a> - "
            " немного более продвинутая загрузка шаблона с замена сответствующих лексем, если таковые переданы<br>"
            ""      
            " * <a href='./load_view_by_jinja2'>с использованием Jinja2</a> - "
            " загрузка шаблона, отдавая всю его обработку на откуп Jinja2<br>"
            ""      
            ""      
            "" % app_config.APP_NAME
            , 'utf-8'
        )
    ]
