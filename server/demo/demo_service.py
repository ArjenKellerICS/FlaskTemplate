# imports
from typing import List
from server import db
from .demo_model import Demo
from .demo_interface import DemoInterface


class DemoService:
    @staticmethod
    def get_all() -> List[Demo]:
        return Demo.query.all()

    @staticmethod
    def get_by_id(demo_id: int) -> Demo:
        return Demo.query.get(demo_id)

    @staticmethod
    def update(demo: Demo, update_changes: DemoInterface) -> Demo:
        demo.update(update_changes)
        db.session.commit()
        return demo

    @staticmethod
    def delete_by_id(demo_id: int) -> List[int]:
        demo = Demo.query.filter(Demo.id == demo_id).first()
        if not demo:
            return []
        db.session.delete(demo)
        db.session.commit()

        return [demo_id]

    @staticmethod
    def create(new_attrs: DemoInterface) -> Demo:
        new_demo = Demo(value=new_attrs["value"])
        db.session.add(new_demo)
        db.session.commit()
        return new_demo
