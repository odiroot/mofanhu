from marshmallow import Schema, fields


class ExampleSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    good = fields.Bool()
