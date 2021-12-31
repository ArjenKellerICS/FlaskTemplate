# imports
from flask import request, jsonify, make_response
from flask.views import MethodView
# in-module imports
from .demo_interface import DemoInterface
from .demo_service import DemoService
from .demo_schema import DemoSchema

demo_schema_many = DemoSchema(many=True)
demo_schema_single = DemoSchema()


class DemoMethodView(MethodView):
    """
    This view can be used for multiple http methods
    """

    # 'GET' method
    def get(self):
        return jsonify(demo_schema_many.dump(DemoService.get_all())), 200

    def post(self):
        new_data = DemoInterface(value=request.json["value"])
        new = DemoService.create(new_data)

        return jsonify(demo_schema_single.dump(new)), 200


class DemoSingleMethodView(MethodView):
    """
    This view can be used for multiple http methods
    """
    def get(self, demo_id: int):
        return jsonify(demo_schema_single.dumps(DemoService.get_by_id(demo_id))), 200
    
    def delete(self, demo_id: int):
        return jsonify(DemoService.delete_by_id(demo_id)), 200
        
        


