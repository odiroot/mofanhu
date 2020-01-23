from marshmallow_sqlalchemy import ModelSchema, field_for

from project.vanilla.models import Example


class ExampleSchema(ModelSchema):
    id = field_for(Example, "id", dump_only=True)

    class Meta:
        model = Example
        transient = True
