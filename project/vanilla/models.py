from flask_admin.contrib.sqla import ModelView

from project.extensions import admin, db


class Example(db.Model):
    __tablename__ = "examples"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    good = db.Column(db.Boolean(), default=True, server_default="TRUE")

    def __repr__(self):
        return f"<Example({self.name})>"


admin.add_view(ModelView(Example, db.session))
