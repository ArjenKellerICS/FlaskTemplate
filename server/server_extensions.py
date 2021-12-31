from flask import Flask


def initialize_extensions(server: Flask):
    """
    All flask extensions can be initialized from here

    first import extension instances from server.__init__.py
    after that initialize the extensions
    """

    # import extension instances from server.__init__.py
    from server import db

    # initialize the extensions
    db.init_app(server)
