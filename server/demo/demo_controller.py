# imports
from flask import request, jsonify, Response
from flask.views import MethodView
# in-module imports
from .demo_interface import DemoInterface
from .demo_service import DemoService
from .demo_schema import DemoSchema

schema_many = DemoSchema(many=True)
schema_single = DemoSchema()


class DemoMethodView(MethodView):
    """
    This view can be used for multiple http methods
    """

    # 'GET' method
    def get(self):
        return jsonify(schema_many.dump(DemoService.get_all())), 200

    def post(self):
        return jsonify(schema_single.dump(DemoService.create(DemoInterface(value=request.json["value"])))), 200


class DemoSingleMethodView(MethodView):
    """
    This view can be used for multiple http methods
    """
    def get(self, demo_id: int):
        return jsonify(schema_single.dumps(DemoService.get_by_id(demo_id))), 200
    
    def delete(self, demo_id: int):
        return jsonify(DemoService.delete_by_id(demo_id)), 200

    def put(self, demo_id: int):
        return jsonify(schema_single.dump(DemoService.update(DemoService.get_by_id(demo_id), DemoInterface(value=request.json["value"]))))
        
        


