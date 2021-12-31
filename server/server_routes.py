# base imports
from flask import Flask


def register_routes(server: Flask, api=None):
    """
    Import all modules of the types [Blueprint, Namespace, MethodView]
    - in case of a MethodView use the following:
        server.add_url_rule('/<str>/', view_func=<imported MethodView>.as_view(<str>))

    - in case of a blueprint instance use the following:
        server.register_blueprint(blueprint, url_prefix=<str>)

    - in case of a Namespace from flask_restx:
       api.add_namespace(api_namespace, path=<str>)

    - its also possible to use factory attachments as stated in the example below
    """

    # import modules
    from server.demo import attach_demo

    # register the routing
    attach_demo(server)
