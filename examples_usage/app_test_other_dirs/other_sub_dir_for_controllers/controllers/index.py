
def controller_response(environ, start_response, app_config):
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
            " * <a href='./a_priori_bad_way'>'Нет маршрута'</a> - в маршрутах приложения нет соответствия данному URI"  
            " (<i><b>проверка RouteDoesNotExists</b></i>)<br>"    
            ""
            " * <a href='./controller_file_does_not_exists'>'Нет файла контроллера'</a> - путь есть, "
            " а файл контроллера умышленно отсутствует</a>"  
            " (<i><b>проверка ControllerFileDoesNotExists</b></i>)<br>"    
            ""
            " * <a href='./controller_with_missing_view_file'>'Нет файла представления'</a> - маршрут есть, "
            " контроллер есть, а HTML-файл представления умышленно отсутствует"
            " (<i><b>проверка ViewDoesNotExists</b></i>)<br>"
            ""      
            "" % app_config.APP_NAME
            , 'utf-8'
        )
    ]
