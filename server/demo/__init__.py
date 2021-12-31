def attach_demo(server):
    from .demo_controller import DemoMethodView, DemoSingleMethodView

    server.add_url_rule('/demos/', view_func=DemoMethodView.as_view("demos"))
    server.add_url_rule('/demos/<demo_id>', view_func=DemoSingleMethodView.as_view("demo_single"))
