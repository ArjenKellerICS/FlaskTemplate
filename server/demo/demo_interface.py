#  imports
from typing import TypedDict


# interface for updating values
class DemoInterface(TypedDict, total=False):
    id: int
    value: str
