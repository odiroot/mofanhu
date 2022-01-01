from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from project.vanilla.models import Example


class ExampleSchema(SQLAlchemySchema):
    id = auto_field(dump_only=True)

    class Meta:
        model = Example
        transient = True
