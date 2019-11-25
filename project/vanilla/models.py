from project.extensions import db


class Example(db.Model):
    __tablename__ = "examples"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    good = db.Column(db.Boolean(), default=True, server_default="TRUE")

    def __repr__(self):
        return f"<Example({self.name})>"
