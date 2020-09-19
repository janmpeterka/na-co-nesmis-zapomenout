# def register_all_controllers(application):
#     from .errors import ErrorsView
#     from .index import IndexView

#     ErrorsView.register(application)
#     IndexView.register(application)


def register_error_handlers(application):
    from .errors import error404
    from .errors import error405
    from .errors import error500

    application.register_error_handler(403, error404)
    application.register_error_handler(404, error404)
    application.register_error_handler(405, error405)
    application.register_error_handler(500, error500)
