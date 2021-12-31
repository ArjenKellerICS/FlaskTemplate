from marshmallow import Schema, fields


class DemoSchema(Schema):
    id = fields.Int()
    value = fields.Str()
